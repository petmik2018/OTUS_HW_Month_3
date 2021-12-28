from selenium.webdriver.common.by import By

from .BasePage import BasePage
from .elements.UserLoginForm import UserLoginForm


class UserPage(BasePage):
    PAYMENT_NEW = (By.ID, "payment-new")
    WISH_LIST = (By.LINK_TEXT, "Wish List")

    def login_with(self, username, password):
        UserLoginForm(self.browser).login_with(username, password)
        return self

    def go_to_wish_list(self):
        self._click_element(self.WISH_LIST)
