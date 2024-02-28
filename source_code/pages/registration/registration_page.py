import allure

from source_code.pages.base_element import BaseElement
from source_code.pages.base_helpers import BaseHelpers
from source_code.pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.email_field = BaseElement(driver, "//*[@type='email']")
        self.password_field = BaseElement(driver, "//*[@type='password']")
        self.name_field = BaseElement(driver, "//*[@id='dwfrm_profile_customer_firstname']")
        self.lastname_field = BaseElement(driver, "//*[@id='dwfrm_profile_customer_lastname']")
        self.number_field = BaseElement(driver, "//*[@type='tel']")
        self.checkbox = BaseElement(driver, "(//*[@class='checkbox-label checkbox-label--registration'])[1]")
        self.submit_button = BaseElement(driver, "//*[@type='submit']")
        self.registration_message = BaseElement(driver, "//*[@class='confirmation-card__title']")
        self.email_error_message = BaseElement(driver, "//*[@id='dwfrm_profile_customer_email-error']")
        self.password_error_message = BaseElement(driver,
                                                  "//*[@class='form-aside-validation__item js-list-password-validation error']")
        self.name_error_message = BaseElement(driver, "//*[@id='dwfrm_profile_customer_firstname-error']")
        self.lastname_error_message = BaseElement(driver, "//*[@id='dwfrm_profile_customer_lastname-error']")
        self.number_error_message = BaseElement(driver, "//*[@id='dwfrm_profile_customer_phoneMobile-error']")
        self.logo_element = BaseElement(driver, "//*[@class='simple-header__logo']")
    @allure.step('Make registration')
    def make_registration(self, email, password, first_name, last_name, phone_number):
        self.email_field.send_keys(email)
        self.password_field.send_keys(password)
        self.name_field.send_keys(first_name)
        self.lastname_field.send_keys(last_name)
        self.number_field.send_keys(phone_number)
        self.checkbox.custom_click()
        self.submit_button.custom_click()
        self.checkbox.wait_until_invisibility()

    def check_field_validation(self, field_name, invalid_input, error_message_text):
        field_element_name = f"{field_name}_field"
        field_element = getattr(self, field_element_name)
        with allure.step(f'Enter an invalid data in the {field_name} field'):
            field_element.send_keys(invalid_input)

        with allure.step('Ensure that error message is displayed'):
            self.logo_element.click()
            error_message_element_name = f"{field_name}_error_message"
            error_message_element = getattr(self, error_message_element_name)
            assert error_message_element.text() == error_message_text, f'Error message is not displayed unexpectedly.'

        field_element.clear()
