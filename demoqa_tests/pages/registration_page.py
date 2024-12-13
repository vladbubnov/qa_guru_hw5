from selene import browser, by, have
from selenium.webdriver import Keys

from demoqa_tests.data.users import User


class RegistrationPage:

    def clear_bunner(self):
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def fill_first_name(self, value):
        browser.element("#firstName").type(value)

    def fill_last_name(self, value):
        browser.element("#lastName").type(value)

    def fill_email(self, value):
        browser.element("#userEmail").type(value)

    def fill_gender(self, value):
        browser.element("#genterWrapper").element(by.text(value)).click()

    def fill_mobile(self, value):
        browser.element("#userNumber").type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element("[class='react-datepicker__month-select']").click().element(by.text(month)).click()
        browser.element("[class='react-datepicker__year-select']").click().element(by.text(year)).click()
        browser.element("[class='react-datepicker__month']").element(by.text(day)).click()

    def type_date_of_birth(self, value):
        browser.element("#dateOfBirthInput").send_keys(f"{Keys.END}{Keys.SHIFT}{Keys.HOME}").type(value)
        browser.element("#subjects-label").click()

    def fill_subjects(self, values):
        for value in values:
            browser.element("#subjectsInput").type(value).press_enter()

    def fill_hobbies(self, values):
        for value in values:
            browser.element(by.text(value)).click()

    def fill_picture(self, image_path):
        browser.element("#uploadPicture").send_keys(image_path)

    def fill_current_address(self, value):
        browser.element("#currentAddress").type(value)

    def fill_state(self, value):
        browser.element("#state").click().element(by.text(value)).click()

    def fill_city(self, city):
        browser.element("#city").click().element(by.text(city)).click()

    def click_submit(self):
        browser.element("#submit").click()

    def should_registered_user_with(self, first_name, last_name, email, gender, telephone,
                                    birth_year, birth_month, birth_day, subjects, hobbies, picture, current_address, state, city):
        browser.element(".table").all("td").even.should(have.exact_texts(
            f"{first_name} {last_name}",
            email,
            gender,
            telephone,
            f"{birth_day} {birth_month},{birth_year}",
            ', '.join(map(str, subjects)),
            ', '.join(map(str, hobbies)),
            picture,
            current_address,
            f"{state} {city}"
        )
        )

    def registration_fill_birthday(self, student: User, image_path):
         self.fill_first_name(student.first_name)
         self.fill_last_name(student.last_name)
         self.fill_email(student.email)
         self.fill_gender(student.gender)
         self.fill_mobile(student.phone_number)
         self.fill_date_of_birth(student.birth_year, student.birth_month, student.birth_day)
         self.fill_subjects(student.subjects)
         self.fill_hobbies(student.hobbies)
         self.fill_picture(image_path)
         self.fill_current_address(student.current_address)
         self.fill_state(student.state)
         self.fill_city(student.city)
         self.click_submit()

    def registration_type_birthday(self, student: User, image_path):
         self.fill_first_name(student.first_name)
         self.fill_last_name(student.last_name)
         self.fill_email(student.email)
         self.fill_gender(student.gender)
         self.fill_mobile(student.phone_number)
         self.type_date_of_birth(student.date_birthday)
         self.fill_subjects(student.subjects)
         self.fill_hobbies(student.hobbies)
         self.fill_picture(image_path)
         self.fill_current_address(student.current_address)
         self.fill_state(student.state)
         self.fill_city(student.city)
         self.click_submit()

