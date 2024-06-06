from selenium.webdriver.common.by import By
from data import *

def data1(chrome_browser):
    chrome_browser.get('https://www.saucedemo.com/')
    chrome_browser.find_element(By.ID, "user_name").send_keys('standard_user')
    chrome_browser.find_element(By.ID, "password").send_keys('secret_sauce')
    chrome_browser.find_element(By.ID, "login").click()
#Добавить 3 товара в корзину
    add_to_cart = [
        (By.ID, 'add-to-cart-sauce-labs-backpack'),
        (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt'),
        (By.ID, 'add-to-cart-sauce-labs-onesie')
    ]
    for cart in add_to_cart:
        chrome_browser.find_element(*cart).click()
#Переход к корзине
    chrome_browser.find_element(By.ID, 'shopping_cart_container').click()
    chrome_browser.find_element(By.ID, 'checkout').click()
#Информация о покупателе 
    chrome_browser.find_element(By.ID, "first-name").send_keys('Ксюха')
    chrome_browser.find_element(By.ID, "last-name").send_keys('Морогова')
    chrome_browser.find_element(By.ID, "postal-code").send_keys('614022')
    chrome_browser.find_element(By.ID, "continue").click()

    price = chrome_browser.find_element(By.CLASS_NAME, 'summary_total_label')
    total_price = price.text.strip().replace('Total : $', '')
    total_amount = '58.29'
    assert total_price == total_amount
    print(f'Итоговая сумма равна ${total_price}')