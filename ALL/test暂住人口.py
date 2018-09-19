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

class TESTCAST_ZZRK(unittest.TestCase):
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

    def zzrk_search(self):
        self.login(login_name, login_password)
        time.sleep(5)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/a[2]').click()
        time.sleep(2)
        self.assertEqual('人口管理', self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '人口管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[3]/p[2]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="803"]').click()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('流动人口信息列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '暂住人口')

    def test1_zzrk_search_name(self):
        self.zzrk_search()
        search_value = '杨东岳'
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text,'姓名条件查询')
        self.dr.find_element_by_xpath('//*[@id="reset"]').click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.assertNotEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text,
                            '重置功能')
        print('人口管理-人员基本信息-暂住人口:姓名条件查询功能正常')

    def test2_zzrk_search_cardid(self):
        self.zzrk_search()
        search_value = '51062319710606001X'
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/div/input').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]').text,'身份证号条件查询')
        self.dr.find_element_by_xpath('//*[@id="reset"]').click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.assertNotEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]').text,
                            '重置功能')
        print('人口管理-人员基本信息-暂住人口:身份证号条件查询功能正常')

    def test3_zzrk_search_tempResidPermitNo(self):
        self.zzrk_search()
        search_value = '04303110'
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[3]/div/input').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[7]').text,'居住证编号条件查询')
        self.dr.find_element_by_xpath('//*[@id="reset"]').click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.assertNotEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[7]').text,
                            '重置功能')
        print('人口管理-人员基本信息-暂住人口:居住证编号条件查询功能正常')

    def test4_zzrk_search_tempAddrRegDetailAddr(self):
        self.zzrk_search()
        search_value = '西藏->山南地区->浪卡子县->普玛江塘乡->下索村->下索'
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[4]/div/input').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]').text,'暂住地址条件查询')
        self.dr.find_element_by_xpath('//*[@id="reset"]').click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.assertNotEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]').text,
                            '重置功能')
        print('人口管理-人员基本信息-暂住人口:暂住地址条件查询功能正常')

    def test5_zzrk_search_isProvInOut(self):
        self.zzrk_search()
        search_value = '省内'
        isProvInOut = Select(self.dr.find_element_by_xpath('//*[@id="form"]/div[5]/div/select'))
        isProvInOut.select_by_visible_text(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[12]').text, '校验结果')
        print('人口管理-人员基本信息-暂住人口:区域条件查询功能正常')

    def test6_zzrk_search_isProvInOut(self):
        self.zzrk_search()
        search_value = '省外'
        isProvInOut = Select(self.dr.find_element_by_xpath('//*[@id="form"]/div[5]/div/select'))
        isProvInOut.select_by_visible_text(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[12]').text, '校验结果')
        print('人口管理-人员基本信息-暂住人口:区域条件查询功能正常')

    def test7_zzrk_search_liveState(self):
        self.zzrk_search()
        search_value = '现住'
        isProvInOut = Select(self.dr.find_element_by_xpath('//*[@id="form"]/div[6]/div/select'))
        isProvInOut.select_by_visible_text(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[13]').text, '校验结果')
        print('人口管理-人员基本信息-暂住人口:居住状态条件查询功能正常')

    def test8_zzrk_search_liveState(self):
        self.zzrk_search()
        search_value = '历史居住'
        isProvInOut = Select(self.dr.find_element_by_xpath('//*[@id="form"]/div[6]/div/select'))
        isProvInOut.select_by_visible_text(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[13]').text, '校验结果')
        print('人口管理-人员基本信息-暂住人口:居住状态条件查询功能正常')

    def test9_zzrk_search_xiangqing(self):
        self.zzrk_search()
        search_value_name='杨东岳'
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value_name)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        search_value_carid=self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]').text
        self.assertEqual(search_value_name, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text, '姓名条件查询')
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[14]/a').click()
        self.dr.implicitly_wait(30)
        self.assertEqual(search_value_name,self.dr.find_element_by_xpath('//*[@id="xm"]').text,'详情信息校验')
        self.assertEqual(search_value_carid,self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').get_attribute('value'),'校验详情')
        print('人口管理-人员基本信息-暂住人口:详情功能正常')

    def test10_zzrk_update(self):
        self.zzrk_search()
        search_value_name='杨东岳'
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value_name)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        search_value_carid=self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]').text
        self.assertEqual(search_value_name, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text, '姓名条件查询')
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[14]/a').click()
        self.dr.implicitly_wait(30)
        self.assertEqual(search_value_name,self.dr.find_element_by_xpath('//*[@id="xm"]').text,'详情信息校验')
        self.assertEqual(search_value_carid,self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').get_attribute('value'),'校验详情')
        Select(self.dr.find_element_by_xpath('//*[@id="tj"]/div/div/div[2]/div[1]/div[1]/div[1]/select')).select_by_value('22')
        self.dr.find_element_by_xpath('//*[@id="tj"]/div/div/div[2]/div[3]/a').click()
        time.sleep(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value_name)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        search_value_carid = self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]').text
        self.assertEqual(search_value_name, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text,
                         '姓名条件查询')
        self.assertEqual('长子',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[8]').text,'校验更新是否正常')
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[14]/a').click()
        Select(self.dr.find_element_by_xpath('//*[@id="tj"]/div/div/div[2]/div[1]/div[1]/div[1]/select')).select_by_value('01')
        self.dr.find_element_by_xpath('//*[@id="tj"]/div/div/div[2]/div[3]/a').click()
        print('人口管理-人员基本信息-暂住人口:编辑功能正常')

if __name__=='__main__':
    unittest.main()
