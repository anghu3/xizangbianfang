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
from public_package.pubilc_package import sheet_setting, search, reset, currMenupath, page_title, goback, saveBtn,sheet_menu,sheet_prompt_message,work_space
from public_package.pubilc_package import TESTCASE
import HTMLTestRunner
import xlrd
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

xlsfile=work_space+r'\\'+sheet_menu.col_values(6,17,18)[0]
excel = xlrd.open_workbook(xlsfile)
global sheet
sheet = excel.sheet_by_name('肇事肇祸人员')

class TESTCAST_ZHAOSHI(TESTCASE):
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

    def zhaoshi_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,17,18)[0]).click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath(currMenupath).text, '人口管理')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,17,18)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,17,18)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('肇事肇祸人员列表', self.dr.find_element_by_xpath(page_title).text,
                         '肇事肇祸人员')

    def test01_zhaoshi_search_name(self):
        self.zhaoshi_search()
        search_value_name=sheet.col_values(1,0,1)[0]
        name_path=sheet.col_values(1,1,2)[0]
        self.dr.find_element_by_xpath(name_path).send_keys(search_value_name)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        column = 3
        self.pagination_num(paginal_number, search_value_name, column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(2)
        self.assertEqual('', self.dr.find_element_by_xpath(name_path).get_attribute('value'), '姓名-重置功能异常')
        print('人口管理-部局七类库-肇事肇祸人员:姓名条件查询功能正常')

    def test02_zhaoshi_search_cardid(self):
        self.zhaoshi_search()
        search_value_cardid=sheet.col_values(1,2,3)[0]
        cardid_path=sheet.col_values(1,3,4)[0]
        self.dr.find_element_by_xpath('//*[@id="sfzh"]').send_keys(search_value_cardid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 2
        self.pagination_num(paginal_number, search_value_cardid, column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(2)
        self.assertEqual('', self.dr.find_element_by_xpath(cardid_path).get_attribute('value'), '身份证号码-重置功能异常')
        print('人口管理-部局七类库-肇事肇祸人员:身份证号码条件查询功能正常')

    def test03_zhaoshi_search_all(self):
        self.zhaoshi_search()
        search_value_name = sheet.col_values(1, 0, 1)[0]
        name_path = sheet.col_values(1, 1, 2)[0]
        search_value_cardid = sheet.col_values(1, 2, 3)[0]
        cardid_path = sheet.col_values(1, 3, 4)[0]
        self.dr.find_element_by_xpath(name_path).send_keys(search_value_name)
        self.dr.find_element_by_xpath('//*[@id="sfzh"]').send_keys(search_value_cardid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(paginal_number, search_value_cardid, 2)
        self.pagination_num(paginal_number, search_value_name, 3)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(2)
        self.assertEqual('', self.dr.find_element_by_xpath(cardid_path).get_attribute('value'), '身份证号码-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(name_path).get_attribute('value'), '姓名-重置功能异常')
        print('人口管理-部局七类库-肇事肇祸人员:条件查询功能正常')

if __name__=='__main__':
    unittest.main()