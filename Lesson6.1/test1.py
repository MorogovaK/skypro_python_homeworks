from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import *
from time import sleep

def data1(chrome_browser):
    chrome_browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    data = {
    'First_name': First_name,
    'Last_name': Last_name,
    'Address': Address,
    'Email': Email,
    'Phone_number' : Phone_number,
    'Zip_code': Zip_code,
    'City' : City,
    'Country':Country,
    'Job_position': Job_position,
    'Company' : Company
    }

    for field, value in data.items():
        chrome_browser.find_element(By.NAME, field).send_keys(value)

    def test_data(chrome_browser):
        WebDriverWait(chrome_browser, 50, 0.5).until(EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()
        sleep(3)

        classes = {
            "First_name" : "success",
            "Last_name" : "success",
            "Address" : "success",
            "Email" : "success",
            "Phone_number" : "success",
            "City" : "success",
            "Country" : "success",
            "Job_position" : "success",
            "Company" : "success",
            "Zip_code" : "danger"
        }

        for f_id, class_name in classes.items():
            assert field in chrome_browser.find_element(By.ID, f_id).get_attribute("class")