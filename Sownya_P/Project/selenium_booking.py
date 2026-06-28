from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import datetime

URL = "https://sqatools.in/dummy-booking-website/"
LOGIN_URL = "https://sqatools.in/wp-login.php"
LOGIN_USERNAME = "psownyassree@gmail.com"
LOGIN_PASSWORD = "trailpassword"


def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView({block:'center', inline:'nearest'})", element)


def fill_if_present(driver, by, locator, value, timeout=5):
    try:
        el = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, locator))
        )
        scroll_to_element(driver, el)
        el.clear()
        el.send_keys(value)
        return True
    except TimeoutException:
        return False
    except Exception:
        return False


def select_option(driver, by, locator, visible_text, timeout=5):
    try:
        el = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, locator))
        )
        scroll_to_element(driver, el)
        Select(el).select_by_visible_text(visible_text)
        return True
    except TimeoutException:
        return False
    except Exception:
        return False


def try_click(driver, by, locator, timeout=5):
    try:
        el = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, locator))
        )
        scroll_to_element(driver, el)
        el.click()
        return True
    except TimeoutException:
        return False
    except Exception:
        return False


def enter_first_last_name(driver, first_name, last_name):
    elements = driver.find_elements(By.ID, "firstname")
    if len(elements) >= 1:
        try:
            scroll_to_element(driver, elements[0])
            elements[0].clear()
            elements[0].send_keys(first_name)
        except Exception:
            pass
    if len(elements) >= 2:
        try:
            scroll_to_element(driver, elements[1])
            elements[1].clear()
            elements[1].send_keys(last_name)
        except Exception:
            pass


def open_login_page(driver, login_url, username, password):
    driver.get(login_url)
    time.sleep(2)

    username_set = False
    for by, locator in [
        (By.ID, "user_login"),
        (By.NAME, "log"),
        (By.NAME, "email"),
        (By.NAME, "username"),
    ]:
        if fill_if_present(driver, by, locator, username):
            username_set = True
            break

    password_set = False
    for by, locator in [
        (By.ID, "user_pass"),
        (By.NAME, "pwd"),
        (By.NAME, "password"),
    ]:
        if fill_if_present(driver, by, locator, password):
            password_set = True
            break

    submit_clicked = False
    for by, locator in [
        (By.NAME, "wp-submit"),
        (By.XPATH, "//input[@type='submit']"),
        (By.XPATH, "//button[contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'login') ]"),
        (By.XPATH, "//button[contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'sign in') ]"),
    ]:
        if try_click(driver, by, locator):
            submit_clicked = True
            break

    return username_set and password_set, submit_clicked


def save_test_result(submitted, screenshot_path, file_path="selenium_booking_result.txt"):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("Test result summary\n")
        f.write(f"URL: {URL}\n")
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

        # Open login page and enter credentials
        logged_in, login_clicked = open_login_page(driver, LOGIN_URL, LOGIN_USERNAME, LOGIN_PASSWORD)
        print(f"Login fields entered: {logged_in}, login button clicked: {login_clicked}")

        # Go to booking page after login attempt
        driver.get(URL)

        # Wait for page to load
        time.sleep(2)

        # Passenger details
        enter_first_last_name(driver, "sownya", "sree")
        fill_if_present(driver, By.ID, "birthday", "1995-03-01")

        # Sex selection
        if not try_click(driver, By.ID, "male"):
            try_click(driver, By.ID, "female")

        # Number of additional passengers
        select_option(driver, By.ID, "admorepass", "Add 1 more passenger (100%)")

        # Travel details
        fill_if_present(driver, By.ID, "fromcity", "srikalahasti")
        fill_if_present(driver, By.ID, "destcity", "hyderabad")
        fill_if_present(driver, By.ID, "departdate", "2026-06-28")
        fill_if_present(driver, By.ID, "returndate", "2026-07-14")

        # Optional delivery fields
        fill_if_present(driver, By.ID, "visadate", "2026-07-15")

        # Billing details
        fill_if_present(driver, By.ID, "billing_name", "sownya sree")
        fill_if_present(driver, By.ID, "billing_phone", "7893279076")
        fill_if_present(driver, By.ID, "billing_email", "psownyasree@gmail.com")
        fill_if_present(driver, By.ID, "billing_address", "Miyapur, Hyderabad, 500049")
        select_option(driver, By.ID, "billing_country", "India")
        fill_if_present(driver, By.ID, "postcode", "517640")

        # Try to submit the form if a submit button exists
        submitted = False
        for locator in [
            (By.XPATH, "//button[normalize-space()='Submit']"),
            (By.XPATH, "//button[contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'submit')]"),
            (By.XPATH, "//input[@type='submit']"),
            (By.XPATH, "//input[@type='button' and contains(translate(@value,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'submit')]"),
        ]:
            if try_click(driver, locator[0], locator[1]):
                submitted = True
                break

        screenshot_path = "selenium_booking_result.png"
        driver.save_screenshot(screenshot_path)
        save_test_result(submitted, screenshot_path)
        print("Form interactions attempted. Submit clicked:", submitted)
        print("Saved screenshot to:", screenshot_path)
        print("Saved result summary to: selenium_booking_result.txt")

        time.sleep(2)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
