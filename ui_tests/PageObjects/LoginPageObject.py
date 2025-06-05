from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common_Utils.browser_utils import BrowserUtils
from Common_Utils.config_reader import ConfigReader


class LoginPage(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.config = ConfigReader()

        self.UserName_field = (By.NAME, 'username')
        self.Password_field = (By.NAME, 'password')
        self.TnC_check = (By.ID,'terms')
        self.signin_btn =(By.XPATH, "//input[@class='btn btn-info btn-md']")

    def login_with_valid_credentials(self):
        url = self.config.get_url()
        self.driver.get(url)
        username = self.config.get_username()
        password = self.config.get_password()

        wait = WebDriverWait(self.driver, 10)

        self.driver.find_element(*self.UserName_field).send_keys(username)
        self.driver.find_element(*self.Password_field).send_keys(password)
        self.driver.find_element(*self.TnC_check).click()
        self.driver.find_element(*self.signin_btn).click()

        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            print("Alert Text:", alert.text)
            alert.accept()
        except:
            print("No alert appeared.")

        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//h1[normalize-space()='Shop Name']"))
        )