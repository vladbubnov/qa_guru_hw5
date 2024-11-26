import os
import time

from selene import browser, have, by
from selenium.webdriver import Keys

from confest import browser_management


def test_registration_datepicker_birth(browser_management):
    browser.open("/")
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")

    browser.element("#firstName").type("Ivan")
    browser.element("#lastName").type("Ivanov")
    browser.element("#userEmail").type("testemail@test.com")
    browser.element("#genterWrapper").element(by.text("Male")).click()
    browser.element("#userNumber").type("9999999999")

    browser.element("#dateOfBirthInput").click()
    browser.element("[class='react-datepicker__month-select']").click().element(by.text("February")).click()
    browser.element("[class='react-datepicker__year-select']").click().element(by.text("1995")).click()
    browser.element("[class='react-datepicker__month']").element(by.text("21")).click()

    browser.element("#subjectsInput").type("Arts").press_enter()
    browser.element("#subjectsInput").type("Biology").press_enter()

    browser.element(by.text("Sports")).click()
    browser.element(by.text("Reading")).click()
    browser.element(by.text("Music")).click()

    browser.element("#uploadPicture").send_keys(os.path.abspath("../images/hubba_bubba.png"))
    browser.element("#currentAddress").type("st. Nicolson, 15")
    browser.element("#state").click().element(by.text("NCR")).click()
    browser.element("#city").click().element(by.text("Gurgaon")).click()
    browser.element("#submit").click()

    browser.element(".modal-body").should(have.text("Student Name")).should(have.text("Ivan Ivanov"))
    browser.element(".modal-body").should(have.text("Student Email")).should(have.text("testemail@test.com"))
    browser.element(".modal-body").should(have.text("Gender")).should(have.text("Male"))
    browser.element(".modal-body").should(have.text("Mobile")).should(have.text("9999999999"))
    browser.element(".modal-body").should(have.text("Date of Birth")).should(have.text("21 February,1995"))
    browser.element(".modal-body").should(have.text("Subjects")).should(have.text("Arts, Biology"))
    browser.element(".modal-body").should(have.text("Hobbies")).should(have.text("Sports, Reading, Music"))
    browser.element(".modal-body").should(have.text("Picture")).should(have.text("hubba_bubba.png"))
    browser.element(".modal-body").should(have.text("Address")).should(have.text("st. Nicolson, 15"))
    browser.element(".modal-body").should(have.text("State and City")).should(have.text("NCR Gurgaon"))


def test_registration_manual_birth(browser_management):
    browser.open("/")
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")

    browser.element("#firstName").type("Ivan")
    browser.element("#lastName").type("Ivanov")
    browser.element("#userEmail").type("testemail@test.com")
    browser.element("#genterWrapper").element(by.text("Male")).click()
    browser.element("#userNumber").type("9999999999")

    browser.element("#dateOfBirthInput").send_keys(f"{Keys.END}{Keys.SHIFT}{Keys.HOME}").type("21 Feb 1995")
    browser.element("#subjects-label").click()

    browser.element("#subjectsInput").type("Arts").press_enter()
    browser.element("#subjectsInput").type("Biology").press_enter()

    browser.element(by.text("Sports")).click()
    browser.element(by.text("Reading")).click()
    browser.element(by.text("Music")).click()

    browser.element("#uploadPicture").send_keys(os.path.abspath("../images/hubba_bubba.png"))
    browser.element("#currentAddress").type("st. Nicolson, 15")
    browser.element("#state").click().element(by.text("NCR")).click()
    browser.element("#city").click().element(by.text("Gurgaon")).click()
    browser.element("#submit").click()

    browser.element(".modal-body").should(have.text("Student Name")).should(have.text("Ivan Ivanov"))
    browser.element(".modal-body").should(have.text("Student Email")).should(have.text("testemail@test.com"))
    browser.element(".modal-body").should(have.text("Gender")).should(have.text("Male"))
    browser.element(".modal-body").should(have.text("Mobile")).should(have.text("9999999999"))
    browser.element(".modal-body").should(have.text("Date of Birth")).should(have.text("21 February,1995"))
    browser.element(".modal-body").should(have.text("Subjects")).should(have.text("Arts, Biology"))
    browser.element(".modal-body").should(have.text("Hobbies")).should(have.text("Sports, Reading, Music"))
    browser.element(".modal-body").should(have.text("Picture")).should(have.text("hubba_bubba.png"))
    browser.element(".modal-body").should(have.text("Address")).should(have.text("st. Nicolson, 15"))
    browser.element(".modal-body").should(have.text("State and City")).should(have.text("NCR Gurgaon"))
