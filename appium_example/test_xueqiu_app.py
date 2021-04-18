#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: test_first
@time: 2021/4/7 3:15 下午
@desc:
"""
from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import assert_that, close_to


class TestAppium():
    def setup(self):
        self.desire_app = {
            "platformName": "android",
            "platformVersion": '9.0',
            "deviceName": "FFKDU17A14004245",
            "noReset": "True",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias"

        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=self.desire_app)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
        el1.click()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        time.sleep(3)
        el2.send_keys("阿里巴巴")
        el2.send_keys("阿里巴巴")
        el3 = self.driver.find_elements_by_xpath("//*[@text='阿里巴巴' and @resource-id='com.xueqiu.android:id/name']")[0]
        el3.click()

        time.sleep(3)
        current_price = self.driver.find_elements_by_xpath("//*[@resource-id='com.xueqiu.android:id/current_price']")[0].text
        print("\n当前股票的价格：" + current_price)
        assert float(current_price) > float(200)
        self.driver.back()
        print(self.driver.contexts)
        time.sleep(3)

    def test_touchAction(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((MobileBy.XPATH, "//*[@text='推荐']")))
        el1 = self.driver.find_element_by_xpath("//*[@text='推荐']")
        el1_name = el1.get_attribute("text")
        print(el1_name)
        time.sleep(3)
        action = TouchAction(self.driver)
        width = self.driver.get_window_rect()['width']
        height = self.driver.get_window_rect()['height']
        x_start = int(width/2)

        y_start = int(height * 0.8)
        y_end = int(height*0.2)
        print(x_start, y_start, y_end)
        action.press(x=x_start, y=y_start).wait(500).move_to(x=x_start, y=y_end).release().perform()
        time.sleep(4)

