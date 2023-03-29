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

    # проверка данных

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    browser.element('.table').all('td').even.should(
        have.exact_texts('Dima Nasedkin',
                         'test@mail.com',
                         'Male',
                         '8926001010',
                         '21 June,2000',
                         'Accounting',
                         'Music',
                         'pic.png',
                         'Pushkina str',
                         'Haryana Karnal'
                         )
    )

    browser.element('#closeLargeModal').click()
