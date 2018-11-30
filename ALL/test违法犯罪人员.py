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
sheet = excel.sheet_by_name('违法犯罪人员')

class TESTCAST_WFFZRY(unittest.TestCase):

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

    def wfzry_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,8,9)[0]).click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath(currMenupath).text, '人口管理')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,8,9)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(4,8,9)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('违法犯罪人员', self.dr.find_element_by_xpath(page_title).text,
                         '违法犯罪人员')

    def test1_wffzry_search_cardid(self):
        self.wfzry_search()
        search_value_cardid = sheet.col_values(1,2,3)[0]
        cardid_path=sheet.col_values(1,3,4)[0]
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value_cardid)
        self.dr.find_element_by_xpath(search).click()
        self.dr.implicitly_wait(240)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 3
        self.pagination_num(paginal_number, search_value_cardid, column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        self.assertEqual('',self.dr.find_element_by_xpath(cardid_path).get_attribute('value'),'身份证号-重置功能异常')
        print('人口管理-违法犯罪人员：身份证号码条件查询功能正常')

    def test2_wffzry_search_xiangqing(self):
        self.wfzry_search()
        name=sheet.col_values(1,0,1)[0]
        search_value_cardid = sheet.col_values(1, 2, 3)[0]
        cardid_path = sheet.col_values(1, 3, 4)[0]
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value_cardid)
        self.dr.find_element_by_xpath(search).click()
        self.dr.implicitly_wait(240)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[11]/a').click()
        time.sleep(2)
        self.assertEqual(search_value_cardid,self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').get_attribute('value'),'校验详情页面身份证号')
        self.assertEqual(name,self.dr.find_element_by_xpath('//*[@id="xm"]').text,'校验详情页面姓名')
        print('人口管理-违法犯罪人员：详情功能正常')

if __name__ == '__main__':
    unittest.main()