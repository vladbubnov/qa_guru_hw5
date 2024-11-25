import os
import time

from selene import browser, have, be, by
from confest import browser_management

first_name, last_name = "Ivan", "Ivanov"
email = "testemail@test.com"
gender = "Male"
phone_number = "9999999999"
birth_month, birth_year, birth_day = "February", "1995", "11"
subjects = ("Arts", "Biology")
current_address = "st. Nicolson, 15"
state = "NCR"
city = "Gurgaon"

image_path = os.path.abspath('../qa_guru_hw5/images/hubba_bubba.png')
hobbies_elements = ("[for='hobbies-checkbox-1']", "[for='hobbies-checkbox-2']", "[for='hobbies-checkbox-3']")

expected_result = [
    'Student Name', f"{first_name} {last_name}",
    'Student Email', email,
    'Gender', gender,
    'Mobile', phone_number,
    'Date of Birth', f"{birth_day} {birth_month},{birth_year}",
    'Subjects', ', '.join(map(str, subjects)),
    'Hobbies', 'Sports, Reading, Music',
    # 'Picture', '',
    'Address', current_address,
    'State and City', f"{state} {city}"
]


def test_registration_datepicker_birth(browser_management):
    browser.open("/")

    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")

    browser.element("#firstName").type(first_name)
    browser.element("#lastName").type(last_name)
    browser.element("#userEmail").type(email)
    browser.element("#genterWrapper").element(by.text(gender)).click()
    browser.element("#userNumber").type(phone_number)

    browser.element("#dateOfBirthInput").click()
    browser.element("[class='react-datepicker__month-select']").click().element(by.text(birth_month)).click()
    browser.element("[class='react-datepicker__year-select']").click().element(by.text(birth_year)).click()
    browser.element("[class='react-datepicker__month']").element(by.text(birth_day)).click()

    for subject in subjects:
        browser.element("#subjectsInput").type(subject).press_enter()

    for hobbies_element in hobbies_elements:
        browser.element(hobbies_element).click()

    # browser.element('#uploadPicture').send_keys(image_path)
    # browser.element('[for="uploadPicture"]').send_keys(image_path)
    # browser.element('[id="uploadPicture"]').set_value(image_path)

    browser.element("#currentAddress").type(current_address)

    browser.element("#state").click().element(by.text(state)).click()
    browser.element("#city").click().element(by.text(city)).click()

    browser.element("#submit").click()

    for i in range(0, len(expected_result), 2):
        browser.element('.modal-body').should(have.text(expected_result[i])).should(have.text(expected_result[i + 1]))
