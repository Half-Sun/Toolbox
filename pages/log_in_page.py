from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def input_data_to_username(self, username):
        username_input = self.driver.find_element(By.ID, "userInput")
        username_input.send_keys(username)

    def input_data_to_password(self, password):
        password_input = self.driver.find_element(By.ID, "pwdInput")
        password_input.send_keys(password)

    def click_on_login_button(self):
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button.btn-primary-login")
        login_button.click()

    def get_text_from_element(self, locator):
        element = self.find_element_and_wait(locator)
        return element.text

    def get_input_class(self, locator):
        element = self.find_element_and_wait(locator)
        return element.get_attribute("class")
