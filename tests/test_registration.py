import os

from selene import browser

from confest import browser_management
from demoqa_tests.data.users import User
from demoqa_tests.pages.registration_page import RegistrationPage

image_path = os.path.abspath("../images/hubba_bubba.png")


def test_registration_datepicker_birth(browser_management):
    registration_page = RegistrationPage()
    student = User(
        "Ivan",
        "Ivanov",
        "testemail@test.com",
        "Male",
        "9999999999",
        "1995",
        "February",
        "21",
        "21 Feb 1995",
        ("Arts", "Biology"),
        ("Sports", "Reading", "Music"),
        "st. Nicolson, 15",
        "NCR",
        "Gurgaon",
        "hubba_bubba.png"
    )

    browser.open("/automation-practice-form")
    registration_page.clear_bunner()

    registration_page.fill_first_name(student.first_name)
    registration_page.fill_last_name(student.last_name)
    registration_page.fill_email(student.email)
    registration_page.fill_gender(student.gender)
    registration_page.fill_mobile(student.phone_number)
    registration_page.fill_date_of_birth(student.birth_year, student.birth_month, student.birth_day)
    registration_page.fill_subjects(student.subjects)
    registration_page.fill_hobbies(student.hobbies)
    registration_page.fill_picture(image_path)
    registration_page.fill_current_address(student.current_address)
    registration_page.fill_state(student.state)
    registration_page.fill_city(student.city)
    registration_page.click_submit()

    registration_page.should_registered_user_with(student.first_name, student.last_name, student.email, student.gender,
                                                  student.phone_number, student.birth_year, student.birth_month,
                                                  student.birth_day, student.subjects, student.hobbies, student.picture,
                                                  student.current_address, student.state, student.city)


def test_registration_manual_birth(browser_management):
    registration_page = RegistrationPage()
    student = User(
        "Ivan",
        "Ivanov",
        "testemail@test.com",
        "Male",
        "9999999999",
        "1995",
        "February",
        "21",
        "21 Feb 1995",
        ("Arts", "Biology"),
        ("Sports", "Reading", "Music"),
        "st. Nicolson, 15",
        "NCR",
        "Gurgaon",
        "hubba_bubba.png"
    )

    browser.open("/automation-practice-form")
    registration_page.clear_bunner()

    registration_page.fill_first_name(student.first_name)
    registration_page.fill_last_name(student.last_name)
    registration_page.fill_email(student.email)
    registration_page.fill_gender(student.gender)
    registration_page.fill_mobile(student.phone_number)
    registration_page.type_date_of_birth(student.date_birthday)
    registration_page.fill_subjects(student.subjects)
    registration_page.fill_hobbies(student.hobbies)
    registration_page.fill_picture(image_path)
    registration_page.fill_current_address(student.current_address)
    registration_page.fill_state(student.state)
    registration_page.fill_city(student.city)
    registration_page.click_submit()

    registration_page.should_registered_user_with(student.first_name, student.last_name, student.email, student.gender,
                                                  student.phone_number, student.birth_year, student.birth_month,
                                                  student.birth_day, student.subjects, student.hobbies, student.picture,
                                                  student.current_address, student.state, student.city)
