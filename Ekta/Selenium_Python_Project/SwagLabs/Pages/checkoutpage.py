from Base.base import BasePage
from .locators import Locators

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def proceed_to_checkout(self):
        """Clicks checkout from the cart view."""
        self.click_element(Locators.CHECKOUT_BUTTON)

    def fill_checkout_information(self, first_name, last_name, postal_code):
        """Fills out the shipping details information form."""
        self.enter_text(Locators.FIRST_NAME_FIELD, first_name)
        self.enter_text(Locators.LAST_NAME_FIELD, last_name)
        self.enter_text(Locators.POSTAL_CODE_FIELD, postal_code)
        self.click_element(Locators.CONTINUE_BUTTON)

    def finish_checkout(self):
        """Clicks the final finish button on the overview summary screen."""
        self.click_element(Locators.FINISH_BUTTON)

    def get_success_message(self):
        """Returns the final completion text header (e.g., 'Thank you for your order!')."""
        element = self.get_element(Locators.COMPLETE_HEADER)
        return element.text