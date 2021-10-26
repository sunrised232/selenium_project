from selenium import webdriver
import time
import func

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

func.do_click(driver, "(//div[@class = 'cl-nav-menu-link'])[3]")

func.do_click(driver, "//span[@class='pr-2']")

func.do_click(driver, "(//td[@class='text-center'])[1]") # Открыть последнюю бг

xpath_give = "//span[contains(text(),'Перейти')]"
if func.check_exists_by_xpath(driver, xpath_give) is True:
    func.do_click(driver, xpath_give)

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
