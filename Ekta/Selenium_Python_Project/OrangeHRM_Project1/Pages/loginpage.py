from Base.base import BasePage
from Pages.adminpage import Adminpage
from .locators import Locators
from selenium.webdriver.common.by import By
import time
from Pages.JobTitlePage import JobTitlePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver) #Initialize the parent class first
        self.locator = Locators()


    def login_to_application(self, username, password):
       
        self.enter_text(self.locator.username_field, username)
         
        self.enter_text(self.locator.password_field, password)
        self.click_element(self.locator.login_btn)
        # Return the next page object so you can chain actions in your test
        # return Adminpage(self.driver)

    def add_user(self,role_name,status,employee_name,admin_username,admin_password,admin_confirm_password):
        self.click_element(self.locator.admin_btn)
        self.click_element(Locators.add_btn)
        self.click_element(Locators.user_role_dropdown)
        #self.click_element(Locators.user_admin_role_options)
        user_admin_role_options=(By.XPATH, f"//div[@role='option']//span[text()='{role_name}']")
        self.click_element(user_admin_role_options)
        self.click_element(Locators.user_status_dropdown)
        status_options=(By.XPATH, f"//div[@role='option']//span[text()='{status}']")
        self.click_element(status_options)
        self.enter_text(Locators.employee_name_field, employee_name)
        time.sleep(3)
        empl_options = (By.XPATH, f"//div[@role='option']//span[text()='{employee_name}']")
        time.sleep(3)
        self.click_element(empl_options)
        self.enter_text(Locators.admin_username_field,admin_username)
        self.enter_text(Locators.admin_password_field,admin_password)
        self.enter_text(Locators.admin_confirm_password_field,admin_confirm_password)
        self.click_element(self.locator.save_btn)
        time.sleep(5)
    
    def click_on_job_title(self):
        self.click_element(Locators.job_btn)
        self.click_element(Locators.job_title_btn)
        time.sleep(2)
        self.click_element(Locators.job_title_add_btn)
        time.sleep(2)
        return JobTitlePage(self.driver)
    
    # Return the JobTitlePage object chaining

 

   

   

   


