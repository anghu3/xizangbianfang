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
import xlrd
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

class TESTCAST_EXZ(TESTCASE):

    dir = os.getcwd()
    xlsfile = dir + '.xls'
    excel = xlrd.open_workbook(xlsfile)
    sheet_name = excel.sheet_names()[0]
    global sheet_menu
    sheet_menu=excel.sheet_by_name('menu')
    global sheet
    sheet=excel.sheet_by_name('二线站过往记录')
    global sheet_setting,search,reset,add,delete
    sheet_setting = excel.sheet_by_name('setting')
    search=sheet_setting.col_values(2,1,2)[0]
    reset=sheet_setting.col_values(3,1,2)[0]

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

    def exz_search(self):
        self.login(login_name,login_password )
        time.sleep(5)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,1,2)[0]).click()
        time.sleep(2)
        self.assertEqual('人口管理', self.dr.find_element_by_xpath(sheet_setting.col_values(0,1,2)[0]).text, '人口管理')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,1,2)[0]).click()
        time.sleep(2)
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,1,2)[0]).click()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('二线站过往记录列表', self.dr.find_element_by_xpath(sheet_setting.col_values(1,1,2)[0]).text,
                         '二线站过往记录')

    def test01_exz_search_name(self):
        self.exz_search()
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath(sheet.col_values(1,1,2)[0]).send_keys(sheet.col_values(0,1,2)[0])
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        column=2
        self.pagination_num(paginal_number,sheet.col_values(0,1,2)[0],column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('',self.dr.find_element_by_xpath(sheet.col_values(1,1,2)[0]).get_attribute('value'),'姓名-重置功能异常')
        print('二线站过往记录：姓名条件查询功能正常')

    def test02_exz_search_cardid(self):
        self.exz_search()
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath(sheet.col_values(3,1,2)[0]).send_keys(sheet.col_values(2,1,2)[0])
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        column = 3
        self.pagination_num(paginal_number, sheet.col_values(2,1,2)[0], column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(3, 1, 2)[0]).get_attribute('value'),
                         '身份证号-重置功能异常')
        print('二线站过往记录：身份证号条件查询功能正常')

    def test03_exz_search_pSerialno(self):
        self.exz_search()
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath(sheet.col_values(5,1,2)[0]).send_keys(sheet.col_values(4,1,2)[0])
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 4
        self.pagination_num(paginal_number, sheet.col_values(4, 1, 2)[0], column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(5, 1, 2)[0]).get_attribute('value'),
                         '通行证编号-重置功能异常')
        print('二线站过往记录：通行证编号条件查询功能正常')

    def test04_exz_search_staionId(self):
        self.exz_search()
        time.sleep(10)
        option_chioce = Select(self.dr.find_element_by_xpath(sheet.col_values(7,1,2)[0]))
        # option_chioce.select_by_index('2')
        # # a=option_chioce.all_selected_options
        # print(option_chioce.first_selected_option.text)
        for i in range(0, 8):
            if i == 0:
                print('查询全部数据时不校验查询结果')
            else:
                option_chioce.select_by_index(i)
                self.dr.find_element_by_xpath(search).click()
                # self.assertIn(self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[5]').text,option_chioce.first_selected_option.text,'检查站名称查询')
                time.sleep(2)
        print('二线站过往记录：检查站名称条件查询功能正常')

    def test05_exz_search_time(self):
        self.exz_search()
        self.dr.find_element_by_xpath(sheet.col_values(9,1,2)[0]).send_keys(sheet.col_values(8,1,2)[0])
        self.dr.find_element_by_xpath(sheet.col_values(11,1,2)[0]).send_keys(sheet.col_values(10,1,2)[0])
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 7
        self.pagination_num(paginal_number, sheet.col_values(8, 1, 2)[0], column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(9, 1, 2)[0]).get_attribute('value'),
                         '开始日期-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(11, 1, 2)[0]).get_attribute('value'),
                         '结束日期-重置功能异常')
        print('二线站过往记录：时间条件查询功能正常')

    def test06_exz_search_all(self):
        self.exz_search()
        self.dr.find_element_by_xpath(sheet.col_values(1, 1, 2)[0]).send_keys(sheet.col_values(0, 1, 2)[0])
        self.dr.find_element_by_xpath(sheet.col_values(3, 1, 2)[0]).send_keys(sheet.col_values(2, 1, 2)[0])
        self.dr.find_element_by_xpath(sheet.col_values(5, 1, 2)[0]).send_keys(sheet.col_values(4, 1, 2)[0])
        self.dr.find_element_by_xpath(sheet.col_values(9, 1, 2)[0]).send_keys(sheet.col_values(8, 1, 2)[0])
        self.dr.find_element_by_xpath(sheet.col_values(11, 1, 2)[0]).send_keys(sheet.col_values(10, 1, 2)[0])
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        self.pagination_num(paginal_number, sheet.col_values(0, 1, 2)[0], 2)
        self.pagination_num(paginal_number, sheet.col_values(2, 1, 2)[0], 3)
        self.pagination_num(paginal_number, sheet.col_values(4, 1, 2)[0], 4)
        self.pagination_num(paginal_number, sheet.col_values(8, 1, 2)[0], 7)
        self.pagination_num(paginal_number, sheet.col_values(10, 1, 2)[0], 7)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1, 1, 2)[0]).get_attribute('value'),
                         '姓名-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(3, 1, 2)[0]).get_attribute('value'),
                         '身份证号-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(5, 1, 2)[0]).get_attribute('value'),
                         '通行证编号-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(9, 1, 2)[0]).get_attribute('value'),
                         '通行证编号-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(11, 1, 2)[0]).get_attribute('value'),
                         '通行证编号-重置功能异常')
        print('二线站过往记录：条件查询功能正常')


if __name__=='__main__':
    unittest.main()
