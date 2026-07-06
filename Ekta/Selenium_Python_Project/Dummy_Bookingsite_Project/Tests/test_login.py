import pytest
import time
from Pages.loginpage import LoginPage
@pytest.mark.usefixtures("get_driver_class") #due to this selenium knows that to run get_driver_class fixture before running the test cases in this class   
class TestLogIn:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, get_driver_class):
        self.driver = get_driver_class
        self.login_pageobj = LoginPage(self.driver)
        print("Test setup initiated")

    def test_login_flow(self):
        # 1. Click on the login link
        self.login_pageobj.click_login_link()
        time.sleep(4)

        # 2. Enter login credentials and submit
        self.login_pageobj.enter_login_details(username="9890284293", password="Nandai@143")
        time.sleep(2)

        self.login_pageobj.enter_second_logindetails(second_sername="9890284293", second_password="Nandai@143")
        time.sleep(2)

        expected_error_message = "Error: The username 9890284293 is not registered on this site. If you are unsure of your username, try your email address instead."
        actual_error_message = self.login_pageobj.get_error_message_text()
        assert actual_error_message == expected_error_message, f"Expected error message: '{expected_error_message}', but got: '{actual_error_message}'"     



  