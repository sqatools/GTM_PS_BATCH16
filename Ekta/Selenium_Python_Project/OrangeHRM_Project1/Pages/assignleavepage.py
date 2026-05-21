
import time

from Base.base import BasePage
from .locators import Locators

class AssignLeavePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = Locators()
        
    def _go_to_leave_module(self):
        """Internal helper to click the main Leave menu item."""
        self.click_element(self.locator.leave_menu)
        time.sleep(2)

    def navigate_to_assign_leave(self):
        """Navigates from the dashboard to the Assign Leave page."""
        self._go_to_leave_module()
        self.click_element(self.locator.assign_leave_tab)
        time.sleep(1)

    def assign_leave(self, employee_keyword, from_date, to_date):
        """Fills out and submits the Assign Leave form."""
        # 1. Type into autocomplete field
        self.enter_text(self.locator.assign_employee_name_input, employee_keyword)
        time.sleep(2)  # Wait for dynamic dropdown search suggestions to load
        self.click_element(self.locator.assign_employee_dropdown_hint)

        # 2. Open and select Leave Type
        self.click_element(self.locator.assign_leave_type_dropdown)
        time.sleep(1)
        self.click_element(self.locator.assign_leave_type_option)

        # 3. Handle dates
        self.enter_text(self.locator.assign_from_date, from_date)
        self.enter_text(self.locator.assign_to_date, to_date)

        # 4. Click Assign button
        self.click_element(self.locator.assign_btn)
        time.sleep(3)