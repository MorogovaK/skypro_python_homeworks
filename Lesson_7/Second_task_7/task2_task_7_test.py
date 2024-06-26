import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from FirstPage import FirstPage
from fixture2 import *



def test_calculator(driver):
    first_page = FirstPage(driver)
    first_page.insert_time()
    first_page.find_numbers()
    first_page.wait_for_result()
    assert "15" in first_page.wait_for_result