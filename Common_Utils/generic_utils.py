from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BrowserUtils:
    def __init__(self, driver):
        self.driver = driver


    def get_title(self):
        return self.driver.title

    def click_when_ready(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()


