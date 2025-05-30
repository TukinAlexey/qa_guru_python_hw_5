import os
from selene import browser, have


def test_google_chrome_open(open_browser):

    my_picture = 'Picture.png'

    # Заполнение полей

    browser.element('#firstName').type('Иван')
    browser.element('#lastName').type('Иванов')
    browser.element('#userEmail').type('test@test.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('9999999999')
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
    browser.element('#submit').click()

    # Проверка данных в таблице

    browser.all('td').should(have.exact_texts(
            'Student Name', 'Иван Иванов', 'Student Email',
        'test@test.com', 'Gender', 'Male', 'Mobile', '9999999999',
        'Date of Birth', '01 January,1991', 'Subjects', 'English',
        'Hobbies', 'Sports', 'Picture', 'Picture.png', 'Address',
        'RF. Moscow, Arbat, 1', 'State and City', 'Haryana Karnal',
        )
    )

