#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: main_page
@time: 2021/4/15 7:14 下午
@desc:
"""
from appium.webdriver.common.mobileby import MobileBy

from page_object.common.pre_page import PrePage
from page_object.page.address_list_page import AddressListPage
from page_object.common import BasePath


class MainPage(PrePage):
    """
    首页
    """

    el_address = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_address(self) -> AddressListPage:
        """
        跳转到通讯录页面
        :return:
        """
        # self.basepage.find_element_and_click(*self.el_address)
        self.basepage.load(BasePath+"data/main_page.json")
        return AddressListPage(self.basepage)
