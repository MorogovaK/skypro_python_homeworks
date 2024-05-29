from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

Chrome = webdriver.Chrome()
Firefox = webdriver.Firefox()

try:
    Chrome.get('https://the-internet.herokuapp.com/inputs')
    Firefox.get('https://the-internet.herokuapp.com/inputs')

    input_type_chrome = Chrome.find_element(By.TAG_NAME, "input")
    input_type_chrome.send_keys('1000')
    sleep(1)
    input_type_chrome.clear()
    sleep(1)
    input_type_chrome.send_keys('999')
    sleep(1)

    input_type_firefox = Firefox.find_element(By.TAG_NAME, "input")
    input_type_firefox.send_keys('1000')
    sleep(1)
    input_type_firefox.clear()
    sleep(1)
    input_type_firefox.send_keys('999')
    sleep(1)

except Exception as e:
    print(e)
finally:
    Chrome.quit()
    Firefox.quit()