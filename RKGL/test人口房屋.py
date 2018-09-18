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

class TESTCAST_RKFW(unittest.TestCase):
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

    def rkfw_search(self):
        self.login(login_name,login_password)
        time.sleep(5)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/a[2]').click()
        time.sleep(2)
        self.assertEqual('人口管理', self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '人口管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[3]/p[2]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="562"]').click()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('房屋信息列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '人口房屋')

    def test1_rkfw_search_name(self):
        self.rkfw_search()
        search_value_name='来玛琼吉'
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value_name)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.assertEqual(search_value_name,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[1]').text,'姓名条件查询')
        self.dr.find_element_by_xpath('//*[@id="reset"]').click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.assertNotEqual(search_value_name, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[1]').text,
                            '重置功能')
        print('人口管理-人员基本信息-人口房屋：姓名条件查询功能正常')

    def test2_rkfw_search_carid(self):
        self.rkfw_search()
        search_value_carid='456485715'
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/div/input').send_keys(search_value_carid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.assertEqual(search_value_carid, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text,
                         '房主证件号码条件查询')
        self.dr.find_element_by_xpath('//*[@id="reset"]').click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.assertNotEqual(search_value_carid, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text,
                            '重置功能')
        print('人口管理-人员基本信息-人口房屋：房主证件号码条件查询功能正常')

    def test3_rkfw_search_jlx_(self):
        self.rkfw_search()
        search_value_jlx='创业街'
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[3]/div/input').send_keys(search_value_jlx)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.assertIn(search_value_jlx,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]').text,'街路巷条件查询')
        self.dr.find_element_by_xpath('//*[@id="reset"]').click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.assertNotEqual(search_value_jlx,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]').text,
                            '重置功能')
        print('人口管理-人员基本信息-人口房屋：街路巷条件查询功能正常')

    def test4_rkfw_searh_mlp(self):
        self.rkfw_search()
        search_value_mpl='102'
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[4]/div/input').send_keys(search_value_mpl)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.assertIn(search_value_mpl,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]').text,'门楼牌条件查询')
        self.dr.find_element_by_xpath('//*[@id="reset"]').click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.assertNotEqual(search_value_mpl,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]').text,
                            '重置功能')
        print('人口管理-人员基本信息-人口房屋：门楼牌条件查询功能正常')

    def test5_rkfw_search_xz(self):
        self.rkfw_search()
        search_value_xz='西藏->林芝地区->朗县->金东乡->来义村->来义自然村'
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[5]/div/input').send_keys(search_value_xz)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.assertIn(search_value_xz, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]').text,
                      '详址条件查询')
        self.dr.find_element_by_xpath('//*[@id="reset"]').click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.assertNotEqual(search_value_xz, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]').text,
                            '重置功能')
        print('人口管理-人员基本信息-人口房屋：详址条件查询功能正常')

if __name__ == '__main__':
    unittest.main()
