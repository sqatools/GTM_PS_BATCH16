from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#expected_conditions is a class which has many methods to wait for elements to be present or clickable. we can use these methods to wait for elements to be present or clickable. we can use these methods in our base class to wait for elements to be present or clickable. we can use these methods in our page classes to wait for elements to be present or clickable. we can use these methods in our test classes to wait for elements to be present or clickable.

class BasePage:
    def __init__(self, driver): # this driver is chrome driver. external driver 
        self.driver = driver # right side driver is chrome driver object which is passed from test case to page class and then to base class
        self.wait = WebDriverWait(driver, 10) # creating a wait object to wait for elements to be present or clickable
        # we provide driver as parameter here becuase wait should know where to wait for 10 seconds. so we provide driver object to wait object. wait object will use this driver to wait for elements to be present or clickable

  
    def click_element(self, locator): # i can use here address as variable name instaed of locator . but then below code change accordingly. so better to use locator as variable name because we are passing locator as parameter to this method.  
        element = self.wait.until(EC.element_to_be_clickable(locator))
        #self.wait.until(EC.element_to_be_clickable(locator)).click() also correct but we are storing element in variable so that we can use it later if needed. if we dont store it in variable then we cant use it later. so better to store it in variable.
        #element=self.wait.until(EC.element_to_be_clickable(address))) 
        # if element is clickable in 2 sec then it will return element and not waited for 10 sec. if element is not clickable in 10 sec then it will throw exception.
       
        element.click()

    def enter_text(self, locator, text):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_title(self):
        return self.driver.title
    
    def get_element(self, locator):
        """Finds and returns an element after waiting for its presence."""
        return self.wait.until(EC.presence_of_element_located(locator))
    

# class BasePage:
#     def __init__(self, driver): 
#         self.driver1 = driver  

#     def get_title(self):
#         return self.driver1.title 
# we always need to use self keyword whenever we are writing any method inside c class.