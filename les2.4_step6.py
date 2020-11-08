from selenium import webdriver
import time
from math import log, sin

link = "http://suninjuly.github.io/cats.html"

def calc(x):
  return str(log(abs(12*sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    button = browser.find_element_by_id("button")

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
