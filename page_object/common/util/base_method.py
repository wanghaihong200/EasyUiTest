#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: base_method
@time: 2021/4/17 9:00 下午
@desc:
"""
import datetime
import random
import os
from page_object.common import BasePath


class BaseMethod:
    def get_udid(self):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        udid = now + "__" + str(random.randint(0, 1000))
        return udid

    def get_date(self):
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        return now

    def make_dir(self, dir):
        dir_path = BasePath + dir + "/" + self.get_date() + "/"
        if not os.path.exists(dir_path):
            # 如果目录不存在，则创建目录
            os.makedirs(dir_path)
        return dir_path
