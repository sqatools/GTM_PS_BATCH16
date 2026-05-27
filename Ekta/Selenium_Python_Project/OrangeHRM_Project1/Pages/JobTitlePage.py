import os
from Base.base import BasePage
from .locators import Locators

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
            
        # Click Save
        self.click_element(self.locator.job_save_btn)