import os

from selene import browser

from confest import browser_management
from demoqa_tests.data import users
from demoqa_tests.pages.registration_page import RegistrationPage

image_path = os.path.abspath("../images/hubba_bubba.png")


def test_registration_datepicker_birth(browser_management):
    registration_page = RegistrationPage()

    browser.open("/automation-practice-form")
    registration_page.clear_bunner()

    registration_page.registration_fill_birthday(users.student, image_path)

    registration_page.should_registered_user_with(users.student.first_name, users.student.last_name,
                                                  users.student.email, users.student.gender,
                                                  users.student.phone_number, users.student.birth_year,
                                                  users.student.birth_month,
                                                  users.student.birth_day, users.student.subjects,
                                                  users.student.hobbies, users.student.picture,
                                                  users.student.current_address, users.student.state,
                                                  users.student.city)


def test_registration_manual_birth(browser_management):
    registration_page = RegistrationPage()

    browser.open("/automation-practice-form")
    registration_page.clear_bunner()

    registration_page.registration_type_birthday(users.student, image_path)

    registration_page.should_registered_user_with(users.student.first_name, users.student.last_name,
                                                  users.student.email, users.student.gender,
                                                  users.student.phone_number, users.student.birth_year,
                                                  users.student.birth_month,
                                                  users.student.birth_day, users.student.subjects,
                                                  users.student.hobbies, users.student.picture,
                                                  users.student.current_address, users.student.state,
                                                  users.student.city)
