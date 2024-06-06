from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import *

def data1(chrome_browser):
    chrome_browser.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
    delay = chrome_browser.find_element(By.ID, "delay")
    delay.clear()
    delay.send_keys(45)

    chrome_browser.find_element(By.XPATH, "//span[text() = '7']").click()
    chrome_browser.find_element(By.XPATH, "//span[text() = '+']").click()
    chrome_browser.find_element(By.XPATH, "//span[text() = '8']").click()
    chrome_browser.find_element(By.XPATH, "//span[text() = '=']").click()

    WebDriverWait(chrome_browser, 48).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), '15'))
    res = chrome_browser.find_element(By.CLASS_NAME, 'screen').text

    assert res == '15'