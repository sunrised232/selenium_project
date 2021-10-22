from threading import Thread

def threadings(n_threads):
    from selenium import webdriver
    import time, func
    list_data = func.read_file_comma('conf/config'+str(n_threads)+'.txt')

    url = "http://192.168.3.115:36635/swagger-ui/index.html?urls.primaryName=mobile#/"
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('window-size=1920,1080')
    driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)

    driver.get(url=url)

    func.do_click(driver, "(//h4[@class = 'opblock-tag'])[15]")

    func.do_click(driver, "//span[contains(text(),'POST')]")

    func.do_click(driver, "//button[contains(text(),'T')]")

    func.do_send(driver, "//input[contains(@placeholder,'X-P')]", list_data[4])

    func.do_send(driver, "//input[contains(@placeholder,'X-U')]", list_data[1])

    list_save = []

    for i in range (1,int(list_data[0])):

        func.clear_area(driver, "//textarea[@class = 'body-param__text']")

        string = '{"attachments": [],"pictures": [],"tagCodes" :[],"text": "Автотесты постов\\nПост №'+str(i)+'\\nid = '+list_data[1]+'\\nusername = '+list_data[2]+'\\nname = '+list_data[3]+'\\nphone = '+list_data[4]+'"}'

        func.do_send(driver, "//textarea[@class = 'body-param__text']", string)

        func.do_click(driver, "//button[contains(@class,'btn e')]")

        time.sleep(0.15)
        string_number_post = driver.find_element_by_xpath("//span[@class = 'token-not-formatted']").text

        post_info = list_data[4]+','+ list_data[1]+','+ string_number_post+'\n'

        list_save.append(post_info)

    for i in list_save:
        file = open('conf/save_post.txt', 'a')
        file.write(i)
        file.close()

    time.sleep(1)

    driver.close()
    driver.quit()


threads = [Thread(target=threadings, args=(n_threads,)) for n_threads in (1,2,3)]
for t in threads: t.start()
for t in threads: t.join()
print ('all threads done!')
