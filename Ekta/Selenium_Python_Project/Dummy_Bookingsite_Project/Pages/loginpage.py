
import time

from Base.base import BasePage
from Pages.locators import Locators
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    
    def click_login_link(self):
        time.sleep(5)
        self.click_element(Locators.login_link)
        time.sleep(3)

         # teeling driver to switch to new tab and perform action on new tab opened after clicking on login link
        handles= self.driver.window_handles # it creates list of all the tabs opened in browser and stores in handles variable
        self.driver.switch_to.window(handles[1])
        print("Switched to new window")

            
    def enter_login_details(self, username, password):
        self.enter_text(Locators.email_username, username)
        self.enter_text(Locators.email_password, password) 
        self.click_element(Locators.login_button)
    
    def enter_second_logindetails(self,second_sername,second_password):
        self.enter_text(Locators.second_username,second_sername)
        self.enter_text(Locators.second_password,second_password)
        self.click_element(Locators.second_login_button)    

    def get_error_message_text(self):
        element = self.wait.until(EC.presence_of_element_located(Locators.error_message))
        return element.text