#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: test_wework
@time: 2021/4/16 10:00 上午
@desc:
"""
import os

from page_object.common.base_page import BasePage
from page_object.common.util.base_method import BaseMethod
from page_object.page.main_page import MainPage
import pytest


class TestWeWork2:
    def setup_class(self):
        self.app = BasePage()

    def teardown_class(self):
        self.app.stop()

    def test_contact(self, record_vedio):
        goto_main = MainPage(self.app)  # 跳转首页
        goto_address = goto_main.goto_address()  # 跳转通讯录页面
        add_member = goto_address.add_member()  # 跳转添加成员主菜单页面
        add_member_manual = add_member.add_member_manual()  # 手动添加成员，跳转到添加成员页面
        add_contact = add_member_manual.add_contact()  # 添加成员


if __name__ == '__main__':
    report_path = BaseMethod().make_dir("report")
    pytest.main(['--alluredir', report_path+"result"])  # 执行测试，生成allure测试结果数据
    # os.system(f'allure generate {report_path}result -o {report_path} --clean')  # 通过测试结果数据生成html报告
    print('结束')
