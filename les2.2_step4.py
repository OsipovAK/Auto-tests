from selenium import webdriver
browser = webdriver.Chrome()
browser.execute_script('document.title="Script executing";')

# ����� ����� ����-������ ���������. ���������� JavaScript �� �������� - ��� ����������� � ������������ Selenium ������ ������ ��������.
# ������ ���������� find_element_by... ����� ������������ ��� ����� �����������:
# element = browser.execute_script('document.getElementsByName("name")')

# ��� �� ���� �����������:
# getElementById
# getElementsByTagName
# getElementsByClassName
# querySelector - ��� CSS
# querySelectorAll - ��� CSS (������� ��� ����������)

# evaluate - ��� XPATH.

# ���������.