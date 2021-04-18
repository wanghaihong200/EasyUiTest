#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: test_wework
@time: 2021/4/13 8:41 下午
@desc:
"""
from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestWeWork():
    def setup_class(self):
        self.desire_app = {
            "platformName": "Android",
            "platformVersion": '9.0',
            "deviceName": "honor9",
            "udid": "FFKDU17A14004245",
            "automationName": "UiAutomator2",
            "noReset": "True",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=self.desire_app)
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        self.driver.quit()


    def test_address_list(self):
        ele_address_list = self.driver.find_element_by_xpath("//*[@text='通讯录']")
        ele_address_list.click()
        ele_hai = self.driver.find_element_by_xpath("//*[@text='王海虹' and @class='android.widget.TextView']")
        ele_hai.click()
        time.sleep(3)

    def test_work_station(self):
        # 外出打卡
        el_work_station = self.driver.find_element_by_xpath("//*[@text='工作台']")
        el_work_station.click()

        el_schedule = self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                                      'scrollable(true).instance(0)).'
                                                                      'scrollIntoView(new UiSelector().'
                                                                      'text("打卡").instance(0));')
        el_schedule.click()
        el_out_punch = self.driver.find_element_by_xpath("//*[@text='外出打卡']")
        el_out_punch.click()
        el_punch = self.driver.find_element_by_xpath("//*[contains(@text, '次外出') and contains(@text, '第')]")
        el_punch.click()

        # WebDriverWait(self.driver, 10).until(lambda x: "外出打卡成功" in self.driver.page_source)  # 显示等待直到 断言文字出现在页面dom中
        WebDriverWait(self.driver, 10).until(lambda x: "离开" in self.driver.page_source)  # 显示等待直到 断言文字出现在页面dom中
        print(self.driver.page_source)
        assert "外出打卡成功" in self.driver.page_source

        time.sleep(3)

    def test_contact(self):
        # 点击通讯录-》添加成员-》手动输入添加-》完整输入，录入成员信息
        el_contact = self.driver.find_element_by_xpath("//*[@text='通讯录']")
        el_contact.click()
        el_contact_add = self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                                         'scrollable(true).instance(0)).'
                                                                         'scrollIntoView(new UiSelector().'
                                                                         'text("添加成员").instance(0));')
        el_contact_add.click()
        el_add_member = self.driver.find_element_by_xpath("//*[@text='手动输入添加']")
        el_add_member.click()
        try:
            el_add_detail = self.driver.find_element_by_xpath("//*[@text='完整输入']")

        except Exception as e:
            el_add_fast = self.driver.find_element_by_xpath("//*[@text='快速输入']")
            print("\n快速输入按钮已定位，目前页面已处于 完整输入页面！")
        else:
            el_add_detail.click()
        el_name_input = self.driver.find_element_by_xpath("//*[contains(@text, '姓名')]/..//*[@text='必填']")
        el_name_input.send_keys("张惠妹")
        el_sex_input = self.driver.find_element_by_xpath("//*[contains(@text, '性别')]/..//*[@text='男']")
        el_sex_input.click()
        el_sex_select = self.driver.find_element_by_xpath("//*[@text='女']")
        el_sex_select.click()
        el_phone_input = self.driver.find_element_by_xpath("//*[@text='手机号']")
        el_phone_input.send_keys('13391387821')
        el_notice = self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                                    'scrollable(true).instance(0)).'
                                                                    'scrollIntoView(new UiSelector().'
                                                                    'text("保存后自动发送邀请通知").instance(0));')
        el_notice.click()
        el_save = self.driver.find_element_by_xpath("//*[@text='保存']")
        el_save.click()
        # 断言
        WebDriverWait(self.driver, 10).until(lambda x: "添加成员" in self.driver.page_source)
        assert '添加成员' in self.driver.page_source
        time.sleep(3)
        self.driver.find_element()




