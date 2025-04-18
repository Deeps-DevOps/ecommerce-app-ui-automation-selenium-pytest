import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Common_Utils.generic_utils import BrowserUtils


class shop(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.PageName = (By.XPATH, "//h1[normalize-space()='Shop Name']")
        self.listofproducts = (By.XPATH, "//div[@class='card h-100']")
        self.ProductName =(By.XPATH, "div/h4/a")
        self.btn_checkout= (By.XPATH,"//a[@class='nav-link btn btn-primary']")
        self.btn_AddtoCart = (By.XPATH,".//button[normalize-space()='Add']")
        self.btn_cartcheckout = (By.XPATH, "//button[@type='button' and normalize-space()='Checkout']")



    def Purchaseproducts(self, product_to_buy):
        products =self.driver.find_elements(*self.listofproducts)

        for product in products:
            # Fetch product name using relative XPath
            NameoftheProduct = product.find_element(*self.ProductName).text
            print("Found product:", NameoftheProduct)

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(self.listofproducts)
            )

            if NameoftheProduct.strip() == product_to_buy:
                # Click the Add button relative to this product
                product.find_element(*self.btn_AddtoCart).click()

        # Now click checkout button after adding product
        self.driver.find_element(*self.btn_checkout).click()

        time.sleep(3)

        # Wait until Nokia Edge is visible in cart page
        WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, f"//h4[@class='media-heading']/a[normalize-space()='{product_to_buy}']")))

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.btn_cartcheckout)).click()






