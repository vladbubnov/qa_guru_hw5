import os

from selene import browser

from confest import browser_management
from demoqa_tests.data import users
from demoqa_tests.pages.registration_page import RegistrationPage

image_path = os.path.abspath("../images/hubba_bubba.png")


def test_registration_datepicker_birth(browser_management):
    registration_page = RegistrationPage()
    student = users.student

    browser.open("/automation-practice-form")
    registration_page.clear_bunner()

    registration_page.registration_fill_birthday(student, image_path)
    registration_page.should_registered_user_with(student.first_name, student.last_name, student.email, student.gender,
                                                  student.phone_number, student.birth_year, student.birth_month,
                                                  student.birth_day, student.subjects, student.hobbies, student.picture,
                                                  student.current_address, student.state, student.city)


def test_registration_manual_birth(browser_management):
    registration_page = RegistrationPage()
    student = users.student

    browser.open("/automation-practice-form")
    registration_page.clear_bunner()

    registration_page.registration_type_birthday(users.student, image_path)
    registration_page.should_registered_user_with(student.first_name, student.last_name, student.email, student.gender,
                                                  student.phone_number, student.birth_year, student.birth_month,
                                                  student.birth_day, student.subjects, student.hobbies, student.picture,
                                                  student.current_address, student.state, student.city)
