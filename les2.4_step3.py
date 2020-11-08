from selenium import webdriver
import time
from math import log, sin

link = "http://suninjuly.github.io/wait1.html"

def calc(x):
  return str(log(abs(12*sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
#    time.sleep(2)
    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")
    assert "successful" in message.text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
