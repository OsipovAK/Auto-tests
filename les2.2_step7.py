from selenium import webdriver
import time

# обязательный модуль для работы с файлами 
import os 

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    firstname = browser.find_element_by_name('firstname')
    firstname.send_keys("Ivan")
    lastname = browser.find_element_by_name('lastname')
    lastname.send_keys("Ivanov")
    email = browser.find_element_by_name('email')
    email.send_keys("Ivanov@mail.ru")

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла 
    file_path = os.path.join(current_dir, 'les2.2_step7_text.txt')
    # ищем элемент для добавления файла
    file = browser.find_element_by_name('file')
    # вписываем полный путь файла
    file.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
