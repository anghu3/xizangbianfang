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
from public_package.pubilc_package import TESTCASE
from public_package.pubilc_package import sheet_setting, search, reset, currMenupath, page_title, goback, saveBtn,sheet_menu,sheet_prompt_message,work_space
import xlrd
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

xlsfile=work_space+r'\\'+sheet_menu.col_values(6,24,25)[0]
excel = xlrd.open_workbook(xlsfile)
global sheet
sheet = excel.sheet_by_name('法会')

class TESTCAST_FAHUI(TESTCASE):
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

    def fahui_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,24,25)[0]).click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath(currMenupath).text, '人口管理')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,24,25)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,24,25)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('法会列表', self.dr.find_element_by_xpath(page_title).text,
                         '法会')

    def test01_fahui_add(self):
        self.fahui_search()
        self.dr.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/a[2]').click()
        self.dr.find_element_by_xpath('//*[@id="ceremonyName"]').send_keys(sheet.col_values(1,0,1)[0])
        self.dr.find_element_by_xpath('//*[@id="ceremonyArea"]').send_keys(sheet.col_values(1,2,3)[0])
        self.dr.find_element_by_xpath('//*[@id="organizateMonkNum"]').send_keys(sheet.col_values(1,4,5)[0])
        self.dr.find_element_by_xpath('//*[@id="realityMonkNum"]').send_keys(sheet.col_values(1,5,6)[0])
        self.dr.find_element_by_xpath('//*[@id="conscientiousPolice"]').send_keys(sheet.col_values(1,6,7)[0])
        self.dr.find_element_by_xpath('//*[@id="telephone"]').send_keys(sheet.col_values(1,7,8)[0])
        self.dr.find_element_by_xpath('//*[@id="remarks"]').send_keys(sheet.col_values(1,8,9)[0])
        self.dr.find_element_by_xpath(sheet_setting.col_values(6,2,3)[0]).click()
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        time.sleep(2)
        self.assertEqual(sheet_prompt_message.col_values(1, 4, 5)[0],
                         self.dr.find_element_by_xpath('//*[@id="gritter-item-1"]/div[2]/div[2]/p').text, '新增成功提示信息校验')
        print('人口管理-701数据库-法会：新增功能正常')

    def test02_fahui_search_name(self):
        self.fahui_search()
        search_value_name=sheet.col_values(1,0,1)[0]
        name_path=sheet.col_values(1,1,2)[0]
        self.dr.find_element_by_xpath(name_path).send_keys(search_value_name)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,2,3)[0]).text
        column = 3
        self.pagination_num(paginal_number, search_value_name, column)
        self.dr.find_element_by_xpath(reset).click()
        time.sleep(2)
        self.dr.find_element_by_xpath(search).click()
        self.assertEqual('',self.dr.find_element_by_xpath(name_path).get_attribute('value'),'姓名-重置功能异常')
        print('人口管理-701数据库-法会：法会名称条件查询功能正常')

    def test03_fahui_search_address(self):
        self.fahui_search()
        search_value_address=sheet.col_values(1,2,3)[0]
        address_path=sheet.col_values(1,3,4)[0]
        self.dr.find_element_by_xpath(address_path).send_keys(search_value_address)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,2,3)[0]).text
        column = 4
        self.pagination_num(paginal_number, search_value_address, column)
        self.dr.find_element_by_xpath(reset).click()
        time.sleep(2)
        self.dr.find_element_by_xpath(search).click()
        self.assertEqual('',self.dr.find_element_by_xpath(address_path).get_attribute('value'),'法会所在地-重置功能异常')
        print('人口管理-701数据库-法会：法会名称条件查询功能正常')

    def test04_fahui_search_all(self):
        self.fahui_search()
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
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 2, 3)[0]).text
        self.pagination_num(paginal_number, search_value_address, 4)
        self.pagination_num(paginal_number, search_value_name, 3)
        self.dr.find_element_by_xpath(reset).click()
        time.sleep(2)
        self.dr.find_element_by_xpath(search).click()
        self.assertEqual('', self.dr.find_element_by_xpath(name_path).get_attribute('value'), '姓名-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(address_path).get_attribute('value'), '法会所在地-重置功能异常')
        print('人口管理-701数据库-法会：条件查询功能正常')

    def test05_fahiu_details(self):
        self.fahui_search()
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
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 2, 3)[0]).text
        self.pagination_num(paginal_number, search_value_address, 4)
        self.pagination_num(paginal_number, search_value_name, 3)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/a').click()
        self.assertEqual(sheet.col_values(1,0,1)[0],self.dr.find_element_by_xpath('//*[@id="ceremonyName"]').get_attribute('value'),'详情页法会名称校验失败')
        self.assertEqual(sheet.col_values(1,2,3)[0],self.dr.find_element_by_xpath('//*[@id="ceremonyArea"]').get_attribute('value'),'详情页法会所在地校验失败')
        self.assertEqual(sheet.col_values(1,4,5)[0],self.dr.find_element_by_xpath('//*[@id="organizateMonkNum"]').get_attribute('value'),'详情页编制僧尼数校验失败')
        self.assertEqual(sheet.col_values(1,5,6)[0],self.dr.find_element_by_xpath('//*[@id="realityMonkNum"]').get_attribute('value'),'详情页实有僧尼数校验失败')
        self.assertEqual(sheet.col_values(1,6,7)[0],self.dr.find_element_by_xpath('//*[@id="conscientiousPolice"]').get_attribute('value'),'详情页负责民警校验失败')
        self.assertEqual(sheet.col_values(1,7,8)[0],self.dr.find_element_by_xpath('//*[@id="telephone"]').get_attribute('value'),'详情页联系方式校验失败')
        self.dr.find_element_by_xpath(goback).click()
        self.assertEqual('法会列表', self.dr.find_element_by_xpath(page_title).text,
                         '法会')
        print('人口管理-701数据库-法会：详情功能正常')

    def test06_fahui_edit(self):
        self.fahui_search()
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
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 2, 3)[0]).text
        self.pagination_num(paginal_number, search_value_address, 4)
        self.pagination_num(paginal_number, search_value_name, 3)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/a').click()
        self.dr.find_element_by_xpath('//*[@id="ceremonyName"]').clear()
        self.dr.find_element_by_xpath('//*[@id="ceremonyName"]').send_keys(sheet.col_values(2, 0, 1)[0])
        self.dr.find_element_by_xpath('//*[@id="ceremonyArea"]').clear()
        self.dr.find_element_by_xpath('//*[@id="ceremonyArea"]').send_keys(sheet.col_values(2, 2, 3)[0])
        self.dr.find_element_by_xpath('//*[@id="organizateMonkNum"]').clear()
        self.dr.find_element_by_xpath('//*[@id="organizateMonkNum"]').send_keys(sheet.col_values(2, 4, 5)[0])
        self.dr.find_element_by_xpath('//*[@id="realityMonkNum"]').clear()
        self.dr.find_element_by_xpath('//*[@id="realityMonkNum"]').send_keys(sheet.col_values(2, 5, 6)[0])
        self.dr.find_element_by_xpath('//*[@id="conscientiousPolice"]').clear()
        self.dr.find_element_by_xpath('//*[@id="conscientiousPolice"]').send_keys(sheet.col_values(2, 6, 7)[0])
        self.dr.find_element_by_xpath('//*[@id="telephone"]').clear()
        self.dr.find_element_by_xpath('//*[@id="telephone"]').send_keys(sheet.col_values(2, 7, 8)[0])
        self.dr.find_element_by_xpath('//*[@id="remarks"]').clear()
        self.dr.find_element_by_xpath('//*[@id="remarks"]').send_keys(sheet.col_values(2, 8, 9)[0])
        self.dr.find_element_by_xpath(sheet_setting.col_values(6,2,3)[0]).click()
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        time.sleep(2)
        self.assertEqual(sheet_prompt_message.col_values(1, 4, 5)[0],
                         self.dr.find_element_by_xpath('//*[@id="gritter-item-1"]/div[2]/div[2]/p').text, '编辑修改成功提示信息校验')
        print('人口管理-701数据库-法会：编辑修改功能正常')



    def test07_fahui_delete(self):
        self.fahui_search()
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
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 2, 3)[0]).text
        self.pagination_num(paginal_number, search_value_address, 4)
        self.pagination_num(paginal_number, search_value_name, 3)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('人口管理-701数据库-法会：删除功能正常')


if __name__=='__main__':
    unittest.main()