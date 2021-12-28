import allure
import pytest

from page_objects.AdminPage import AdminPage
from page_objects.MainPage import MainPage
from page_objects.CategoryPage import CategoryPage
from page_objects.ProductPage import ProductPage
from page_objects.UserPage import UserPage
from page_objects.WishListPage import WishListPage
from page_objects.CartPage import CartPage
from page_objects.elements.Alerts import SuccessAlert


@allure.feature('WishList Page')
@allure.story('Adding product to wish list')
@allure.title('Add one product to wishlist')
def test_add_product_to_wish_list(browser, number=2):
    main_page = MainPage(browser).open()
    product_name = main_page.get_featured_product_name(number)
    main_page.click_featured_product(number)
    ProductPage(browser).add_to_wish_list()
    SuccessAlert(browser).click_login()
    UserPage(browser)\
        .login_with("test2@mail.ru", "test")\
        .go_to_wish_list()
    WishListPage(browser)\
        .logout()\
        .go_to_main_page()
    CartPage(browser).verify_product(product_name)


@allure.feature('Main Page')
@allure.story('Finding main page elements')
@allure.title('Finding main page elements')
def test_main_page_elements(browser):
    page = MainPage(browser).open()
    page.verify_top()
    page.verify_top_links()
    page.verify_common_home()
    page.verify_content()
    page.verify_slideshow()
    page.verify_featured_products()


@allure.feature('Admin Page')
@allure.story('Elements existing tests')
@allure.title('Finding admin page elements')
def test_admin_navigation(browser):
    page = AdminPage(browser).open()
    page.login_admin()
    page.verify_navigation()
    page.verify_menu()
    page.logout_admin()


@allure.feature('Category Page')
@allure.story('Elements existing tests')
@allure.title('Finding category page elements')
def test_category(browser):
    page = CategoryPage(browser)
    page.open_components_category()
    page.verify_product_category()
    page.verify_left_menu()
    page.verify_content()
    page.verify_products_list()
    page.verify_products_quantity()


@allure.feature('Admin Page')
@allure.story('Filtering products list test')
@allure.title('Filter products list by name of the first product')
def test_admin_filter_products(browser, url):
    page = AdminPage(browser).open()
    page\
        .login_admin()\
        .go_to_products_list()
    featured_product_name = page.get_product_name(1)
    page\
        .open_filter_form()\
        .fill_name_field(featured_product_name)\
        .submit_filter()
    filtered_product_name = page.get_product_name(1)
    page.logout_admin()
    assert filtered_product_name == featured_product_name


@allure.feature('WishList Page')
@allure.story('Deleting product from wish list')
@allure.title('Delete one product from wishlist')
def test_delete_product_from_wish_list(browser):
    MainPage(browser)\
        .open()\
        .go_to_wish_list()
    UserPage(browser).login_with("test2@mail.ru", "test")
    WishListPage(browser).remove_first_product()


@allure.feature('WishList Page')
@allure.story('Deleting product from empty wish list')
@allure.title('Fail expected')
@pytest.mark.skip(reason="Wishlist is empty")
@allure.issue('Products quantity in wishlist not checked before deleting')
def test_delete_product_from_wish_list_to_fail(browser):
    MainPage(browser)\
        .open()\
        .go_to_wish_list()
    UserPage(browser).login_with("test2@mail.ru", "test")
    WishListPage(browser).remove_first_product()



