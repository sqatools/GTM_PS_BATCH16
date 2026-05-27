import pytest
import time
from Pages.loginpage import LoginPage
from Pages.JobTitlePage import JobTitlePage

@pytest.mark.usefixtures("get_driver_class")
class TestOrangeHRM:    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.lp = LoginPage(self.driver)
        self.job_title_page = JobTitlePage(self.driver)
        print("Test setup initiated")
       
    def test_login_to_orangehrm(self):
        self.lp.login_to_application(username="Admin", password="admin123")
       # self.lp.login_to_application.log.info("Login successful")
        time.sleep(3)  
     
   
    def test_add_user(self):
        self.lp.add_user(

            role_name="ESS", 
            status="Disabled", 
            employee_name="Ranga  Akunuri",
            admin_username="Tester0000",
            admin_password="@Tetser12345",
            admin_confirm_password="@Tetser12345",
         
        )
    #something is incorrect here need to check it again      
    def test_add_job_title(self):
        self.job_title_page = self.lp.click_on_job_title()
        time.sleep(5)
    
   
    def test_fill_job_title_form(self):
        self.job_title_page.add_new_job_title(
            job_title="Automation Engineer L1",  
            description="Responsible for developing and maintaining automated test scripts to ensure software quality.",
            file_path="C:\\Users\\User_Resume.docx",
            note="This is a critical role for our QA team."     
        )
        time.sleep(8)
        
    
     
