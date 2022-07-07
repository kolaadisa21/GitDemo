import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from Data.ContactUsTestData import ContactUsTestData


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )

@pytest.fixture(scope='class')
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=ContactUsTestData.CHROME_EXECUTABLE_PATH)

    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=ContactUsTestData.FIREFOX_EXECUTABLE_PATH)

    # elif browser == 'edge':
    #     driver = ContactUsTestData.EDGE_DRIVER

    driver.get(ContactUsTestData.CONTACTUS_URL)
    driver.maximize_window()
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Allow all cookies')))
    element.click()


    request.cls.driver = driver

    yield
    driver.quit()
