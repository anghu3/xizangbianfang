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
sheet = excel.sheet_by_name('驾驶员信息')

class TESTCAST_JSYXX(TESTCASE):

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

    def jsyxx_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,5,6)[0]).click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath(currMenupath).text, '人口管理')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,5,6)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,5,6)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('驾驶员信息列表', self.dr.find_element_by_xpath(page_title).text,
                         '驾驶员信息')

    def test01_jsyxx_search_name(self):
        self.jsyxx_search()
        search_value_name = sheet.col_values(1,0,1)[0]
        name_path=sheet.col_values(1,1,2)[0]
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath(name_path).send_keys(search_value_name)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(2)
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 2
        self.pagination_num(paginal_number,search_value_name,column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(name_path).get_attribute('value'),
                            '姓名-重置功能异常')
        print('人口管理-人员基本信息-驾驶员信息:姓名条件查询功能正常')

    def test02_jsyxx_search_cardid(self):
        self.jsyxx_search()
        search_value_idcard = sheet.col_values(1,2,3)[0]
        idcard_path=sheet.col_values(1,3,4)[0]
        self.dr.find_element_by_xpath(idcard_path).send_keys(search_value_idcard)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(180)
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 3
        self.pagination_num(paginal_number, search_value_idcard, column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(idcard_path).get_attribute('value'),
                            '身份证-重置功能异常')
        print('人口管理-人员基本信息-驾驶员信息:姓名条件查询功能正常')

    def test03_jsyxx_search_all(self):
        self.jsyxx_search()
        search_value_idcard = sheet.col_values(1, 2, 3)[0]
        idcard_path = sheet.col_values(1, 3, 4)[0]
        search_value_name = sheet.col_values(1, 0, 1)[0]
        name_path = sheet.col_values(1, 1, 2)[0]
        self.dr.find_element_by_xpath(name_path).send_keys(search_value_name)
        self.dr.find_element_by_xpath(idcard_path).send_keys(search_value_idcard)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(180)
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        self.pagination_num(paginal_number, search_value_idcard, 3)
        self.pagination_num(paginal_number,search_value_name,2)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(idcard_path).get_attribute('value'),
                            '重置功能')
        self.assertEqual('', self.dr.find_element_by_xpath(name_path).get_attribute('value'),
                         '姓名-重置功能异常')
        print('人口管理-人员基本信息-驾驶员信息:条件查询功能正常')


if __name__ == '__main__':
    unittest.main()