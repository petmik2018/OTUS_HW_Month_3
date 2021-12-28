from selenium.webdriver.common.by import By
from ..BasePage import BasePage


class UserLoginForm(BasePage):
    INPUT_EMAIL = (By.ID, 'input-email')
    INPUT_USERNAME = (By.ID, 'input-username')
    INPUT_PASSWORD = (By.ID, 'input-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'input[value=Login]')

    def fill_input_field_with_locator(self, locator, data):
        BasePage._click_element(self, locator).send_keys(data)

    def login_with(self, username, password):
        self.fill_input_field_with_locator(self.INPUT_EMAIL, username)
        self.fill_input_field_with_locator(self.INPUT_PASSWORD, password)
        self.browser.find_element(*self.LOGIN_BUTTON).click()

