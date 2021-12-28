from selenium.webdriver.common.by import By

from .BasePage import BasePage


class ProductPage(BasePage):
    ADD_TO_WISH_LIST_BUTTON = (By.CSS_SELECTOR, '[data-original-title="Add to Wish List"]')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#button-cart')

    def add_to_wish_list(self):
        self._click_element(self.ADD_TO_WISH_LIST_BUTTON)

    def add_to_cart(self):
        self._click_element(self.ADD_TO_CART_BUTTON)