# -*- coding:utf-8 -*-
# 测试信用钱包提现功能

from time import sleep
from config import Config
from screen import screen
import unittest


class WithdrawTest(Config):
    def test_withdraw(self):
        self.login()
        driver = self.driver
        driver.get(self.base_url+'/')
        sleep(Config.STIME)
        # 首页点击信用钱包按钮
        driver.find_element_by_xpath('/html/body/div[2]/ul/li[2]/a').click()

        # 信用钱包页面
        self.assertEqual(self.base_url+'/tmpl/denglu_money.html', driver.current_url)
        sleep(Config.STIME)

        # 验证可用额度
        # 信用钱包页面的可用额度
        credit_able2 = driver.find_element_by_xpath('//*[@id="credit_title"]/a[1]').text
        driver.find_element_by_id('dy-available-credit').click()
        sleep(Config.STIME+4)
        # 分期联盟首页的可用额度
        credit_able3 = driver.find_element_by_xpath('//*[@id="page-finance"]/div[1]/div[2]/p[2]').text
        self.assertEqual(credit_able2+'.00', credit_able3)

        # 返回信用钱包页面
        driver.get(self.base_url+'/tmpl/denglu_money.html')
        sleep(Config.STIME)

        # 选择分期期数
        driver.find_element_by_xpath('//*[@id="fqqs_money"]/li[1]').click()

        # 选择提现金额
        # wd_money1 = driver.find_element_by_xpath('//*[@class="tixian_jine_list js-container-use2"]/li[1]')
        # wd_money2 = driver.find_element_by_xpath('//*[@class="tixian_jine_list js-container-use2"]/li[2]')
        # wd_money3 = driver.find_element_by_xpath('//*[@class="tixian_jine_list js-container-use2"]/li[3]')
        # wd_money4 = driver.find_element_by_xpath('//*[@class="tixian_jine_list js-container-use2"]/li[4]')
        # # wd_money = [wd_money1, wd_money2, wd_money3, wd_money4]
        # 遍历提现金额
        for i in range(1, 5):
            # 选择提现用途
            driver.find_element_by_xpath('//*[@class="input_yt"]/ul/li[1]').click()
            # 可用额度
            wd_money = driver.find_element_by_xpath('//*[@class="tixian_jine_list js-container-use2"]/li['+str(i)+']')
            wd_money.click()
            wd_money_text = wd_money.text
            # 可用额度足够
            if float(wd_money_text) <= float(credit_able2):

                # 点击立即提现按钮
                driver.find_element_by_class_name('ljtx').click()
                sleep(Config.STIME)
                # 确认支付页面的可用额度
                credit_able4 = driver.find_element_by_xpath('//*[@id="app"]/div[1]/ul[1]/li[1]/span').text
                wd_money2 = driver.find_element_by_xpath('//*[@id="app"]/div[1]/ul[1]/li[2]/span').text
                # 验证可用额度正确性
                self.assertEqual(u'￥'+credit_able2+'.00', credit_able4)
                # 验证申请金额正确性
                self.assertEqual(u'￥'+wd_money_text+'.00', wd_money2)
                sleep(Config.STIME)

                # 分期付款协议
                checkbox = driver.find_element_by_class_name('attention_fang')
                if checkbox.is_selected():
                    print 'checkbox is enabled'
                else:
                    checkbox.click()
                sleep(Config.STIME)

                # 点击确认按钮
                driver.find_element_by_xpath('//*[@id="app"]/div[1]/a[1]').click()
                sleep(Config.STIME)

            # 进入支付密码页面
                # 输入错误的支付密码
                pay_pwd = driver.find_element_by_name('pwd')
                pay_pwd.send_keys(222222)
                sleep(Config.STIME)
                # 点击确认支付按钮
                pay_btn = driver.find_element_by_xpath('//*[@id="app"]/div[1]/a[1]')
                pay_btn.click()
                sleep(Config.STIME)
                # 密码错误弹框提示，点击重试
                driver.find_element_by_id('modal-btn-left').click()
                sleep(Config.STIME)
                # 清空密码输入框
                pay_pwd.clear()
                sleep(Config.STIME)
                # 再次输入正确的支付密码,点击确定支付按钮
                pay_pwd.send_keys(111111)
                sleep(Config.STIME)
                pay_btn.click()
                sleep(Config.STIME)
                driver.find_element_by_id('modal-btn-right').click()
                sleep(Config.STIME)
                self.assertEqual(self.base_url+'/tmpl/order_cash.html?backHome=1', driver.current_url)

                # 返回至信用钱包页面
                driver.get(self.base_url+'/tmpl/denglu_money.html')
                sleep(Config.STIME)
                break
            # 额度不足
            else:
                # 点击立即提现按钮
                driver.find_element_by_class_name('ljtx').click()
                sleep(Config.STIME)
                # 弹框提示额度不足去还款，点击去还款
                # driver.find_element_by_class_name('s-dialog-btn-cancel').click() # 点击取消按钮
                driver.find_element_by_class_name('s-dialog-btn-ok').click()
                sleep(Config.STIME)
                # 页面跳转到我的账单页面
                self.assertEqual('http://fqlm2test.i.hrbbwx.com/fenqipay/index#!/repay-newlist', driver.current_url)
                sleep(Config.STIME)
                # 点击账单查看账单详情
                driver.find_element_by_xpath('//*[@id="app"]/div[4]/div[2]/div[2]/ul[1]/li[2]').click()
                sleep(Config.STIME)
                # 验证账单详情页面的分期总额显示
                instalments_total = driver.find_element_by_xpath('//*[@id="app"]/ul/li[1]/div[1]')
                self.assertEqual(instalments_total, wd_money_text)
                sleep(Config.STIME)

            # 还款
                # 全选
                check_all_btn = driver.find_element_by_xpath('//*[@id="app"]/div[8]/div/img')
                # 如果全选选中了，则点击一键还清按钮
                if check_all_btn.is_selected():
                    driver.find_element_by_class_name('tap-normal-state right r-blue').click()
                    sleep(Config.STIME)
                # 如果全选没有选，则选择全选
                else:
                    check_all_btn.click()
                sleep(Config.STIME)
                # 点击一键还清
                driver.find_element_by_class_name('tap-normal-state right r-blue').click()
                sleep(Config.STIME)
                # 点击快捷支付方式
                driver.find_element_by_xpath('//*[@id="pay_app"]/ul[1]/li/a/input').click()
                sleep(Config.STIME)
                # 点击立即支付按钮
                driver.find_element_by_class_name('btn pay_btn blue').click()
                sleep(Config.STIME+10)
                # 输入验证码，点击下一步按钮
                driver.find_element_by_class_name('btn save gray').click()
                sleep(Config.STIME)
                # 点击支付成功页面的完成按钮，跳转至我的账单页面
                driver.find_element_by_class_name('btn blue').click()
                sleep(Config.STIME+5)

if __name__ == "__main__":
    unittest.main()
