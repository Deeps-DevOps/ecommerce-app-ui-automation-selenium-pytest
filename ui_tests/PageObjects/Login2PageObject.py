from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Common_Utils.browser_utils import BrowserUtils
from Common_Utils.config_reader import ConfigReader
from selenium.webdriver.common.by import By

from Common_Utils.excel_utils import ExcelUtils


class LoginPageBase(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.config = ConfigReader()

        self.category_page1_link= (By.XPATH,"//a[@class='list-group-item' and text()='Category 1']")
        self.page_name =(By.XPATH, "//a[normalize-space()='ProtoCommerce']")
        self.name_text=(By.XPATH,"//label[normalize-space()='Name']")
        self.username_field = (By.XPATH, "(//input[@class='form-control ng-untouched ng-pristine ng-invalid'])[1]")
        self.email_text = (By.XPATH,"//label[normalize-space()='Email']")
        self.email_validation_msg = (By.XPATH,"//div[normalize-space()='Email is required']")
        self.email= (By.NAME,"email")
        self.password_text=(By.XPATH,"//label[normalize-space()='Password']")
        self.password= (By.XPATH, "//input[@type='password']")
        self.checkbox_text= (By.XPATH, "//input[@id='exampleCheck1']//..//label[normalize-space()='Check me out if you Love IceCreams!']")
        self.icecream_checkbox = (By.XPATH,"//input[@type='checkbox']")
        self.gender_text = (By.XPATH, "//label[normalize-space()='Gender']")
        self.gender_option_female= (By.XPATH, "//select[@id='exampleFormControlSelect1']/option[text()='Female']")
        self.employee_status_text = (By.XPATH,"//label[normalize-space()='Employment Status:']")
        self.employee_status_employed_redio_button =(By.XPATH,"//label[normalize-space()='Employed']//..//input[@type='radio']")
        self.DOB_text=(By.XPATH,"//label[normalize-space()='Date of Birth']")
        self.enter_DOB =(By.XPATH,"//input[@type='date']")
        self.success_message=(By.XPATH, "//div[contains(@class, 'alert-success') and contains(., 'The Form has been submitted successfully')]")
        self.submit_button=(By.XPATH,"//input[@type='submit']")


    def login_details(self):

        self.driver.find_element(*self.category_page1_link).click()

        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='ProtoCommerce']")))


        file_path = "/Users/deeps-devops/Documents/Python_Projects/ProtoCommerce_Test/Test_Data/ProtoCommerce_login_data.xlsx"
        test_data = ExcelUtils.read_excel_as_dicts(file_path)

        for user in test_data:
            # Fill in the form fields
            assert self.is_element_text_present(self.name_text), "'Name' label not present on the page"
            self.driver.find_element(*self.username_field).click()
            self.driver.find_element(*self.username_field).send_keys(user['Name'])

            assert self.is_element_text_present(self.email_text), "'Email' label not present on the page"
            self.driver.find_element(*self.email).click()
            self.driver.find_element(*self.email).send_keys(user['Email'])

            assert self.is_element_text_present(self.password_text), "'Password' label not present on the page"
            self.driver.find_element(*self.password).click()
            self.driver.find_element(*self.password).send_keys(user['Password'])

            assert self.is_element_text_present(self.checkbox_text), "'Check me out if you Love IceCreams!' label not present on the page"
            self.driver.find_element(*self.icecream_checkbox).click()

            assert self.is_element_text_present(self.gender_text), "'Gender' label not present on the page"
            self.driver.find_element(*self.enter_DOB).click()
            self.driver.find_element(*self.gender_option_female).click()

            assert self.is_element_text_present(self.employee_status_text), "'Employment Status' label not present on the page"
            self.driver.find_element(*self.employee_status_employed_redio_button).click()

            assert self.is_element_text_present(self.DOB_text), "'Date of Birth' label not present on the page"
            self.driver.find_element(*self.enter_DOB).click()
            self.driver.find_element(*self.enter_DOB).send_keys(user['DOB'].strftime("%d-%m-%y"))

            self.driver.find_element(*self.submit_button).click()

            # validate success message
            success = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(self.success_message)
            )
            assert "successfully" in success.text, "Form submission failed"