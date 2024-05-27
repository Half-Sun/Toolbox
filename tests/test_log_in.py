import uuid

import allure
from locators.log_in_locators import LogInLocators
from config import ADMIN_USERNAME, ADMIN_PASSWORD, ERROR_MESSAGE_USERNAME_REQUIRED, ERROR_MESSAGE_PASSWORD_REQUIRED
from conftest import login_page, unique_username, driver
class TestLogin:
    @allure.title("Successful login via main admin")
    def test_successful_admin_login(self, login_page):
        login_page.input_data_to_username(ADMIN_USERNAME)
        login_page.input_data_to_password(ADMIN_PASSWORD)
        login_page.click_on_login_button()
        create_group_button = login_page.find_element_and_wait(LogInLocators.CREATE_GROUP_BUTTON)
        assert create_group_button.is_displayed()

    @allure.title("Login user not found")
    def test_login_user_does_not_exist(self, login_page, unique_username):
        login_page.input_data_to_username(unique_username)
        login_page.input_data_to_password(ADMIN_PASSWORD)
        login_page.click_on_login_button()
        error_message_element = login_page.find_element_and_wait(LogInLocators.ERROR_POP_UP)
        assert error_message_element.is_displayed()

    @allure.title("Login password is wrong")
    def test_login_user_password_is_incorrect(self, login_page):
        random_password = f"password_{uuid.uuid4()}"
        login_page.input_data_to_username(ADMIN_USERNAME)
        login_page.input_data_to_password(random_password)
        login_page.click_on_login_button()
        error_message_element = login_page.find_element_and_wait(LogInLocators.ERROR_POP_UP)
        assert error_message_element.is_displayed()

    @allure.title("Username is empty and field is invalidated")
    def test_login_username_is_empty_and_form_is_invalidated(self, login_page):
        random_password = f"password_{uuid.uuid4()}"
        login_page.input_data_to_password(random_password)
        login_page.click_on_login_button()
        username_input_class = login_page.get_input_class(LogInLocators.USERNAME_INPUT_CLASS)
        assert 'form-control is-invalid' in username_input_class

    @allure.title("Error message while username is empty is correct")
    def test_login_username_is_empty_and_error_message_is_correct(self, login_page):
        random_password = f"password_{uuid.uuid4()}"
        login_page.input_data_to_password(random_password)
        login_page.click_on_login_button()
        error_message_element = login_page.get_text_from_element(LogInLocators.ERROR_MESSAGE_USERNAME)
        assert error_message_element == ERROR_MESSAGE_USERNAME_REQUIRED

    @allure.title("Password is empty and field is invalidated")
    def test_login_password_is_empty_and_form_is_invalidated(self, login_page, unique_username):
        login_page.input_data_to_username(unique_username)
        login_page.click_on_login_button()
        password_input_class = login_page.get_input_class(LogInLocators.PASSWORD_INPUT_CLASS)
        assert 'form-control is-invalid' in password_input_class

    @allure.title("Error message while password is empty is correct")
    def test_login_password_is_empty(self, login_page, unique_username):
        login_page.input_data_to_username(unique_username)
        login_page.click_on_login_button()
        error_message_element = login_page.get_text_from_element(LogInLocators.ERROR_MESSAGE_PASSWORD)
        assert error_message_element == ERROR_MESSAGE_PASSWORD_REQUIRED
