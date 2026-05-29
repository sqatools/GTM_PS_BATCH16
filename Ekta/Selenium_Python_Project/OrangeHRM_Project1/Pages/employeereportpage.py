import time
from Base.base import BasePage
from .locators import Locators
from selenium.webdriver.common.by import By

#class EmployeeReportPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = Locators()

    def generate_employee_report(self, employee_name, project_name=None, activity_name=None, from_date=None, to_date=None):
        """Fills criteria for Employee Report and clicks View."""
        
        # १. Employee Name (Mandatory)
        self.enter_text(self.locator.report_employee_name_field, employee_name)
        time.sleep(3)
        emp_option = (By.XPATH, f"//div[@role='option']//span[contains(text(), '{employee_name}')]")
        self.click_element(emp_option)
        
        # २. Project Name (Optional)
        if project_name:
            self.enter_text(self.locator.report_project_name_field, project_name)
            time.sleep(3)
            proj_option = (By.XPATH, f"//div[@role='option']//span[contains(text(), '{project_name}')]")
            self.click_element(proj_option)
            
        # ३. Activity Name Dropdown (Optional)
        if activity_name:
            self.click_element(self.locator.report_activity_dropdown)
            time.sleep(1)
            act_option = (By.XPATH, f"//div[@role='option']//span[text()='{activity_name}']")
            self.click_element(act_option)
            
        # ४. Project Date Range - From (Optional)
        if from_date:
            self.enter_text(self.locator.report_from_date, from_date)
            
        # ५. Project Date Range - To (Optional)
        if to_date:
            self.enter_text(self.locator.report_to_date, to_date)
            
        # Click View button to generate the report
        self.click_element(self.locator.report_view_btn)
        time.sleep(5)