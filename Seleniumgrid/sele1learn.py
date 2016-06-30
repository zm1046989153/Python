from selenium import selenium
import unittest,time,re


class  serc(unittest.TestCase):
    def setUp(self):
        self.verificationErrors=[]
        self.selenium=selenium("localhost",4444,"*firefox D:\Mozilla Firefox\\firefox.exe","http://www.baidu.com/")
        self.selenium.start()
        

    def test_serc(self):
        sel=self.selenium
        sel.open('/')
        sel.type("id=kw","selenium grid")
        sel.click("id=su")
        sel.wait_for_page_to_load("3000")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([],self.verificationErrors)

if __name__ =="__main__":
    unittest.main()
