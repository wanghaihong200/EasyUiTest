#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: contact_add_page
@time: 2021/4/15 7:15 下午
@desc:
"""
import time

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from page_object.common.pre_page import PrePage


class ContactAddPage(PrePage):
    """
    联系人添加详情页
    """

    # el_add_detail = (MobileBy.XPATH, "//*[@text='完整输入']")  # 加入到了黑名单中，如果是快捷输入页面，则自动点击 完整输入按钮，切换到 完整输入页面
    el_add_fast = (MobileBy.XPATH, "//*[@text='快速输入']")
    el_name_input = (MobileBy.XPATH, "//*[contains(@text, '姓名')]/..//*[@text='必填']")
    el_sex_input = (MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[@text='男']")
    el_sex_select = (MobileBy.XPATH, "//*[@text='女']")
    el_phone_input = (MobileBy.XPATH, "//*[@text='手机号']")
    el_save = (MobileBy.XPATH, "//*[@text='保存']")
    el_notice = (MobileBy.XPATH, "//*[@text='保存后自动发送邀请通知']")
    el_notice_text = "保存后自动发送邀请通知"

    def add_contact(self, name="林志玲", gender="女", phone="13391387822"):
        self.el_sex_select = (MobileBy.XPATH, f"//*[@text='{gender}']")
        self.basepage.find_element(*self.el_add_fast)  # 若处于完整输入页面，则页面上可查找到 "快速输入"
        el_name_input = self.basepage.find_element(*self.el_name_input)
        el_name_input.send_keys(name)
        self.basepage.find_element_and_click(*self.el_sex_input)  # 点击性别单选框
        self.basepage.find_element_and_click(*self.el_sex_select)  # 选择性别 "女"

        el_phone_input = self.basepage.find_element(*self.el_phone_input)
        el_phone_input.send_keys(phone)
        # el_notice = self.basepage.find_by_scroll(text=self.el_notice_text)
        el_notice = self.basepage.find_by_swipe_above(*self.el_notice)
        el_notice.click()
        self.basepage.find_element_and_click(*self.el_save)

        # 断言
        # WebDriverWait(self.basepage.driver, 10).until(lambda x: "添加成员" in self.basepage.driver.page_source)
        # assert '添加成员' in self.basepage.driver.page_source
        time.sleep(3)
