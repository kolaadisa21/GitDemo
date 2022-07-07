import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
'''URL'''
CONTACTUS_URL = 'https://www.mortgageadvicebureau.com/contact-us'

'''Input Fields'''
FirstNameFld = (By.ID, 'FirstName')
LastName_Fld = (By.ID, 'LastName')
EMail_Fld = (By.ID, 'EmailAddress')
PhoneNumber_FLd = (By.ID, 'PhoneNumber')
TimeToCall_Fld = (By.ID, 'BestTimeToCallYou')
HelpOption_Fld = (By.ID, 'ReasonForEnquiry')
'''Keys'''
FIRST_NAME = 'Gregory'
LAST_NAME = 'Anderson'
EMAIL_ADDRESS = 'greg.anderson@gmail.com'
MOBILE_NO = '07989694894'
TIME_TO_CALL = '7:00 PM'
HELP_OPTIONS = 'I’m moving home'


driver = ''

def setup():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(CONTACTUS_URL)
    driver.maximize_window()
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Allow all cookies')))
    element.click()





def sendKeys(bylocator, keys):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(bylocator)).send_keys(keys)

def selectByVisibleTextFromDrpDwn(bylocator, visible_text):
        select = Select(WebDriverWait(driver, 10).until(EC.visibility_of_element_located(bylocator)))
        select.select_by_visible_text(visible_text)

setup()
sendKeys(FirstNameFld, FIRST_NAME)
sendKeys(LastName_Fld, LAST_NAME)
sendKeys(EMail_Fld, EMAIL_ADDRESS)
sendKeys(PhoneNumber_FLd, MOBILE_NO)
sendKeys(TimeToCall_Fld, TIME_TO_CALL)
selectByVisibleTextFromDrpDwn(HelpOption_Fld, HELP_OPTIONS)
time.sleep(3)
driver.quit()

