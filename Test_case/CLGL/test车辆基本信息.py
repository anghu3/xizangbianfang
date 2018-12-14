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

xlsfile=work_space+r'\\'+sheet_menu.col_values(6,34,35)[0]
excel = xlrd.open_workbook(xlsfile)
global sheet
sheet = excel.sheet_by_name('车辆基本信息')

class TESTCAST_CHELIANGJIBENXINXI(TESTCASE):
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

    def cheliangjibenxinxi_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,34,35)[0]).click()
        time.sleep(2)
        self.assertEqual('车辆管理',self.dr.find_element_by_xpath(currMenupath).text,'校验车辆管理菜单')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,34,35)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,34,35)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(3)
        self.assertEqual('车辆信息列表',self.dr.find_element_by_xpath(page_title).text,'车辆信息')

    def test01_cheliangjibenxinxi_search_cphm(self):
        self.cheliangjibenxinxi_search()
        search_value_cphm=sheet.col_values(1,0,1)[0]
        cphm_path=sheet.col_values(1,1,2)[0]
        self.dr.find_element_by_xpath(cphm_path).send_keys(search_value_cphm)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number=self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column=2
        self.pagination_num(paginal_number,search_value_cphm,column)
        self.dr.find_element_by_xpath(reset).click()
        time.sleep(2)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(1)
        self.assertEqual('',self.dr.find_element_by_xpath(cphm_path).get_attribute('value'),'车牌号码-重置功能异常')
        print('车辆管理-车辆基本信息：车牌号码条件查询和详情功能正常')

    def test02_cheliangjibenxinxi_xiangqing(self):
        self.cheliangjibenxinxi_search()
        search_value_cphm=sheet.col_values(1,0,1)[0]
        cphm_path=sheet.col_values(1,1,2)[0]
        self.dr.find_element_by_xpath(cphm_path).send_keys(search_value_cphm)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number=self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column=2
        self.pagination_num(paginal_number,search_value_cphm,column)
        search_value_hpzl = self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]').text
        search_value_ower = self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[8]').text
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[11]/a').click()
        self.assertEqual(search_value_cphm,
                         self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div[2]').text,
                         '校验详情页面车牌号')
        self.assertEqual(search_value_hpzl,
                         self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]').text,
                         '校验详情页面车牌类型')
        self.assertEqual(search_value_ower,
                         self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[3]/div[2]').text,
                         '校验详情页面车辆所有人')
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('车辆信息列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text, '校验返回功能')
        print('车辆管理-车辆基本信息：详情功能正常')

if __name__ == '__main__':
    unittest.main()