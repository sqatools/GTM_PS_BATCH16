from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver): # constructor method to initialize the driver and wait objects
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def get_element(self, locator):
        """Finds and returns an element after waiting for its presence."""
        # visibility_of_element_located is EC class method which will wait until the element is visible on the page before returning it
        return self.wait.until(EC.visibility_of_element_located(locator)) # This will wait until the element is visible on the page before returning it
      
    def get_clickable_element(self, locator):
        """Use this specifically for clicking."""
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    
    def click_element(self, locator):
        element = self.get_clickable_element(locator) # use the get_clickable_element method for clickable elements
        element.click()

    def enter_text(self, locator, value):
        element = self.get_clickable_element(locator) # this is correct get_element check visibilty of element
        element.clear() # clear the existing text before entering new text
        element.send_keys(value)
    
    def get_present_element(self, locator):
        """Finds a hidden or structural element after waiting for its presence in the DOM."""
        return self.wait.until(EC.presence_of_element_located(locator))

    
