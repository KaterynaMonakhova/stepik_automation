from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
link1="http://suninjuly.github.io/get_attribute.html"

try:
    browser=webdriver.Chrome()
    browser.get(link1)
    img_box = browser.find_element_by_id("treasure")
    x_element = img_box.get_attribute("valuex")
    x = x_element
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y=(calc(x))
    input1=browser.find_element_by_id("answer")
    input1.send_keys(y)
    input2=browser.find_element_by_id("robotCheckbox")
    input2.click()
    input3=browser.find_element_by_id("peopleRule")
    input4=browser.find_element_by_id("robotsRule")
    input4.click()
    button1=browser.find_element_by_class_name("btn")
    button1.click()
finally:
    time.sleep(15)
    browser.quit()
