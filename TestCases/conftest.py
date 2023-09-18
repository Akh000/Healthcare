import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser')


@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')


@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'edge':
        driver = webdriver.Edge()
    # elif browser == 'firefox':
    #     options = Options()
    #     options.binary_location = ""
    #     driver = webdriver.Firefox(options=options)
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com")
    return driver