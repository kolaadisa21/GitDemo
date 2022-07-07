import time

from Data.ContactUsTestData import ContactUsTestData
from Pages.ContactUsPage import ContactUsPage
from Tests.BaseTest import BaseTest


class Test_ContactPage(BaseTest):
    def test_Fill_Contact_Us_Form(self):
        contactUs = ContactUsPage(self.driver)
        contactUs.enterFirstName(ContactUsTestData.FIRST_NAME)
        contactUs.enterLastName(ContactUsTestData.LAST_NAME)
        contactUs.enterEMail(ContactUsTestData.EMAIL_ADDRESS)
        contactUs.enterMobileNumber(ContactUsTestData.MOBILE_NO)
        contactUs.enterTimeTOCall(ContactUsTestData.TIME_TO_CALL)
        contactUs.selectHowToHelp(ContactUsTestData.HELP_OPTIONS)
        time.sleep(3)