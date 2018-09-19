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

class TESTCAST_SANFEI(TESTCASE):
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

    def sanfei_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/a[2]').click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '人口管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[6]/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="771"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('三非人员信息列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text,
                         '三非人员')

    def test1_sanfei_add(self):
        self.sanfei_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        add_value_name='索朗旺堆'
        add_value_carid='540123198506025515'
        self.dr.find_element_by_xpath('//*[@id="personName"]').send_keys(add_value_name)
        Select(self.dr.find_element_by_xpath('//*[@id="personType"]')).select_by_value('1')
        Select(self.dr.find_element_by_xpath('//*[@id="idType"]')).select_by_value('111')
        self.dr.find_element_by_xpath('//*[@id="idNumber"]').send_keys(add_value_carid)
        self.dr.find_element_by_xpath('//*[@id="entryPosition"]').send_keys('米林县边防线')
        self.dr.find_element_by_xpath('//*[@id="residentialAddress"]').send_keys('拉萨市城关区发展大道建设1路101号')
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/a').click()
        # self.dr.switch_to.default_content()
        time.sleep(2)
        # self.dr.switch_to.frame('iframeb')
        self.assertEqual('三非人员信息列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text,
                         '三非人员')
        self.assertEqual(add_value_carid,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[5]').text,'校验新增和默认排序')
        print('人口管理-部局七类库-三非人员：新增功能正常')


    def test2_sanfei_search_name(self):
        self.sanfei_search()
        search_value_name='索朗旺堆'
        self.dr.find_element_by_xpath('//*[@id="personName"]').send_keys(search_value_name)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number=self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column=3
        self.pagination_num(paginal_number,search_value_name,column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[8]/a').click()
        self.assertEqual(search_value_name,self.dr.find_element_by_xpath('//*[@id="personName"]').get_attribute('value'),'校验详情信息')
        print('人口管理-部局七类库-三非人员：姓名条件查询功能正常')

    def test3_sanfei_search_zjlx(self):
        self.sanfei_search()
        search_value_zjlx='居民身份证'
        Select(self.dr.find_element_by_xpath('//*[@id="idType"]')).select_by_value('111')
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number,search_value_zjlx,column)
        print('人口管理-部局七类库-三非人员：证件类型条件查询功能正常')

    def test4_sanfei_search_carid(self):
        self.sanfei_search()
        search_value_carid='540123198506025515'
        self.dr.find_element_by_xpath('//*[@id="idNumber"]').send_keys(search_value_carid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_carid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[8]/a').click()  # 返回功能
        self.assertEqual(search_value_carid,
                         self.dr.find_element_by_xpath('//*[@id="idNumber"]').get_attribute('value'), '校验详情信息')
        print('人口管理-部局七类库-三非人员：证件编号条件查询功能正常')

    def test5_sanfei_search_rylx(self):
        self.sanfei_search()
        search_value_rylx = '非法入境'
        Select(self.dr.find_element_by_xpath('//*[@id="personType"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 6
        self.pagination_num(paginal_number,search_value_rylx,column)
        print('人口管理-部局七类库-三非人员：人员类型条件查询功能正常')

    def test6_sanfei_delete(self):
        self.sanfei_search()
        search_value_carid = '540123198506025515'
        self.dr.find_element_by_xpath('//*[@id="idNumber"]').send_keys(search_value_carid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_carid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[2]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text,'校验删除是否成功')
        print('人口管理-部局七类库-三非人员：删除功能正常')


if __name__=='__main__':
    unittest.main()





