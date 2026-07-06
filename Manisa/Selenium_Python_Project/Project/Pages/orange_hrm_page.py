import time
from .orange_hrm_locators import OrangeHRMLocators
from Project.Base.base import SeleniumBase
from selenium.webdriver.common.by import By
#from Pages.Jobpage import JobPage

class OrangeHRMPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.enter_text(OrangeHRMLocators.username_field, username)
        self.enter_text(OrangeHRMLocators.password_field, password)
        self.click_element(OrangeHRMLocators.login_button)

    def verify_login_successful(self, expected_url, time_out=10):
        actual_url = self.get_current_url()
        if actual_url == expected_url:
            self.log.info("Login successful, URL matched")
            return True
        else:
            self.log.error(f"Login failed, expected URL: {expected_url}, but got: {actual_url}")
            return False
        
    def add_user(self, role_name, status, employee_name):
        self.click_element(OrangeHRMLocators.admin_menu)
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
        time.sleep(5)
        self.click_element(empl_options)

        self.enter_text(OrangeHRMLocators.user_username, "manisa" )
        
        self.enter_text(OrangeHRMLocators.user_password, "Manisadddd8" )

        self.enter_text(OrangeHRMLocators.user_confirm_password, "Manisadddd8" )

        self.click_element(OrangeHRMLocators.save_button)
        
    def job_add(self):
        self.click_element(OrangeHRMLocators.job_button)
        self.click_element(OrangeHRMLocators.job_options)
        self.click_element(OrangeHRMLocators.add_job_button)
        time.sleep(5)
        self.enter_text(OrangeHRMLocators.job_title, "ASST.Consultant")
        self.enter_text(OrangeHRMLocators.job_desc, "consultant work for emp details")
        self.click_element(OrangeHRMLocators.job_save_button)
        #return JobPage(self.driver)

    def leave(self):
        self.click_element(OrangeHRMLocators.leave_button)
        self.click_element(OrangeHRMLocators.leave_status_dropdown)
        time.sleep(2)
        self.click_element(OrangeHRMLocators.leave_status)
        self.click_element(OrangeHRMLocators.leave_type)
        self.click_element(OrangeHRMLocators.leave_type_dropdown) 
        time.sleep(2)
        self.click_element(OrangeHRMLocators.search_button)


        

