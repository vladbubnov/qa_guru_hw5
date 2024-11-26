import os

from selene import browser, have, by
from selenium.webdriver import Keys

from confest import browser_management

first_name, last_name = "Ivan", "Ivanov"
email = "testemail@test.com"
gender = "Male"
phone_number = "9999999999"
birth_month, birth_year, birth_day = "February", "1995", "21"
date_birthday = "21 Feb 1995"
subjects = ("Arts", "Biology")
hobbies = ("Sports", "Reading", "Music")
current_address = "st. Nicolson, 15"
state = "NCR"
city = "Gurgaon"

image_path = os.path.abspath("../images/hubba_bubba.png")

expected_result = [
    'Student Name', f"{first_name} {last_name}",
    'Student Email', email,
    'Gender', gender,
    'Mobile', phone_number,
    'Date of Birth', f"{birth_day} {birth_month},{birth_year}",
    'Subjects', ', '.join(map(str, subjects)),
    'Hobbies', 'Sports, Reading, Music',
    'Picture', 'hubba_bubba.png',
    'Address', current_address,
    'State and City', f"{state} {city}"
]


def clear_bunner():
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")


def select_subjects(values):
    for value in values:
        browser.element("#subjectsInput").type(value).press_enter()


def select_hobbies(values):
    for value in values:
        browser.element(by.text(value)).click()


def select_date_of_birthday(day, month, year):
    browser.element("#dateOfBirthInput").click()
    browser.element("[class='react-datepicker__month-select']").click().element(by.text(month)).click()
    browser.element("[class='react-datepicker__year-select']").click().element(by.text(year)).click()
    browser.element("[class='react-datepicker__month']").element(by.text(day)).click()


def set_date_of_birthday(date):
    browser.element("#dateOfBirthInput").send_keys(f"{Keys.END}{Keys.SHIFT}{Keys.HOME}").type(date)
    browser.element("#subjects-label").click()


def check_result(result):
    for i in range(0, len(result), 2):
        browser.element('.modal-body').should(have.text(result[i])).should(have.text(result[i + 1]))


def test_registration_datepicker_birth(browser_management):
    browser.open("/")
    clear_bunner()

    browser.element("#firstName").type(first_name)
    browser.element("#lastName").type(last_name)
    browser.element("#userEmail").type(email)
    browser.element("#genterWrapper").element(by.text(gender)).click()
    browser.element("#userNumber").type(phone_number)
    select_date_of_birthday(birth_day, birth_month, birth_year)
    select_subjects(subjects)
    select_hobbies(hobbies)
    browser.element("#uploadPicture").send_keys(image_path)
    browser.element("#currentAddress").type(current_address)
    browser.element("#state").click().element(by.text(state)).click()
    browser.element("#city").click().element(by.text(city)).click()
    browser.element("#submit").click()
    check_result(expected_result)


def test_registration_manual_birth(browser_management):
    browser.open("/")
    clear_bunner()

    browser.element("#firstName").type(first_name)
    browser.element("#lastName").type(last_name)
    browser.element("#userEmail").type(email)
    browser.element("#genterWrapper").element(by.text(gender)).click()
    browser.element("#userNumber").type(phone_number)
    set_date_of_birthday(date_birthday)
    select_subjects(subjects)
    select_hobbies(hobbies)
    browser.element("#uploadPicture").send_keys(image_path)
    browser.element("#currentAddress").type(current_address)
    browser.element("#state").click().element(by.text(state)).click()
    browser.element("#city").click().element(by.text(city)).click()
    browser.element("#submit").click()
    check_result(expected_result)
