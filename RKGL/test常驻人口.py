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
import sys
from public_package.pubilc_package import url,login_name,login_name_test,login_password,login_password_test
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

def findnum(string):
    comp = re.compile('-?[1-9]\d*')
    list_str = comp.findall(string)
    list_num = []
    for item in list_str:
        item = int(item)
        list_num.append(item)
    return list_num

class TESTCAST_CZRK(unittest.TestCase):
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

    def czrk_search(self):
        self.login(login_name,login_password)
        time.sleep(5)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/a[2]').click()
        time.sleep(2)
        self.assertEqual('人口管理', self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '人口管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[3]/p[2]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="802"]').click()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('常住人口', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '常住人口')

    def test1_czrk_search_name(self):
        self.czrk_search()
        search_value = '荆帅'
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(20)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]').text,
                         '姓名条件查询')
        self.dr.find_element_by_xpath('//*[@id="reset"]').click()
        time.sleep(5)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.assertNotEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]').text,
                            '重置功能')
        print('人口管理-人员基本信息-常住人口:姓名条件查询功能正常')

    def test2_czrk_search_cardid(self):
        self.czrk_search()
        search_value = '370123198009220510'
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/div/input').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(240)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text,
                         '身份证条件查询')
        self.dr.find_element_by_xpath('//*[@id="reset"]').click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.assertNotEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text,
                            '重置功能')
        print('人口管理-人员基本信息-常住人口:身份证号条件查询功能正常')

    def test3_czrk_search_hh(self):
        self.czrk_search()
        search_value = '0704010095'
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[3]/div/input').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[7]').text,
                         '户号条件查询')
        self.dr.find_element_by_xpath('//*[@id="reset"]').click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.assertNotEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[7]').text,
                            '重置功能')
        print('人口管理-人员基本信息-常住人口:户号条件查询功能正常')

    def test4_czrk_search_hjdz(self):
        self.czrk_search()
        search_value = '卧龙镇卧龙行政村嘎加自然村48'
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[4]/div/input').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]').text,
                         '户籍地址条件查询')
        self.dr.find_element_by_xpath('//*[@id="reset"]').click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.assertNotEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]').text,
                            '重置功能')
        print('人口管理-人员基本信息-常住人口:户籍地址条件查询功能正常')

    def test5_czrk_xiangqing(self):
        self.czrk_search()
        search_value = '荆帅'
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        name=self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]').text
        carid=self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        self.dr.implicitly_wait(30)
        self.assertEqual(name,self.dr.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/div/div[4]/div/div[2]').text,'详情信息校验')
        self.assertEqual(carid, self.dr.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div/div[2]/div/div[9]/div/div[2]').text, '详情信息校验')
        print('人口管理-人员基本信息-常住人口:详情功能正常')

if __name__ == '__main__':
    unittest.main()

