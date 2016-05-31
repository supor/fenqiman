# -*- coding:utf-8 -*-
# 整体配置

from selenium import webdriver
from time import sleep
import unittest


class Config(unittest.TestCase):

    STIME = 1

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/supor/Downloads/chromedriver')
        self.base_url = "http://test.fenqiman.com/wap"
        self.driver.set_window_size(1000, 800)

    def tearDown(self):
        self.driver.quit()

    def login(self):

        self.driver.get(self.base_url+'/tmpl/member/login.html')
        sleep(Config.STIME)
        username = 13717648820
        pwd = 111111
        self.driver.find_element_by_id('username').send_keys(username)
        sleep(Config.STIME)
        self.driver.find_element_by_id('userpwd').send_keys(pwd)
        sleep(Config.STIME)
        self.driver.find_element_by_id('loginbtn').click()
        sleep(Config.STIME)
