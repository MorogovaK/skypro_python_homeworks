from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

Chrome = webdriver.Chrome()
Firefox = webdriver.Firefox()

try:
    Chrome.get('https://the-internet.herokuapp.com/login')
    Firefox.get('https://the-internet.herokuapp.com/login')

    chrome_input_username = Chrome.find_element(By.ID, "username").send_keys('tomsmith')
    sleep(1)
    chrome_input_password = Chrome.find_element(By.ID, "password").send_keys('SuperSecretPassword!')
    sleep(1)
    button_login = Chrome.find_element(By.TAG_NAME, "button").click()
    sleep(1)

    firefox_input_username = Firefox.find_element(By.ID, "username").send_keys('tomsmith')
    sleep(1)
    firefox_input_password = Firefox.find_element(By.ID, "password").send_keys('SuperSecretPassword!')
    sleep(1)
    button_login = Firefox.find_element(By.TAG_NAME, "button").click()
    sleep(1)

except Exception as e:
    print(e)
finally:
    Chrome.quit()
    Firefox.quit()