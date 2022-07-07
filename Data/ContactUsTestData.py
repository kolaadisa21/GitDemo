from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager


class ContactUsTestData:
    CONTACTUS_URL = 'https://www.mortgageadvicebureau.com/contact-us'
    CHROME_EXECUTABLE_PATH = '\Driver\chromedriver.exe'
    FIREFOX_EXECUTABLE_PATH = '\Driver\geckodriver.exe'
    # EDGE_DRIVER = driver = webdriver.Edge(EdgeChromiumDriverManager().install())


    FIRST_NAME = 'Gregory'
    LAST_NAME = 'Anderson'
    EMAIL_ADDRESS = 'greg.anderson@gmail.com'
    MOBILE_NO = '07989694894'
    TIME_TO_CALL = '7:00 PM'
    HELP_OPTIONS = 'I’m moving home'