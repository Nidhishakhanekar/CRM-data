import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture
def Setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif browser == 'edge':
        driver = webdriver.Edge()
        driver.maximize_window()
    else:
        driver = webdriver.Firefox()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    return driver


@pytest.fixture(params=
                [('Admin', 'admin'),
                 ('admin', 'admin123'),
                 ('admins', 'admkins'),
                 ('Admin', 'admin123')
                 ])
def getdataforlogin(request):
    return request.param
