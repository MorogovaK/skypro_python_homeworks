from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E


Chrome = webdriver.Chrome()
expectation = WebDriverWait(Chrome, 50)
try:
    Chrome.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')
    expectation.until(E.text_to_be_present_in_element((By.CSS_SELECTOR, "#text"), 'Done!'))
#атрибут у 3-ей картинки
    atribute = Chrome.find_element(By.CSS_SELECTOR, '#award').get_attribute('src')
    print(atribute)

except Exception as e:
    print(e)
finally:
    Chrome.quit()