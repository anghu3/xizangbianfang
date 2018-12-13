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
from public_package.pubilc_package import sheet_setting, search, reset, currMenupath, page_title, goback, saveBtn,sheet_menu,sheet_prompt_message
from public_package.pubilc_package import TESTCASE
import xlrd
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

xlsfile = r'F:\pythonkeys\自动化测试\lasa\RKGL.xls'
excel = xlrd.open_workbook(xlsfile)
global sheet
sheet = excel.sheet_by_name('边防证办理情况')

class TESTCAST_BFZ(TESTCASE):

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
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,2,3)[0]).click()
        time.sleep(2)
        self.assertEqual('人口管理', self.dr.find_element_by_xpath(sheet_setting.col_values(0,1,2)[0]).text, '人口管理')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,2,3)[0]).click()
        time.sleep(2)
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,2,3)[0]).click()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('边防证列表', self.dr.find_element_by_xpath(sheet_setting.col_values(1,1,2)[0]).text,
                         '边防证办理情况')

    def test01_bfz_search_name(self):
        self.bfz_search()
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath(sheet.col_values(1,1,2)[0]).send_keys(sheet.col_values(1,0,1)[0])
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 2
        self.pagination_num(paginal_number,sheet.col_values(1,0,1)[0],column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1, 1, 2)[0]).get_attribute('value'),
                         '姓名-重置功能异常')
        print('人口管理-边防证办理情况：姓名条件查询功能正常')

    def test02_bfz_search_cardid(self):
        self.bfz_search()
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath(sheet.col_values(1,3,4)[0]).send_keys(sheet.col_values(1,2,3)[0])
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 3
        self.pagination_num(paginal_number, sheet.col_values(1, 2, 3)[0], column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1, 3, 4)[0]).get_attribute('value'),
                         '身份证号码-重置功能异常')
        print('人口管理-边防证办理情况：身份证号条件查询功能正常')

    def test03_bfz_search_passportCode(self):
        self.bfz_search()
        self.dr.find_element_by_xpath(sheet.col_values(1,5,6)[0]).send_keys(sheet.col_values(1,4,5)[0])
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 4
        self.pagination_num(paginal_number, sheet.col_values(1, 4, 5)[0], column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1, 5, 6)[0]).get_attribute('value'),
                         '姓名-重置功能异常')
        print('人口管理-边防证办理情况：通行证编号条件查询功能正常')

    def test04_bfz_search_orgName(self):
        self.bfz_search()
        option_chioce = Select(self.dr.find_element_by_xpath(sheet.col_values(1,7,8)[0]))
        for i in range(0, 28):
            option_chioce.select_by_index(i)
            self.dr.find_element_by_xpath(search).click()
            time.sleep(2)
        print('人口管理-边防证办理情况：办理单位条件查询功能正常')

    def test05_bfz_search_time(self):
        self.bfz_search()
        self.dr.find_element_by_xpath(sheet.col_values(1,9,10)[0]).send_keys(sheet.col_values(1,8,9)[0])
        self.dr.find_element_by_xpath(sheet.col_values(1,11,12)[0]).send_keys(sheet.col_values(1,10,11)[0])
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 8
        self.pagination_num(paginal_number, sheet.col_values(1, 8, 9)[0], column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1, 9, 10)[0]).get_attribute('value'),
                         '开始日期-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1, 11, 12)[0]).get_attribute('value'),
                         '结束日期-重置功能异常')
        print('人口管理-边防证办理情况：时间条件查询功能正常')

    def test06_bfz_search_all(self):
        self.bfz_search()
        self.dr.find_element_by_xpath(sheet.col_values(1, 1, 2)[0]).send_keys(sheet.col_values(1, 0, 1)[0])
        self.dr.find_element_by_xpath(sheet.col_values(1, 3, 4)[0]).send_keys(sheet.col_values(1, 2, 3)[0])
        self.dr.find_element_by_xpath(sheet.col_values(1, 5, 6)[0]).send_keys(sheet.col_values(1, 4, 5)[0])
        self.dr.find_element_by_xpath(sheet.col_values(1, 9, 10)[0]).send_keys(sheet.col_values(1, 8, 9)[0])
        self.dr.find_element_by_xpath(sheet.col_values(1, 11, 12)[0]).send_keys(sheet.col_values(1, 10, 11)[0])
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        self.pagination_num(paginal_number, sheet.col_values(1, 0, 1)[0], 2)
        self.pagination_num(paginal_number, sheet.col_values(1, 2, 3)[0], 3)
        self.pagination_num(paginal_number, sheet.col_values(1, 4, 5)[0], 4)
        self.pagination_num(paginal_number, sheet.col_values(1, 8, 9)[0], 8)
        self.pagination_num(paginal_number, sheet.col_values(1, 10, 11)[0], 8)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1, 1, 2)[0]).get_attribute('value'),
                         '姓名-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1, 3, 4)[0]).get_attribute('value'),
                         '身份证号码-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1, 5, 6)[0]).get_attribute('value'),
                         '姓名-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1, 9, 10)[0]).get_attribute('value'),
                         '开始日期-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1, 11, 12)[0]).get_attribute('value'),
                         '结束日期-重置功能异常')

if __name__=='__main__':
    unittest.main()