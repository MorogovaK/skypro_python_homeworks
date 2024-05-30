from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

Chrome = webdriver.Chrome()
Firefox = webdriver.Firefox()

try:
    Chrome.get('https://uitestingplayground.com/classattr')
    Firefox.get('https://uitestingplayground.com/classattr')
    for _ in range(3):
        button = Chrome.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
        sleep(2)
        Chrome.switch_to.alert.accept()

        button = Firefox.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
        sleep(2)
        Firefox.switch_to.alert.accept()

except Exception as e:
    print(e)
finally:
    Chrome.quit()
    Firefox.quit()