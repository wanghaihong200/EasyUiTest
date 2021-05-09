#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: test_sample_app
@time: 2021/5/8 10:45 下午
@desc:
"""
import time

from page_object.common.base_page import BasePage
from page_object.page.sample_app.main_page import MainPage


class TestSampleApp():
    def setup_class(self):
        self.app = BasePage(appPackage="com.appsflyer.androidsampleapp", appActivity=".MainActivity")

    def teardown_class(self):
        self.app.stop()

    def test_main(self):
        goto_main = MainPage(self.app)
        time.sleep(3)
