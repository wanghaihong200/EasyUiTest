#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: util
@time: 2021/4/15 6:14 下午
@desc:
"""
import json
import logging

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from page_object.common.util.black_handle import black_wrapper
from page_object.common.constants.key_words_constant import *
from pytest_testconfig import config

from .black import get_black_list

udid = ["192.168.0.152:5555", "FFKDU17A14004245"]


class BasePage:
    def __init__(self, udid=udid[1], appPackage="com.tencent.wework",
                 appActivity=".launch.LaunchSplashActivity"):

        self.black_list = get_black_list()

        self.desire_app = config['desired_caps']
        self.desire_app["udid"] = udid
        self.desire_app["appPackage"] = appPackage
        self.desire_app["appActivity"] = appActivity
        self.driver = webdriver.Remote(config["appium_server_url"], desired_capabilities=self.desire_app)
        self.driver.implicitly_wait(5)


    def restart(self):
        # 重启app
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        # 停止app
        self.driver.quit()

    @black_wrapper
    def find_element(self, by, locator):
        return self.driver.find_element(by, locator)

    @black_wrapper
    def find_elements(self, by, locator):
        return self.driver.find_elements(by, locator)

    @black_wrapper
    def find_element_and_click(self, by, locator):
        self.find_element(by, locator).click()

    @black_wrapper
    def send(self, by, locator, content):
        self.find_element(by, locator).send_keys(content)

    @black_wrapper
    def find_by_scroll(self, text):
        # 安卓原生的滑动定位
        print('new UiScrollable(new UiSelector().'
              'scrollable(true).instance(0)).'
              'scrollIntoView(new UiSelector().'
              f'text("{text}").instance(0));')
        return self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                               'scrollable(true).instance(0)).'
                                                               'scrollIntoView(new UiSelector().'
                                                               f'text("{text}").instance(0));')

    @black_wrapper
    def find_by_scroll_and_click(self, text):
        self.find_by_scroll(text).click()

    def find_by_swipe_above(self, by, locator):
        # 向上滑动定位
        self.driver.implicitly_wait(1)
        elements = self.driver.find_elements(by, locator)
        for i in range(20):
            if len(elements) == 0:
                self.driver.swipe(0, 800, 0, 400)
                elements = self.driver.find_elements(by, locator)
        self.driver.implicitly_wait(5)

        return elements[0]

    def find_by_swipe_lower(self, by, locator):
        # 向下滑动定位
        self.driver.implicitly_wait(1)
        elements = self.driver.find_elements(by, locator)
        for i in range(20):
            if len(elements) == 0:
                self.driver.swipe(0, 0, 0, 400)
                elements = self.driver.find_elements(by, locator)
        self.driver.implicitly_wait(5)

        return elements[0]

    def wait_for(self, by, locator):
        def wait_ele_for(driver: WebDriver):
            eles = driver.find_elements(by, locator)
            return len(eles) > 0

        WebDriverWait(self.driver, 10).until(wait_ele_for)

    def get_toast_text(self):
        # 获取toast的text属性
        result = self.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        logging.info(result)
        return result

    def load(self, json_path):
        # 解析json数据，转化为对应的测试代码， 关键字驱动
        with open(json_path, mode="r") as f:
            data = json.load(f)
        for step in data:
            xpath_expr = step[FIND_ELEMENT]
            action = step[ACTION]
            if action == FIND_ELEMENT_AND_CLICK:
                self.find_element_and_click(MobileBy.XPATH, xpath_expr)
            elif action == SEND_KEYS:
                content = step.get(CONTENT)
                self.send(MobileBy.XPATH, xpath_expr, content)

    def screen_shot(self, picture_path):
        self.driver.save_screenshot(picture_path)
