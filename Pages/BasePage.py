from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def selectByVisibleTextFromDrpDwn(self, by_locator, visible_text):
        select = Select(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)))
        select.select_by_visible_text(visible_text)

    def do_send_keys(self, by_locator, keys):
        element  = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        element.send_keys(keys)
