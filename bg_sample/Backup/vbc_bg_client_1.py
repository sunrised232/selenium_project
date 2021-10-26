from selenium import webdriver
import time, func

list_data = func.read_file('conf/conf_vbc_client_bg.txt')


url = "https://test.vbc.loc/resources/secured/app/entry/login/client"
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_argument('window-size=1920,1080')
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)

driver.get(url=url)

func.do_click(driver, "//button[@id = 'email-tab']")# Переключится на вход по email

func.do_send(driver, "//input[@id = 'email-input']", list_data[0])# Ввод логина

func.do_send(driver, "//input[@id = 'password-input']", list_data[1])# Ввод пароля

func.do_click(driver, "//button[@id = 'email_sign-in-button']") # Войти

xpath_give = "//button[@class = 'btn-close modal-btn btn-round']" # Закрыть всплывающее окно
if func.check_exists_by_xpath(driver, xpath_give) is True:
    func.do_click(driver, xpath_give)
    
func.do_click(driver, "//button[@class = 'btn btn-success-700']") #Получить продукт

func.do_click(driver, "//img[@class = 'credit-header-img']") #Экспресс БГ

func.do_send(driver, "//input[contains(@formcontrolname, 'purchaseNumber')]", list_data[2])#Ввод номера закупки

func.do_click(driver, "//button[@class = 'mt-3 success']") #Загрузить

# 1 Данные
func.do_send(driver, "//input[contains(@class,'ng-empty ng-u')]", list_data[3])#написать Дату

func.do_click(driver, "//button[@class='success']") #Кнопка Далее

# 2 Анкета
#xpath_give = "//td[contains(@routerlink,'check/blank')]" # 115 фз проверка
#if func.check_exists_by_xpath(driver, xpath_give) is True:
func.do_click(driver, "//td[contains(@routerlink,'check/blank')]")

# Получение номера заявки
number_order = driver.find_element_by_xpath("(//div[@class = 'item'])[1]").text

func.do_click(driver, "//div[@class = 'd-inline-flex']") #Сохранить

func.do_click(driver, "//button[@class = 'success']") #Подтвердить

func.do_click(driver, "//button[text() = ' Запустить проверку ']")#Запустить проверку

time.sleep(5)

driver.close()
driver.quit()
