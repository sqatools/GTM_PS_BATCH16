import pytest
from Pages.loginpage import LoginPage
from Pages.Inventorypage import InventoryPage
from Pages.checkoutpage import CheckoutPage 
import time
#import pyautogui

@pytest.mark.usefixtures("get_driver_class")
class Testswaglabs: 
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.lpobj = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver) #self.driver is working here because we written self.cls.drover=driver in conftest.py file and we are using get_driver_class fixture in this test class    
        self.checkout_page = CheckoutPage(self.driver)
        print("Test setup initiated")
    
    def test_login_to_swaglabs(self):
        self.lpobj.login_to_application(username="visual_user", password="secret_sauce")
        time.sleep(5)
        pyautogui.press('enter') # used this for pop up alert which is not allowing to click on login button and move forward to inventory page
    
    def test_add_elements_to_cart(self):
        self.inventory_page.add_backpack_to_cart()
        self.inventory_page.add_tshirt_to_cart()
        cart_count = self.inventory_page.get_cart_count()
        assert cart_count == "2", f"Expected cart count to be 2, but got {cart_count}"
        self.inventory_page.navigate_to_cart()     
        time.sleep(4) 

    def test_complete_checkout_flow(self):
        # 1. Start Checkout from Cart page
        self.checkout_page.proceed_to_checkout()

        # 2. Fill details on 'Checkout: Your Information'
        self.checkout_page.fill_checkout_information(
            first_name="Ekta", 
            last_name="Gund", 
            postal_code="123456789"
        )
        time.sleep(4)

        # 3. Finish order on 'Checkout: Overview'
        self.checkout_page.finish_checkout()
        time.sleep(4)

        # 4. Verify checkout order completion status
        success_text = self.checkout_page.get_success_message()
        assert "Thank you for your order!" in success_text, f"Checkout failed! Got message: {success_text}"