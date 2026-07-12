from Base.Base import Base_page
from Pages.locators import Locators


class BookingPage(Base_page):

    def __init__(self, driver):
        super().__init__(driver)

    def select_option(self):
        self.click_element(Locators.option_button)
      
    def enter_booikng_details(self, first_name, last_name, d_o_b):
        self.enter_text(Locators.firstname, first_name)
        self.enter_text(Locators.lastname, last_name)
        self.enter_text(Locators.dob, d_o_b)

    def select_gender(self, gender):
        if gender.lower() == "male":
            self.click_element(Locators.gendermale)  
        elif gender.lower() == "female":
            self.click_element(Locators.genderfemale) 

    