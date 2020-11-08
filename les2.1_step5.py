from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/math.html"

# Объявляем функцию для вычисления переменной Y
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    robotCheckbox = browser.find_element_by_class_name('form-check-label')
    robotCheckbox.click()
    radio = browser.find_element_by_id('robotsRule')
    radio.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла