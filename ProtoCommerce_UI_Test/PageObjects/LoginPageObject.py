from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common_Utils.generic_utils import BrowserUtils

class LoginPage(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.UserName_field = (By.NAME, 'username')
        self.Password_field = (By.NAME, 'password')
        self.TnC_check = (By.ID,'terms')
        self.signin_btn =(By.XPATH, "//input[@class='btn btn-info btn-md']")


    def loginActions(self):
        self.driver.find_element(*self.UserName_field).send_keys('rahulshettyacademy')
        self.driver.find_element(*self.Password_field).send_keys('learning')
        self.driver.find_element(*self.TnC_check).click()
        self.driver.find_element(*self.signin_btn).click()

        try:
            # Handle alert popup (JavaScript alert)
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            print("Alert Text:", alert.text)
            alert.accept()
        except:
            print("No alert appeared.")

        #Explicit wait for redirection or specific element on next page
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//h1[normalize-space()='Shop Name']")))


