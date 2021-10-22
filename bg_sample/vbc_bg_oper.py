from selenium import webdriver
import time, func

from selenium.webdriver.common.action_chains import ActionChains

#Функция отвечающая за поиск элементов и клика по нему
def find_click(driver, xpath):
    driver.find_element_by_xpath(xpath).click()

list_data = func.read_file('conf/conf_vbc_oper_bg.txt')

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

xpath_give ="//button[@class='btn-close modal-btn btn-round']"
if func.check_exists_by_xpath(driver, xpath_give) is True:
    func.do_click(driver, xpath_give)

func.do_click(driver, "//span[contains(text(),'Банко')]")#Пункт меню "Банковская гарантия"

func.do_click(driver, "//vbc-op-nav-sub[@routerlink= 'bg/list/orders']")
time.sleep(2)

element = func.find_element(driver,"//td[contains(text(),'",number_order,"')]")
actions = ActionChains(driver)
actions.double_click(element).perform()

func.do_click(driver, "//button[@class='primary']")#Взять на валидацию

func.do_click(driver, "(//button[@vbcuibutton])[2]") #Далее

func.do_click(driver, "//button[@class = 'h-100 success']") #Подтвердить и сохранить

func.do_click(driver, "(//button[@class='light ng-star-inserted'])[2]") #Подтвердить и сохранить

time.sleep(2)
func.do_click(driver, "//button[@class='success']")

func.do_click(driver, "(//button[@class='light ng-star-inserted'])[2]")#Далее

func.do_click(driver, "(//span[@class='af-value af-success-value'])[8]")#Участие акционеров...>нет

func.do_click(driver, "//button[contains(@class,'succes')]")#Сохранить донесение информации
    
func.do_click(driver, "(//button[@class='light ng-star-inserted'])[2]")#Далее

func.wait_do_click_list(driver, "//fa-icon[contains(@class,'ng-fa-icon ui-checkbox-icon-unchecked')]")#Произвести клики по всем банкам

func.do_click(driver, "//button[contains(@class,'succes')]")#Сохранить результаты скоринга
    
time.sleep(7)

print ('Confirm!')

driver.close()
driver.quit()
