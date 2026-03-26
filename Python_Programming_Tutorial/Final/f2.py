import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

QUOTES_BASE_URL = "https://quotes.toscrape.com/login"

ACTION_DELAY = 1.0  # วินาที


def pause(seconds: float = ACTION_DELAY) -> None:
    time.sleep(seconds)


def main():
    driver = webdriver.Chrome()
    try:
        driver.get(QUOTES_BASE_URL)
        pause()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )

        username_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")
        pause()

        username_input.send_keys("comsci")
        pause(0.7)
        password_input.send_keys("password")
        pause(0.7)

        login_button = driver.find_element(By.XPATH, "//input[@type='submit']")
        pause()
        login_button.click()

        # รอให้หน้าเปลี่ยนหลัง login
        WebDriverWait(driver, 10).until(EC.url_changes(QUOTES_BASE_URL))
        pause(2)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
