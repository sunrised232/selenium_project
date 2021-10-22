from selenium import webdriver
import time, func
from selenium.webdriver.common.action_chains import ActionChains

alfa = '1234567890'
number_order = ''

list_data = func.read_file('conf/conf_vbc_client_bg.txt')

url = "https://test.vbc.loc/resources/secured/app/entry/login/client"
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_argument('window-size=1920,1080')
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)

driver.get(url=url)

func.do_click(driver, "//button[@id = 'email-tab']")  # Переключится на вход по email

func.do_send(driver, "//input[@id = 'email-input']", list_data[0])  # Ввод логина

func.do_send(driver, "//input[@id = 'password-input']", list_data[1])  # Ввод пароля

func.do_click(driver, "//button[@id = 'email_sign-in-button']")  # Войти

xpath_give = "//button[@class = 'btn-close modal-btn btn-round']"  # Закрыть всплывающее окно
if func.check_exists_by_xpath(driver, xpath_give) is True:
    func.do_click(driver, xpath_give)

func.do_click(driver, "//button[@class = 'btn btn-success-700']")  # Получить продукт

func.do_click(driver, "//img[@class = 'credit-header-img']")  # Экспресс БГ

func.do_send(driver, "//input[contains(@formcontrolname, 'purchaseNumber')]", list_data[2])  # Ввод номера закупки

func.do_click(driver, "//button[@class = 'mt-3 success']")  # Загрузить

# 1 Данные
func.do_send(driver, "//input[contains(@class,'ng-empty ng-u')]", list_data[3])  # написать Дату

func.do_click(driver, "//button[@class='success']")  # Кнопка Далее

# 2 Анкета
func.do_click(driver, "//td[contains(@routerlink,'check/blank')]")

# Получение номера заявки
string_number_order = driver.find_element_by_xpath("(//div[@class = 'item'])[1]").text
for i in string_number_order:
    if i in alfa:
        number_order = number_order + i

func.do_click(driver, "//div[@class = 'd-inline-flex']")  # Сохранить

func.do_click(driver, "//button[@class = 'success']")  # Подтвердить

func.do_click(driver, "//button[text() = ' Запустить проверку ']")  # Запустить проверку

time.sleep(5)

driver.close()
driver.quit()

list_data = func.read_file('conf/conf_vbc_oper_bg.txt')

'''
vbc_Oper
'''

url = "https://test.vbc.loc/resources/secured/app/entry/login/oper-or-partner"
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_argument('window-size=1920,1080')
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)

driver.get(url=url)
func.do_click(driver, "//button[@id = 'email-tab']")  # Переключится на вход по email

func.do_send(driver, "//input[@id = 'email-input']", list_data[0])  # Ввод логина

func.do_send(driver, "//input[@id = 'password-input']", list_data[1])  # Ввод пароля

func.do_click(driver, "//button[@id = 'email_sign-in-button']")  # Войти

xpath_give = "//button[@class='btn-close modal-btn btn-round']"
if func.check_exists_by_xpath(driver, xpath_give) is True:
    func.do_click(driver, xpath_give)

func.do_click(driver, "//span[contains(text(),'Банко')]")  # Пункт меню "Банковская гарантия"

func.do_click(driver, "//vbc-op-nav-sub[@routerlink= 'bg/list/orders']")
time.sleep(2)

element = func.find_element(driver, "//td[contains(text(),'" + number_order + "')]")
actions = ActionChains(driver)
actions.double_click(element).perform()

func.do_click(driver, "//button[@class='primary']")  # Взять на валидацию

func.do_click(driver, "(//button[@vbcuibutton])[2]")  # Далее

func.do_click(driver, "//button[@class = 'h-100 success']")  # Подтвердить и сохранить

func.do_click(driver, "(//button[@class='light ng-star-inserted'])[2]")  # Подтвердить и сохранить

time.sleep(2)
func.do_click(driver, "//button[@class='success']")

func.do_click(driver, "(//button[@class='light ng-star-inserted'])[2]")  # Далее

func.do_click(driver, "(//span[@class='af-value af-success-value'])[8]")  # Участие акционеров...>нет

func.do_click(driver, "//button[contains(@class,'succes')]")  # Сохранить донесение информации

func.do_click(driver, "(//button[@class='light ng-star-inserted'])[2]")  # Далее

func.wait_do_click_list(driver,
                        "//fa-icon[contains(@class,'ng-fa-icon ui-checkbox-icon-unchecked')]")  # Произвести клики по всем банкам

func.do_click(driver, "//button[contains(@class,'succes')]")  # Сохранить результаты скоринга

time.sleep(7)

print('Confirm!')

driver.close()
driver.quit()


list_data = func.read_file('conf/conf_vbc_client_bg.txt')

'''
vbc_client_2
'''
url = "https://test.vbc.loc/resources/secured/app/entry/login/client"
options = webdriver.ChromeOptions()
options.add_extension("extension_1_2_8_0.crx")
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_argument('window-size=1920,1080')
driver = webdriver.Chrome(executable_path="chromedriver.exe",options=options)

