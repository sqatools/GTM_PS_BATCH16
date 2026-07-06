import time

from Base.base import BasePage
from Pages.locators import Locators


class BookingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def select_option(self):
        self.click_element(Locators.option) # here we are calling click_element method so no nned to pass self keyword.
        # In python while defining method we need to pass self keyword but while calling method we don't need to pass self keyword.
        # while calling function we need to use self. but dont need to pass self as parameter. self is automatically passed when we call method using self keyword.
       #self.baseclassmethod(Name of locator class.locatorname(variable name of locator in locators.py file )) 
      
       

    def enter_booikng_details(self, first_name, last_name, d_o_b):
        self.enter_text(Locators.firstname, first_name)
        self.enter_text(Locators.lastname, last_name)
        self.enter_text(Locators.dob, d_o_b)

    def select_gender(self, gender):
        if gender.lower() == "male":
            self.click_element(Locators.gendermale)  # Assuming Locators.gendermale is the male radio button locator
        elif gender.lower() == "female":
            self.click_element(Locators.genderfemale)  # Assuming Locators.genderfemale is the female radio button locator  


    