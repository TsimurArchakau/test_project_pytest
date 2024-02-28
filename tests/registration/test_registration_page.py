import allure
import pytest
from source_code.pages.base_helpers import BaseHelpers
from source_code.pages.registration.registration_page import RegistrationPage


class TestRegistrationPage:
    @allure.feature('Registration')
    @allure.story('Validation of email field')
    @pytest.mark.parametrize('invalid_email',
                             ['@gmail.com', '!@gmail.com', 'nikagmail.com', 'nika@.com', 'nika@q!q.com',
                              'nika@gmailcom', 'nika@gmail.', 'nika@gmail.com1', 'nika@gmail.co!', 'nika@gmail.q'])
    def test_email_field(self, driver, invalid_email):
        registration_page = RegistrationPage(driver)
        expected_error_message = 'Podany adres e-mail jest nieprawidłowy, proszę nie używać znaków diakrytycznych, przerw (spacja), ani znaków specjalnych.'
        registration_page.check_field_validation('email', invalid_email, expected_error_message)

    @allure.feature('Registration')
    @allure.story('Validation of password field')
    @pytest.mark.parametrize('invalid_password,expected_error_message',
                             [['hyujki1!', 'Wielka litera'], ['Hariboi1', 'Cyfra i znak specjalny'],
                              ['Hariboi!', 'Cyfra i znak specjalny'], ['DAREKI1!', 'Mała litera'],
                              ['Darek1!', 'Minimum 8 znaków']])
    def test_password_field(self, driver, invalid_password, expected_error_message):
        registration_page = RegistrationPage(driver)
        registration_page.check_field_validation('password', invalid_password, expected_error_message)

    @allure.feature('Registration')
    @allure.story('Validation of name field')
    @pytest.mark.parametrize('invalid_name', ['f1', 'F!'])
    def test_name_field(self, driver, invalid_name):
        registration_page = RegistrationPage(driver)
        expected_error_message = 'Pole nie może zawierać cyfr oraz znaków specjalnych.'
        registration_page.check_field_validation('name', invalid_name, expected_error_message)

    @allure.feature('Registration')
    @allure.story('Validation of last name field')
    @pytest.mark.parametrize('invalid_lastname', ['a5', 'a!'])
    def test_lastname_field(self, driver, invalid_lastname):
        registration_page = RegistrationPage(driver)
        expected_error_message = 'Pole nie może zawierać cyfr oraz znaków specjalnych.'
        registration_page.check_field_validation('lastname', invalid_lastname, expected_error_message)

    @allure.feature('Registration')
    @allure.story('Validation of number field')
    @pytest.mark.parametrize('invalid_number', ['1234567', '123f56788', '12345678!'])
    def test_number_field(self, driver, invalid_number):
        registration_page = RegistrationPage(driver)
        expected_error_message = 'Numer telefonu powinien składać się z ciągu dziewięciu cyfr bez znaków specjalnych'
        registration_page.check_field_validation('number', invalid_number, expected_error_message)

    @allure.feature('Registration')
    @allure.story('Registration with valid data')
    def test_valid_registration(self, driver):
        base_helpers = BaseHelpers()
        registration_page = RegistrationPage(driver)

        email, password, first_name, last_name, phone_number = base_helpers.generate_random_data()
        registration_page.make_registration(email, password, first_name, last_name, phone_number)

        with allure.step('Check the registration is performed sucessfully'):
            assert registration_page.registration_message.text() == 'Udało Ci się założyć konto!', \
                f'Registration failed.'

        base_helpers.save_credentials(email, password)
