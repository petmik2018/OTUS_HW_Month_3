import logging
import inspect
import allure

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    GO_HOME = (By.CLASS_NAME, 'fa-home')
    LOGGER_FORMAT ='%(asctime)s  - %(levelname)s - %(name)s - %(method_name)s - %(message)s'
    LOG_LEVEL = logging.ERROR

    def __init__(self, browser):
        self.browser = browser
        self.base_url = browser.base_url
        self.__config_logger()

    def __config_logger(self):
        old_factory = logging.getLogRecordFactory()

        def record_factory(*args, **kwargs):
            record = old_factory(*args, **kwargs)
            # record.method_name = self.__method_name(6)
            record.method_name = inspect.stack()[6][3]
            return record

        logging.setLogRecordFactory(record_factory)

        self.logger = logging.getLogger(type(self).__name__)
        formatter = logging.Formatter(self.LOGGER_FORMAT)
        f = logging.FileHandler(f"logs/{self.browser.test_name}.log")
        f.setFormatter(formatter)
        self.logger.addHandler(f)
        self.logger.setLevel(level=self.LOG_LEVEL)

    def __method_name(self, index):
        return inspect.stack()[index][3]

    def __make_screenshot(self):
        self.browser.save_screenshot(f'logs/{inspect.stack()[3][3]}.png')

    def _open(self, path=""):
        url = self.base_url + path
        self.logger.info(f"Opening url: {url}")
        with allure.step(f"Opening url: {url}"):
            self.browser.get(url)

    @allure.step("Click to element {locator}")
    def _click_element(self, locator):
        self.logger.info(f"Clicking element: {locator}")
        try:
            element = WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(locator))
            element.click()
        except TimeoutException:
            self.logger.error(f"Error with clicking element: {locator}")
            self.__make_screenshot()
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name=f"{self.browser.current_url}",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Cant find element by locator: {locator}")
        return element

    @allure.step("Find element {locator}")
    def _find_element(self, locator):
        self.logger.info(f"Finding element: {locator}")
        try:
            element = WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.logger.error(f"Error with finding element: {locator}")
            self.__make_screenshot()
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name=f"{self.browser.current_url}",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError("Cant find element: {}".format(locator))
        return element

    @allure.step("Find list of to elements {locator}")
    def _find_list_of_elements(self, locator):
        self.logger.info(f"Finding list of elements: {locator}")
        try:
            elements_list = WebDriverWait(self.browser, 2).until(EC.visibility_of_any_elements_located(locator))
        except TimeoutException:
            self.logger.error(f"Error with finding list of elements: {locator}")
            self.__make_screenshot()
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name=f"{self.browser.current_url}",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Cant find elements by locator: {locator}")
        return elements_list

    @allure.step("Find element {locator} inside parent element")
    def _find_element_in_element(self, element, locator: tuple):
        self.logger.info(f"Finding element {locator} inside the parent element")
        time_limit = 2
        delta_time = 0.1
        curr_time = 0
        while True:
            if curr_time > time_limit:
                self.logger.error(f"Error with finding element: {locator} inside the mother element")
                self.__make_screenshot()
                allure.attach(
                    body=self.browser.get_screenshot_as_png(),
                    name=f"{self.browser.current_url}",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(f"Cant find elements by locator: {locator}")
            try:
                sub_element = element.find_element(*locator)
                return sub_element
            except NoSuchElementException:
                curr_time += delta_time

    @allure.step("Find list of elements {locator} inside parent element")
    def _find_list_of_elements_in_element(self, element, locator: tuple):
        self.logger.info(f"Finding list of element by locator {locator} inside the parent element")
        time_limit = 2
        delta_time = 0.1
        curr_time = 0
        while True:
            if curr_time > time_limit:
                self.logger.error(f"Error with finding list of elements: {locator} inside the mother element")
                self.__make_screenshot()
                allure.attach(
                    body=self.browser.get_screenshot_as_png(),
                    name=f"{self.browser.current_url}",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(f"Cant find list of elements by locator: {locator}")
            elements_list = element.find_elements(*locator)
            if elements_list:
                return elements_list
            else:
                curr_time += delta_time

    @allure.step("Go to main page")
    def go_to_main_page(self):
        self._click_element(self.GO_HOME)
