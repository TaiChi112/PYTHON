from __future__ import annotations

import re
import time
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


QUOTES_BASE_URL = "https://quotes.toscrape.com"
LOTUS_URL = "https://www.lotuss.com/th"
LOTUS_QUERY = "น้ำดื่มตราสิงห์"
LOTUS_PRODUCT_API = "https://api-o2o.lotuss.com/lotuss-mobile-bff/product/v4/products"
BASE_DIR = Path(__file__).resolve().parent


@dataclass
class QuoteItem:
    quote: str
    author: str


@dataclass
class ProductItem:
    product: str
    price: str


def scrape_quotes_to_excel(
    output_path: str | Path = BASE_DIR / "quotes_data.xlsx",
) -> None:
    """Scrape all quote pages and save as an Excel file."""
    quotes: list[QuoteItem] = []
    next_page = "/"

    while next_page:
        response = requests.get(f"{QUOTES_BASE_URL}{next_page}", timeout=30)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        for quote_block in soup.select("div.quote"):
            text_tag = quote_block.select_one("span.text")
            author_tag = quote_block.select_one("small.author")

            if not text_tag or not author_tag:
                continue

            quotes.append(
                QuoteItem(
                    quote=text_tag.get_text(strip=True),
                    author=author_tag.get_text(strip=True),
                )
            )

        next_link = soup.select_one("li.next > a")
        next_page = (
            next_link["href"] if next_link and next_link.has_attr("href") else ""
        )

    quotes_df = pd.DataFrame([{"Quote": q.quote, "Author": q.author} for q in quotes])
    quotes_df.to_excel(output_path, index=False)
    print(f"Saved {len(quotes_df)} quotes to {Path(output_path)}")


def build_chrome_driver() -> Chrome:
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--lang=th-TH")
    return webdriver.Chrome(options=options)


def find_search_input(driver: Chrome, wait: WebDriverWait):
    selectors = [
        (By.CSS_SELECTOR, "input[type='search']"),
        (By.CSS_SELECTOR, "input[placeholder*='ค้นหา']"),
        (By.CSS_SELECTOR, "input[aria-label*='ค้นหา']"),
        (By.CSS_SELECTOR, "input[name='q']"),
    ]

    for by, selector in selectors:
        try:
            return wait.until(EC.element_to_be_clickable((by, selector)))
        except TimeoutException:
            continue
    raise TimeoutException("Cannot locate search input on Lotus page")


def accept_cookies_if_present(driver: Chrome, wait: WebDriverWait) -> None:
    """Dismiss cookie banner when present to avoid blocked interactions."""
    cookie_buttons = [
        (By.XPATH, "//button[contains(., 'ยอมรับคุกกี้ทั้งหมด')]"),
        (By.XPATH, "//button[contains(., 'Accept All Cookies')]"),
    ]

    for by, selector in cookie_buttons:
        try:
            button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((by, selector))
            )
            driver.execute_script("arguments[0].click();", button)
            time.sleep(1)
            return
        except Exception:
            continue


def scroll_until_loaded(
    driver: Chrome, pause_seconds: float = 1.2, max_idle_rounds: int = 4
) -> None:
    """Scroll to bottom repeatedly until page height stabilizes."""
    idle_rounds = 0
    previous_height = driver.execute_script("return document.body.scrollHeight")

    while idle_rounds < max_idle_rounds:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause_seconds)
        current_height = driver.execute_script("return document.body.scrollHeight")

        if current_height == previous_height:
            idle_rounds += 1
        else:
            idle_rounds = 0

        previous_height = current_height