driver.get(url=url)

func.do_click(driver, "//button[@id = 'email-tab']")#Переключится на вход по email

func.do_send(driver, "//input[@id = 'email-input']",list_data[0])#Ввод логина

func.do_send(driver, "//input[@id = 'password-input']",list_data[1])#Ввод пароля

func.do_click(driver, "//button[@id = 'email_sign-in-button']")#Войти

xpath_give = "//button[@class = 'btn-close modal-btn btn-round']" # Закрыть всплывающее окно
if func.check_exists_by_xpath(driver, xpath_give) is True:
    func.do_click(driver, xpath_give)

func.do_click(driver, "(//div[@class = 'cl-nav-menu-link'])[3]")

func.do_click(driver, "//span[@class='pr-2']")
#НИХУЯ НЕ РАБОТАЕТ ЗДЕСЬ
#НИХУЯ НЕ РАБОТАЕТ ЗДЕСЬ
#НИХУЯ НЕ РАБОТАЕТ ЗДЕСЬ
#НИХУЯ НЕ РАБОТАЕТ ЗДЕСЬ
#НИХУЯ НЕ РАБОТАЕТ ЗДЕСЬ
#НИХУЯ НЕ РАБОТАЕТ ЗДЕСЬ
#НИХУЯ НЕ РАБОТАЕТ ЗДЕСЬ
#НИХУЯ НЕ РАБОТАЕТ ЗДЕСЬ
#НИХУЯ НЕ РАБОТАЕТ ЗДЕСЬ
#НИХУЯ НЕ РАБОТАЕТ ЗДЕСЬ#НИХУЯ НЕ РАБОТАЕТ ЗДЕСЬ#НИХУЯ НЕ РАБОТАЕТ ЗДЕСЬ#НИХУЯ НЕ РАБОТАЕТ ЗДЕСЬ
#НИХУЯ НЕ РАБОТАЕТ ЗДЕСЬ
#НИХУЯ НЕ РАБОТАЕТ ЗДЕСЬ#НИХУЯ НЕ РАБОТАЕТ ЗДЕСЬ





time.sleep(2)
element = func.find_element(driver, "//td[contains(text(),'" + number_order + "')]")
actions = ActionChains(driver)
actions.double_click(element).perform()

xpath_give = "//button[@theme = 'success']"
if func.check_exists_by_xpath(driver, xpath_give) is True:
    func.do_click(driver, xpath_give)

func.do_click(driver, "(//button[@class = 'btn btn-success-700'])[2]") # Подписать и отправить

time.sleep(1)

func.do_click(driver, "//div[@class = 'ng-select-container']") # подписи в наличии

func.do_click(driver, "//div[@class = 'ng-option ng-option-marked']")# Выбрать подпись


time.sleep(15)

print('Confirm!')

driver.close()
driver.quit()

'''
vbc_bank_1
'''
list_data = func.read_file('conf/conf_vbc_bank_bg.txt')

url = "https://test.vbc.loc/resources/secured/app/entry/login/oper-or-partner"
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_argument('window-size=1920,1080')
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)

driver.get(url=url)

func.do_click(driver, "//button[@id = 'email-tab']")  # Переключится на вход по email

func.do_send(driver, "//input[@id = 'email-input']", list_data[0])  # Ввод логина

func.do_send(driver, "//input[@id = 'password-input']", list_data[1])  # Ввод пароля

func.do_click(driver, "//button[@id = 'email_sign-in-button']")  # Войти

func.do_click(driver, "(//div[@class='pr-nav-menu-link'])[2]")  # Пункт бг

func.do_click(driver, "// span[contains(text(), 'Заявки')]")  # Перейти в заявки

time.sleep(2)
element = func.find_element(driver, "//td[contains(text(),'" + number_order + "')]")
actions = ActionChains(driver)
actions.double_click(element).perform()

time.sleep(1)
func.do_click(driver, "//button[@class = 'btn btn-lg btn-primary']")  # Взять на рассмотрение

func.do_click(driver, "//button[@theme= 'success']")  # Да

func.do_click(driver, "//button[contains(@class, 'btn btn-lg btn-pr')]")  # Отправить на ЭКХ

func.do_click(driver, "//button[@theme= 'success']")  # Да

func.do_send(driver, "//input[@formcontrolname='commission']", list_data[2])  # Ввод комиссии

func.do_click(driver, "(//input[@aria-autocomplete='list'])[3]")  # Лист

func.do_click(driver, "//span[contains(@class,'ng-option-label ng-star-inserted')]")  # Выбор первого подписанта

func.do_click(driver, "(//button[@class = 'btn btn-lg btn-primary'])[2]")  # Сформировать предложение

func.do_click(driver, "//button[@theme= 'success']")  # Да

func.do_click(driver, "(//button[@class = 'btn btn-lg btn-primary'])[2]")  # Сформировать предложение

print('Confirm!')

driver.close()
driver.quit()
