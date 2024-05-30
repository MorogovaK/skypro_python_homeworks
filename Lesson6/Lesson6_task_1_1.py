from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E


Chrome = webdriver.Chrome()
expectation = WebDriverWait(Chrome, 20)

try:
    Chrome.get('https://uitestingplayground.com/ajax')

#Кликнуть на синюю кнопку
    button = Chrome.find_element(By.CSS_SELECTOR, '#ajaxButton').click()
#Вывести текст в консоль
    text = expectation.until(E.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))).text
    print(text)

except Exception as e:
    print(e)
finally:
    Chrome.quit()