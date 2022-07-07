from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class ContactUsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    FirstNameFld = (By.ID, 'FirstName')
    LastName_Fld = (By.ID, 'LastName')
    EMail_Fld = (By.ID, 'EmailAddress')
    PhoneNumber_FLd = (By.ID, 'PhoneNumber')
    TimeToCall_Fld = (By.ID, 'BestTimeToCallYou')
    HelpOption_Fld = (By.ID, 'ReasonForEnquiry')



    def enterFirstName(self, firstName):
        self.do_send_keys(self.FirstNameFld, firstName)


    def enterLastName(self, lastName):
        self.do_send_keys(self.LastName_Fld, lastName)


    def enterEMail(self, email):
        self.do_send_keys(self.EMail_Fld, email)


    def enterMobileNumber(self, mobileNumber):
        self.do_send_keys(self.PhoneNumber_FLd, mobileNumber)


    def enterTimeTOCall(self, time):
        self.do_send_keys(self.TimeToCall_Fld, time)



    def selectHowToHelp(self, visibleText):
        self.selectByVisibleTextFromDrpDwn(self.HelpOption_Fld, visibleText)

