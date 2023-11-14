# Toolbox
from selene.support.shared import browser
from selene import be, have


def test_hw_conflict_conflict():
    browser.open('https://demoqa.com/text-box')
    browser.element('[class=" mr-sm-2 form-control"]').should(be.blank).type('LAYLA')
    browser.element('[class="mr-sm-2 form-control"]').should(be.blank).type('123@GMAIL.COM')
    browser.element('[class="form-control"]').should(be.blank).type('Moscow')
    browser.element('[id="permanentAddress"]').should(be.blank).type('Russia')

    browser.element('[class="btn btn-primary"]').click()

    browser.element('#name').should(have.text('Name:LAYLA'))
    browser.element('#email').should(have.text('Email:123@GMAIL.COM'))
    browser.element('[id="output"] [id="currentAddress"]').should(have.text('Current Address :Moscow'))
    browser.element('[id="output"] [id="permanentAddress"]').should(have.text('Permananet Address :Russia'))