import pytest, time
import page_objects.OrangeHRM.orange_hrm_page as orange_hrm_page


@pytest.mark.usefixtures("get_driver_class")
class TestOrangeHRM:

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.orange_hrm_page = orange_hrm_page.OrangeHRMPage(self.driver)

    def test_login(self):
        self.orange_hrm_page.Navigate_to_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.orange_hrm_page.login("Admin", "admin123")
        self.orange_hrm_page.log.info("Login successful")
        self.orange_hrm_page.add_user(role_name="Admin", status="Enabled", employee_name="Ravi MB")
        time.sleep(5)