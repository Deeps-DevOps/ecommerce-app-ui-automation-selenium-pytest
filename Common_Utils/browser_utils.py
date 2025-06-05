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

    # to check the label with specific text is present or not
    def is_element_text_present(self, locator):
        """
        Checks whether the given locator is present and has visible text.
        Returns True if found and has non-empty text, else False.
        """
        try:
            element = self.driver.find_element(*locator)
            return bool(element.text.strip())
        except:
            return False


