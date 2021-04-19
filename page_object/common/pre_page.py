#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: pre_page
@time: 2021/4/19 10:04 下午
@desc:
"""

from page_object.common.base_page import BasePage


class PrePage:
    def __init__(self, basepage: BasePage):
        self.basepage = basepage
