import pytest
from selenium import webdriver
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button_on_the_page(browser):
    browser.get(link)
    time.sleep(30)
    btn = browser.find_elements_by_css_selector(".btn-primary .btn-add-to-busket")
    assert btn != 0, "Button was not found"
