import allure
import pytest
from selenium import webdriver

from source_code.pages.base_helpers import BaseHelpers
from source_code.pages.favorites.favorites_page import FavoritesPage
from source_code.pages.login.login_page import LoginPage
from source_code.pages.main.main_page import MainPage


@pytest.fixture(scope='class', autouse=True)
@allure.step('Open main page, accept_cookies, go to login page and make a login')
def suite_setup(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    base_helpers = BaseHelpers()

    main_page.open()
    main_page.accept_cookies()
    main_page.go_to_login_page()
    user_email, user_password = base_helpers.load_credentials()
    login_page.make_authorization(user_email, user_password)


@pytest.fixture(scope='function', autouse=True)
@allure.step('Go to main page')
def test_teardown(driver):
    yield
    favorite_page = FavoritesPage(driver)
    favorite_page.driver.get('https://www.hebe.pl/')
