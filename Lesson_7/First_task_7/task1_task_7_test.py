from Mpage import MainPage 
from second_page import NextPage
from fixture import *


def test_color_of_fields(chrome_browser):
    main_page = MainPage(chrome_browser)
    main_page.find_fields()
    main_page.information_about_me()
    main_page.button_click()

    next_page = NextPage(chrome_browser)
    next_page.find_fields()
    next_page.get_class_first_name()
    next_page.get_class_last_name()
    next_page.get_class_phone()
    next_page.get_class_email()
    next_page.get_class_city()
    next_page.get_class_address()
    next_page.get_class_country()
    next_page.get_class_company()
    next_page.get_class_job_position()
    next_page.get_class_zip_code

    assert "success" in next_page.get_class_first_name()
    assert "success" in next_page.get_class_last_name()
    assert "succes" in next_page.get_class_address()
    assert "succes" in next_page.get_class_city()
    assert "succes" in next_page.get_class_country()
    assert "success" in next_page.get_class_phone()
    assert "success" in next_page.get_class_email()
    assert "success" in next_page.get_class_job_position()
    assert "success" in next_page.get_class_company()
    assert "danger" in next_page.get_class_zip_code()