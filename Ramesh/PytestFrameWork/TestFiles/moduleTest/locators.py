from selenium.webdriver.common.by import By

class DummyLocators:
    fromCityField = (By.ID, "fromcity")
    DestCityField = (By.ID, "destcity")

    DepartDate = (By.NAME, "departdate")
    ReturnDate = (By.NAME, "returndate")

    PageHeading = (By.CLASS_NAME, "entry-title")


    male_radio_btn = (By.ID, "male")


    passenger_dropdown = (By.ID, "admorepass")

    contry_dropdown = (By.ID, "billing_country")