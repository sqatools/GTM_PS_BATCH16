from selenium.webdriver.common.by import By

class DummyLocators:
    #Dummy booking  booking website locators 
    visa_radio_1 = (By.XPATH, "//input[@value='radio_123']")
    visa_radio_2 = (By.XPATH, "//input[@value='radio_345']")

    firstnameField = (By.ID, "firstname")
    lastnameField = (By.XPATH, "//span[contains(text(), 'Last Name')]/following-sibling::input[1]")

    DOB = (By.ID, "birthday")

    male_radio_btn = (By.ID, "male")
    female_radio_btn = (By.ID, "female")

    passenger_dropdown = (By.ID, "admorepass")

    tripField = (By.ID, "roundtrip")

    fromCityField = (By.ID, "fromcity")
    DestCityField = (By.ID, "destcity")

    departDate = (By.NAME, "departdate")
    returnDate = (By.NAME, "returndate")

    PageHeading = (By.CLASS_NAME, "entry-title")

    contry_dropdown = (By.ID, "billing_country")

    second_row_checkbox = (By.XPATH, "(//input[@value='checkbox'])[2]")