import pytest, time
import Project.Pages.orange_hrm_page as orange_hrm_page



@pytest.mark.usefixtures("get_driver_class")
class TestOrangeHRM:

    @pytest.fixture(autouse=True)
    def setup(self, get_driver_class):
        self.orange_hrm_page = orange_hrm_page.OrangeHRMPage(self.driver)

    def test_login(self):
        self.orange_hrm_page.login("Admin", "admin123")
        self.orange_hrm_page.log.info("Login successful")
        time.sleep(5)

    #verification
    # Calling your page helper method inside an assert block
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        assert self.orange_hrm_page.verify_login_successful(expected_url) == True, "Login verification failed: Current URL does not match dashboard!"
       
        self.orange_hrm_page.add_user(role_name="Admin", status="Enabled", employee_name="Ranga Akunuri")
        time.sleep(5)
        self.orange_hrm_page.job_add()
        self.orange_hrm_page.leave()