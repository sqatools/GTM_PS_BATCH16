from selenium.webdriver.common.by import By

class OrangeHRMLocators:
    username_field = (By.XPATH, "//input[@placeholder='Username']")
    password_field = (By.XPATH, "//input[@placeholder='Password']")
    login_btn = (By.XPATH, "//button[normalize-space()='Login']")

    # Admin Module Locators
    Admin_page_link = (By.XPATH, "//span[text()='Admin']/parent::a")
    add_button = (By.XPATH, "//button[normalize-space()='Add']")
    user_role_dropdown = (By.XPATH, "//label[text()='User Role']//parent::div/parent::div//div[text()='-- Select --']")
    user_admin_role_options = (By.XPATH, "//div[@role='option']//span[text()='Admin']")
    status_dropdown = (By.XPATH, "//label[text()='Status']//parent::div/parent::div//div[text()='-- Select --']")
    employee_name_field = (By.XPATH, "//label[text()='Employee Name']//parent::div/parent::div//input")
