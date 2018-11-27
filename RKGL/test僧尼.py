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

class TESTCAST_sengni(TESTCASE):
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

    def sengni_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/a[2]').click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '人口管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[7]/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="703"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('僧尼信息列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '僧尼信息')

    def test1_sengni_add(self):
        self.sengni_search()
        add_value_carid='500107198901218926'
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        self.dr.find_element_by_xpath('//*[@id="idCard"]').send_keys(add_value_carid)
        self.dr.find_element_by_xpath('//*[@id="priestName"]').send_keys('萱玄')
        self.dr.find_element_by_xpath('//*[@id="telephone"]').send_keys('15474587458')
        '''选择支队'''
        self.dr.find_element_by_xpath('//*[@id="attributeBranchRankName"]').click()
        self.dr.find_element_by_xpath('//*[@id="treeSelect_1_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_9_span"]').click()
        '''选择大队'''
        self.dr.find_element_by_xpath('//*[@id="attributeBigRankName"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect2_1_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect2_24_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect2_25_span"]').click()
        '''选择派出所'''
        self.dr.find_element_by_xpath('//*[@id="attributePoliceStationName"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect3_1_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect3_43_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect3_47_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect3_50_span"]').click()
        self.dr.find_element_by_xpath('//*[@id="templeName"]').send_keys('大昭寺')
        self.dr.find_element_by_xpath('//*[@id="religionCertificateNo"]').send_keys('54745874')
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual('僧尼信息列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '僧尼信息')
        print('人口管理-701数据库-僧尼：新增功能正常')

    def test2_sengni_search_name(self):
        self.sengni_search()
        search_value_name='刘钰萱'
        self.dr.find_element_by_xpath('//*[@id="monkName"]').send_keys(search_value_name)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_name, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(search_value_name,self.dr.find_element_by_xpath('//*[@id="monkName"]').get_attribute('value'),'校验详情页面姓名')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('僧尼信息列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '僧尼信息')
        print('人口管理-701数据库-僧尼：姓名条件查询功能正常')

    def test3_sengni_search_faming(self):
        self.sengni_search()
        search_value_faming='萱玄'
        self.dr.find_element_by_xpath('//*[@id="priestName"]').send_keys(search_value_faming)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_faming, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(search_value_faming,self.dr.find_element_by_xpath('//*[@id="priestName"]').get_attribute('value'),'校验详情页面法名')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('僧尼信息列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '僧尼信息')
        print('人口管理-701数据库-僧尼：法名条件查询功能正常')

    def test4_sengni_search_carid(self):
        self.sengni_search()
        search_value_carid='500107198901218926'
        self.dr.find_element_by_xpath('//*[@id="idCard"]').send_keys(search_value_carid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_carid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(search_value_carid,self.dr.find_element_by_xpath('//*[@id="idCard"]').get_attribute('value'),'校验详情页面身份证号')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('僧尼信息列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '僧尼信息')
        print('人口管理-701数据库-僧尼：身份证条件查询功能正常')

    def test5_sengni_search_templeName(self):
        self.sengni_search()
        search_value_templeName='大昭寺'
        self.dr.find_element_by_xpath('//*[@id="templeName"]').send_keys(search_value_templeName)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 7
        self.pagination_num(paginal_number, search_value_templeName, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(search_value_templeName,self.dr.find_element_by_xpath('//*[@id="templeName"]').get_attribute('value'),'校验详情页面身份证号')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('僧尼信息列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '僧尼信息')
        print('人口管理-701数据库-僧尼：寺庙名称条件查询功能正常')

    def test6_sengni_delete(self):
        self.sengni_search()
        search_value_carid = '500107198901218926'
        self.dr.find_element_by_xpath('//*[@id="idCard"]').send_keys(search_value_carid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_carid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('人口管理-701数据库-僧尼：删除功能正常')

if __name__=='__main__':
    unittest.main()