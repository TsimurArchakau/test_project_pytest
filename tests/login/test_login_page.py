import allure
import pytest

from source_code.pages.base_helpers import BaseHelpers
from source_code.pages.login.login_page import LoginPage
from source_code.pages.main.main_page import MainPage


class TestLoginPage:
    @allure.feature('Login')
    @allure.story('Login with valid data')
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        base_helpers = BaseHelpers()

        user_email, user_password = base_helpers.load_credentials()
        login_page.make_authorization(user_email, user_password)

        with allure.step('Ensure that login is performed sucсessfully'):
            assert login_page.content_title.text() == "Zamówienia", 'Login failed.'

        login_page.logout_from_account()

    @allure.feature('Login')
    @allure.story('User login with invalid data')
    @pytest.mark.parametrize('user_email, user_password', [['violataranova@gmail1.com', 'Viola123!'],
                                                           ['violataranova@gmail.com', '12345678']])
    def test_user_authorization_with_invalid_data(self, driver, user_email, user_password):
        login_page = LoginPage(driver)

        login_page.make_authorization(user_email, user_password)
        with allure.step('Ensure that error message is displayed'):
            assert login_page.error_message.text() == 'Login lub hasło nie zostało rozpoznane. Spróbuj ponownie.', 'Error message is not displayed'

        login_page.close_button.click()

    @allure.feature('Login')
    @allure.story('Logout from account')
    def test_logout(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        base_helpers = BaseHelpers()

        user_email, user_password = base_helpers.load_credentials()
        login_page.make_authorization(user_email, user_password)

        login_page.logout_from_account()
        with allure.step('Ensure that redirection to the main page is performed'):
            assert main_page.driver.current_url == 'https://www.hebe.pl/home', 'Redirection to the main page is not performed'
