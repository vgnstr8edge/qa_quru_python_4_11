from selene import browser, be, have
import os


def test_practice_form(browser_settings):
    browser.element('#firstName').should(be.blank).type('Dima')
    browser.element('#lastName').should(be.blank).type('Nasedkin')
    browser.element('#userEmail').should(be.blank).type('test@mail.com')
    browser.element('[for=gender-radio-1]').should(have.text('Male')).click()
    browser.element('#userNumber').should(be.blank).type('89260010101')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select [value="5"]').should(have.text('June')).click()
    browser.element('.react-datepicker__year-select [value="2000"]').should(have.text('2000')).click()
    browser.element('.react-datepicker__day--021').should(have.text('21')).click()
    browser.element('#subjectsInput').should(be.blank).type('Accounting').press_enter()
    browser.element('[for=hobbies-checkbox-3]').should(have.text('Music')).click()
    browser.element('#uploadPicture').send_keys((os.getcwd() + '/resources/pic.png'))
    browser.element('#currentAddress').should(be.blank).type('Pushkina str')
    browser.element('#react-select-3-input').should(be.blank).type('Haryana').press_enter()
    browser.element('#react-select-4-input').should(be.blank).type('Karnal').press_enter()
    browser.element('#submit').click()

#проверка данных

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    browser.element('tr:nth-child(1) td:nth-child(2)').should(have.text('Dima Nasedkin'))
    browser.element('tr:nth-child(2) td:nth-child(2)').should(have.text('test@mail.com'))
    browser.element('tr:nth-child(3) td:nth-child(2)').should(have.text('Male'))
    browser.element('tr:nth-child(4) td:nth-child(2)').should(have.text('8926001010'))
    browser.element('tr:nth-child(5) td:nth-child(2)').should(have.text('21 June,2000'))
    browser.element('tr:nth-child(6) td:nth-child(2)').should(have.text('Accounting'))
    browser.element('tr:nth-child(7) td:nth-child(2)').should(have.text('Music'))
    browser.element('tr:nth-child(8) > td:nth-child(2)').should(have.text('pic.png'))
    browser.element('tr:nth-child(9) td:nth-child(2)').should(have.text('Pushkina str'))
    browser.element('tr:nth-child(10) td:nth-child(2)').should(have.text('Haryana Karnal'))

    browser.element('#closeLargeModal').click()






