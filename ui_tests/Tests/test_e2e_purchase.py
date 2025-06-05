import pytest
from ui_tests.PageObjects.LoginPageObject import LoginPage
from ui_tests.PageObjects.ShopPage import ShopPage
from ui_tests.PageObjects.DeliveryAddressPage import DeliveryAddressPage


@pytest.mark.usefixtures("browserInstance")
class TestE2EPurchase:

    def test_complete_purchase_flow(self):
        LoginPage(self.driver).login_with_valid_credentials()
        ShopPage(self.driver).add_product_and_checkout("Nokia Edge")
        DeliveryAddressPage(self.driver).enter_country_and_complete_order("India")
