import time
from .orange_hrm_locators import OrangeHRMLocators
from base.selenium_base import SeleniumBase
from selenium.webdriver.common.by import By


class OrangeHRMPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def Navigate_to_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def login(self, username, password):
        self.enter_text(OrangeHRMLocators.username_field, username)
        self.enter_text(OrangeHRMLocators.password_field, password)
        self.click_element(OrangeHRMLocators.login_btn)


    def add_user(self, role_name, status, employee_name):
        self.click_element(OrangeHRMLocators.Admin_page_link)
        self.click_element(OrangeHRMLocators.add_button)
        self.click_element(OrangeHRMLocators.user_role_dropdown)
        user_admin_role_options = (By.XPATH, f"//div[@role='option']//span[text()='{role_name}']")
        self.click_element(user_admin_role_options)
        self.click_element(OrangeHRMLocators.status_dropdown)
        status_options = (By.XPATH, f"//div[@role='option']//span[text()='{status}']")
        self.click_element(status_options)
        self.enter_text(OrangeHRMLocators.employee_name_field, employee_name)
        time.sleep(3)
        empl_options = (By.XPATH, f"//div[@role='option']//span[text()='{employee_name}']")
        self.click_element(empl_options)



    