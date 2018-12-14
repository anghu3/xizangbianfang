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

xlsfile=work_space+r'\\'+sheet_menu.col_values(6,36,37)[0]
excel = xlrd.open_workbook(xlsfile)
global sheet
sheet = excel.sheet_by_name('二线站车辆过往记录')

class TESTCAST_ERXIANZHANCHELIANG(TESTCASE):
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

    def erxianzhancheliang_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,36,37)[0]).click()
        time.sleep(2)
        self.assertEqual('车辆管理',self.dr.find_element_by_xpath(currMenupath).text,'校验车辆管理菜单')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,36,37)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,36,37)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(3)
        self.assertEqual('二线站过往记录列表',self.dr.find_element_by_xpath(page_title).text,'二线站车辆过往记录')

    def test1_erxianzhancheliang_search_cphm(self):
        self.erxianzhancheliang_search()
        time.sleep(30)
        search_vale_cphm='青A7S171'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_vale_cphm)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 2
        self.pagination_num(paginal_number, search_vale_cphm, column)
        print('车辆管理-二线站过往车辆：车牌号码条件查询功能正常')

    def test2_erxianzhancheliang_jcz(self):
        self.erxianzhancheliang_search()
        time.sleep(30)
        option_chioce=Select(self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/div/select'))
        for i in range(0, 8):
            if i == 0:
                print('查询全部数据时不校验查询结果')
            else:
                option_chioce.select_by_index(i)
                search_value=option_chioce.first_selected_option.text
                self.dr.find_element_by_xpath('//*[@id="search"]').click()
                time.sleep(2)
                # self.dr.switch_to.default_content()
                # time.sleep(3)
                # self.dr.switch_to.frame('iframeb')
                # paginal_number = self.dr.find_element_by_xpath(
                #     '/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
                # column = 3
                # try:
                #     # self.assertIsNone(self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text,'校验是否有数据')
                #     self.pagination_num(paginal_number, search_value, column)
                # except IOError:
                #     print('查询数据为空')
        print('车辆管理-二线站过往车辆：检查站名称条件查询功能正常')

    def test3_erxianzhancheliang_search_date(self):
        self.erxianzhancheliang_search()
        time.sleep(30)
        search_vale_date='2018-04-02'
        self.dr.find_element_by_xpath('//*[@id="startDate"]').clear()
        self.dr.find_element_by_xpath('//*[@id="endDate"]').clear()
        self.dr.find_element_by_xpath('//*[@id="startDate"]').send_keys(search_vale_date)
        self.dr.find_element_by_xpath('//*[@id="endDate"]').send_keys(search_vale_date)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_vale_date, column)
        print('车辆管理-二线站过往车辆：时间条件查询功能正常')

if __name__ == '__main__':
    unittest.main()