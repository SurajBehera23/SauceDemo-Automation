import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key


# browser selction on runtime
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Specify the browser: chrome or firefox or edge")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# Use pytest --browser=chrome,pytest --browser=firefox or pytest --browser=edge for cross browser
@pytest.fixture()
def setup_driver(request, browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser")

    request.cls.driver = driver
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver
    driver.close()


###########for pytest html reports ###########
#hook for adding environment info in html report
def pytest_configure(config):
   config.stash[metadata_key] ['Project Name'] = 'Ecommerce Project, SauceDemo'
   config.stash[metadata_key]['Test Module Name'] = 'Login Tests'
   config.stash[metadata_key]['Tester Name'] = 'Suraj'
#
# #hook for delete/modify environment info in html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
   metadata.pop('JAVA_HOME',None)
   metadata.pop('Plugins', None)
