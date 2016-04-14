#coding=utf-8

import time,os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#os.system("java -jar selenium-server-standalone-2.44.0.jar")

#指定运行主机与端口号
driver=webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME)
    
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium server")
sleep(0.5)
driver.find_element_by_id("su").click()
sleep(0.5)

driver.close()

driver.quit()
