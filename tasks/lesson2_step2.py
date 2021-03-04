from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
link1="http://suninjuly.github.io/selects1.html"

try:
    browser=webdriver.Chrome()
    browser.get(link1)
    value1 = browser.find_element_by_id("num1")
    x_element = value1.text
    x = int(x_element)
    value2 = browser.find_element_by_id("num2")
    y_element = value2.text
    y = int(y_element)

    def calc(x):
        return str(x+y)
    z=(calc(x))
    browser.find_element_by_id("dropdown").click()
    browser.find_element_by_css_selector('[value="' + z +'"]').click()
    button1=browser.find_element_by_class_name("btn")
    button1.click()
finally:
    time.sleep(10)
    browser.quit()
