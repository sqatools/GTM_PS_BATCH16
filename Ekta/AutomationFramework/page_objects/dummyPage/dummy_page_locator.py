from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys

class DummyLocators:
    fromCityField = (By.ID, "fromcity")
    DestCityField = (By.ID, "destcity")

    DepartDate = (By.NAME, "departdate")
    ReturnDate = (By.NAME, "returndate")

    PageHeading = (By.CLASS_NAME, "entry-title")
  # PageHeading2 = (Keys.class_name, "entry-title")

    female_radio_btn = (By.ID, "female")
    
    passenger_dropdown = (By.ID, "admorepass")

    contry_dropdown = (By.ID, "billing_country")