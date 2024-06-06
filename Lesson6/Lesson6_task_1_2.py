from selenium import webdriver
from selenium.webdriver.common.by import By

Chrome = webdriver.Chrome()

try:
    Chrome.get('https://uitestingplayground.com/textinput')

#Указать в поле ввода название кнопки "SkyPro"
    button = Chrome.find_element(By.ID, 'newButtonName').send_keys("SkyPro")
#Кликнуть на синюю кнопку  
    blue_batton = Chrome.find_element(By.ID, 'updatingButton').click()
#ПолучитЬ текст кнопки и вывести в консоль
    button_SkyPro = Chrome.find_element(By.ID, 'updatingButton').text
    print(button_SkyPro)

except Exception as e:
    print(e)
finally:
    Chrome.quit()