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
from public_package.pubilc_package import sheet_setting, search, reset, currMenupath, page_title, goback, saveBtn,sheet_menu,sheet_prompt_message
from public_package.pubilc_package import TESTCASE
import HTMLTestRunner
import xlrd
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

xlsfile = r'F:\pythonkeys\自动化测试\lasa\CLGL.xlsx'
excel = xlrd.open_workbook(xlsfile)
global sheet
sheet = excel.sheet_by_name('被盗车辆信息')

class TESTCAST_BEIDAOCHELIANG(TESTCASE):
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

    def beidaocheliang_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,35,36)[0]).click()
        time.sleep(2)
        self.assertEqual('车辆管理',self.dr.find_element_by_xpath(currMenupath).text,'校验车辆管理菜单')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,35,36)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,35,36)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(3)
        self.assertEqual('盗抢车辆列表',self.dr.find_element_by_xpath(page_title).text,'被盗车辆信息')

    def test01_beidaocheliang_search_hmhp(self):
        self.beidaocheliang_search()
        search_value_hmhp=sheet.col_values(1,0,1)[0]
        hmhp_path=sheet.col_values(1,1,2)[0]
        self.dr.find_element_by_xpath(hmhp_path).send_keys(search_value_hmhp)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        column = 2
        self.pagination_num(paginal_number,search_value_hmhp,column)
        self.dr.find_element_by_xpath(reset).click()
        time.sleep(1)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(1)
        self.assertEqual('',self.dr.find_element_by_xpath(hmhp_path).get_attribute('value'),'号码号牌-重置功能异常')


    def test02_beidaocheliang_details(self):
        self.beidaocheliang_search()
        search_value_hmhp = sheet.col_values(1, 0, 1)[0]
        hmhp_path = sheet.col_values(1, 1, 2)[0]
        self.dr.find_element_by_xpath(hmhp_path).send_keys(search_value_hmhp)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 2
        self.pagination_num(paginal_number, search_value_hmhp, column)
        search_value_hplx=self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]').text
        search_value_ajbm=self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[4]').text
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/a').click()
        self.assertEqual(search_value_hmhp,self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[1]/div[2]').text,'校验详情页面车牌号')
        self.assertEqual(search_value_hplx,self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[1]/div[2]').text,'校验详情页面号牌类型')
        self.assertEqual(search_value_ajbm,self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[2]/div[2]').text,'校验详情页面案件编号')
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('盗抢车辆列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text, '校验返回功能')
        print('车辆管理-被盗车辆信息：号码号牌条件查询和详情功能正常')

if __name__ == '__main__':
    unittest.main()