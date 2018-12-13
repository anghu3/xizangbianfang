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
sheet = excel.sheet_by_name('寺庙')

class TESTCAST_SIMIAO(TESTCASE):
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

    def simiao_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,25,26)[0]).click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath(currMenupath).text, '人口管理')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,25,26)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,25,26)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('寺庙列表', self.dr.find_element_by_xpath(page_title).text,
                         '寺庙')

    def test01_simiao_add(self):
        self.simiao_search()
        search_add_name=sheet.col_values(1,0,1)[0]
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        self.dr.find_element_by_xpath('//*[@id="name"]').send_keys(search_add_name)
        self.dr.find_element_by_xpath('//*[@id="location"]').send_keys(sheet.col_values(1,2,3)[0])
        Select(self.dr.find_element_by_xpath('//*[@id="category"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="compilingCount"]').send_keys(sheet.col_values(1,8,9)[0])
        Select(self.dr.find_element_by_xpath('//*[@id="rank"]')).select_by_value('2')
        self.dr.find_element_by_xpath('//*[@id="realCount"]').send_keys(sheet.col_values(1,9,10)[0])
        Select(self.dr.find_element_by_xpath('//*[@id="police"]')).select_by_value(sheet.col_values(1,12,13)[0])
        self.dr.find_element_by_xpath('//*[@id="contact"]').send_keys(sheet.col_values(1,10,11)[0])
        self.dr.find_element_by_xpath('//*[@id="remark"]').send_keys(sheet.col_values(1,11,12)[0])
        self.dr.find_element_by_xpath(saveBtn).click()
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        time.sleep(1)
        self.assertEqual(sheet_prompt_message.col_values(1, 4, 5)[0],
                         self.dr.find_element_by_xpath('//*[@id="gritter-item-1"]/div[2]/div[2]/p').text, '新增成功提示信息校验')
        print('人口管理-701数据库-寺庙：新增功能正常')

    def test02_simiao_search_name(self):
        self.simiao_search()
        search_value_name=sheet.col_values(1,0,1)[0]
        name_path=sheet.col_values(1,1,2)[0]
        self.dr.find_element_by_xpath(name_path).send_keys(search_value_name)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        column = 2
        self.pagination_num(paginal_number, search_value_name, column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(2)
        self.assertEqual('', self.dr.find_element_by_xpath(name_path).get_attribute('value'), '姓名-重置功能异常')
        print('人口管理-701数据库-寺庙：姓名条件查询功能正常')

    def test03_simiao_search_address(self):
        self.simiao_search()
        search_value_address = sheet.col_values(1,2,3)[0]
        address_path=sheet.col_values(1,3,4)[0]
        self.dr.find_element_by_xpath(address_path).send_keys(search_value_address)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        column = 3
        self.pagination_num(paginal_number, search_value_address, column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(2)
        self.assertEqual('', self.dr.find_element_by_xpath(address_path).get_attribute('value'), '所在地-重置功能异常')
        print('人口管理-701数据库-寺庙：所在地条件查询功能正常')

    def test04_simiao_search_category(self):
        self.simiao_search()
        search_value_category = sheet.col_values(1,4,5)[0]
        category_path=sheet.col_values(1,5,6)[0]
        Select(self.dr.find_element_by_xpath(category_path)).select_by_value('1')
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        column = 6
        self.pagination_num(paginal_number, search_value_category, column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(2)
        self.assertEqual('', self.dr.find_element_by_xpath('//*[@id="category"]/option[1]').text, '教派类别-重置功能异常')
        print('人口管理-701数据库-寺庙：教派类别条件查询功能正常')

    def test05_simiao_search_rank(self):
        self.simiao_search()
        search_value_rank = sheet.col_values(1,6,7)[0]
        rank_path=sheet.col_values(1,7,8)[0]
        Select(self.dr.find_element_by_xpath(rank_path)).select_by_value('2')
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        column = 7
        self.pagination_num(paginal_number, search_value_rank, column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(2)
        self.assertEqual('', self.dr.find_element_by_xpath('//*[@id="rank"]/option[1]').text, '寺管会级别-重置功能异常')
        print('人口管理-701数据库-寺庙：寺管会级别条件查询功能正常')

    def test06_simiao_search_all(self):
        self.simiao_search()
        search_value_name = sheet.col_values(1, 0, 1)[0]
        name_path = sheet.col_values(1, 1, 2)[0]
        self.dr.find_element_by_xpath(name_path).send_keys(search_value_name)
        search_value_address = sheet.col_values(1, 2, 3)[0]
        address_path = sheet.col_values(1, 3, 4)[0]
        self.dr.find_element_by_xpath(address_path).send_keys(search_value_address)
        search_value_category = sheet.col_values(1, 4, 5)[0]
        category_path = sheet.col_values(1, 5, 6)[0]
        Select(self.dr.find_element_by_xpath(category_path)).select_by_value('1')
        search_value_rank = sheet.col_values(1, 6, 7)[0]
        rank_path = sheet.col_values(1, 7, 8)[0]
        Select(self.dr.find_element_by_xpath(rank_path)).select_by_value('2')
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        self.pagination_num(paginal_number, search_value_name, 2)
        self.pagination_num(paginal_number, search_value_address, 3)
        self.pagination_num(paginal_number, search_value_category, 6)
        self.pagination_num(paginal_number, search_value_rank, 7)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(2)
        self.assertEqual('', self.dr.find_element_by_xpath('//*[@id="rank"]/option[1]').text, '寺管会级别-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath('//*[@id="category"]/option[1]').text, '教派类别-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(address_path).get_attribute('value'), '所在地-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(name_path).get_attribute('value'), '姓名-重置功能异常')
        print('人口管理-701数据库-寺庙：条件查询功能正常')

    def test07_simiao_details(self):
        self.simiao_search()
        search_value_name = sheet.col_values(1, 0, 1)[0]
        name_path = sheet.col_values(1, 1, 2)[0]
        self.dr.find_element_by_xpath(name_path).send_keys(search_value_name)
        search_value_address = sheet.col_values(1, 2, 3)[0]
        address_path = sheet.col_values(1, 3, 4)[0]
        self.dr.find_element_by_xpath(address_path).send_keys(search_value_address)
        search_value_category = sheet.col_values(1, 4, 5)[0]
        category_path = sheet.col_values(1, 5, 6)[0]
        Select(self.dr.find_element_by_xpath(category_path)).select_by_value('1')
        search_value_rank = sheet.col_values(1, 6, 7)[0]
        rank_path = sheet.col_values(1, 7, 8)[0]
        Select(self.dr.find_element_by_xpath(rank_path)).select_by_value('2')
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[9]/a').click()
        time.sleep(2)
        self.assertEqual(sheet.col_values(1,0,1)[0],self.dr.find_element_by_xpath('//*[@id="name"]').get_attribute('value'),'')
        self.assertEqual(sheet.col_values(1,2,3)[0],self.dr.find_element_by_xpath('//*[@id="location"]').get_attribute('value'),'')
        self.dr.find_element_by_xpath(goback).click()
        self.assertEqual('寺庙列表', self.dr.find_element_by_xpath(page_title).text,
                         '寺庙')
        print('人口管理-701数据库-寺庙：详情功能正常')

    def test08_simiao_edit(self):
        self.simiao_search()
        search_value_name = sheet.col_values(1, 0, 1)[0]
        name_path = sheet.col_values(1, 1, 2)[0]
        self.dr.find_element_by_xpath(name_path).send_keys(search_value_name)
        search_value_address = sheet.col_values(1, 2, 3)[0]
        address_path = sheet.col_values(1, 3, 4)[0]
        self.dr.find_element_by_xpath(address_path).send_keys(search_value_address)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        self.pagination_num(paginal_number, search_value_name, 2)
        self.pagination_num(paginal_number, search_value_address, 3)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[9]/a').click()
        self.dr.find_element_by_xpath('//*[@id="name"]').clear()
        self.dr.find_element_by_xpath('//*[@id="name"]').send_keys(sheet.col_values(2,0,1)[0])
        self.dr.find_element_by_xpath('//*[@id="location"]').clear()
        self.dr.find_element_by_xpath('//*[@id="location"]').send_keys(sheet.col_values(2, 2, 3)[0])
        Select(self.dr.find_element_by_xpath('//*[@id="category"]')).select_by_value('5')
        self.dr.find_element_by_xpath('//*[@id="compilingCount"]').clear()
        self.dr.find_element_by_xpath('//*[@id="compilingCount"]').send_keys(sheet.col_values(2, 8, 9)[0])
        Select(self.dr.find_element_by_xpath('//*[@id="rank"]')).select_by_value('3')
        self.dr.find_element_by_xpath('//*[@id="realCount"]').clear()
        self.dr.find_element_by_xpath('//*[@id="realCount"]').send_keys(sheet.col_values(2, 9, 10)[0])
        Select(self.dr.find_element_by_xpath('//*[@id="police"]')).select_by_value(sheet.col_values(2,12,13)[0])
        self.dr.find_element_by_xpath('//*[@id="contact"]').clear()
        self.dr.find_element_by_xpath('//*[@id="contact"]').send_keys(sheet.col_values(2, 10, 11)[0])
        self.dr.find_element_by_xpath('//*[@id="remark"]').clear()
        self.dr.find_element_by_xpath('//*[@id="remark"]').send_keys(sheet.col_values(2, 11, 12)[0])
        self.dr.find_element_by_xpath(saveBtn).click()
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        time.sleep(1)
        self.assertEqual(sheet_prompt_message.col_values(1, 4, 5)[0],
                         self.dr.find_element_by_xpath('//*[@id="gritter-item-1"]/div[2]/div[2]/p').text, '编辑修改成功提示信息校验')
        print('人口管理-701数据库-寺庙：编辑修改功能正常')

    def test09_simiao_delete(self):
        self.simiao_search()
        search_value_name = sheet.col_values(2, 0, 1)[0]
        name_path = sheet.col_values(1, 1, 2)[0]
        self.dr.find_element_by_xpath(name_path).send_keys(search_value_name)
        search_value_address = sheet.col_values(2, 2, 3)[0]
        address_path = sheet.col_values(1, 3, 4)[0]
        self.dr.find_element_by_xpath(address_path).send_keys(search_value_address)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        self.pagination_num(paginal_number, search_value_name, 2)
        self.pagination_num(paginal_number, search_value_address, 3)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        time.sleep(1)
        self.assertEqual(sheet_prompt_message.col_values(1, 3, 4)[0],
                         self.dr.find_element_by_xpath('//*[@id="gritter-item-1"]/div[2]/div[2]/p').text, '校验删除成功提示信息')
        print('人口管理-701数据库-寺庙：删除功能正常')

if __name__=='__main__':
    unittest.main()