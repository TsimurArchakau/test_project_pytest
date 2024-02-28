import allure
import pytest
from selenium import webdriver
from source_code.pages.main.main_page import MainPage


@pytest.fixture(scope='class', autouse=True)
@allure.step('Open main page, accept_cookies and go to registration page')
def suite_setup(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.accept_cookies()
    main_page.go_to_registration_page()
