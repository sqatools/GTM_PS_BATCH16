from selenium.webdriver.common.by import By

class OrangeHRMLocators:
    #login locators
    username_field = (By.XPATH, "//input[@placeholder='Username']")
    password_field = (By.XPATH, "//input[@placeholder='Password']")
    login_button = (By.XPATH, "//button[normalize-space()='Login']")

    #admin page locators
    #Admin_page_link = (By.XPATH, "//span[text()='Admin']/parent::a")
    admin_menu = (By.XPATH, "//span[normalize-space()='Admin']")
    add_button = (By.XPATH, "//button[normalize-space()='Add']")
    user_role_dropdown = (By.XPATH, "//label[text()='User Role']//parent::div/parent::div//div[text()='-- Select --']")
    user_admin_role_options = (By.XPATH, "//span[text()='Admin']")

    #employee_name_field = (By.XPATH, "//label[text()='Employee Name']//parent::div/parent::div//input")

    employee_name_field = (By.XPATH, "//input[@placeholder='Type for hints...']")

    status_dropdown = (By.XPATH, "//div[@class='oxd-select-text-input'][normalize-space()='-- Select --']")

    user_username = (By.XPATH, "//label[text()='Username']//parent::div/following-sibling::div/input")

    user_password = (By.XPATH, "//input[@type='password']")

    user_confirm_password = (By.XPATH, "(//input[@type='password'])[2]")

    save_button = (By.XPATH,  "//button[normalize-space()='Save']")

    #job loactors
    job_button = (By.XPATH, "//span[normalize-space()='Job']")
    job_options = (By.XPATH, "//a[normalize-space()='Job Titles']")
    add_job_button = (By.XPATH, "//button[normalize-space()='Add']")
    job_title = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
    job_desc = (By.XPATH, "//textarea[@placeholder='Type description here']")
    job_save_button = (By.XPATH, "//button[normalize-space()='Save']")


    #leave locators
    leave_button = (By.XPATH,  "//span[normalize-space()='Leave']")
    leave_from = (By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[1]")    
    leave_to = (By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[2]")
    leave_status_dropdown = (By.XPATH, "//div[@class='oxd-select-text-input'][normalize-space()='-- Select --']")
    leave_status = (By.XPATH, "//div[contains(@class, 'oxd-select-option')]//span[text()='Rejected']")
    leave_type = (By.XPATH, "(//div[@class='oxd-select-text-input'][normalize-space()='-- Select --'])[2]")
    leave_type_dropdown = (By.XPATH, "//span[text()='CAN - Bereavement']")
    search_button = (By.XPATH, "//button[normalize-space()='Search']")
    




