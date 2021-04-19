#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: confetest
@time: 2021/4/18 10:44 下午
@desc:
"""
import os
import signal
import random

import pytest

from page_object.common.util.base_method import BaseMethod
import subprocess
import datetime


@pytest.fixture(scope='function', autouse=False)
def record_vedio():
    name = datetime.datetime.now().strftime("%H:%M:%S") + "__" + str(random.randint(0, 1000)) + ".mp4"
    screen_shot_path = BaseMethod().make_dir("screen_shot_picture")+name
    print(screen_shot_path)
    cmd = f'scrcpy --record {screen_shot_path}'
    print(cmd)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(p)
    yield
    print('Press Ctrl+C')
    p.send_signal(signal.SIGINT)
    os.kill(p.pid, signal.SIGINT)


