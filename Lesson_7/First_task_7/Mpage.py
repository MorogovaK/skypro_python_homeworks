from selenium.webdriver.common.by import By
from task1 import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[type="submit"]')))


    def find_fields(self):
        self._first_name = (By.NAME, "first_name")
        self._last_name = (By.NAME, "last_name")
        self._address = (By.NAME, "address")
        self._zip_code = (By.NAME, "zip_code")
        self._city = (By.NAME, "city")
        self._country = (By.NAME, "country")
        self._email = (By.NAME, "email")
        self._phone = (By.NAME, "phone")
        self._job_position = (By.NAME, "job_position")
        self._company = (By.NAME, "company")

    def information_about_me(self):
        self.driver.find_element(*self._first_name).send_keys(first_name)
        self.driver.find_element(*self._last_name).send_keys(last_name)
        self.driver.find_element(*self._address).send_keys(address)
        self.driver.find_element(*self._city).send_keys(city)
        self.driver.find_element(*self._country).send_keys(country)
        self.driver.find_element(*self._phone).send_keys(phone)
        self.driver.find_element(*self._email).send_keys(email)
        self.driver.find_element(*self._zip_code).send_keys(zip_code)
        self.driver.find_element(*self._job_position).send_keys(job_position)
        self.driver.find_element(*self._company).send_keys(company)


    def button_click(self):
        self.driver.find_element(By.CSS_SELECTOR,'[type="submit"]').click()