import pytest
from Pages.loginpage import LoginPage
from Pages.Inventorypage import InventoryPage
from Pages.checkoutpage import CheckoutPage 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.mark.usefixtures("get_driver_class")
class Testswaglabs: 
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.lp = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
        print("Test setup initiated")
    
    def test_login_to_swaglabs(self):
        self.lp.login_to_application(username="visual_user", password="secret_sauce")
        time.sleep(5)
        # Handle possible popup/alert using Selenium instead of pyautogui
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except Exception:
            try:
                body = self.driver.find_element(By.TAG_NAME, 'body')
                body.send_keys(Keys.ENTER)
            except Exception:
                # no alert or body interaction possible; continue
                pass
    
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
            first_name="Jwewl", 
            last_name="Mishra", 
            postal_code="753014"
        )
        time.sleep(4)

        # 3. Finish order on 'Checkout: Overview'
        self.checkout_page.finish_checkout()
        time.sleep(4)

        # 4. Verify checkout order completion status
        success_text = self.checkout_page.get_success_message()
        assert "Thank you for your order!" in success_text, f"Checkout failed! Got message: {success_text}"