from selenium.webdriver.common.by import By
class LogInLocators:
    USERNAME_FIELD = By.NAME, "username"
    PASSWORD_FIELD = By.NAME, "password"
    LOGIN_BUTTON = By.CLASS_NAME, "btn-primary-login"
    CREATE_GROUP_BUTTON = By.CSS_SELECTOR, "button.app-btn-reset"
    ERROR_POP_UP = By.CSS_SELECTOR, ".Toastify__toast-container.Toastify__toast-container--bottom-right"
    ERROR_MESSAGE_USERNAME = (By.CSS_SELECTOR, "div.login-controls > div:nth-of-type(1) .invalid-feedback")
    ERROR_MESSAGE_PASSWORD = (By.CSS_SELECTOR, "div.login-controls > div:nth-of-type(2) .invalid-feedback")
    PASSWORD_INPUT_CLASS = By.ID, "pwdInput"
    USERNAME_INPUT_CLASS = By.ID, "userInput"



