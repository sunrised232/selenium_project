# -*- coding: utf-8 -*-
#Синтаксис xpath
'''
//tag[text()='something']
//a поиск по элементам а
//button поиск по элементам кнопок
//a[@class = ''] поиск по классам
//a[@id = ''] поиск по id
//button[contains(text(),'Открыть')] Находит текст в элементе
'''
#Синтаксис Selenium
'''
element.send_keys("sunrised232") ввод в найденное поле
element.click() клик по найденному элементу
'''

from selenium import webdriver
import time, sys,codecs

#Получение данных из файла

with codecs.open('auotreg/conf_vbc_reg_client.txt', encoding='utf-8') as fin:
    line = next(fin)
    work_with_file = line.strip()
list_data = work_with_file.split(',')

#Функция отвечающая за поиск элементов и клика по нему
def find_click(xpath):
    element = driver.find_element_by_xpath(xpath).click()
    return element

#Функция отвечающая за поиск элементов и ввода
def find_and_send(xpath,string_to_send):
    element = driver.find_element_by_xpath(xpath).send_keys(string_to_send)
    return element


url = "https://test.vbc.loc/resources/secured/app/auth/sign-up/by-email"
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(executable_path="chromedriver.exe",options=options)

try:
    driver.get(url=url)
    #element = find_click("//button[@id = 'email-tab']")#Переключится на вход по email

    if list_data[0] == '1':
        element = find_click("//label[contains(text(),'Индивидуальный предприниматель')]")#Рег ИП
        
    element = find_and_send("//input[@name = 'inn']",list_data[1])#Огрнип

    element = find_and_send("//input[@name= 'fullName']",list_data[2])#list_data[2]) #ФИО

    element = find_and_send("//input[@name= 'phone']",'0000000000') #Телефон

    element = find_and_send("//input[@name= 'email']",list_data[3]) #Email

    element = find_click("//label[@for='privacy-policy']")#Соглашение
    
    element = find_click("//button[text()=' Зарегистрироваться ']")#Зарегать
    
    time.sleep(15)
except Exception as ex:
    print(ex)
    
finally:
    driver.close()
    driver.quit()


url = "http://mail.vbc.loc/?_task=mail&_mbox=INBOX"
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(executable_path="chromedriver.exe",options=options)
try:
    driver.get(url=url)
    element = find_and_send("//input[@name = '_user']",'test1@vbc.loc')#Логин на почте
    element = find_and_send(" //input[@name = '_pass']",'testpassuser')#Логин на почте
    
    element = find_click("//button[@id= 'rcmloginsubmit']")#Войти
    
    time.sleep(5)
    element = find_click("//span[text()='ВБЦ: Регистрация в системе']")
    element = find_click("//span[text()='ВБЦ: Регистрация в системе']")
    time.sleep(2)
    url_pars = driver.find_element_by_xpath("//a[contains(text(),'test')][@rel = 'noreferrer']").text
    time.sleep(1)
except Exception as ex:
    print(ex)
    
finally:
    driver.close()
    driver.quit()

url = url_pars
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(executable_path="chromedriver.exe",options=options)

try:
    driver.get(url=url)
    print ('Test confirm')
    element = find_and_send("//input[@name ='phone']",'0000000000')#
    element = find_and_send("//input[@name ='password']",'123')
    element = find_and_send("//input[@name ='confirmPassword']",'123')
    element = find_click("//label[contains(text(),'кон')]")
    element = find_click("//button[contains(text(),'Под')]")
    time.sleep(20)
    
    
except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
