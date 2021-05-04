#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: start_appium
@time: 2021/5/4 12:22 下午
@desc:
"""
import time

import subprocess


def start_appium():
    # 先杀掉appium的进程

    subprocess.Popen('taskkill /im node.exe /t /f', shell=True)

    # time.sleep(1)
    #
    # appium_log=os.path.join(APP_HOME,'log')+os.sep+'appium.log'
    #
    # subprocess.Popen('appium -g %s'%appium_log,shell=True)
    #
    # time.sleep(3)

