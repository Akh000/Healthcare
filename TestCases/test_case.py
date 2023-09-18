import time
import openpyxl
from PageObject.PageRegistration import Appoint
from Utilities import Xutil
from Utilities.Logger import LogGenerator


class Test_Register:
    XlPath = "D:\\Python\\Revision 1\\OpenCart-Pytest\\TestData\\Reg.xlsx"
    log = LogGenerator.loggen()

    def test_case_001(self, setup):
        self.log.info("Web Browser Started..")
        self.driver = setup
        self.log.info("Open Website..")
        self.ap = Appoint(self.driver)
        self.log.info("Click on Appointment Button")
        self.ap.click_on_appointment()
        self.log.info("Enter Username..")
        self.ap.enter_username("John Doe")
        self.log.info("Enter Password..")
        self.ap.enter_password("ThisIsNotAPassword")
        self.log.info("Click on Login Button..")
        self.ap.click_on_login_button()
        self.row = Xutil.RowCount(self.XlPath, 'Sheet1')
        if self.driver.title == "CURA Healthcare Service":
            for r in range(2, self.row+1):
                self.facility = Xutil.ReadData(self.XlPath, 'Sheet1', r, 2)
                self.healthcare = Xutil.ReadData(self.XlPath, 'Sheet1', r, 3)
                self.visit_date = Xutil.ReadData(self.XlPath, 'Sheet1', r, 4)
                self.visit_date = str(self.visit_date)
                self.comment = Xutil.ReadData(self.XlPath, 'Sheet1', r, 5)
                print("login Successfully")
                self.log.info("Select Facility Option..")
                self.ap.select_facility(self.facility)
                self.log.info("Select Readmission Checkbox..")
                self.ap.click_checkbox_readmission()
                self.log.info("Select Healthcare Program Radio Button..")
                self.ap.click_checkbox_healthcare_program(self.healthcare)
                self.log.info("Choose Visit Date..")
                self.ap.input_visit_date(self.visit_date)
                self.log.info("Write down general comment..")
                self.ap.input_comment(self.comment)
                self.log.info("Enter Book Appointment Button..")
                self.ap.enter_book_appointment()
                self.log.info("Print Appointment Details For All Process..")
                self.ap.get_text()
                # ls = []
                # ls.append(facility)
                self.ap.click_on_goto_homepage()
                self.log.info("Click on Appointment Button")
                self.ap.click_on_appointment()
                time.sleep(3)
                # if self.driver.title == "CURA Healthcare Service":
                #     assert True
                # else:
                #     self.driver.save_screenshot("D:\\Python\\Revision 1\\OpenCart-Pytest\\Screenshot\\fail.png")
                #     assert False
            self.driver.save_screenshot("D:\\Python\\Revision 1\\OpenCart-Pytest\\Screenshot\\Login_successful.png")
            assert True
        else:
            self.driver.save_screenshot("D:\\Python\\Revision 1\\OpenCart-Pytest\\Screenshot\\LoginFail.png")
            assert False
