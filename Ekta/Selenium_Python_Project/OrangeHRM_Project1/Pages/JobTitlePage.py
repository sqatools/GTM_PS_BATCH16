import os
import time
from Base.base import BasePage
from .locators import Locators
#from Pages import EmployeeReportPage

class JobTitlePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = Locators()

    def add_new_job_title(self, job_title, description=None, file_path=None, note=None):
        """Fills out the Add Job Title form and saves it."""
        # Enter Job Title (Required Field)
        self.enter_text(self.locator.job_title_input, job_title)
        
        # Enter Description if provided
        if description:
            self.enter_text(self.locator.job_description_textarea, description)
            
        # Upload Job Specification file if provided (Must be an absolute path)
        if file_path:
            # Note: We send keys directly to the hidden file input element, no clicking 'Browse'
            file_input = self.get_present_element(self.locator.job_specification_upload)
            file_input.send_keys(os.path.abspath(file_path))
            
        # Enter Note if provided
        if note:
            self.enter_text(self.locator.job_note_textarea, note)
            
        # Click Save button
        self.click_element(self.locator.job_save_btn)
        time.sleep(2)
        
    #def navigate_to_employee_reports(self):
        """Navigates to the Reports section from the Job Titles page."""
        self.click_element(self.locator.time_btn)
        time.sleep(2)
        self.click_element(self.locator.reports_btn)
        time.sleep(2)
        self.click_element(self.locator.employee_reports_option)
        time.sleep(2)
        return EmployeeReportPage(self.driver)
        