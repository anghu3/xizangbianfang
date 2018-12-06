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
sheet = excel.sheet_by_name('自定义车辆')

class TESTCAST_ZIDINGYICHELIANG(TESTCASE):
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

    def zidingyicheliang_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,33,34)[0]).click()
        time.sleep(2)
        self.assertEqual('车辆管理',self.dr.find_element_by_xpath(currMenupath).text,'校验车辆管理菜单')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,33,34)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,33,34)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(3)
        self.assertEqual('自定义车辆列表',self.dr.find_element_by_xpath(page_title).text,'校验自定义车辆菜单')

    def test01_zidingyicheliang_add(self):
        self.zidingyicheliang_search()
        add_value_cphm=sheet.col_values(1,0,1)[0]
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        self.dr.find_element_by_xpath('//*[@id="vehicleNo"]').send_keys(add_value_cphm)
        self.dr.find_element_by_xpath('//*[@id="veForm"]/div[1]/div[2]/a/span').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="monitorReason"]').send_keys(sheet.col_values(1,2,3)[0])
        self.dr.find_element_by_xpath('//*[@id="modifyBy"]').send_keys(sheet.col_values(1,3,4)[0])
        self.dr.find_element_by_xpath('//*[@id="monitorUnit"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_46_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_48_span"]').click()
        self.dr.find_element_by_xpath(saveBtn).click()
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        time.sleep(1)
        self.assertEqual(sheet_prompt_message.col_values(1, 1, 2)[0],
                         self.dr.find_element_by_xpath('//*[@id="gritter-item-1"]/div[2]/div[2]/p').text, '新增成功提示信息校验')
        print('车辆管理-自定义车辆：新增功能正常')

    def test02_zidingyicheliang_search_cphm(self):
        self.zidingyicheliang_search()
        search_value_cphm=sheet.col_values(1,0,1)[0]
        cphm_path=sheet.col_values(1,1,2)[0]
        self.dr.find_element_by_xpath(cphm_path).send_keys(search_value_cphm)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number=self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        column=3
        self.pagination_num(paginal_number,search_value_cphm,column)
        self.dr.find_element_by_xpath(reset).click()
        time.sleep(2)
        self.dr.find_element_by_xpath(search).click()
        self.assertEqual('',self.dr.find_element_by_xpath(cphm_path).get_attribute('value'),'车牌号码-重置功能异常')
        print('车辆管理-自定义车辆：车牌条件查询功能正常')

    def test03_zidingyicheliang_details(self):
        self.zidingyicheliang_search()
        search_value_cphm = sheet.col_values(1, 0, 1)[0]
        cphm_path = sheet.col_values(1, 1, 2)[0]
        self.dr.find_element_by_xpath(cphm_path).send_keys(search_value_cphm)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 3
        self.pagination_num(paginal_number, search_value_cphm, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[11]/a').click()
        self.assertEqual(sheet.col_values(1,0,1)[0],self.dr.find_element_by_xpath('//*[@id="vehicleNo"]').get_attribute('value'),'详情页面车牌号码校验异常')
        print('车辆管理-自定义车辆：详情功能正常')

    def test04_zidingyicheliang_edit(self):
        self.zidingyicheliang_search()
        search_value_cphm = sheet.col_values(1, 0, 1)[0]
        cphm_path = sheet.col_values(1, 1, 2)[0]
        self.dr.find_element_by_xpath(cphm_path).send_keys(search_value_cphm)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 3
        self.pagination_num(paginal_number, search_value_cphm, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[11]/a').click()
        self.dr.find_element_by_xpath('//*[@id="monitorReason"]').send_keys(sheet.col_values(2, 2, 3)[0])
        self.dr.find_element_by_xpath('//*[@id="modifyBy"]').send_keys(sheet.col_values(2, 3, 4)[0])
        self.dr.find_element_by_xpath(saveBtn).click()
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        time.sleep(1)
        self.assertEqual(sheet_prompt_message.col_values(1, 1, 2)[0],
                         self.dr.find_element_by_xpath('//*[@id="gritter-item-1"]/div[2]/div[2]/p').text, '新增成功提示信息校验')
        print('车辆管理-自定义车辆：新增功能正常')

    def test05_zidingyicheliang_delete(self):
        self.zidingyicheliang_search()
        search_value_cphm = '藏DK0700'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value_cphm)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_cphm, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text,'校验删除功能是否正常')
        print('车辆管理-自定义车辆：删除功能正常')

if __name__ == '__main__':
    unittest.main()