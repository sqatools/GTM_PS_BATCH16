from Base.base import BasePage
from .locators import Locators

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = Locators()

    def login_to_application(self, username, password):
       
        self.enter_text(self.locator.username_field, username)
         
        self.enter_text(self.locator.password_field, password)
        self.click_element(self.locator.login_btn)

