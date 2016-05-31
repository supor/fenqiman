# -*- coding:utf-8 -*-
# 截图


import datetime


def screen(driver, basename):
    time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    driver.get_screenshot_as_file('./screenshot/'+basename+time+'.png')