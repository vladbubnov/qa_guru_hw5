from selene import browser, by, have
from selenium.webdriver import Keys


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


