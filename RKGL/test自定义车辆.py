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

class TESTCAST_ZIDINGYICHELIANG(TESTCASE):
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

    def zidingyicheliang_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/a[3]').click()
        time.sleep(2)
        self.assertEqual('车辆管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text,'校验车辆管理菜单')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[1]/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="950"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(3)
        self.assertEqual('自定义车辆列表',self.dr.find_element_by_xpath('/html/body/div[1]/div').text,'校验自定义车辆菜单')

    def test1_zidingyicheliang_add(self):
        self.zidingyicheliang_search()
        add_value='藏DK0700'
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        self.dr.find_element_by_xpath('//*[@id="vehicleNo"]').send_keys(add_value)
        self.dr.find_element_by_xpath('//*[@id="veForm"]/div[1]/div[2]/a/span').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="monitorReason"]').send_keys('涉嫌交通逃逸')
        self.dr.find_element_by_xpath('//*[@id="modifyBy"]').send_keys('马汉')
        self.dr.find_element_by_xpath('//*[@id="monitorUnit"]').click()
        self.dr.find_element_by_xpath('//*[@id="monitorUnit"]').click()
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('自定义车辆列表',self.dr.find_element_by_xpath('/html/body/div[1]/div').text,'校验返回功能')
        print('车辆管理-自定义车辆：新增功能正常')

    def test2_zidingyicheliang_search_cphm(self):
        self.zidingyicheliang_search()
        search_value_cphm='藏DK0700'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value_cphm)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number=self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column=3
        self.pagination_num(paginal_number,search_value_cphm,column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        self.assertEqual(search_value_cphm,self.dr.find_element_by_xpath('//*[@id="vehicleNo"]').get_attribute('value'),'校验详情页面的车牌号')
        print('车辆管理-自定义车辆：车牌条件查询功能正常')

    def test3_zidingyicheliang_delete(self):
        self.zidingyicheliang_search()
        search_value_cphm = '藏DK0700'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value_cphm)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_cphm, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text,'校验删除功能是否正常')
        print('车辆管理-自定义车辆：删除功能正常')

if __name__ == '__main__':
    unittest.main()