# -*- coding:utf-8 -*-
# 测试订单分类

from config import Config
from time import sleep
import unittest
from screen import screen


class OrderCategory(Config):

    # 订单分类
    def test_order_category(self):
        self.login()
        driver = self.driver
        driver.get(self.base_url+'/tmpl/member/member.html')
        sleep(Config.STIME)

        # 查看全部订单
        driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/dl[1]/dt/a/h5').click()
        self.assertEqual(self.base_url+'/tmpl/member/order_list.html', driver.current_url)
        sleep(Config.STIME)
        # 全部订单
        all_orders = driver.find_element_by_xpath('//*[@id="filtrate_ul"]/li[1]/a')
        # 商品订单
        goods_order = driver.find_element_by_xpath('//*[@id="header"]/div[1]/span/a[1]')
        # 现金订单
        cash_order = driver.find_element_by_xpath('//*[@id="header"]/div[1]/span/a[2]')
        # 待付款
        state_new = driver.find_element_by_xpath('//*[@id="filtrate_ul"]/li[2]/a')
        # 待收货
        state_send = driver.find_element_by_xpath('//*[@id="filtrate_ul"]/li[3]/a')
        # 待评价
        state_comment = driver.find_element_by_xpath('//*[@id="filtrate_ul"]/li[4]/a')
        # 订单分类
        oder_category = [all_orders, state_new, state_send, state_comment, cash_order, goods_order]
        for i in range(len(oder_category)):
            if oder_category[i] == goods_order:
                goods_order = driver.find_element_by_xpath('//*[@id="header"]/div[1]/span/a[1]')
                goods_order.click()
            else:
                oder_category[i].click()
                sleep(Config.STIME)
        sleep(5)

    # 订单分类入口
    def test_order_category_entry(self):
        self.login()
        driver = self.driver
        driver.get(self.base_url+'/tmpl/member/member.html')
        sleep(Config.STIME+5)

        # # 待付款入口
        # state_new = driver.find_element_by_xpath('//*[@id="order_ul"]/li[1]/a')
        # # 待收货
        # state_send = driver.find_element_by_xpath('//*[@id="order_ul"]/li[2]/a')
        # # 待评价
        # state_comment = driver.find_element_by_xpath('//*[@id="order_ul"]/li[3]/a')
        # # 退款退货
        # refund = driver.find_element_by_xpath('//*[@id="order_ul"]/li[4]/a')
        # category_entry = [state_new, state_send, state_comment, refund]
        # category_name = ['state_new', 'state_send', 'state_comment', 'refund']
        # for i in range(len(category_entry)):
        #         s = category_entry[i]
        #         s.click()
        #         self.assertEqual(self.base_url+'/tmpl/member/order_list.html?data-state='+str(category_name[i]), driver.current_url)
        #         sleep(Config.STIME)
        #         driver.get(self.base_url+'/tmpl/member/member.html')
        #         sleep(Config.STIME+5)

        # 分类页面的url列表
        category_url = ['state_new', 'state_send', 'state_noeval']
        # 循环遍历定位订单分类：待付款、待收货、待评价、退款退货
        for i in range(1, 5):
            # 到付款、待收货、待评价
            if i < 4:
                driver.find_element_by_xpath('//*[@id="order_ul"]/li['+str(i)+']/a').click()
                sleep(Config.STIME)
                self.assertEqual(self.base_url+'/tmpl/member/order_list.html?data-state='+category_url[i-1], driver.current_url)
                driver.get(self.base_url+'/tmpl/member/member.html')
                sleep(Config.STIME+5)
            # 退款退货
            else:
                driver.find_element_by_xpath('//*[@id="order_ul"]/li['+str(i)+']/a').click()
                sleep(Config.STIME)
                self.assertEqual(self.base_url+'/tmpl/member/member_refund.html', driver.current_url)

    # 测试待付款详情
    def test_state_new(self):
        self.login()
        driver = self.driver

        # 首页
        driver.get(self.base_url+'/')
        sleep(Config.STIME)

    # 全额购买商品，不支付
        # 点击商品
        driver.find_element_by_xpath('//*[@id="main-container2"]/div[4]/ul/li[4]/a/div/img').click()
        sleep(Config.STIME)

        # 第一次点击立即购买按钮
        # driver.find_element_by_xpath('//*[@id="product_detail_html"]/div[2]/div[9]/div/a').click() #线上环境
        driver.find_element_by_xpath('//*[@id="product_detail_html"]/div[2]/div[10]/div/a').click()#测试环境
        sleep(2)

        # 选择全额支付
        driver.find_element_by_xpath('//*[@id="product_detail_spec_html"]/div[2]/div[4]/div[2]/dl/dt/div[3]/em').click()
        sleep(Config.STIME)

        # 第二次点击立即购买按钮
        driver.find_element_by_id('buy-now').click()
        # self.assertEqual(self.bwase_url+'/tmpl/order/buy_step1.html?goods_id=100134&buynum=1&credit_id=0', driver.current_url) #线上环境
        sleep(Config.STIME)

        # 提交订单
        driver.find_element_by_id('ToBuyStep2').click()
        sleep(Config.STIME)

        # 到待付款订单列表页面
        driver.get(self.base_url+'/tmpl/member/order_list.html?data-state=state_new')
        sleep(Config.STIME)

        # 商品订单状态
        state_no_finish = driver.find_element_by_xpath('//*[@id="order-list"]/li/div/div[1]/span/span')
        self.assertEqual(state_no_finish.text, u'待付款')

        # 商品价格
        goods_price = driver.find_element_by_xpath('//*[@id="order-list"]/li/div/div[2]/div/a/div[3]/span[1]/em')
        # self.assertEqual(goods_price.text, '2549.00')  # 线上环境
        self.assertEqual(goods_price.text, '10.00')
        # 实付金额
        total_pay = driver.find_element_by_xpath('//*[@id="order-list"]/li/div/div[3]/div[1]/span[2]/em')
        self.assertEqual(total_pay.text, '10.00')
        sleep(Config.STIME)
        # 订单支付按钮
        pay_btn = driver.find_element_by_xpath('//*[@id="order-list"]/li/a')
        self.assertEqual(pay_btn.text, u'订单支付（￥10.00）')
        # 支付按钮功能验证
        pay_btn.click()
        sleep(Config.STIME)
        pay_price = driver.find_element_by_xpath('//*[@id="pay_app"]/div[1]/span[2]/span')
        self.assertEqual(pay_price.text, '10.00')
        # 查看订单详情
        driver.get(self.base_url+'/tmpl/member/order_list.html?data-state=state_new')
        sleep(Config.STIME)
        driver.find_element_by_xpath('//*[@id="order-list"]/li/div/div[2]/div/a').click()
        sleep(Config.STIME)
        # self.assertEqual(self.base_url+'/tmpl/member/order_detail.html?order_id=150289', driver.current_url)
    # 订单详情页
        #订单状态
        order_status = driver.find_element_by_xpath('//*[@id="order-info-container"]/div[1]/div[1]')
        self.assertEqual(order_status.text, u'待付款')
        sleep(Config.STIME)
        # 支付方式
        payment_method = driver.find_element_by_xpath('//*[@id="order-info-container"]/div[3]/div')
        self.assertEqual(payment_method.text, u'全额支付')

        # 实付金额
        total_payment = driver.find_element_by_xpath('//*[@id="order-info-container"]/div[4]/div[2]/div[2]/dl[2]/dd/em')
        self.assertEqual(total_payment.text, '10.00')
        sleep(Config.STIME)

        # 验证取消按钮
        driver.find_element_by_xpath('//*[@id="order-info-container"]/div[6]/a').click()
        sleep(Config.STIME)
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/a[2]').click()
        sleep(Config.STIME)
        order_cancel_states = driver.find_element_by_xpath('//*[@id="order-info-container"]/div[1]/div[1]')
        self.assertEqual(order_cancel_states.text, u'已取消')


if __name__ == "__main":
    unittest.main()
