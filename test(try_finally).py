import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

try:
# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
	driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
	time.sleep(5)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
	driver.get("http://suninjuly.github.io/simple_form_find_task.html")
	time.sleep(5)

# Найдем кнопку, которая отправляет введенное решение
	button = driver.find_element_by_id("submit_button")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
	button.click()
	time.sleep(5)
finally:
# После выполнения всех действий мы не должны забыть закрыть окно браузера
	driver.quit()
