# -*- coding: utf-8 -*-
from selenium import selenium
import unittest, time, re

class sele1(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "https://www.baidu.com/")
        self.selenium.start()
    
    def test_sele1(self):
        sel = self.selenium
        sel.open("/")
        sel.click("//form[@id='form']/span")
        sel.click("id=kw")
        sel.click("id=kw")
        sel.click("id=kw")
        sel.type("id=kw", "selenium1")
        sel.click("id=su")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
