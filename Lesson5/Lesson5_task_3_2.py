from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

Chrome = webdriver.Chrome()
Firefox = webdriver.Firefox()

try:
    Check = 0
    Chrome.get('https://uitestingplayground.com/dynamicid')
    Firefox.get('https://uitestingplayground.com/dynamicid')

#Кликнуть на синюю кнопку
    button = Chrome.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
    button = Firefox.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
#Кликнуть на кнопку 3 раза 
    for _ in range(3):
        button = Chrome.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
        button = Firefox.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
        Check = Check + 1
        sleep(3)
        print(Check)

except Exception as e:
    print(e)
finally:
    Chrome.quit()
    Firefox.quit()