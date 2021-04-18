#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: member_invite_menu_page
@time: 2021/4/15 7:16 下午
@desc:
"""
from appium.webdriver.common.mobileby import MobileBy

from page_object.common.base_page import BasePage
from page_object.page.contact_add_page import ContactAddPage


class MemberInviteMenuPage(BasePage):
    '''
    成员邀请主菜单页
    '''
    def __init__(self, driver):
        super(MemberInviteMenuPage, self).__init__(driver)
        self.el_add_member_manual = (MobileBy.XPATH, "//*[@text='手动输入添加']")

    def add_member_manual(self) -> ContactAddPage:
        self.find_element_and_click(*self.el_add_member_manual)
        return ContactAddPage(self.driver)
