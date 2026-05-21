from Base.base import BasePage
from .locators import Locators
import time

class MyInfoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = Locators()

    def navigate_to_my_info(self):
        """Clicks on the My Info tab from the sidebar menu."""
        self.click_element(self.locator.my_info_tab)
        # Give OrangeHRM's dynamic single-page app architecture a brief split-second 
        # to process the page routing state change before trying to find the input field
        time.sleep(1) 
        self.get_element(self.locator.first_name_field)

    def update_personal_details(self, first_name, middle_name, last_name):
        """Clears and updates the main personal details fields."""
        self.enter_text(self.locator.first_name_field, first_name)
        self.enter_text(self.locator.middle_name_field, middle_name)
        self.enter_text(self.locator.last_name_field, last_name)
        self.click_element(self.locator.personal_details_save_btn)