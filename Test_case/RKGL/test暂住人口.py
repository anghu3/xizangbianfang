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
sheet = excel.sheet_by_name('暂住人口')

class TESTCAST_ZZRK(TESTCASE):

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

    def zzrk_search(self):
        self.login(login_name, login_password)
        time.sleep(5)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,4,5)[0]).click()
        time.sleep(2)
        self.assertEqual('人口管理', self.dr.find_element_by_xpath(currMenupath).text, '人口管理')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,4,5)[0]).click()
        time.sleep(2)
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,4,5)[0]).click()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('流动人口信息列表', self.dr.find_element_by_xpath(page_title).text,
                         '暂住人口')

    def test01_zzrk_search_name(self):
        self.zzrk_search()
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath(sheet.col_values(1,1,2)[0]).send_keys(sheet.col_values(1,0,1)[0])
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 2
        self.pagination_num(paginal_number, sheet.col_values(1, 0, 1)[0], column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1, 1, 2)[0]).get_attribute('value'),
                         '姓名-重置功能异常')
        print('人口管理-人员基本信息-暂住人口:姓名条件查询功能正常')

    def test02_zzrk_search_cardid(self):
        self.zzrk_search()
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath(sheet.col_values(1,3,4)[0]).send_keys(sheet.col_values(1,2,3)[0])
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
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
        print('人口管理-人员基本信息-暂住人口:身份证号条件查询功能正常')

    def test03_zzrk_search_tempResidPermitNo(self):
        self.zzrk_search()
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath(sheet.col_values(1,5,6)[0]).send_keys(sheet.col_values(1,4,5)[0])
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 7
        self.pagination_num(paginal_number, sheet.col_values(1, 4, 5)[0], column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1,5,6)[0]).get_attribute('value'),
                            '居住证编号-重置功能异常')
        print('人口管理-人员基本信息-暂住人口:居住证编号条件查询功能正常')

    def test04_zzrk_search_tempAddrRegDetailAddr(self):
        self.zzrk_search()
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath(sheet.col_values(1,7,8)[0]).send_keys(sheet.col_values(1,6,7)[0])
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 9
        self.pagination_num(paginal_number, sheet.col_values(1, 6, 7)[0], column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1,7,8)[0]).get_attribute('value'),
                            '暂住地址-重置功能异常')
        print('人口管理-人员基本信息-暂住人口:暂住地址条件查询功能正常')

    def test05_zzrk_search_isProvInOut(self):
        self.zzrk_search()
        isProvInOut = Select(self.dr.find_element_by_xpath('//*[@id="form"]/div[5]/div/select'))
        for i in range(1,3):
            isProvInOut.select_by_index(i)
            search_value_isProvInOut=isProvInOut.all_selected_options[0].text
            self.dr.find_element_by_xpath(search).click()
            self.dr.switch_to.default_content()
            time.sleep(5)
            self.dr.switch_to.frame('iframeb')
            paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
            column = 12
            self.pagination_num(paginal_number,search_value_isProvInOut,column)
            self.dr.find_element_by_xpath(reset).click()
            self.dr.implicitly_wait(10)
            self.dr.find_element_by_xpath(search).click()
            time.sleep(5)
            self.assertEqual('--全部--', self.dr.find_element_by_xpath('//*[@id="form"]/div[5]/div/select/option[1]').get_attribute('text'),
                                 '区域-重置功能异常')
        print('人口管理-人员基本信息-暂住人口:区域条件查询功能正常')

    def test06_zzrk_search_liveState(self):
        self.zzrk_search()
        liveState = Select(self.dr.find_element_by_xpath('//*[@id="form"]/div[6]/div/select'))
        for i in range(1,3):
            liveState.select_by_index(i)
            search_value_liveState=liveState.all_selected_options[0].text
            # print(search_value_liveState)
            self.dr.find_element_by_xpath(search).click()
            self.dr.switch_to.default_content()
            time.sleep(5)
            self.dr.switch_to.frame('iframeb')
            paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
            column = 13
            self.pagination_num(paginal_number,search_value_liveState,column)
            self.dr.find_element_by_xpath(reset).click()
            self.dr.implicitly_wait(10)
            self.dr.find_element_by_xpath(search).click()
            time.sleep(5)
            self.assertEqual('--全部--',self.dr.find_element_by_xpath('//*[@id="form"]/div[6]/div/select/option[1]').get_attribute('text'),'居住状态-重置功能异常')
        print('人口管理-人员基本信息-暂住人口:居住状态条件查询功能正常')

    def test07_zzrk_search_xiangqing(self):
        self.zzrk_search()
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(sheet.col_values(1,0,1)[0])
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        search_value_carid=self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]').text
        self.assertEqual(sheet.col_values(1,0,1)[0], self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text, '姓名条件查询')
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[14]/a').click()
        self.dr.implicitly_wait(30)
        self.assertEqual(sheet.col_values(1,0,1)[0],self.dr.find_element_by_xpath('//*[@id="xm"]').text,'详情信息校验')
        self.assertEqual(sheet.col_values(1,2,3)[0],self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').get_attribute('value'),'校验详情')
        print('人口管理-人员基本信息-暂住人口:详情功能正常')

    def test08_zzrk_update(self):
        self.zzrk_search()
        search_value_name=sheet.col_values(1,0,1)[0]
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value_name)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        search_value_carid=sheet.col_values(1,2,3)[0]
        self.assertEqual(search_value_name, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text, '姓名条件查询')
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[14]/a').click()
        self.dr.implicitly_wait(30)
        self.assertEqual(search_value_name,self.dr.find_element_by_xpath('//*[@id="xm"]').text,'详情信息校验')
        self.assertEqual(search_value_carid,self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').get_attribute('value'),'校验详情')
        Select(self.dr.find_element_by_xpath('//*[@id="tj"]/div/div/div[2]/div[1]/div[1]/div[1]/select')).select_by_value('22')
        self.dr.find_element_by_xpath('//*[@id="tj"]/div/div/div[2]/div[3]/a').click()
        time.sleep(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value_name)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value_name, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text,
                         '姓名条件查询')
        self.assertEqual('长子',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[8]').text,'校验更新是否正常')
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[14]/a').click()
        Select(self.dr.find_element_by_xpath('//*[@id="tj"]/div/div/div[2]/div[1]/div[1]/div[1]/select')).select_by_value('01')
        self.dr.find_element_by_xpath('//*[@id="tj"]/div/div/div[2]/div[3]/a').click()
        print('人口管理-人员基本信息-暂住人口:编辑功能正常')

if __name__=='__main__':
    unittest.main()
