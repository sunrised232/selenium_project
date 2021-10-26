from selenium import webdriver
import time
import func

list_data = func.read_file('conf/conf_vbc_bank_bg.txt')

url = "https://test.vbc.loc/resources/secured/app/entry/login/oper-or-partner"
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_argument('window-size=1920,1080')
driver = webdriver.Chrome(executable_path="chromedriver.exe",options=options)

driver.get(url=url)

func.do_click(driver, "//button[@id = 'email-tab']")#Переключится на вход по email

func.do_send(driver, "//input[@id = 'email-input']",list_data[0])#Ввод логина

func.do_send(driver, "//input[@id = 'password-input']",list_data[1])#Ввод пароля

func.do_click(driver, "//button[@id = 'email_sign-in-button']")#Войти

func.do_click(driver, "(//div[@class='pr-nav-menu-link'])[2]")#Пункт бг

func.do_click(driver, "// span[contains(text(), 'Заявки')]")#Перейти в заявки

func.do_click(driver, "(// button[contains(@class,'dropdown-t')])[1]")#Перейти в последнюю заявку

func.do_click(driver, "(// button[contains(text(), 'Откры')])[19]")#Открыть

time.sleep(1)
func.do_click(driver, "//button[@class = 'btn btn-lg btn-primary']")#Взять на рассмотрение

func.do_click(driver, "//button[@theme= 'success']")#Да

func.do_click(driver, "//button[contains(@class, 'btn btn-lg btn-pr')]") #Отправить на ЭКХ

func.do_click(driver, "//button[@theme= 'success']")  # Да

func.do_send(driver, "//input[@formcontrolname='commission']",list_data[2])#Ввод комиссии

func.do_click(driver, "(//input[@aria-autocomplete='list'])[3]")#Лист

func.do_click(driver, "//span[contains(@class,'ng-option-label ng-star-inserted')]")#Выбор первого подписанта

func.do_click(driver, "(//button[@class = 'btn btn-lg btn-primary'])[2]")#Сформировать предложение

func.do_click(driver, "//button[@theme= 'success']")  # Да

func.do_click(driver, "(//button[@class = 'btn btn-lg btn-primary'])[2]")  # Сформировать предложение
time.sleep(1500)
    
print('Confirm!')

driver.close()
driver.quit()
