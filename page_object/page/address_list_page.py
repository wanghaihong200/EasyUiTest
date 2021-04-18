#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: address_list_page
@time: 2021/4/15 7:15 下午
@desc:
"""
import time

from appium.webdriver.common.mobileby import MobileBy

from page_object.common.base_page import BasePage
from page_object.page.member_invite_menu_page import MemberInviteMenuPage


class AddressListPage(BasePage):
    """
    通讯录页面
    """
    def __init__(self, driver):
        super(AddressListPage, self).__init__(driver)
        self.el_add_member = (MobileBy.XPATH, "//*[@text='添加成员']")
        self.el_add_member_text = "添加成员"

    def add_member(self) -> MemberInviteMenuPage:
        self.find_by_scroll(text=self.el_add_member_text).click()
        # self.find_by_swipe_above(*self.el_add_member).click()
        return MemberInviteMenuPage(self.driver)
