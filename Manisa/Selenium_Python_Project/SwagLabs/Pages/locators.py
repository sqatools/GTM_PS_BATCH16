from selenium.webdriver.common.by import By

class Locators:
    username_field= (By.ID, "user-name")
    password_field = (By.ID, "password")
    login_button = (By.ID, "login-button")
    

# Products / Inventory Page Locators
    ADD_BACKPACK_BUTTON = (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']")
    ADD_TSHIRT_BUTTON = (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-bolt-t-shirt']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

# Cart & Checkout Page Locators
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")