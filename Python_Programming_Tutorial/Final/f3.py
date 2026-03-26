URL = "https://books.toscrape.com/"

# ฉันต้องการดึงข้อมูล Book Title เเละ Price ของ Books ทุกเล่มที่อยู่ใน website มีอยู่ 1000 เล่ม

# นำ data ที่ได้ทั้งหมดเก็บลงใน books.xlsx โดยใน จะต้องมี 2 column คือ Book Title เเละ Price

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

URL = "https://books.toscrape.com/"


def scrape_all_books(base_url: str) -> list[tuple[str, str]]:
    books: list[tuple[str, str]] = []
    next_page_url = base_url

    while next_page_url:
        response = requests.get(next_page_url, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        book_items = soup.select("article.product_pod")

        for item in book_items:
            title_tag = item.select_one("h3 a")
            price_tag = item.select_one("p.price_color")

            if title_tag and price_tag:
                title = title_tag.get("title", "").strip()
                price = price_tag.get_text(strip=True)
                books.append((title, price))

        next_btn = soup.select_one("li.next a")
        if next_btn:
            href = next_btn.get("href", "")
            # หน้าถัดไปจะเป็นแบบ relative path เช่น "catalogue/page-2.html"
            next_page_url = requests.compat.urljoin(next_page_url, href)
        else:
            next_page_url = None

    return books


def save_to_excel(books: list[tuple[str, str]], filename: str = "books.xlsx") -> None:
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Books"

    sheet.append(["Book Title", "Price"])
    for title, price in books:
        sheet.append([title, price])

    workbook.save(filename)


def main() -> None:
    books = scrape_all_books(URL)
    save_to_excel(books, "books.xlsx")
    print(f"Saved {len(books)} books to books.xlsx")


if __name__ == "__main__":
    main()
