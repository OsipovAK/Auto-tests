from selenium import webdriver
import time
from math import log, sin

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(log(abs(12*sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_css_selector("button")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)


    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
