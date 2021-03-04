from selenium import webdriver
import math
link = "http://suninjuly.github.io/execute_script.html"

browser=webdriver.Chrome()
browser.get(link)
value1 = browser.find_element_by_id("input_value")
x_element = value1.text
x = int(x_element)
   
def calc(x):
    return str(math.log(abs(12*math.sin(x))))
z=(calc(x))

input1 = browser.find_element_by_id("answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
input1.send_keys(z)
check1 = browser.find_element_by_id("robotCheckbox")
check1.click()
radio1=browser.find_element_by_id("robotsRule")
radio1.click()
#robots=radio1.get_attribute("checked")
button = browser.find_element_by_tag_name("button")
button.click()
assert True
