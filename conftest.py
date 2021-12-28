import os
import pytest

from selenium import webdriver

DRIVERS = os.path.expanduser("~/Downloads/drivers")


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox", "opera"])
    parser.addoption("--executor", action="store", default="10.0.0.138")
    parser.addoption("--url", action="store", default="https://demo.opencart.com/")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    url = request.config.getoption("--url")
    test_name = request.node.name

    if executor == "local":
        caps = {'goog:chromeOptions': {}}
        driver = webdriver.Chrome(
            executable_path=f"{DRIVERS}/chromedriver",
            desired_capabilities=caps
        )

    else:
        executor_url = f"http://{executor}:4444/wd/hub"
        caps = {
            "browserName": browser,
            'goog:chromeOptions': {}
        }
        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps
        )

    def fin():
        driver.quit()

    # driver.maximize_window()
    driver.base_url = url
    driver.test_name = test_name

    request.addfinalizer(fin)
    return driver
