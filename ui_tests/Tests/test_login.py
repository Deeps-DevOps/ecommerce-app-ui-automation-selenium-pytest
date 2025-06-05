import allure
import pytest

from ui_tests.PageObjects.Login2PageObject import LoginPageBase
from ui_tests.PageObjects.LoginPageObject import LoginPage


@pytest.mark.usefixtures("browserInstance")
class TestLogin_details:

    @pytest.mark.login
    @allure.feature("Login Feature")
    @allure.story("Valid login scenario")
    def test_login(self):
        LoginPage(self.driver).login_with_valid_credentials()
        LoginPageBase(self.driver).login_details()
