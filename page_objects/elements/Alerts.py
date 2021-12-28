import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..BasePage import BasePage


class SuccessAlert(BasePage):
    ALERT_SUCCESS = (By.CLASS_NAME, 'alert-success')
    LOGIN = 'login'
    SHOPPING_CART = 'shopping cart'

    def source_alert_success(self, action_text):
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.ALERT_SUCCESS))
        self._click_element((By.LINK_TEXT, action_text))
        time.sleep(1)

    def click_login(self):
        self.source_alert_success(self.LOGIN)

    def click_shopping_cart(self):
        self.source_alert_success(self.SHOPPING_CART)
