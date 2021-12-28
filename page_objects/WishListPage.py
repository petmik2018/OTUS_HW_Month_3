from selenium.webdriver.common.by import By

from .BasePage import BasePage


class WishListPage(BasePage):
    TOP_LINKS = (By.ID, 'top-links')
    WISH_LIST_TOTAL = (By.ID, 'wishlist-total')
    REMOVE_BUTTON = (By.CSS_SELECTOR, '[data-original-title="Remove"]')
    COLUMN_RIGHT = (By.ID, 'column-right')
    LOGOUT_LINK = (By.LINK_TEXT, 'Logout')

    def remove_first_product(self):
        self._click_element(self.REMOVE_BUTTON)
        return self

    def get_text_from_wishlist_link(self):
        top_links = self._find_element(self.TOP_LINKS)
        wish_list_link = self._find_element_in_element(top_links, self.WISH_LIST_TOTAL)
        return self._find_element_in_element(wish_list_link, (By.TAG_NAME, 'span')).text

    def logout(self):
        column_right = self._find_element(self.COLUMN_RIGHT)
        self._find_element_in_element(column_right, self.LOGOUT_LINK).click()
        return self
