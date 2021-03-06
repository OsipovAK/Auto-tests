from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/get_attribute.html"

# Объявляем функцию для вычисления переменной Y
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    treasure = browser.find_element_by_id('treasure')
    x = treasure.get_attribute("valuex")
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    robotCheckbox = browser.find_element_by_id('robotCheckbox')
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
