from Base.base import BasePage
from .locators import Locators

class Adminpage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = Locators()

    def navigate_to_admin(self):
        """Clicks on the Admin tab from the sidebar menu."""
        self.click_element(self.locator.admin_tab)
        # Give OrangeHRM's dynamic single-page app architecture a brief split-second 
        # to process the page routing state change before trying to find the input field
        #time.sleep(1) 
        self.get_element(self.locator.user_management_header)