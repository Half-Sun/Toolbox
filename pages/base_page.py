import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Open main page")
    def go_to_log_in_page(self):
        main_page_url = "https://test.web-cfg.com:4324/summary/products"
        self.driver.get(main_page_url)

    @allure.step("Find element and wait")
    def find_element_and_wait(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
