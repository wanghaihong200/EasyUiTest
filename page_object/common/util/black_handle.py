#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: black_handle
@time: 2021/4/17 10:48 上午
@desc:
"""
from page_object.common.util.logger import log
from page_object.common.util.base_method import BaseMethod
import allure


def black_wrapper(fun):
    """
    针对页面点击时，有时会出一些广告弹窗、通知弹窗，将这些弹窗用 黑名单的方式定位，关闭，
    使其不影响自动化测试
    :param fun:
    :return:
    """
    def run(*args, **kwargs):
        base_page = args[0]
        try:
            log.info("start find: \nargs: " +str(args) + " kwargs: "+ str(kwargs))
            return fun(*args, **kwargs)
        except Exception as e:
            dir_path = BaseMethod().make_dir("screen_shot_picture")
            screen_picture_path = dir_path + BaseMethod().get_udid() + ".png"
            base_page.screen_shot(picture_path=screen_picture_path)  # 对错误页面进行截图保存
            with open(screen_picture_path, "rb") as f:
                picture_data = f.read()
            allure.attach(picture_data, attachment_type=allure.attachment_type.PNG)  # 将错误截图传给allure
            # 遍历黑名单中的元素，进行处理
            for black in base_page.black_list:
                eles = base_page.find_elements(*black)
                # 找到黑名单
                if len(eles) > 0:
                    eles[0].click()
                    return fun(*args, **kwargs)
            raise e

    return run


