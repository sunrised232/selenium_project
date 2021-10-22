from selenium import webdriver
import time, func

url = "http://192.168.3.115:36635/swagger-ui/index.html?urls.primaryName=mobile#/"
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_argument('window-size=1920,1080')
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)

driver.get(url=url)

func.do_click(driver, "(//h4[@class = 'opblock-tag'])[15]") #открыть пункт api с постами

func.do_click(driver, "//span[contains(text(),'D')]") #Перейти в api удаления

func.do_click(driver, "//button[contains(text(),'T')]")

f = open('conf/save_post.txt')

for line in f:
    line = line.replace('\n','')
    info_post = line.split(',')

    time.sleep(0.2)

    func.do_send(driver, "//input[contains(@placeholder,'X-P')]", info_post[0])

    func.do_send(driver, "//input[contains(@placeholder,'X-U')]", info_post[1])

    func.do_send(driver, "// input[contains( @ placeholder, 'id ')]", info_post[2])

    func.do_click(driver, "//button[contains(@class,'btn e')]")

    func.clear_area(driver,"//input[contains(@placeholder,'X-P')]")

    func.clear_area(driver, "//input[contains(@placeholder,'X-U')]")

    func.clear_area(driver, "// input[contains( @ placeholder, 'id ')]")

f = open('conf/save_post.txt', 'w')
f.close()

driver.close()
driver.quit()
