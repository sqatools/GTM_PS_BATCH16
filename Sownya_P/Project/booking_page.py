from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import datetime
import time

from login_page import open_login_page, fill_if_present, try_click

BOOKING_URL = "https://sqatools.in/dummy-booking-website/"


def enter_first_last_name(driver, first_name, last_name):
    elements = driver.find_elements(By.ID, "firstname")
    if len(elements) >= 1:
        try:
            elements[0].clear()
            elements[0].send_keys(first_name)
        except Exception:
            pass
    if len(elements) >= 2:
        try:
            elements[1].clear()
            elements[1].send_keys(last_name)
        except Exception:
            pass


def select_option(driver, by, locator, visible_text, timeout=5):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, locator))
        )
        Select(element).select_by_visible_text(visible_text)
        return True
    except Exception:
        return False


def save_test_result(submitted, screenshot_path, file_path="selenium_booking_result.txt"):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("Booking test result summary\n")
        f.write(f"URL: {BOOKING_URL}\n")
        f.write(f"Submit button clicked: {submitted}\n")
        if not submitted:
            f.write("Note: No submit button was found, so the test result is based on field interaction and screenshot evidence.\n")
        f.write(f"Screenshot: {screenshot_path}\n")
        f.write(f"Timestamp: {datetime.datetime.now().isoformat()}\n")


def main():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.maximize_window()

        # Login first if required
        logged_in, login_clicked = open_login_page(driver)
        print(f"Login performed: {logged_in}, login clicked: {login_clicked}")

        driver.get(BOOKING_URL)
        time.sleep(2)

        enter_first_last_name(driver, "sownya", "sree")
        fill_if_present(driver, By.ID, "birthday", "1995-03-01")
        if not try_click(driver, By.ID, "male"):
            try_click(driver, By.ID, "female")
        try:
            select_option(driver, By.ID, "admorepass", "Add 1 more passenger (100%)")
        except Exception:
            pass
        fill_if_present(driver, By.ID, "fromcity", "srikalahasti")
        fill_if_present(driver, By.ID, "destcity", "hyderabad")
        fill_if_present(driver, By.ID, "departdate", "2026-06-28")
        fill_if_present(driver, By.ID, "returndate", "2026-07-14")
        fill_if_present(driver, By.ID, "visadate", "2026-07-15")
        fill_if_present(driver, By.ID, "billing_name", "sownya sree")
        fill_if_present(driver, By.ID, "billing_phone", "7893279076")
        fill_if_present(driver, By.ID, "billing_email", "psownyasree@gmail.com")
        fill_if_present(driver, By.ID, "billing_address", "Miyapur, Hyderabad, 500049")
        try:
            select_option(driver, By.ID, "billing_country", "India")
        except Exception:
            pass
        fill_if_present(driver, By.ID, "postcode", "517640")

        submitted = False
        for locator in [
            (By.XPATH, "//button[normalize-space()='Submit']"),
            (By.XPATH, "//button[contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'submit')]"),
            (By.XPATH, "//input[@type='submit']"),
        ]:
            if try_click(driver, locator[0], locator[1]):
                submitted = True
                break

        screenshot_path = "selenium_booking_result.png"
        driver.save_screenshot(screenshot_path)
        save_test_result(submitted, screenshot_path)
        print("Saved booking screenshot to:", screenshot_path)
        print("Saved result summary to: selenium_booking_result.txt")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
