from Base.base import BasePage
from .locators import Locators

class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def add_backpack_to_cart(self):
        self.click_element(Locators.ADD_BACKPACK_BUTTON)

    def add_tshirt_to_cart(self):
        self.click_element(Locators.ADD_TSHIRT_BUTTON)

    def get_cart_count(self):
        """Returns the number of items currently displayed on the cart badge."""
        # Using get_element because we are reading text, not clicking it
        badge = self.get_element(Locators.CART_BADGE)
        return badge.text

    def navigate_to_cart(self):
        self.click_element(Locators.CART_ICON)