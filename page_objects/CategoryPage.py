from selenium.webdriver.common.by import By
from .BasePage import BasePage


class CategoryPage(BasePage):
    DESKTOPS_CATEGORY_URL = "index.php?route=product/category&path=20"
    LAPTOPS_CATEGORY_URL = "index.php?route=product/category&path=18"
    COMPONENTS_CATEGORY_URL = "index.php?route=product/category&path=25"
    TABLETS_CATEGORY_URL = "index.php?route=product/category&path=57"
    PRODUCTS_LIST = (By.CLASS_NAME, 'product-layout')
    PRODUCT_CATEGORY = (By.ID, 'product-category')
    LEFT_MENU = (By.ID, 'column-left')
    CONTENT = (By.ID, 'content')
    INFO = (By.CLASS_NAME, 'text-right')

    def open_desktops_category(self):
        self._open(self.DESKTOPS_CATEGORY_URL)
        return self

    def open_laptops_category(self):
        self._open(self.LAPTOPS_CATEGORY_URL)
        return self

    def open_components_category(self):
        self._open(self.COMPONENTS_CATEGORY_URL)
        return self

    def open_tablets_category(self):
        self._open(self.TABLETS_CATEGORY_URL)
        return self

    def verify_left_menu(self):
        self._find_element(self.LEFT_MENU)
        return self

    def verify_product_category(self):
        self._find_element(self.PRODUCT_CATEGORY)
        return self

    def verify_content(self):
        self._find_element(self.CONTENT)
        return self

    def verify_products_list(self):
        assert self._find_list_of_elements(self.PRODUCTS_LIST)
        return self

    def verify_products_quantity(self):
        products_qty = len(self._find_list_of_elements(self.PRODUCTS_LIST))
        content = self._find_element(self.CONTENT)
        information = self._find_element_in_element(content, self.INFO).text
        quantity_info = int(information.split(' ')[5])
        assert products_qty == quantity_info
