#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: __init__.py
@time: 2021/4/15 5:31 下午
@desc:
"""
import os

current_path = os.path.dirname(__file__)
BasePath = "/".join(current_path.split("/")[:-2]) + "/"
print(current_path, BasePath)

