from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

LOGIN_URL = "https://sqatools.in/wp-login.php"
LOGIN_USERNAME = "your_username"
LOGIN_PASSWORD = "your_password"


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


def open_login_page(driver, login_url=LOGIN_URL, username=LOGIN_USERNAME, password=LOGIN_PASSWORD):
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


def main():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.maximize_window()
        success, clicked = open_login_page(driver)
        print(f"Login page opened. Username/password set: {success}. Login button clicked: {clicked}.")
        driver.save_screenshot("login_page_result.png")
        print("Saved login screenshot to login_page_result.png")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
