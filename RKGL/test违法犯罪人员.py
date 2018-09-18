# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 14:11:17 2018

@author: PCCC
"""
import unittest
from selenium import webdriver
import selenium.webdriver.support.ui as ui
import time
import os
import re
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

class TESTCAST_WFFZRY(unittest.TestCase):
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

    def wfzry_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/a[2]').click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '人口管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[4]/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="326"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('违法犯罪人员', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '违法犯罪人员')

    def test1_wffzry_search_cardid(self):
        self.wfzry_search()
        search_value = '37012319810702291'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.implicitly_wait(240)
        self.assertIn(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]').text, '校验结果')
        print('人口管理-违法犯罪人员：身份证号码条件查询功能正常')

    def test2_wffzry_search_xiangqing(self):
        self.wfzry_search()
        carid=self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text
        name=self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[11]/a').click()
        time.sleep(2)
        self.assertEqual(carid,self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').get_attribute('value'),'校验详情页面身份证号')
        self.assertEqual(name,self.dr.find_element_by_xpath('//*[@id="xm"]').text,'校验详情页面姓名')
        print('人口管理-违法犯罪人员：详情功能正常')


if __name__ == '__main__':
    unittest.main()