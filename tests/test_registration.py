import os

import allure
from selene import browser

from confest import browser_management
from demoqa_tests.data import users
from demoqa_tests.pages.registration_page import RegistrationPage

image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../images/hubba_bubba.png"))


@allure.tag('web')
@allure.feature("Регистрируем нового пользователя через выбор даты в дейтпикере")
@allure.story("Регистрация")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Vladislav Bubnov")
@allure.description("Тест проверяет ввода данных в инпуты")
@allure.link("https://demoqa.com/", name="Testing")
def test_registration_datepicker_birth(browser_management):
    registration_page = RegistrationPage()
    student = users.student
    with allure.step("Открываем страницу регистрации"):
        browser.open("/automation-practice-form")

    with allure.step("Удаляем баннеры"):
        registration_page.clear_bunner()

    with allure.step("Вводим имя пользователя"):
        registration_page.fill_first_name(student.first_name)

    with allure.step("Вводим фамилию пользователя"):
        registration_page.fill_last_name(student.last_name)

    with allure.step("Вводим емайл пользователя"):
        registration_page.fill_email(student.email)

    with allure.step("Вводим пол пользователя"):
        registration_page.fill_gender(student.gender)

    with allure.step("Вводим номер телефона пользователя"):
        registration_page.fill_mobile(student.phone_number)

    with allure.step("Выбираем дату рождения пользователя"):
        registration_page.fill_date_of_birth(student.birth_year, student.birth_month, student.birth_day)

    with allure.step("Вводим объекты пользователя"):
        registration_page.fill_subjects(student.subjects)

    with allure.step("Выбираем хобби пользователя"):
        registration_page.fill_hobbies(student.hobbies)

    with allure.step("Загружаем изображение пользователя"):
        registration_page.fill_picture(image_path)

    with allure.step("Вводим адресс пользователя"):
        registration_page.fill_current_address(student.current_address)

    with allure.step("Вводим штат пользователя"):
        registration_page.fill_state(student.state)

    with allure.step("Вводим город пользователя"):
        registration_page.fill_city(student.city)

    with allure.step("Нажимаем кнопку submit"):
        registration_page.click_submit()

    with allure.step("Проверка данных в модальном окне успешной регистрации"):
        registration_page.should_registered_user_with(student.first_name, student.last_name, student.email,
                                                      student.gender,student.phone_number, student.birth_year,
                                                      student.birth_month, student.birth_day, student.subjects,
                                                      student.hobbies, student.picture, student.current_address,
                                                      student.state, student.city)


@allure.tag('web')
@allure.feature("Регистрируем нового пользователя через ввод даты рождения вручную")
@allure.story("Регистрация")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Vladislav Bubnov")
@allure.description("Тест проверяет ввода данных в инпуты")
@allure.link("https://demoqa.com/", name="Testing")
def test_registration_manual_birth(browser_management):
    registration_page = RegistrationPage()
    student = users.student

    with allure.step("Открываем страницу регистрации"):
        browser.open("/automation-practice-form")

    with allure.step("Удаляем баннеры"):
        registration_page.clear_bunner()

    with allure.step("Вводим имя пользователя"):
        registration_page.fill_first_name(student.first_name)

    with allure.step("Вводим фамилию пользователя"):
        registration_page.fill_last_name(student.last_name)

    with allure.step("Вводим емайл пользователя"):
        registration_page.fill_email(student.email)

    with allure.step("Вводим пол пользователя"):
        registration_page.fill_gender(student.gender)

    with allure.step("Вводим номер телефона пользователя"):
        registration_page.fill_mobile(student.phone_number)

    with allure.step("Вводим дату рождения пользователя"):
        registration_page.type_date_of_birth(student.date_birthday)

    with allure.step("Вводим объекты пользователя"):
        registration_page.fill_subjects(student.subjects)

    with allure.step("Выбираем хобби пользователя"):
        registration_page.fill_hobbies(student.hobbies)

    with allure.step("Загружаем изображение пользователя"):
        registration_page.fill_picture(image_path)

    with allure.step("Вводим адресс пользователя"):
        registration_page.fill_current_address(student.current_address)

    with allure.step("Вводим штат пользователя"):
        registration_page.fill_state(student.state)

    with allure.step("Вводим город пользователя"):
        registration_page.fill_city(student.city)

    with allure.step("Нажимаем кнопку submit"):
        registration_page.click_submit()

    with allure.step("Проверка данных в модальном окне успешной регистрации"):
        registration_page.should_registered_user_with(student.first_name, student.last_name, student.email,
                                                      student.gender,student.phone_number, student.birth_year,
                                                      student.birth_month, student.birth_day, student.subjects,
                                                      student.hobbies, student.picture, student.current_address,
                                                      student.state, student.city)
