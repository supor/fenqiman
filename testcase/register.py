# -*- coding:utf-8 -*-
# 测试注册流程


from config import Config
from time import sleep
import unittest
from screen import screen


class RegisterTest(Config):
    def test_register_user_exist(self):
        driver = self.driver
        driver.get(self.base_url+'/tmpl/member/register.html')
        sleep(1)
        # 分别是手机号已注册，手机号格式正确且未注册
        username = [13717648820, 15000000005]
        sleep(2)
        # 遍历手机号
        for i in range(len(username)):
            user_mobile = driver.find_element_by_id('usermobile')
            user_mobile.send_keys(username[i])
            sleep(1)
            checkbox = driver.find_element_by_id('checkbox')
            if checkbox.is_selected():
                print 'checkbox is enabled'
            else:
                checkbox.click()

            register_mobile_btn = driver.find_element_by_id('refister_mobile_btn')
            sleep(2)
            register_mobile_btn.click()
            screen(driver, 'register_mobile')
            sleep(1)
            # 设置短信验证码固定为：111111
            driver.find_element_by_id('mobilecode').send_keys(111111)
            sleep(3)
            driver.find_element_by_id('register_mobile_password').click()
            sleep(1)
            screen(driver, 'security_code')
            url1 = driver.current_url
            sleep(1)
            if url1 == self.base_url+'/tmpl/member/register_mobile_password.html?mobile='+str(username[i])+'&captcha=111111&invitation=undefined':
                # 获取完验证码后，设置密码
                driver.find_element_by_id('password').send_keys('111111')
                sleep(2)
                # 点击注册完成
                driver.find_element_by_id('completebtn').click()
                sleep(2)
                # 跳转至首页
                self.assertEqual('http://test.fenqiman.com/wap/index.html', driver.current_url)
                sleep(2)
            else:
                driver.find_element_by_xpath('//*[@id="header"]/div/div[1]/a/i').click()
                sleep(2)
                user_mobile2 = driver.find_element_by_id('usermobile')
                user_mobile2.clear()
                sleep(3)
                # driver.clear()
                # invitation_box.clear()
                print 'failure'


if __name__ == "__main__":
    unittest.main()
