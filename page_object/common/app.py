#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: app
@time: 2021/4/15 6:02 下午
@desc:
"""
from appium import webdriver
from page_object.common.base_page import BasePage
from page_object.page.main_page import MainPage

udid = ["192.168.0.152:5555", "FFKDU17A14004245"]


class App():
    def __init__(self, udid=udid[1], appPackage="com.tencent.wework",
                 appActivity=".launch.LaunchSplashActivity"):
        # 启动app
        super(App, self).__init__()
        if self.driver is None:
            self.desire_app = {
                "platformName": "Android",
                "platformVersion": '9.0',
                "deviceName": "honor9",
                "udid": udid,
                "automationName": "UiAutomator2",
                "noReset": "True",  # 保留app缓存
                "appPackage": appPackage,
                "appActivity": appActivity
            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=self.desire_app)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()

    def restart(self):
        # 重启app
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        # 停止app
        self.driver.quit()

    def goto_main(self) -> MainPage:
        # 进入首页
        return MainPage(self.driver)


