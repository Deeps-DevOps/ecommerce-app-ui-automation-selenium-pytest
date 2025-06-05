import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Common_Utils.browser_utils import BrowserUtils


class DeliveryAddressPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver= driver

        self.country_input =(By.XPATH,"//input[@id='country']")
        self.terms_checkbox=(By.XPATH,"//div[@class='checkbox checkbox-primary']")
        self.purchase_button = (By.XPATH,"//input[@type='submit']")
        self.success_message=(By.XPATH,"//div[@class='alert alert-success alert-dismissible']")


    def enter_country_and_complete_order(self,country_name):
        print("Typing country...")

        input_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.country_input)
        )
        input_field.clear()
        input_field.send_keys(country_name)

        # Dynamic country suggestion
        country_suggestion = (By.XPATH, f"//li/a[normalize-space()='{country_name}']")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(country_suggestion)
        ).click()
        print("Country clicked")

        print("Waiting for T&C checkbox...")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.terms_checkbox)
        ).click()
        print("Terms checkbox clicked")

        print("Waiting for Purchase button...")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.purchase_button)
        ).click()
        print("Purchase button clicked")

        success_text = self.driver.find_element(*self.success_message).text
        assert "Success! Thank you!" in success_text
        print("Order was successful")

