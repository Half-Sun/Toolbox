import uuid

import pytest
from selenium import webdriver
from pages.log_in_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    login_page = LoginPage(driver)
    login_page.go_to_log_in_page()
    return login_page

@pytest.fixture
def unique_username():
    return f"user_{uuid.uuid4()}"