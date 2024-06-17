from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from configuration import *
from data_test import chrome_browser
from time import sleep

def test_shop(chrome_browser):
    chrome_browser.get(URL_3)

    chrome_browser.find_element(By.ID, "user-name").send_keys("standard_user")
    chrome_browser.find_element(By.ID, "password").send_keys("secret_sauce")
    chrome_browser.find_element(By.ID, "login-button").click()

    add_to_cart_button = [
        (By.ID, "add-to-cart-sauce-labs-backpack"),
        (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
        (By.ID, "add-to-cart-sauce-labs-onesie")
    ]
    for button in add_to_cart_button:
        chrome_browser.find_element(*button).click()

    chrome_browser.find_element(By.ID, "shopping_cart_container").click()
    chrome_browser.find_element(By.ID, "checkout").click()

    chrome_browser.find_element(By.ID, "first-name").send_keys("Ksenia")
    chrome_browser.find_element(By.ID, "last-name").send_keys("Morogova")
    chrome_browser.find_element(By.ID, "postal-code").send_keys("614022")
    chrome_browser.find_element(By.ID, "continue").click()

    total_price = chrome_browser.find_element(By.CLASS_NAME, 'summary_total_label')
    total = total_price.text.strip().replace("Total: $", "")
    expected_total = "58.29"
    assert total == expected_total
    print(f"Итоговая сумма равна ${total}")