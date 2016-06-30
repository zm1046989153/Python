# -*- coding: cp936 -*-

from  selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

'''

#配置测试主机及使用的浏览器
def getconfig():
    d={'http://127.0.0.1:4444/wd/hub':'chrome',
       'http://192.168.1.10:5555/wd/hub':'chrome'}
    print "success read computer and browser!!"
    return d

#各个主机和浏览器执行测试
for host,browser in getconfig().items():
    print host
    print browser
    driver=webdriver.Remote(
        command_executor=host,
        desired_capabilities={
            'platform':'ANY',
            'browserName':browser,
            'version':'',
            'javascriptEnabled':True
            })

    
'''   
#浏览器数组
bro_list=['firefox','chrome']

#通过不同浏览器执行脚本
for browser in bro_list:
    print browser
    driver=webdriver.Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
            desired_capabilities={'platform':'ANY',
                                'browserName':browser,
                                  'version':'',
                                  'javascriptEnabled':True
                                  })
                                  


    

    #driver=webdriver.Firefox()

    driver.get("http://www.youdao.com")
    driver.maximize_window()
    driver.find_element_by_name("q").send_keys("hello")
    driver.find_element_by_id("qb").click()

    time.sleep(2)

    driver.close()
    driver.quit()
