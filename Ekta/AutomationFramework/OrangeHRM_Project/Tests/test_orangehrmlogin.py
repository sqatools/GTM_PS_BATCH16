import pytest
import time
#from utilities.utils import Utils
from Pages.myinfopage import MyInfoPage
from Pages.loginpage import LoginPage

@pytest.mark.usefixtures("get_driver_class")
class TestOrangeHRM:    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.lp = LoginPage(self.driver)
        self.mi = MyInfoPage(self.driver)
        print("Test setup initiated")

    def test_login_to_orangehrm(self):
        self.lp.login_to_application(username="Admin", password="admin123")
        time.sleep(5)
    
  
    def test_update_my_info(self):
        """Test case to login, navigate to My Info, and update personal details."""
        # 1. Login
        self.lp.login_to_application(username="Admin", password="admin123")
        
        # 2. Navigate to My Info
        self.mi.navigate_to_my_info()
        
        # 3. Update Details
        self.mi.update_personal_details(
            first_name="John", 
            middle_name="Robert", 
            last_name="Doe"
        )
        time.sleep(3)