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
#vbc_Oper
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
#vbc_client_2
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

func.do_click(driver, "//td[contains(text(),'" + number_order + "')]")

time.sleep(1)
func.do_click(driver, "//span[contains(text(),'Перейти в заявку')]")

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
#vbc_bank_1
'''


list_data = func.read_file('conf/conf_vbc_bank_bg.txt')

url = "https://test.vbc.loc/resources/secured/app/entry/login/oper-or-partner"
options = webdriver.ChromeOptions()
options.add_extension("extension_1_2_8_0.crx")
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_argument('window-size=1920,1080')
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)

driver.get(url=url)

func.do_click(driver, "//button[@id = 'email-tab']")  # Переключится на вход по email

func.do_send(driver, "//input[@id = 'email-input']", list_data[0])  # Ввод логина

func.do_send(driver, "//input[@id = 'password-input']", list_data[1])  # Ввод пароля

func.do_click(driver, "//button[@id = 'email_sign-in-button']")  # Войти

xpath_give = "//button[@class = 'btn-close modal-btn btn-round']" # Закрыть всплывающее окно
if func.check_exists_by_xpath(driver, xpath_give) is True:
    func.do_click(driver, xpath_give)

func.do_click(driver, "(//div[@class='pr-nav-menu-link'])[2]")  # Пункт бг

func.do_click(driver, "// span[contains(text(), 'Заявки')]")  # Перейти в заявки

time.sleep(2)
element = func.find_element(driver, "//div[contains(text(),'" + number_order + "')]")#Открыть заявку по номеру
actions = ActionChains(driver)
actions.double_click(element).perform()

func.do_click(driver, "//button[contains(text(),'В')]")  # Взять на рассмотрение

func.do_click(driver, "//button[contains(text(),'Да')]") #Да

func.do_click(driver, "//button[contains(text(),'ЭКК')]") #Отправить на ЭКК

func.do_click(driver, "//button[contains(text(),'Да')]") #Да

time.sleep(1)
func.do_send(driver, "//input[contains(@formcontrolname,'co')]", '1')  # Ввод комиссии

func.do_click(driver, "(//input[@type='text'])[3]") #Выбрать подписанта

func.do_click(driver, "//div[contains(@class, 'ng-o')]") #Выбрать подписанта из списка

func.do_click(driver, "//button[contains(text(),'Сфор')]") #Сформировать предложение

func.do_click(driver, "//button[contains(text(),'Да')]") #Да

func.do_click(driver, "//button[contains(text(),' Подписать и')]") #Да

func.do_click(driver, "//div[@class = 'ng-select-container']") # подписи в наличии

func.do_click(driver, "//div[@role='option']")# Выбрать подпись

time.sleep(5)

print('Confirm!')

driver.close()
driver.quit()
'''

#vbc_client_3
'''
list_data = func.read_file('conf/conf_vbc_client_bg.txt')

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

func.do_click(driver, "(//div[@class = 'cl-nav-menu-link'])[3]")#Продукты по бизнесу

func.do_click(driver, "//span[@class='pr-2']")#Бг

func.do_click(driver, "//div[contains(text(),'Е')]")#Есть предложение

xpath_give = "//vbc-offer-preview[@prefix='BG']" # Закрыть всплывающее окно
if func.check_exists_by_xpath(driver, xpath_give) is True:
    func.do_click(driver, "//td[@class = 'text-center']")

func.do_click(driver, "//td[contains(text(),'" + number_order + "')]")#Открыть окно заявки

func.do_click(driver, "//span[contains(text(),'Пере')]") # перейти в заявку

func.do_click(driver, "//tr/td[contains(text(),' Откры')]") # перейти в гпб

func.do_click(driver, "//button[contains(text(),'При')]") # принять в гпб

func.do_click(driver, "//button[contains(text(),'Само')]")

func.do_click(driver, "//label")

func.do_click(driver, "//button[contains(text(),'и п')]")

func.do_click(driver, "(//div[@class='ng-select-container'])[2]")

func.do_click(driver, "//div[@role='option']")

func.do_click(driver, "//button[@class='close']")


time.sleep(5)
driver.close()
driver.quit()

'''
#vbc_bank_2
'''


list_data = func.read_file('conf/conf_vbc_bank_bg.txt')

url = "https://test.vbc.loc/resources/secured/app/entry/login/oper-or-partner"
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

func.do_click(driver, "(//div[@class = 'pr-nav-menu-link'])[2]")#Продукты по бизнесу

func.do_click(driver, "//span[contains(text(),'Зая')]")#Бг

func.do_click(driver, "//label[contains(text(),'е з')]")#Есть предложение

time.sleep(2)
element = func.find_element(driver, "//div[contains(text(),'" + number_order + "')]")#Поиск закупки по номеру
actions = ActionChains(driver)
actions.double_click(element).perform()

func.do_send(driver, "//input[@formcontrolname='orderId']",number_order)#Ввод номера заявки

func.do_send(driver, "//input[@formcontrolname='amount']",'1')#Ввод суммы платежа

func.do_click(driver, "//button[contains(text(),'По')]")#подтвердить

func.do_click(driver, "//button[contains(text(),'Да')]")#да

func.do_click(driver, "(//button[contains(@class,'dropdown-t')])[3]")

func.load_file(driver,"//input[@type='file']","C:/Users/Kovalev_a/Desktop/1.png")#Сюда грузить

time.sleep(500)
driver.close()
driver.quit()






