# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 14:11:17 2018

@author: PCCC
"""
import unittest
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import Select
import time
import os
import re
from public_package.pubilc_package import url,login_name,login_name_test,login_password,login_password_test
from public_package.pubilc_package import TESTCASE
import HTMLTestRunner
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

class TESTCAST_ZHIBANGUANLI(TESTCASE):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()

    def tearDown(self):
        # print("脚本执行完成")
        self.dr.quit()

    def login(self, username, password):
        self.dr.get(url)
        self.dr.find_element_by_id('vv').send_keys(username)
        self.dr.find_element_by_xpath('//*[@id="login_ff"]/div[2]/input').send_keys(password)
        self.dr.find_element_by_xpath('//*[@id="login_ff"]/a').click()

    def zhibanguanli_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div/a[2]/div[2]/img[2]').click()
        time.sleep(5)
        self.assertEqual('勤务管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '勤务管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="537"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('值班管理列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '值班管理')

    def test1_zhibanguanli_add(self):
        self.zhibanguanli_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        time_now=now = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        self.dr.find_element_by_xpath('//*[@id="dutyDate"]').click()

        option_choice=Select(self.dr.find_element_by_xpath('//*[@id="dutyType"]'))
        option_choice.select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="dutyArea"]').send_keys('拉萨市实验中学')
        self.dr.find_element_by_xpath('//*[@id="dutyPerson"]').send_keys('包涵')
        self.dr.find_element_by_xpath('//*[@id="dutyPersonCharge"]').send_keys('林峰')
        self.dr.find_element_by_xpath('//*[@id="telephone"]').send_keys('15874587474')
        self.dr.find_element_by_xpath('//*[@id="dutyContent"]').send_keys('中学上学和放学时间段周边情况执勤')
        self.dr.find_element_by_xpath('//*[@id="saveDutyManage"]').click()
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual('值班管理列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '值班管理')
        print('勤务管理-值班管理：新增功能正常')

    # def test2_zhibanguanli_search_date(self):
    #     self.zhibanguanli_search()
    #     search_value_date = '2018-09-05'
    #     self.dr.find_element_by_xpath('//*[@id="dutyDates"]').send_keys(search_value_date)
    #     self.dr.find_element_by_xpath('//*[@id="search"]').click()
    #     self.dr.switch_to.default_content()
    #     time.sleep(5)
    #     self.dr.switch_to.frame('iframeb')
    #     paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
    #     column = 4
    #     self.pagination_num(paginal_number, search_value_date, column)
    #     self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[9]/a').click()
    #     self.assertIn(search_value_date,self.dr.find_element_by_xpath('//*[@id="dutyDate"]').get_attribute('value'),'校验详情页的日期')
    #     self.dr.find_element_by_xpath('/html/body/a').click()
    #     self.dr.implicitly_wait(2)
    #     self.assertEqual('值班管理列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,'值班管理')
    #     print('勤务管理-值班管理：时间条件查询功能正常')
    #
    # def test3_zhibanguanli_search_dutyType(self):
    #     self.zhibanguanli_search()
    #     option_chioce=Select(self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/div/select'))
    #     option_chioce.select_by_value('1')
    #     option_chioce_value=option_chioce.first_selected_option.text
    #     self.dr.find_element_by_xpath('//*[@id="search"]').click()
    #     self.dr.switch_to.default_content()
    #     time.sleep(5)
    #     self.dr.switch_to.frame('iframeb')
    #     paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
    #     column = 5
    #     self.pagination_num(paginal_number, option_chioce_value, column)
    #     self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[9]/a').click()
    #     self.assertIn(option_chioce_value,self.dr.find_element_by_xpath('//*[@id="dutyType"]/option[2]').text,'校验详情页值班类型')
    #     self.dr.find_element_by_xpath('/html/body/a').click()
    #     self.dr.implicitly_wait(2)
    #     self.assertEqual('值班管理列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,'值班管理')
    #     print('勤务管理-值班管理：值班类型条件查询功能正常')
    #
    # def test4_zhibanguanli_delete(self):
    #     self.zhibanguanli_search()
    #     self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[1]/input').click()
    #     self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
    #     self.dr.switch_to.default_content()
    #     time.sleep(2)
    #     self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
    #     time.sleep(5)
    #     self.dr.switch_to.frame('iframeb')
    #     self.assertEqual('值班管理列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,'值班管理')
    #     print('勤务管理-值班管理：新增功能正常')

if __name__=='__main__':
    unittest.main()