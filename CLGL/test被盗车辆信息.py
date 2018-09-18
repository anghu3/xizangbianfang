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

class TESTCAST_BEIDAOCHELIANG(TESTCASE):
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

    def beidaocheliang_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/a[3]').click()
        time.sleep(2)
        self.assertEqual('车辆管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text,'校验车辆管理菜单')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[3]/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="940"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(3)
        self.assertEqual('盗抢车辆列表',self.dr.find_element_by_xpath('/html/body/div[1]/div').text,'被盗车辆信息')

    def test1_beidaocheliang_search_hmhp(self):
        self.beidaocheliang_search()
        search_value_hmhp='藏EA2961'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value_hmhp)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 2
        self.pagination_num(paginal_number,search_value_hmhp,column)
        search_value_hplx=self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]').text
        search_value_ajbm=self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[4]').text
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/a').click()
        self.assertEqual(search_value_hmhp,self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[1]/div[2]').text,'校验详情页面车牌号')
        self.assertEqual(search_value_hplx,self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[1]/div[2]').text,'校验详情页面号牌类型')
        self.assertEqual(search_value_ajbm,self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[2]/div[2]').text,'校验详情页面案件编号')
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('盗抢车辆列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text, '校验返回功能')
        print('车辆管理-被盗车辆信息：号码号牌条件查询和详情功能正常')

if __name__ == '__main__':
    unittest.main()