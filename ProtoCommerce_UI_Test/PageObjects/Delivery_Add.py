import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Common_Utils.generic_utils import BrowserUtils


class delivery_Address(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver= driver
        self.countryInputField =(By.XPATH,"//input[@id='country']")
        self.TnC_CheckBox=(By.XPATH,"//div[@class='checkbox checkbox-primary']")
        self.btn_purchase = (By.XPATH,"//input[@type='submit']")
        self.Success_msg=(By.XPATH,"//div[@class='alert alert-success alert-dismissible']")


    def Dynamic_Cuntry_input(self,country):
        print("Typing country...")

        country_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.countryInputField)
        )
        country_input.clear()
        country_input.send_keys(country)

        # Build dynamic locator
        country_xpath = (By.XPATH, f"//li/a[normalize-space()='{country}']")
        print("Waiting for dropdown suggestion...")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(country_xpath)
        ).click()
        print("✅Country clicked")

        time.sleep(1)


        print("Waiting for T&C checkbox...")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.TnC_CheckBox)
        ).click()
        print("✅ T&C checkbox clicked")

        print("Waiting for Purchase button...")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.btn_purchase)
        ).click()
        print("✅ Purchase button clicked")

        success=self.driver.find_element(*self.Success_msg).text
        assert "Success! Thank you!" in success
        print("✅ Order is Successful")

