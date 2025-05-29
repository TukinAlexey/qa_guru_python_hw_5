import os

from selene import browser


def test_google_chrome_open(open_browser):

    my_picture = 'Picture.png'

    browser.element('#lastName').type('Иванов')#.press_enter()
    browser.element('#userEmail').type('test@test.com')#.press_enter()
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('9999999999')#.press_enter()
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="0"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1991"]').click()
    browser.element('[aria-label="Choose Tuesday, January 1st, 1991"]').click()
    browser.element('#subjectsInput').type('English').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath(my_picture))

    browser.element('#currentAddress').type('RF. Moscow, Arbat, 1')
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Karnal').press_enter()
    browser.element('#firstName').type('Иван').press_enter()
    pass

