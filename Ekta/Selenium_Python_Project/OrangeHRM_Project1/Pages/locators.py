from selenium.webdriver.common.by import By


class Locators:
    #locators for Login Page
    username_field = (By.NAME, "username")

    password_field = (By.NAME, "password")

    login_btn = (By.XPATH, "//button[@type='submit']")
    #Admin module locators
    admin_btn=(By.XPATH, "//span[text()='Admin']") # qn -sir used link admin_page link but i used button
    add_btn=(By.XPATH, "//button[normalize-space()='Add']")
    user_role_dropdown=(By.XPATH, "//label[text()='User Role']//parent::div/parent::div//div[text()='-- Select --']")
    user_admin_role_options = (By.XPATH, "//div[@role='option']//span[text()='Admin']")
    user_status_dropdown=(By.XPATH, "//label[text()='Status']//parent::div/parent::div//div[text()='-- Select --']")
    employee_name_field = (By.XPATH, "//label[text()='Employee Name']//parent::div/parent::div//input")
    # User creation input fields
    admin_username_field=(By.XPATH, "//label[text()='Username']//parent::div/parent::div//input")
    admin_password_field=(By.XPATH, "//label[text()='Password']//parent::div/parent::div//input")
    admin_confirm_password_field=(By.XPATH, "//label[text()='Confirm Password']//parent::div/parent::div//input")
    save_btn = (By.XPATH, "//button[@type='submit']")
    
    #locators for Job
    job_btn=(By.XPATH, "//span[text()='Job ']") # 
    job_title_btn=(By.XPATH, "//a[text()='Job Titles']")
    job_title_add_btn=(By.XPATH, "//button[contains(., 'Add')]")

    # locators for Add Job Title Page
    job_title_input = (By.XPATH, "//label[text()='Job Title']/parent::div/following-sibling::div/input")
    job_description_textarea = (By.XPATH, "//label[text()='Job Description']/parent::div/following-sibling::div/textarea")
    job_specification_upload = (By.XPATH, "//input[@type='file']")
    job_note_textarea = (By.XPATH, "//label[text()='Note']/parent::div/following-sibling::div/textarea")
    job_save_btn = (By.XPATH, "//button[@type='submit']")
    job_cancel_btn = (By.XPATH, "//button[text()=' Cancel ' or normalize-space()='Cancel']")
  
    # locators for Time and Reports 
    time_btn = (By.XPATH, "//span[text()='Time' or normalize-space()='Time']")
    reports_btn = (By.XPATH, "//span[text()='Reports' or normalize-space()='Reports']")
    employee_reports_option = (By.XPATH, "//ul[@class='oxd-dropdown-menu']//a[text()='Employee Reports']")

    #  Employee Report locators 
    report_employee_name_field = (By.XPATH, "//label[text()='Employee Name']/parent::div/following-sibling::div//input")
    report_project_name_field = (By.XPATH, "//label[text()='Project Name']/parent::div/following-sibling::div//input")
    report_activity_dropdown = (By.XPATH, "//label[text()='Activity Name']/parent::div/following-sibling::div//div[contains(@class, 'select-text')]")
    
    # Date Range Locators 
    report_from_date = (By.XPATH, "//label[text()='From']/parent::div/following-sibling::div//input")
    report_to_date = (By.XPATH, "//label[text()='To']/parent::div/following-sibling::div//input")
    
    # View Report Button
    report_view_btn = (By.XPATH, "//button[@type='submit' or normalize-space()='View']")


    
   
