from selenium.webdriver.common.by import By

class DummyLocators:
    fromCityField = (By.ID, "fromcity")
    DestCityField = (By.ID, "destcity")

    DepartDate = (By.NAME, "departdate")
    ReturnDate = (By.NAME, "returndate")

    PageHeading = (By.CLASS_NAME, "entry-title")