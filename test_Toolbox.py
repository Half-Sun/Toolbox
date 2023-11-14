import pytest

from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def window():
    browser.open('https://test.web-cfg.com:4324/login')


@pytest.fixture
def login(window):
    browser.element('[id="userInput"]').should(be.blank).type('admin').press_enter()
    browser.element('[id="pwdInput"]').should(be.blank).type('admin')
    browser.element('[class="btn-primary-login btn btn-primary"]').click()


def test_no_result(login):
    browser.element('[data-icon="user-group"]').click()
