#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: test_params
@time: 2021/4/10 5:50 下午
@desc:
"""

from appium import webdriver
import time
import pytest
from data.datas_search import DatasSearch

from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestAppium():
    def setup_class(self):
        self.desire_app = {
            "platformName": "Android",
            "platformVersion": '9.0',
            "deviceName": "honor9",
            "udid": "FFKDU17A14004245",
            "automationName": "UiAutomator2",
            "noReset": "True",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=self.desire_app)
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        self.driver.quit()


    @pytest.mark.parametrize("search_key", DatasSearch.search_key)
    def test_search(self, search_key):
        el_search = self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
        el_search.click()
        el_search_text = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        time.sleep(3)
        el_search_text.send_keys(search_key)
        el_search_text.send_keys(search_key)
        el_search_result = self.driver.find_elements_by_xpath(f"//*[contains(@text, '{search_key}') and @resource-id='com.xueqiu.android:id/name']")[0]
        el_search_result.click()

        time.sleep(3)
        current_price = self.driver.find_elements_by_xpath("//*[@resource-id='com.xueqiu.android:id/current_price']")[0].text
        print("\n当前股票的价格：" + current_price)
        # assert float(current_price) > float(200)
        self.driver.back()
        time.sleep(3)

    def test_hybrid(self):
        el_trade = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/tab_name' and @text='交易']")
        el_trade.click()
        print(self.driver.contexts)
        el_aAccount = self.driver.find_element_by_xpath("//*[@text='A股开户']")
        el_aAccount.click()
        print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts[-1])
        el_username = self.driver.find_elements_by_xpath("//*[@class='android.widget.EditText']")[0]
        el_username.send_keys('13391387820')
        el_send_code = self.driver.find_element_by_xpath("//*[@text='获取验证码' and @class='android.view.View']")
        el_send_code.click()
        el_identify_code = self.driver.find_elements_by_xpath("//*[@class='android.widget.EditText']")[1]
        el_identify_code.send_keys('8888')
        time.sleep(3)
        self.driver.set_network_connection()

