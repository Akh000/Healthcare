import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Appoint:
    appointment_xpath = (By.ID, "btn-make-appointment")
    username_name = (By.NAME, "username")
    password_name = (By.NAME, "password")
    login_button_xpath = (By.XPATH, "//button[@id='btn-login']")
    facility_xpath = (By.XPATH, "//select[@id='combo_facility']")
    hospital_read_adm_xpath = (By.XPATH, "//input[@id='chk_hospotal_readmission']")
    healthcare_program_xpath = (By.XPATH, "//input[@id='radio_program_medicare']")
    healthcare_program_xpath2 = (By.XPATH, "//input[@id='radio_program_medicaid']")
    healthcare_program_xpath3 = (By.XPATH, "//input[@id = 'radio_program_none']")
    visit_date_xpath = (By.XPATH, "//input[@id='txt_visit_date']")
    comment_xpath = (By.XPATH, "//textarea[@id='txt_comment']")
    book_appointment_xpath = (By.XPATH, "//button[@id='btn-book-appointment']")
    text_facility_xpath = (By.XPATH, "//p[@id='facility']")
    text_readmission_xpath = (By.XPATH, "//p[@id='hospital_readmission']")
    text_healthcare_program_xpath = (By.XPATH, "//p[@id='program']")
    text_visit_date_xpath = (By.XPATH, "//p[@id='visit_date']")
    text_comment_xpath = (By.XPATH, "//p[@id='comment']")
    goto_homepage_button_xpath = (By.XPATH, "//a[@class='btn btn-default']")

    def __init__(self, driver):
        self.driver = driver

    def click_on_appointment(self):
        self.driver.find_element(*Appoint.appointment_xpath).click()

    def enter_username(self, username):
        self.driver.find_element(*Appoint.username_name).send_keys(username)

    def enter_password(self, pwd):
        self.driver.find_element(*Appoint.password_name).send_keys(pwd)

    def click_on_login_button(self):
        self.driver.find_element(*Appoint.login_button_xpath).click()

    def select_facility(self, healthcare_facility):
        facility = Select(self.driver.find_element(*Appoint.facility_xpath))
        if healthcare_facility == 0:
            facility.select_by_index(0)
        elif healthcare_facility == 1:
            facility.select_by_index(1)
        else:
            facility.select_by_index(2)

    def click_checkbox_readmission(self):
        self.driver.find_element(*Appoint.hospital_read_adm_xpath).click()

    def click_checkbox_healthcare_program(self, healthcare_program):
        if healthcare_program == "Medicare":
            self.driver.find_element(*Appoint.healthcare_program_xpath).click()
        elif healthcare_program == "Medicaid":
            self.driver.find_element(*Appoint.healthcare_program_xpath2).click()
        else:
            self.driver.find_element(*Appoint.healthcare_program_xpath3).click()

    def input_visit_date(self, visit_date):
        self.driver.find_element(*Appoint.visit_date_xpath).send_keys(visit_date)

    def input_comment(self, comment):
        self.driver.find_element(*Appoint.comment_xpath).send_keys(comment)

    def enter_book_appointment(self):
        self.driver.find_element(*Appoint.book_appointment_xpath).click()

    def get_text(self):
        time.sleep(3)
        facility = (self.driver.find_element(*Appoint.text_facility_xpath)).text
        read_mission = (self.driver.find_element(*Appoint.text_readmission_xpath)).text
        healthcare = (self.driver.find_element(*Appoint.text_healthcare_program_xpath)).text
        visit_date = (self.driver.find_element(*Appoint.text_visit_date_xpath)).text
        comment = (self.driver.find_element(*Appoint.text_comment_xpath)).text
        print("Facility                             ", facility)
        print("Apply for Hospital Readmission       ", read_mission)
        print("Healthcare Program                   ", healthcare)
        print("Visit Date                           ", visit_date)
        print("Comment                              ", comment)

    def click_on_goto_homepage(self):
        self.driver.find_element(*Appoint.goto_homepage_button_xpath).click()
