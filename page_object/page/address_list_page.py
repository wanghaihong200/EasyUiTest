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

from page_object.common.pre_page import PrePage
from page_object.page.member_invite_menu_page import MemberInviteMenuPage


class AddressListPage(PrePage):
    """
    通讯录页面
    """

    el_add_member = (MobileBy.XPATH, "//*[@text='添加成员']")
    el_add_member_text = "添加成员"

    def add_member(self) -> MemberInviteMenuPage:
        self.basepage.find_by_scroll(text=self.el_add_member_text).click()
        # self.basepage.find_by_swipe_above(*self.el_add_member).click()
        return MemberInviteMenuPage(self.basepage)
