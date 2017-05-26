# -*- coding:utf-8 -*-
# 测试购买流程

from config import Config
from time import sleep
import unittest
from screen import screen


class BuyGoods(Config):

    # def setUp(self):
    #     Config.setUp(self)
    #     self.login()

    def test_full_pay(self):
        self.login()
        driver = self.driver
        # driver.add_cookie({'name': 'username', 'value': '13717648820'})
        # driver.add_cookie({'name': 'userpwd', 'value': '111111'})
        driver.get(self.base_url+'/')
        sleep(Config.STIME+3)

    # 全额购买商品

        # 点击商品
        driver.find_element_by_xpath('//*[@id="main-container2"]/div[4]/ul/li[4]/a/div/img').click()
        sleep(Config.STIME)

        # 控制滚动条，暂时没有成功，待寻找原因
        # js="var s=document.documentElement.scrollTop=100000"
        # sleep(2)
        # driver.execute_script(js)
        # sleep(3)
        # driver.find_element_by_xpath('//*[@id="product_detail_html"]/div[2]/div[5]/div[2]/dl/dt/div[1]').click()
        # sleep(1)

        # 第一次点击立即购买按钮
        # driver.find_element_by_xpath('//*[@id="product_detail_html"]/div[2]/div[9]/div/a').click() #线上环境
        driver.find_element_by_xpath('//*[@id="product_detail_html"]/div[2]/div[10]/div/a').click()#测试环境
        sleep(2)

        # 选择全额支付
        driver.find_element_by_xpath('//*[@id="product_detail_spec_html"]/div[2]/div[4]/div[2]/dl/dt/div[3]/em').click()
        sleep(Config.STIME)

        # 第二次点击立即购买按钮
        driver.find_element_by_id('buy-now').click()
        sleep(Config.STIME+3)
        # self.assertEqual(self.base_url+'/tmpl/order/buy_step1.html?goods_id=100134&buynum=1&credit_id=0', driver.current_url) #线上环境
        self.assertEqual(self.base_url+'/tmpl/order/buy_step1.html?goods_id=100115&buynum=1&credit_id=0', driver.current_url) #测试环境
        sleep(Config.STIME+2)

        # 提交订单
        driver.find_element_by_id('ToBuyStep2').click()
        sleep(Config.STIME)

    # 收银台支付页面
        # 查看支付页面的金额是否显示正确
        # self.assertEqual(driver.find_element_by_xpath('//*[@id="pay_app"]/div[1]/span[2]/span').text, '2549.00') #线上环境
        self.assertEqual(driver.find_element_by_xpath('//*[@id="pay_app"]/div[1]/span[2]/span').text, '10.00') #测试环境

        # 选择支付方式
        driver.find_element_by_xpath('//*[@id="pay_app"]/ul[2]/li[1]/a/input').click()
        sleep(Config.STIME)

        # 点击立即支付
        driver.find_element_by_xpath('//*[@id="pay_app"]/a').click()
        sleep(Config.STIME+20)
        # 获取验证码页面
        driver.find_element_by_xpath('//*[@id="pay_app"]/div[4]/a').click()
        sleep(Config.STIME+5)
        driver.find_element_by_xpath('//*[@id="pay_app"]/div[5]/a').click()
        sleep(Config.STIME)
        self.assertEqual(self.base_url+'/tmpl/member/order_list.html?backHome=1', driver.current_url)
        sleep(Config.STIME)

    # 分期支付
    def test_instalment(self):
        self.login()
        driver = self.driver
        driver.get(self.base_url+'/')
        sleep(Config.STIME)

    # 全额购买商品

        # 点击商品
        driver.find_element_by_xpath('//*[@id="main-container2"]/div[4]/ul/li[4]/a/div/img').click()
        sleep(Config.STIME)

        # 第一次点击立即购买按钮
        # driver.find_element_by_xpath('//*[@id="product_detail_html"]/div[2]/div[9]/div/a').click() #线上环境
        driver.find_element_by_xpath('//*[@id="product_detail_html"]/div[2]/div[10]/div/a').click()#测试环境
        sleep(2)

        # 选择分期支付
        driver.find_element_by_xpath('//*[@id="product_detail_spec_html"]/div[2]/div[4]/div[2]/dl/dt/div[2]').click()
        sleep(Config.STIME)

        # 第二次点击立即购买按钮
        driver.find_element_by_id('buy-now').click()
        sleep(Config.STIME)
        self.assertEqual(self.base_url+'/tmpl/order/buy_step1.html?goods_id=100115&buynum=1&credit_id=2', driver.current_url) #测试环境

        # 提交订单
        credit_able = driver.find_element_by_id('credit_able').text
        goods_price = driver.find_element_by_xpath('//*[@id="deposit"]/div/ul/li/div[2]/span/em').text
        # 额度足够
        if credit_able >= goods_price:
            # 点击提交订单按钮
            driver.find_element_by_id('ToBuyStep2').click()
            sleep(Config.STIME+3)
            # 跳转到确认支付页面
            self.assertEqual('http://fqlm2test.i.hrbbwx.com/fenqipay/index#!/order', driver.current_url)
            # 点击确认按钮
            driver.find_element_by_xpath('//*[@id="app"]/div[1]/a[1]').click()
            sleep(Config.STIME+2)
            # 跳转到输入支付密码页面
            self.assertEqual('http://fqlm2test.i.hrbbwx.com/fenqipay/index#!/defrayal', driver.current_url)
            # 输入支付密码
            driver.find_element_by_name('pwd').send_keys(111111)
            sleep(Config.STIME)
            driver.find_element_by_xpath('//*[@id="app"]/div[1]/a[1]').click()
            sleep(Config.STIME+3)
            driver.find_element_by_xpath('//*[@id="modal-btn-right"]').click()
            sleep(Config.STIME)
            self.assertEqual('http://test.fenqiman.com/wap/tmpl/member/order_list.html?backHome=1', driver.current_url)
        else:
            driver.find_element_by_id('ToBuyStep2').click()
            screen(driver, 'limit')

if __name__ == "__main__":
    unittest.main()

