#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: black
@time: 2021/4/17 5:31 下午
@desc:
"""
from appium.webdriver.common.mobileby import MobileBy


class Black:
    def __init__(self):
        self.el_add_detail = (MobileBy.XPATH, "//*[@text='完整输入']")
        self.el_add_hai = (MobileBy.XPATH, "//*[@text='海之蓝']")


def get_black_list():
    black = vars(Black())
    black_list = []
    print("黑名单: ")
    for k, v in black.items():
        black_list.append(v)
    print(black_list)
    return black_list



if __name__ == '__main__':
    b = Black()
    print(vars(b))
    get_black_list()
