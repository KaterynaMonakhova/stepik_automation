from selenium import webdriver
import math
link = "http://suninjuly.github.io/redirect_accept.html"

browser=webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_class_name("trollface")
button.click()

browser.switch_to.window(Redirect page)
new_window = browser.window_handles[1]

value1 = browser.find_element_by_id("input_value")
x_element = value1.text
x = int(x_element)
   
def calc(x):
    return str(math.log(abs(12*math.sin(x))))
z=(calc(x))

input1 = browser.find_element_by_id("answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
input1.send_keys(z)

button = browser.find_element_by_class_name("btn-primary")
button.click()
assert True
