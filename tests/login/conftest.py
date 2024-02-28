import allure
import pytest
from selenium import webdriver
from source_code.pages.main.main_page import MainPage


@pytest.fixture(scope='class', autouse=True)
@allure.step('Open main page and accept_cookies')
def suite_setup(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.accept_cookies()


@pytest.fixture(scope='function', autouse=True)
@allure.step('Go to login page')
def test_setup(driver):
    main_page = MainPage(driver)
    main_page.go_to_login_page()
