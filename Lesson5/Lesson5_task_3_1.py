from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

Chrome = webdriver.Chrome()
Firefox = webdriver.Firefox()

try:
    Chrome.get("https://the-internet.herokuapp.com/add_remove_elements/")
    Firefox.get("https://the-internet.herokuapp.com/add_remove_elements/")

#Нажать на кнопку Add Element 5 раз
    for _ in range(5):
        add_button = Chrome.find_element(By.XPATH, "//button[text()='Add Element']").click()
        add_button = Firefox.find_element(By.XPATH, "//button[text()='Add Element']").click()
        sleep(2)

#Собрать список кнопки Delete
    Chrome_delete_buttons = Chrome.find_elements("xpath", "//button[text()='Delete']")
    Firefox_delete_buttons = Firefox.find_elements("xpath", "//button[text()='Delete']")

#Вывести на экран размер списка
    print(f'Размер списка кнопок Delete в Chrome:{len(Chrome_delete_buttons)}')
    print(f'Размер списка кнопок Delete в Firefox:{len(Firefox_delete_buttons)}')


except Exception as e:
    print(e)
finally:
    Chrome.quit()
    Firefox.quit()