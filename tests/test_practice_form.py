import os
from selene import browser, be, have
import allure


def test_practice_form(setup_browser):

    with allure.step("Открыть форму регистрации"):
        browser.open("https://demoqa.com/automation-practice-form")
        browser.element(".practice-form-wrapper").should(have.text("Student Registration Form"))
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")

    with allure.step('Заполнить имя_фамилию'):
        browser.element('#firstName').should(be.blank).type('Dima')
        browser.element('#lastName').should(be.blank).type('Nasedkin')

    with allure.step('Заполнить почту'):
        browser.element('#userEmail').should(be.blank).type('test@mail.com')

    with allure.step('Заполнить поле "гендер"'):
        browser.element('[for=gender-radio-1]').should(have.text('Male')).click()

    with allure.step('Заполнить номер телефона'):
        browser.element('#userNumber').should(be.blank).type('89260010101')

    with allure.step('Заполнить дату рождения'):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select [value="5"]').should(have.text('June')).click()
        browser.element('.react-datepicker__year-select [value="2000"]').should(have.text('2000')).click()
        browser.element('.react-datepicker__day--021').should(have.text('21')).click()

    with allure.step('Заполнить личную информацию и интересы'):
        browser.element('#subjectsInput').should(be.blank).type('Accounting').press_enter()
        browser.element('[for=hobbies-checkbox-3]').should(have.text('Music')).click()

    with allure.step('Загрузить фото'):
        browser.element('#uploadPicture').send_keys((os.getcwd() + '/tests/resources/pic.png'))

    with allure.step('Указать место жительства: адрес, город, штат'):
        browser.element('#currentAddress').should(be.blank).type('Pushkina str')
        browser.element('#react-select-3-input').should(be.blank).type('Haryana').press_enter()
        browser.element('#react-select-4-input').should(be.blank).type('Karnal').press_enter()

    with allure.step('нажать кнопку "Submit"'):
        browser.element('#submit').click()

    # проверка данных
    with allure.step('Подтвеждение ввода данных'):
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



