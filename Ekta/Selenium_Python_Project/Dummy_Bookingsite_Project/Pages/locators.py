from selenium.webdriver.common.by import By


class Locators:
  #booking website locators 
  option = (By.XPATH,"//input[@value='radio_558']")
  firstname = (By.ID,"firstname")
  lastname= (By.XPATH,"//text()[contains(., 'Last Name')]/following::input[1]")
  dob = (By.ID,"birthday")
  genderfemale = (By.ID,"female")
  gendermale = (By.ID,"male")
  #login locators 
  login_link=(By.XPATH,"(//a[text()='Login Page'])[1]")
  email_username=(By.XPATH,"(//input[@id='email'])[1]")
  email_password=(By.XPATH,"//input[@id='pass']")
  login_button=(By.XPATH,"(//button[@id='loginbutton'])")
  #second login page locators 
  second_username=(By.XPATH,"//input[@id='user_login']")
  second_password=(By.XPATH,"//input[@id='user_pass']") 
  second_login_button=(By.XPATH,"//input[@id='wp-submit']")
  error_message=(By.XPATH,"//div[@id='login_error']")


  