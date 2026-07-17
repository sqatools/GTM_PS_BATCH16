from selenium import webdriver

from selenium.webdriver.common.by import By

class Element_locator:

    fromcity = (By.XPATH,"//input[@name='fromcity']")
    descity = (By.XPATH,"//input[@name='destcity']")
    drpart_date = (By.XPATH,"//input[@name='departdate']")
    return_date = (By.XPATH,"//input[@name='returndate']")
    text_field = (By.XPATH,"//h1[text()='Dummy Booking Website']")

    click_field = (By.LINK_TEXT,"Home")

    male_radio = (By.ID,"male")
    female_radio = (By.ID,"female")
    drop_down_1 = (By.XPATH,"//select[@id='admorepass']")
    drop_down_2 = (By.XPATH,"//select[@id='billing_country']")

    



    

    