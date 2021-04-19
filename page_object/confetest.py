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

import pytest

from page_object.common.util.base_method import BaseMethod
import subprocess


@pytest.fixture(scope='function', autouse=False)
def record_vedio():
    screen_shot_path = BaseMethod().make_dir("screen_shot_picture")+"video/"+BaseMethod().get_udid() + ".mp4"
    cmd = f"scrcpy --record {screen_shot_path}"
    print(cmd)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(p)
    yield
    os.kill(p.pid, signal.CTRL_C_EVENT)
