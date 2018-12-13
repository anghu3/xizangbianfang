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
from public_package.pubilc_package import TESTCASE
from public_package.pubilc_package import sheet_setting, search, reset, currMenupath, page_title, goback, saveBtn,sheet_menu,sheet_prompt_message
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
sheet=excel.sheet_by_name('人口房屋')

class TESTCAST_RKFW(TESTCASE):

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

    def rkfw_search(self):
        self.login(login_name,login_password)
        time.sleep(5)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,6,7)[0]).click()
        time.sleep(2)
        self.assertEqual('人口管理', self.dr.find_element_by_xpath(currMenupath).text, '人口管理')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,6,7)[0]).click()
        time.sleep(2)
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,6,7)[0]).click()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('房屋信息列表', self.dr.find_element_by_xpath(page_title).text,
                         '人口房屋')

    def test01_rkfw_search_name(self):
        self.rkfw_search()
        search_value_name=sheet.col_values(1,0,1)[0]
        name_path=sheet.col_values(1,1,2)[0]
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath(name_path).send_keys(search_value_name)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 1
        self.pagination_num(paginal_number, search_value_name, column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(name_path).get_attribute('value'),
                            '姓名-重置功能异常')
        print('人口管理-人员基本信息-人口房屋：姓名条件查询功能正常')

    def test02_rkfw_search_carid(self):
        self.rkfw_search()
        search_value_carid=sheet.col_values(1,2,3)[0]
        carid_path=sheet.col_values(1,3,4)[0]
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath(carid_path).send_keys(search_value_carid)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 2
        self.pagination_num(paginal_number, search_value_carid, column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(carid_path).get_attribute('value'),
                            '房主证件号码-重置功能异常')
        print('人口管理-人员基本信息-人口房屋：房主证件号码条件查询功能正常')

    def test03_rkfw_search_jlx(self):
        self.rkfw_search()
        search_value_jlx=sheet.col_values(1,4,5)[0]
        jlx_path=sheet.col_values(1,5,6)[0]
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath(jlx_path).send_keys(search_value_jlx)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 9
        self.pagination_num(paginal_number, search_value_jlx, column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('',self.dr.find_element_by_xpath(jlx_path).get_attribute('value'),
                            '街路巷-重置功能异常')
        print('人口管理-人员基本信息-人口房屋：街路巷条件查询功能正常')

    def test04_rkfw_searh_mlp(self):
        self.rkfw_search()
        search_value_mpl=sheet.col_values(1,6,7)[0]
        mpl_path=sheet.col_values(1,7,8)[0]
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath(mpl_path).send_keys(search_value_mpl)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 10
        self.pagination_num(paginal_number, search_value_mpl, column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('',self.dr.find_element_by_xpath(mpl_path).get_attribute('value'),
                            '门派楼-重置功能异常')
        print('人口管理-人员基本信息-人口房屋：门楼牌条件查询功能正常')

    def test05_rkfw_search_xz(self):
        self.rkfw_search()
        search_value_xz=sheet.col_values(1,8,9)[0]
        xz_path=sheet.col_values(1,9,10)[0]
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath(xz_path).send_keys(search_value_xz)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        column = 11
        self.pagination_num(paginal_number, search_value_xz, column)
        # self.dr.find_element_by_xpath('//*[@id="reset"]').click()
        # self.dr.implicitly_wait(10)
        # self.dr.find_element_by_xpath(search).click()
        # time.sleep(5)
        # self.assertEqual('', self.dr.find_element_by_xpath(xz_path).get_attribute('value'),
        #                     '详址-重置功能异常')
        print('人口管理-人员基本信息-人口房屋：详址条件查询功能正常')

    def test06_rkfw_search_all(self):
        self.rkfw_search()
        search_value_name = sheet.col_values(1, 0, 1)[0]
        name_path = sheet.col_values(1, 1, 2)[0]
        search_value_carid = sheet.col_values(1, 2, 3)[0]
        carid_path = sheet.col_values(1, 3, 4)[0]
        search_value_jlx = sheet.col_values(1, 4, 5)[0]
        jlx_path = sheet.col_values(1, 5, 6)[0]
        search_value_mpl = sheet.col_values(1, 6, 7)[0]
        mpl_path = sheet.col_values(1, 7, 8)[0]
        search_value_xz = sheet.col_values(1, 8, 9)[0]
        xz_path = sheet.col_values(1, 9, 10)[0]
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath(name_path).send_keys(search_value_name)
        self.dr.find_element_by_xpath(carid_path).send_keys(search_value_carid)
        self.dr.find_element_by_xpath(jlx_path).send_keys(search_value_jlx)
        self.dr.find_element_by_xpath(mpl_path).send_keys(search_value_mpl)
        self.dr.find_element_by_xpath(xz_path).send_keys(search_value_xz)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        self.pagination_num(paginal_number, search_value_name, 1)
        self.pagination_num(paginal_number, search_value_carid, 2)
        self.pagination_num(paginal_number, search_value_jlx, 9)
        self.pagination_num(paginal_number, search_value_mpl, 10)
        self.pagination_num(paginal_number, search_value_xz, 11)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(name_path).get_attribute('value'),
                         '姓名-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(carid_path).get_attribute('value'),
                         '房主证件号码-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(jlx_path).get_attribute('value'),
                         '街路巷-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(mpl_path).get_attribute('value'),
                         '门派楼-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(xz_path).get_attribute('value'),
                         '详址-重置功能异常')
        print('人口管理-人员基本信息-人口房屋：条件查询功能正常')

    def test07_rkfw_edit(self):
        self.rkfw_search()


if __name__ == '__main__':
    unittest.main()
