#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: main_page
@time: 2021/5/8 10:52 下午
@desc:
"""
from appium.webdriver.common.mobileby import MobileBy

from page_object.common.pre_page import PrePage



class MainPage(PrePage):
    """
    首页
    """

    el_address = (MobileBy.XPATH, "//*[@text='RECORD EVENT']")

    def goto_address(self):
        """
        跳转到sample_app主页面
        :return:
        """
        self.basepage.find_element(*self.el_address)
        print(self.basepage.driver.page_source)

