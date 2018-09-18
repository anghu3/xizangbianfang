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

class TESTCAST_SHEXIANGTOU(TESTCASE):
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

    def shexiangtou_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div/a[1]/div[2]/img[2]').click()
        time.sleep(5)
        self.assertEqual('管理防范',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '管理防范')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="954"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('摄像头基本信息列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text,
                         '摄像头基本信息')

    def test1_shexiangtou_search_deviceCode(self):
        self.shexiangtou_search()
        search_value_deviceCode='54260000001310017818'
        self.dr.find_element_by_xpath('//*[@id="deviceCode"]').send_keys(search_value_deviceCode)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 2
        self.pagination_num(paginal_number, search_value_deviceCode, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(search_value_deviceCode,self.dr.find_element_by_xpath('//*[@id="cameraForm"]/div/div[1]/div[1]/div[1]/div[2]').text
                         ,'校验详情页面设备编号')
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.assertEqual('摄像头基本信息列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text,'摄像头基本信息')
        print('管理防范-摄像头基本信息管理：设备编号条件查询功能正常')

    def test2_shexiangtou_search_detachment(self):
        self.shexiangtou_search()
        search_value_detachment='西藏公安边防总队'
        self.dr.find_element_by_xpath('//*[@id="detachment"]').send_keys(search_value_detachment)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_detachment, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(search_value_detachment,self.dr.find_element_by_xpath('//*[@id="cameraForm"]/div/div[1]/div[2]/div[1]/div[2]').text
                         ,'校验详情页面支队')
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.assertEqual('摄像头基本信息列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text,'摄像头基本信息')
        print('管理防范-摄像头基本信息管理：支队条件查询功能正常')

    def test3_shexiangtou_search_brigade(self):
        self.shexiangtou_search()
        search_value_brigade='总队机关营区'
        self.dr.find_element_by_xpath('//*[@id="brigade"]').send_keys(search_value_brigade)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_brigade, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(search_value_brigade,self.dr.find_element_by_xpath('//*[@id="cameraForm"]/div/div[1]/div[1]/div[2]/div[2]').text
                         ,'校验详情页面大队')
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.assertEqual('摄像头基本信息列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text,'摄像头基本信息')
        print('管理防范-摄像头基本信息管理：大队条件查询功能正常')

    def test4_shexiangtou_search_policeStation(self):
        self.shexiangtou_search()
        search_value_policeStation='总队机关营区3'
        self.dr.find_element_by_xpath('//*[@id="policeStation"]').send_keys(search_value_policeStation)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_policeStation, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(search_value_policeStation,self.dr.find_element_by_xpath('//*[@id="cameraForm"]/div/div[1]/div[2]/div[2]/div[2]').text
                         ,'校验详情页面派出所/工作站')
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.assertEqual('摄像头基本信息列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text,'摄像头基本信息')
        print('管理防范-摄像头基本信息管理：派出所/工作站条件查询功能正常')

    def test5_shexiangtou_search_units(self):
        self.shexiangtou_search()
        search_value_units='总队机关营区3'
        self.dr.find_element_by_xpath('//*[@id="units"]').send_keys(search_value_units)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_units, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(search_value_units,self.dr.find_element_by_xpath('//*[@id="cameraForm"]/div/div[1]/div[1]/div[3]/div[2]').text
                         ,'校验详情页面所属单位')
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.assertEqual('摄像头基本信息列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text,'摄像头基本信息')
        print('管理防范-摄像头基本信息管理：所属单位条件查询功能正常')

if __name__=='__main__':
    unittest.main()