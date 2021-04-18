#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: test_wework
@time: 2021/4/16 10:00 上午
@desc:
"""
from page_object.common.app import App


class TestWeWork2():
    def setup_class(self):
        self.app = App()

    def teardown_class(self):
        self.app.stop()

    def test_contact(self):
        goto_main = self.app.goto_main()  # 跳转首页
        goto_address = goto_main.goto_address()  # 跳转通讯录页面
        add_member = goto_address.add_member()  # 跳转添加成员主菜单页面
        add_member_manual = add_member.add_member_manual()  # 手动添加成员，跳转到添加成员页面
        add_contact = add_member_manual.add_contact()  # 添加成员
