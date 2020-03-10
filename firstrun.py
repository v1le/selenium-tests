import time
import math
import os
from selenium import webdriver


URL = "http://suninjuly.github.io/file_input.html"

def get_answer(value):
    return str(math.log(abs(12*math.sin(int(value)))))

def get_dir():
    return os.getcwd() + '\\temp.txt'

try:
    browser = webdriver.Chrome()
    browser.get(URL)

    name = browser.find_element_by_css_selector('[name="firstname"]')
    name.send_keys('name')

    surname = browser.find_element_by_css_selector('[name="lastname"]')
    surname.send_keys('surname')

    email = browser.find_element_by_css_selector('[name="email"]')
    email.send_keys('e@ma.il')

    file = browser.find_element_by_css_selector('[name="file"]')
    file.send_keys(get_dir())

    button = browser.find_element_by_css_selector('.btn-primary')
    button.click()


finally:
    time.sleep(10)
    browser.quit()
