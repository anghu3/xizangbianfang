# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 14:11:17 2018

@author: PCCC
"""

import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import Select
import time
import os
import re
import sys
from public_package.pubilc_package import url,login_name,login_name_test,login_password,login_password_test
from public_package.pubilc_package import sheet_setting, search, reset, currMenupath, page_title, goback, saveBtn,sheet_menu,sheet_prompt_message,work_space
from public_package.pubilc_package import TESTCASE
import xlrd
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

xlsfile=work_space+r'\\'+sheet_menu.col_values(6,3,4)[0]
excel = xlrd.open_workbook(xlsfile)
global sheet
sheet = excel.sheet_by_name('常住人口')

class TESTCAST_CZRK(TESTCASE):

    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()

    def tearDown(self):
        # print("脚本执行完成")
        self.dr.quit()

    def bj(self,x,y):
        if x==y:
            return True
        else:
            return False

    def login(self, username, password):
        self.dr.get(url)
        self.dr.find_element_by_id('vv').send_keys(username)
        self.dr.find_element_by_xpath('//*[@id="login_ff"]/div[2]/input').send_keys(password)
        self.dr.find_element_by_xpath('//*[@id="login_ff"]/a').click()

    def czrk_search(self):
        self.login(login_name,login_password)
        time.sleep(5)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,3,4)[0]).click()
        time.sleep(2)
        self.assertEqual('人口管理', self.dr.find_element_by_xpath(currMenupath).text, '人口管理')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,3,4)[0]).click()
        time.sleep(2)
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,3,4)[0]).click()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('常住人口', self.dr.find_element_by_xpath(page_title).text,
                         '常住人口')

    def test01_czrk_search_name(self):
        self.czrk_search()
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath(sheet.col_values(1,1,2)[0]).send_keys(sheet.col_values(1,0,1)[0])
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(20)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 3
        self.pagination_num(paginal_number,sheet.col_values(1,0,1)[0],column)
        self.dr.find_element_by_xpath(reset).click()
        time.sleep(5)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1, 1, 2)[0]).get_attribute('value'),
                         '姓名-重置功能异常')
        print('人口管理-人员基本信息-常住人口:姓名条件查询功能正常')

    def test02_czrk_search_cardid(self):
        self.czrk_search()
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath(sheet.col_values(1,3,4)[0]).send_keys(sheet.col_values(1,2,3)[0])
        self.dr.find_element_by_xpath(search).click()
        time.sleep(240)
        # WebDriverWait(self.dr, 240).until(
        #     self.bj(sheet.col_values(1, 2, 3)[0], self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text))
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 2
        self.pagination_num(paginal_number,sheet.col_values(1,2,3)[0],column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1, 3, 4)[0]).get_attribute('value'),
                         '身份证号码-重置功能异常')
        print('人口管理-人员基本信息-常住人口:身份证号条件查询功能正常')

    def test03_czrk_search_hh(self):
        self.czrk_search()
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath(sheet.col_values(1,5,6)[0]).send_keys(sheet.col_values(1,4,5)[0])
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 7
        self.pagination_num(paginal_number,sheet.col_values(1,4,5)[0],column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1, 5, 6)[0]).get_attribute('value'),
                         '户号-重置功能异常')
        print('人口管理-人员基本信息-常住人口:户号条件查询功能正常')

    def test04_czrk_search_hjdz(self):
        self.czrk_search()
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath(sheet.col_values(1,7,8)[0]).send_keys(sheet.col_values(1,6,7)[0])
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 9
        self.pagination_num(paginal_number, sheet.col_values(1, 6, 7)[0], column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1, 7, 8)[0]).get_attribute('value'),
                         '户籍地址-重置功能异常')
        print('人口管理-人员基本信息-常住人口:户籍地址条件查询功能正常')

    def test05_czrk_search_all(self):
        self.czrk_search()
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath(sheet.col_values(1, 1, 2)[0]).send_keys(sheet.col_values(1, 0, 1)[0])
        self.dr.find_element_by_xpath(sheet.col_values(1, 3, 4)[0]).send_keys(sheet.col_values(1, 2, 3)[0])
        self.dr.find_element_by_xpath(sheet.col_values(1, 5, 6)[0]).send_keys(sheet.col_values(1, 4, 5)[0])
        self.dr.find_element_by_xpath(sheet.col_values(1, 7, 8)[0]).send_keys(sheet.col_values(1, 6, 7)[0])
        self.dr.find_element_by_xpath(search).click()
        f=lambda a,b:a==b
        time.sleep(240)
        # WebDriverWait(self.dr,240).until(f(sheet.col_values(1,2,3)[0],self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text))
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        self.pagination_num(paginal_number, sheet.col_values(1, 0, 1)[0], 3)
        self.pagination_num(paginal_number, sheet.col_values(1, 2, 3)[0], 2)
        self.pagination_num(paginal_number, sheet.col_values(1, 4, 5)[0], 7)
        self.pagination_num(paginal_number, sheet.col_values(1, 6, 7)[0], 9)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1, 1, 2)[0]).get_attribute('value'),
                         '姓名-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1, 3, 4)[0]).get_attribute('value'),
                         '身份证号码-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1, 5, 6)[0]).get_attribute('value'),
                         '户号-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1, 7, 8)[0]).get_attribute('value'),
                         '户籍地址-重置功能异常')
        print('人口管理-人员基本信息-常住人口:条件查询功能正常')

    def test06_czrk_xiangqing(self):
        self.czrk_search()
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath(sheet.col_values(1, 1, 2)[0]).send_keys(sheet.col_values(1, 0, 1)[0])
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        name=self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]').text
        carid=self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        self.dr.implicitly_wait(30)
        self.assertEqual(name,self.dr.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/div/div[4]/div/div[2]').text,'详情信息校验')
        self.assertEqual(carid, self.dr.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div/div[2]/div/div[9]/div/div[2]').text, '详情信息校验')
        print('人口管理-人员基本信息-常住人口:详情功能正常')

if __name__ == '__main__':
    unittest.main()

