import pytest

from ProtoCommerce_UI_Test.PageObjects.Delivery_Add import delivery_Address
from ProtoCommerce_UI_Test.PageObjects.LoginPageObject import LoginPage
from ProtoCommerce_UI_Test.PageObjects.Shop import shop


@pytest.mark.usefixtures("browserInstance")
class  TestloginPurchase:

    def test_login(self):
        login = LoginPage(self.driver)
        login.loginActions()
        print("Login success, Title: ", login.get_title())

    def test_getProducts(self):
        e2ePurchase = shop(self.driver)
        e2ePurchase.Purchaseproducts("Nokia Edge")

    def test_deliveryLoction(self):
        location= delivery_Address(self.driver)
        location.Dynamic_Cuntry_input("India")
