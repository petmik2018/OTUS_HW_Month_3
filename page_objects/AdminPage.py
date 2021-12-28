from selenium.webdriver.common.by import By
import time

from .BasePage import BasePage


class AdminPage(BasePage):
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.btn.btn-primary')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '.fa-sign-out')
    CATALOG = (By.ID, "menu-catalog")
    NAVIGATION = (By.ID, 'navigation')
    MENU = (By.ID, 'menu')
    PRODUCTS_LINK = (By.LINK_TEXT, "Products")
    FILTER_ICON = (By.CSS_SELECTOR, '[data-original-title="Filter"]')
    FORM_PRODUCTS = (By.ID, "form-product")
    INPUT_NAME = (By.ID, "input-name")
    SUBMIT_FILTER = (By.ID, "button-filter")
    TBODY_TAG = (By.TAG_NAME, 'tbody')
    TD_TAG = (By.TAG_NAME, 'td')
    TR_TAG = (By.TAG_NAME, 'tr')

    def open(self):
        self._open('admin')
        return self

    def login_admin(self):
        self._click_element(self.LOGIN_BUTTON)
        return self

    def logout_admin(self):
        self._click_element(self.LOGOUT_BUTTON)

    def verify_navigation(self):
        self._find_element(self.NAVIGATION)

    def verify_menu(self):
        self._find_element(self.MENU)

    def go_to_products_list(self):
        self._click_element(self.CATALOG)
        self._click_element(self.PRODUCTS_LINK)

    def get_products_quantity(self):
        return len(BasePage(self.browser)._find_list_of_elements(self.TR_TAG))

    def get_product_name(self, number):
        form_products = self._find_element(self.FORM_PRODUCTS)
        products_block = self._find_element_in_element(form_products, self.TBODY_TAG)
        products = self._find_list_of_elements_in_element(products_block, self.TR_TAG)
        titles = self._find_list_of_elements_in_element(products[number-1], self.TD_TAG)
        return titles[2].text

    def open_filter_form(self):
        self._find_element(self.FORM_PRODUCTS)
        try:
            self._find_element(self.INPUT_NAME)
        except:
            self._click_element(self.FILTER_ICON)
        return self

    def fill_name_field(self, data):
        self._click_element(self.INPUT_NAME).send_keys(data)
        return self

    def submit_filter(self):
        self._click_element(self.SUBMIT_FILTER)
