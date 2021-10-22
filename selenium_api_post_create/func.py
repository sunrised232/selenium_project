import codecs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# Проверка есть ли элемент на странице
def check_exists_by_xpath(driver, xpath):
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return True
    except TimeoutException:
        return False

# Функция поиска элемента
def find_element(driver, xpath):
    return WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))

# Нажать по всем элементам списка
def wait_do_click_list(driver, xpath):
    element = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH,xpath)))
    for i in element:
        i.click()

# Функция отвечающая за поиск элементов и клика по нему
def do_click(driver, xpath):
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, xpath))).click()#10

# Функция отвечающая за поиск элементов и ввода
def do_send(driver, xpath, string_to_send):
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, xpath))).send_keys(string_to_send)

def read_file(path):
    with codecs.open(path, encoding='utf-8') as fin:
        line = next(fin)
        work_with_file = line.strip()
    return work_with_file.split()

def clear_area(driver, xpath):
    WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, xpath))).clear()

def read_file_comma(path):
    with codecs.open(path, encoding='utf-8') as fin:
        line = next(fin)
        work_with_file = line.strip()
    return work_with_file.split(',')