from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from configuration import *
from data_test import chrome_browser

def test_data(chrome_browser):
    chrome_browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    form_data = {
    "first-name": First_name,
    "last-name": Last_name,
    "address": Address,
    "e-mail": Email,
    "phone": Phone_number,
    "zip-code": Zip_code,
    "city": City,
    "country": Country,
    "job-position": Job_position,
    "company": Company
    }
    
    for field_name, value in form_data.items():
        chrome_browser.find_element(By.NAME, field_name).send_keys(value)

    WebDriverWait(chrome_browser, 30, 0.2).until(EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()

    field_class = {
        "zip-code": "danger",
        "first-name": "success",
        "last-name": "success",
        "address": "success",
        "e-mail": "success",
        "phone": "success",
        "city": "success",
        "country": "success",
        "job-position": "success",
        "company": "success",
    }

    for field_id, class_name in field_class.items():
        assert class_name in chrome_browser.find_element(By.ID, field_id).get_attribute("class")