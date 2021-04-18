#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: logger
@time: 2021/4/17 11:10 上午
@desc:
"""
import logging
import logging.handlers
from page_object.common.util.base_method import BaseMethod


def log_init():
    # 设置格式
    log_format_str = '[%(asctime)s] %(filename)s:%(lineno)d:%(funcName)s: %(message)s'
    format = logging.Formatter(log_format_str)
    # 根据log标识获取log
    root = logging.getLogger("easy_ui_test_log")
    # 加入文件句柄
    dir_path = BaseMethod().make_dir("log")
    h = logging.handlers.RotatingFileHandler(filename=dir_path+"ui_test_info.log", encoding='utf-8', maxBytes=1024 * 1024, backupCount=3)
    h.setFormatter(format)
    # 加入输出流句柄, 日志输出到console
    console = logging.StreamHandler()
    console.setFormatter(format)
    root.addHandler(h)
    root.addHandler(console)
    root.setLevel(logging.INFO)

log_init()
log = logging.getLogger("easy_ui_test_log")


if __name__ == '__main__':
    log.info("start")
