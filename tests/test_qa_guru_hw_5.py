import os

import allure
from selene import have

@allure.title("Successful fill form")
def test_google_chrome_open(setup_browser):
    browser = setup_browser
    first_name = "Alexey"
    last_name = "Tukin"

    my_picture = 'Picture.png'

    with allure.step("Open registrations form"):
        browser.open("https://demoqa.com/automation-practice-form")
        browser.element(".practice-form-wrapper").should(have.text("Student Registration Form"))
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")
    # Заполнение полей

    with allure.step("Fill form"):
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
    with allure.step("Check form results"):
        browser.all('td').should(have.exact_texts(
                'Student Name', 'Иван Иванов', 'Student Email',
            'test@test.com', 'Gender', 'Male', 'Mobile', '9999999999',
            'Date of Birth', '01 January,1991', 'Subjects', 'English',
            'Hobbies', 'Sports', 'Picture', 'Picture.png', 'Address',
            'RF. Moscow, Arbat, 1', 'State and City', 'Haryana Karnal',
            )
        )

