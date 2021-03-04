from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

button1 = browser.find_element_by_id("book")
# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
message = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
button1.click()

value1 = browser.find_element_by_id("input_value")
x_element = value1.text
x = int(x_element)
   
def calc(x):
    return str(math.log(abs(12*math.sin(x))))
z=(calc(x))

input1 = browser.find_element_by_id("answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
input1.send_keys(z)

button = browser.find_element_by_id("solve")
button.click()
assert True
