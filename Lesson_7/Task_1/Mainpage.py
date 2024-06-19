from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from Data import *
from configuration1 import URL_1
from drivertest import chrome_browser


class MainPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get(URL_1)


    def find_fields(self):
        self._first_name = (By.NAME, "first-name")
        self._last_name = (By.NAME, "last-name")
        self._addres = (By.NAME, "address")
        self._email = (By.NAME, "e-mail")
        self._phone = (By.NAME, "phone")
        self._zip_code = (By.NAME, "zip-code")
        self._city = (By.NAME, "city")
        self._country = (By.NAME, "country")
        self._job_position = (By.NAME, "job-position")
        self._company = (By.NAME, "company")
        self._button = (By.TAG_NAME, "button")


    def filling_in_the_fields(self):
        self.browser.find_element(*self._first_name).send_keys(first_name)
        self.browser.find_element(*self._last_name).send_keys(last_name)
        self.browser.find_element(*self._addres).send_keys(address)
        self.browser.find_element(*self._email).send_keys(email)
        self.browser.find_element(*self._phone).send_keys(phone)
        self.browser.find_element(*self._zip_code).send_keys(zip_code)
        self.browser.find_element(*self._city).send_keys(city)
        self.browser.find_element(*self._country).send_keys(country)
        self.browser.find_element(*self._job_position).send_keys(job_position)
        self.browser.find_element(*self._company).send_keys(company)


    def click_submint_button(self):
        WebDriverWait(self.browser, 40, 0.2).until(EC.element_to_be_clickable(self._button)).click()