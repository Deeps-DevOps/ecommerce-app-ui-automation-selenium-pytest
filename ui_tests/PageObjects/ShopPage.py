import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Common_Utils.browser_utils import BrowserUtils


class ShopPage(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

        self.page_title = (By.XPATH, "//h1[normalize-space()='Shop Name']")
        self.products = (By.XPATH, "//div[@class='card h-100']")
        self.product_name =(By.XPATH, "div/h4/a")
        self.checkout_button= (By.XPATH,"//a[@class='nav-link btn btn-primary']")
        self.add_to_cart_button = (By.XPATH,".//button[normalize-space()='Add']")
        self.cart_checkout_button = (By.XPATH, "//button[@type='button' and normalize-space()='Checkout']")



    def add_product_and_checkout(self, product_name_to_buy):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.products)
        )

        product_elements =self.driver.find_elements(*self.products)

        for product in product_elements :
            # Fetch product name using relative XPath
            product_name = product.find_element(*self.product_name).text
            print(f"Found product: {product_name}")
            if product_name == product_name_to_buy:
                product.find_element(*self.add_to_cart_button).click()
                break

        # Now click checkout button after adding product
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, f"//h4[@class='media-heading']/a[normalize-space()='{product_name_to_buy}']"))
        )

        self.driver.find_element(*self.cart_checkout_button).click()





