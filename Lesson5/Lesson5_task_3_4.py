from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time 

Chrome = webdriver.Chrome()
Firefox = webdriver.Firefox()

try:
    Chrome.get('https://the-internet.herokuapp.com/entry_ad')
    Firefox.get('https://the-internet.herokuapp.com/entry_ad')
    expectation = WebDriverWait(Chrome, 7)
    expectation = WebDriverWait(Firefox, 7)
    MODAL_WINDOW = expectation.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.modal')))
    close_button = expectation.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.modal-footer')))
    time.sleep(2)

    close_button.click()

    time.sleep(2)
except Exception as e:
    print(e)
finally:
    Chrome.quit()
    Firefox.quit()
