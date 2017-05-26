# -*- coding:utf-8 -*-
# 测试登陆流程

from time import sleep
from config import Config
from screen import screen
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class LoginTest(Config):
    def test_login(self):
        driver = self.driver
        driver.get(self.base_url+'/tmpl/member/login.html')
        sleep(Config.STIME)
        username = [15000000006, 13717648820]
        pwd = [111112, 111111]

        for i in range(len(username)):
            driver.get(self.base_url+'/tmpl/member/login.html')
            user_textfield = driver.find_element_by_id('username')
            pwd_textfield = driver.find_element_by_id('userpwd')
            login_btn = driver.find_element_by_id('loginbtn')
            for j in range(len(pwd)):
                user_textfield.send_keys(username[i])
                sleep(Config.STIME)
                pwd_textfield.send_keys(pwd[j])
                sleep(Config.STIME)
                login_btn.click()
                sleep(Config.STIME)
                current_url = driver.current_url
                if current_url == self.base_url+'/tmpl/member/member.html':
                    print 'login seccessed'
                    sleep(Config.STIME)
                    # s = driver.get_cookies()
                    print s
                    sleep(Config.STIME+10)
                else:
                    screen(driver, 'login_err')
                    sleep(Config.STIME)
                    print 'login failed'
                    user_textfield.clear()
                    pwd_textfield.clear()
                    sleep(Config.STIME)

    # 退出登录
    def test_log_out(self):
        driver = self.driver
        driver.maximize_window()
        self.login()
        driver.get(self.base_url+'/tmpl/member/member.html')
        sleep(Config.STIME)
        # 页面向上滑动
        driver.execute_script("window.scrollBy(0,200)","")
        sleep(Config.STIME)
        # 点击用户设置按钮
        driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/dl[6]/dt/a').click()
        # #我要还款
        # driver.find_element_by_xpath('//*[@id="js-repay"]/dt/a').click()
        sleep(Config.STIME)
        driver.find_element_by_id('logoutbtn').click()
        sleep(Config.STIME)
        self.assertEqual(self.base_url+'/', driver.current_url)


if __name__ == "__main__":
    unittest.main()









