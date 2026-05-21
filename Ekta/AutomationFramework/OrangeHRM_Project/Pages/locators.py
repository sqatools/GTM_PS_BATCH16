from selenium.webdriver.common.by import By


class Locators:
    #locators for Login Page
    username_field = (By.NAME, "username")

    password_field = (By.NAME, "password")

    login_btn = (By.XPATH, "//button[@type='submit']")
   
    # --- My Info Page Locators ---
    # Robust XPATH targets the menu anchor directly regardless of DOM depth variations
    my_info_tab = (By.XPATH, "//a[contains(@href, 'viewMyDetails')]")
    
    first_name_field = (By.NAME, "firstName")
    middle_name_field = (By.NAME, "middleName")
    last_name_field = (By.NAME, "lastName")
    
    # Highly resilient locator targeting the first submit button within the personal details form section
    personal_details_save_btn = (By.XPATH, "(//button[@type='submit'])[1]")