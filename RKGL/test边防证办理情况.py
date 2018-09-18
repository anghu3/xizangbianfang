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

class TESTCAST_BFZ(unittest.TestCase):
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

    def bfz_search(self):
        self.login(login_name, login_password)
        time.sleep(5)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/a[2]').click()
        time.sleep(2)
        self.assertEqual('人口管理', self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '人口管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[2]/p[2]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="823"]').click()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('边防证列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '边防证办理情况')

    def test1_bfz_search_name(self):
        self.bfz_search()
        search_value = '达娃次吉'
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[2]').text,'姓名条件查询')
        self.dr.find_element_by_xpath('//*[@id="reset"]').click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.assertNotEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text, '重置功能')
        print('人口管理-边防证办理情况：姓名条件查询功能正常')

    def test2_bfz_search_cardid(self):
        self.bfz_search()
        search_value = '542223198103060102'
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/div/input').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,
                         '身份证条件查询')
        self.dr.find_element_by_xpath('//*[@id="reset"]').click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.assertNotEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]').text, '重置功能')
        print('人口管理-边防证办理情况：身份证号条件查询功能正常')

    def test3_bfz_search_passportCode(self):
        self.bfz_search()
        search_value = 'K03725694'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[3]/div/input').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,
                         '通行证条件查询')
        self.dr.find_element_by_xpath('//*[@id="reset"]').click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.assertNotEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[4]').text, '重置功能')
        print('人口管理-边防证办理情况：通行证编号条件查询功能正常')

    def test4_bfz_search_orgName(self):
        self.bfz_search()
        option_chioce = Select(self.dr.find_element_by_xpath('//*[@id="form"]/div[4]/div/select'))
        for i in range(0, 28):
            option_chioce.select_by_index(i)
            self.dr.find_element_by_xpath('//*[@id="search"]').click()
            time.sleep(2)
        print('人口管理-边防证办理情况：办理单位条件查询功能正常')

    def test5_bfz_search_time(self):
        self.bfz_search()
        self.dr.find_element_by_xpath('//*[@id="form"]/div[5]/div/input').send_keys('2018-04-02')
        self.dr.find_element_by_xpath('//*[@id="form"]/div[6]/div/input').send_keys('2018-04-02')
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(2)
        print('人口管理-边防证办理情况：时间条件查询功能正常')

if __name__=='__main__':
    unittest.main()