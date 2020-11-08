from selenium import webdriver
import time 
import math
from math import log, sin

link = "http://suninjuly.github.io/execute_script.html"

# Объявляем функцию для вычисления переменной Y
def calc(x):
  return str(log(abs(12*sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    browser.execute_script("window.scrollBy(0, 100);")
    robotCheckbox = browser.find_element_by_id('robotCheckbox')
    robotCheckbox.click()
    radio = browser.find_element_by_id('robotsRule')
    radio.click()
    button = browser.find_element_by_tag_name("button")

    button.click()
#   button = browser.find_element_by_css_selector("button.btn")
#   button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
