from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .BasePage import BasePage


class CartPage(BasePage):
    BUTTONS = (By.CSS_SELECTOR, ".buttons")
    CHECKOUT_LINK = (By.LINK_TEXT, "Checkout")

    def go_to_checkout(self):
        self.browser.find_element(*self.BUTTONS).find_element(*self.CHECKOUT_LINK).click()

    def verify_product(self, product_name):
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
        return self
