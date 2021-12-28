from selenium.webdriver.common.by import By
from .BasePage import BasePage


class MainPage(BasePage):
    TOP = (By.ID, 'top')
    TOP_LINKS = (By.ID, 'content')
    COMMON_HOME = (By.ID, 'common-home')
    CONTENT = (By.ID, 'content')
    SLIDESHOW = (By.ID, 'slideshow0')
    FEATURE_PRODUCTS = (By.CLASS_NAME, 'product-layout')
    FEATURE_PRODUCT_NAME = (By.CSS_SELECTOR, '.caption h4 a')
    GO_TO_WISHLIST = (By.ID, 'wishlist-total')

    def open(self):
        self._open()
        return self

    def verify_top(self):
        self._find_element(self.TOP)

    def verify_top_links(self):
        self._find_element(self.TOP_LINKS)

    def verify_common_home(self):
        self._find_element(self.COMMON_HOME)

    def verify_content(self):
        self._find_element(self.CONTENT)

    def verify_slideshow(self):
        content = self._find_element(self.CONTENT)
        self._find_element_in_element(content, self.SLIDESHOW)

    def verify_featured_products(self):
        content = self._find_element(self.CONTENT)
        if self._find_list_of_elements_in_element(content, self.FEATURE_PRODUCTS):
            assert True
        else:
            AssertionError("Featured products list not found")

    def get_featured_product_by_number(self, number):
        index = number - 1
        content = self._find_element(self.CONTENT)
        products_list = self._find_list_of_elements_in_element(content, self.FEATURE_PRODUCTS)
        if number > len(products_list):
            raise AssertionError("Out of range in list by locator: {}".format(self.FEATURE_PRODUCTS))
        else:
            return products_list[index]

    def get_featured_product_name(self, number):
        featured_product = self.get_featured_product_by_number(number)
        product_name = self._find_element_in_element(featured_product, self.FEATURE_PRODUCT_NAME).text
        return product_name

    def click_featured_product(self, number):
        featured_product = self.get_featured_product_by_number(number)
        featured_product.click()
        return self

    # def go_to_all_laptops(self):
    #     nav_menu = self.browser.find_element(*self.MAIN_MENU)
    #     nav_menu.find_elements(*self.DROPDOWN_MENU_LIST)[1].click()
    #     self.browser.find_elements(*self.OPENED_DROPDOWN_MENU)[2].click()

    def go_to_wish_list(self):
        self._click_element(self.GO_TO_WISHLIST)
