# -*- coding:utf-8 -*-
# 集成化

import unittest
from register import RegisterTest
from login import LoginTest
from buy import BuyGoods
from order import OrderCategory
from withdraw import WithdrawTest

if __name__ == "__main__":
    # 加载测试套件
    # 登陆
    suite_login = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    # 注册
    suite_register = unittest.TestLoader().loadTestsFromTestCase(RegisterTest)
    # 购买
    suite_buy = unittest.TestLoader().loadTestsFromTestCase(BuyGoods)
    # 订单分类
    suite_oder = unittest.TestLoader().loadTestsFromTestCase(OrderCategory)
    # 提现
    suite_withdraw = unittest.TestLoader().loadTestsFromTestCase(WithdrawTest)
    # 组织测试用例的实例
    suite = unittest.TestSuite([suite_login, suite_register, suite_buy, suite_oder, suite_withdraw])
    # 运行测试用例
    unittest.TextTestRunner(verbosity=2).run(suite)

