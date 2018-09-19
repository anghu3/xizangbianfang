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
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

class TESTCAST_QUNFANGCAIJI(TESTCASE):
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

    def qunfangxinxicaiji_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/a[2]').click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '人口管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[10]/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="604"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('群防信息采集列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '群防信息采集')

    def test1_qunfangxinxicaiji_search_infoCollectIp(self):
        self.qunfangxinxicaiji_search()
        search_value_infoCollectIp='192.168.110.81'
        self.dr.find_element_by_xpath('//*[@id="infoCollectIp"]').send_keys(search_value_infoCollectIp)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 2
        self.pagination_num(paginal_number,search_value_infoCollectIp , column)
        print('人口管理-群防信息采集：信息采集接口IP条件查询功能正常')

    def test2_qunfangxinxicaiji_search_infoSendIp(self):
        self.qunfangxinxicaiji_search()
        search_value_infoSendIp='192.168.0.81'
        self.dr.find_element_by_xpath('//*[@id="infoSendIp"]').send_keys(search_value_infoSendIp)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 6
        self.pagination_num(paginal_number,search_value_infoSendIp , column)
        print('人口管理-群防信息采集：信息采集接口IP条件查询功能正常')

    def test3_qunfangxinxicaiji_search_caishijian(self):
        self.qunfangxinxicaiji_search()
        search_value_caijishijian='2018-09-04'
        self.dr.find_element_by_xpath('//*[@id="startTime"]').send_keys(search_value_caijishijian)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 7
        self.pagination_num(paginal_number,search_value_caijishijian , column)
        print('人口管理-群防信息采集：信息采集接口IP条件查询功能正常')

if __name__=='__main__':
    unittest.main()