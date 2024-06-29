from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from BuyOnStorePage import BuyOnStorePage
import allure


@allure.title("Оформление заказа в интернет-магазине")
@allure.description("Добавление в корзину товаров: Sauce Labs Backpack, Sauce Labs Bolt T-Shirt, Sauce Labs Onesie")
@allure.feature("FUNCTIONALITY")
@allure.severity("blocker")
def test_buy_on_store():
    with allure.step("Открытие браузера"):
        browser = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))

    with allure.step("Открытие сайта магазина: https://www.saucedemo.com/"):
        page = BuyOnStorePage(browser)

    with allure.step("Ввод standard_user в поле Username"):
        page.authorization_username('standard_user')

    with allure.step("Ввод secret_sauce в поле Password"):
        page.authorization_password('secret_sauce')

    with allure.step("Добавление в корзину товаров"):
        page.add_to_cart()

    with allure.step("Переход в корзину"):
        page.shopping_cart()

    with allure.step("Нажатие Checkout"):
        page.checkout()

    with allure.step("Ввод в поле First Name"):
        page.input_first_name('Ксения')

    with allure.step("Ввод в поле Last Name"):
        page.input_last_name('Морогова')

    with allure.step("Ввод в поле Zip/Postal Code"):
        page.input_postal_code('614095')

    with allure.step("Нажатие Continue"):
        page.button_continue()

    with allure.step("Отображение со страницы Итоговой стоимости (Total)"):
        total = page.summary_total()

    with allure.step("Проверка Итоговой стоимости (Total)"):
        assert total == 'Total: $58.29'

    with allure.step("Закрытие браузера"):
        browser.quit()