def _extract_products_from_text(driver: Chrome) -> list[ProductItem]:
    """Fallback parser using visible body text lines."""
    products: list[ProductItem] = []
    seen: set[tuple[str, str]] = set()
    body_text = driver.find_element(By.TAG_NAME, "body").text
    lines = [line.strip() for line in body_text.splitlines() if line.strip()]

    price_pattern = re.compile(r"^(?:฿\s*)?([\d,]+\.\d{1,2})$")
    noise_pattern = re.compile(
        r"^(ผลลัพธ์สำหรับ|เรียงตาม|แสดงสินค้าจากหมวดหมู่|ไม่แสดงครั้งนี้|"
        r"ซื้อ\s*\d+\s*ชิ้น|\d+\s*บาท|TH\s*\|\s*EN|เข้าสู่ระบบ|สมัครสมาชิก|"
        r"หมวดหมู่|คำสั่งซื้อทั้งหมด|ดาวน์โหลดแอปพลิเคชัน|นโยบายคุ้มครอง)",
        re.IGNORECASE,
    )

    for idx, line in enumerate(lines):
        price_match = price_pattern.match(line)
        if not price_match:
            continue

        product_price = f"฿{price_match.group(1)}"
        product_name = ""

        for back in range(idx - 1, max(-1, idx - 7), -1):
            candidate = lines[back]
            if price_pattern.match(candidate):
                continue
            if noise_pattern.match(candidate):
                continue
            if candidate.startswith("-"):
                continue
            if "@" in candidate:
                continue
            if "lotus" in candidate.lower():
                continue
            if re.search(r"[ก-๙A-Za-z]", candidate):
                product_name = candidate
                break

        if product_name:
            pair = (product_name, product_price)
            if pair not in seen:
                seen.add(pair)
                products.append(ProductItem(product=product_name, price=product_price))
    return products


def _chunked(items: list[str], chunk_size: int) -> list[list[str]]:
    return [items[i : i + chunk_size] for i in range(0, len(items), chunk_size)]


def _extract_products_from_api(driver: Chrome) -> list[ProductItem]:
    """Extract SKU from page source and resolve product name/price via Lotus API."""
    page_source = driver.page_source
    skus = re.findall(
        r"o2o-static\.lotuss\.com/products/\d+/([0-9]{4,})\.jpg", page_source
    )
    unique_skus = list(dict.fromkeys(skus))

    products: list[ProductItem] = []
    seen: set[tuple[str, str]] = set()

    for sku_batch in _chunked(unique_skus, 90):
        params = {
            "sku": ",".join(sku_batch),
            "page": 1,
            "limit": 99,
            "seller_id": 3,
        }

        try:
            response = requests.get(LOTUS_PRODUCT_API, params=params, timeout=30)
            response.raise_for_status()
            data = response.json().get("data", {})
            for item in data.get("products", []):
                name = str(item.get("name", "")).strip()
                price_value = (
                    item.get("priceRange", {})
                    .get("minimumPrice", {})
                    .get("finalPrice", {})
                    .get("value")
                )

                if not name or price_value in (None, ""):
                    continue

                price_text = f"฿{float(price_value):.2f}"
                pair = (name, price_text)
                if pair not in seen:
                    seen.add(pair)
                    products.append(ProductItem(product=name, price=price_text))
        except Exception:
            continue

    return products


def extract_products(driver: Chrome) -> list[ProductItem]:
    # Prefer API-backed extraction (stable) and fallback to text parsing.
    products = _extract_products_from_api(driver)
    if products:
        return products
    return _extract_products_from_text(driver)


def scrape_lotus_products_to_excel(
    output_path: str | Path = BASE_DIR / "products_data.xlsx",
    query: str = LOTUS_QUERY,
) -> None:
    """Search Lotus products and save Product/Price to Excel."""
    driver = build_chrome_driver()

    try:
        wait = WebDriverWait(driver, 20)
        driver.get(LOTUS_URL)
        accept_cookies_if_present(driver, wait)

        search_input = find_search_input(driver, wait)
        search_input.clear()
        search_input.send_keys(query)
        search_input.send_keys(Keys.ENTER)

        wait.until(lambda d: "/search/" in d.current_url)
        try:
            wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[contains(., 'ผลลัพธ์สำหรับ')]")
                )
            )
        except TimeoutException:
            # Retry cookie dismiss in case a late banner blocks search result rendering.
            accept_cookies_if_present(driver, wait)

        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        products: list[ProductItem] = []
        direct_search_url = f"{LOTUS_URL}/search/{quote(query)}?sort=relevance:DESC"

        for attempt in range(3):
            time.sleep(2)
            scroll_until_loaded(driver)
            products = extract_products(driver)

            if len(products) >= 5:
                break

            if attempt == 0:
                driver.get(direct_search_url)
                accept_cookies_if_present(driver, wait)
            else:
                driver.refresh()
                accept_cookies_if_present(driver, wait)

        products_df = pd.DataFrame(
            [{"Product": p.product, "Price": p.price} for p in products],
            columns=["Product", "Price"],
        )
        products_df.to_excel(output_path, index=False)
        print(f"Saved {len(products_df)} products to {Path(output_path)}")
    finally:
        driver.quit()


def main() -> None:
    scrape_quotes_to_excel()
    scrape_lotus_products_to_excel()


if __name__ == "__main__":
    main()
