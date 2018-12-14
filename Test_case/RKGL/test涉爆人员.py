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
import xlrd
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

xlsfile=work_space+r'\\'+sheet_menu.col_values(6,11,12)[0]
excel = xlrd.open_workbook(xlsfile)
global sheet
sheet = excel.sheet_by_name('涉爆人员')

class TESTCAST_SHEBAO(TESTCASE):

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

    def shebao_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,11,12)[0]).click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath(currMenupath).text, '人口管理')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,11,12)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,11,12)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('涉爆人员', self.dr.find_element_by_xpath(page_title).text,
                         '涉爆人员')

    def test01_shebao_add(self):
        self.shebao_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        add_value_cardid = sheet.col_values(1,2,3)[0]
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(add_value_cardid)
        self.dr.find_element_by_xpath('//*[@id="wadeForm"]/div[1]/div[2]/div/div[1]/div[2]/a').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="xjzdz"]').send_keys(sheet.col_values(1,6,7)[0])
        self.dr.find_element_by_xpath('//*[@id="zyzbh"]').send_keys(sheet.col_values(1,7,8)[0])
        self.dr.find_element_by_xpath('//*[@id="gzdw"]').send_keys(sheet.col_values(1,8,9)[0])
        option_chioce = Select(self.dr.find_element_by_xpath('//*[@id="sbzt"]'))
        option_chioce.select_by_index(1)
        self.dr.find_element_by_xpath('//*[@id="fzjg"]').send_keys(sheet.col_values(1,9,10)[0])
        self.dr.find_element_by_xpath('//*[@id="supervName"]').send_keys(sheet.col_values(1,10,11)[0])
        self.dr.find_element_by_xpath('//*[@id="supervIdcardNo"]').send_keys(sheet.col_values(1,11,12)[0])
        self.dr.find_element_by_xpath('//*[@id="supervWx"]').send_keys(sheet.col_values(1,12,13)[0])
        self.dr.find_element_by_xpath('//*[@id="reportCycle"]').send_keys(sheet.col_values(1,13,14)[0])
        self.dr.find_element_by_xpath('//*[@id="supervBeWx"]').send_keys(sheet.col_values(1,14,15)[0])
        time.sleep(2)
        self.dr.find_element_by_xpath(saveBtn).click()
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        time.sleep(2)
        self.assertEqual(sheet_prompt_message.col_values(1,1,2)[0],self.dr.find_element_by_xpath('//*[@id="gritter-item-1"]/div[2]/div[2]/p').text,'新增成功提示信息校验')
        print('人口管理-局部七类库-涉爆人员：新增功能正常')

    def test02_shebao_search_name(self):
        self.shebao_search()
        search_value_name = sheet.col_values(1,0,1)[0]
        name_path=sheet.col_values(1,1,2)[0]
        self.dr.find_element_by_xpath(name_path).send_keys(search_value_name)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 4
        self.pagination_num(paginal_number, search_value_name, column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        self.assertEqual('',self.dr.find_element_by_xpath(name_path).get_attribute('value'),'姓名-重置功能异常')
        print('人口管理-部局七类库-涉爆人员：姓名条件查询功能正常')

    def test03_shebao_search_cardid(self):
        self.shebao_search()
        search_value_cardid =sheet.col_values(1,2,3)[0]
        cardid_path=sheet.col_values(1,3,4)[0]
        self.dr.find_element_by_xpath(cardid_path).send_keys(search_value_cardid)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 3
        self.pagination_num(paginal_number, search_value_cardid, column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        self.assertEqual('', self.dr.find_element_by_xpath(cardid_path).get_attribute('value'), '身份证号-重置功能异常')
        print('人口管理-部局七类库-涉爆人员：身份证号条件查询功能正常')

    def test04_shebao_search_zyzbh(self):
        self.shebao_search()
        search_value_zyzbh = sheet.col_values(1,4,5)[0]
        zyzhb_path=sheet.col_values(1,5,6)[0]
        self.dr.find_element_by_xpath(zyzhb_path).send_keys(search_value_zyzbh)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 7
        self.pagination_num(paginal_number, search_value_zyzbh, column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        self.assertEqual('', self.dr.find_element_by_xpath(zyzhb_path).get_attribute('value'), '作业证编号-重置功能异常')
        print('人口管理-部局七类库-涉爆人员：作业证编号条件查询功能正常')


    def test05_shebao_search_all(self):
        self.shebao_search()
        search_value_name = sheet.col_values(1, 0, 1)[0]
        name_path = sheet.col_values(1, 1, 2)[0]
        search_value_cardid = sheet.col_values(1, 2, 3)[0]
        cardid_path = sheet.col_values(1, 3, 4)[0]
        search_value_zyzbh = sheet.col_values(1, 4, 5)[0]
        zyzhb_path = sheet.col_values(1, 5, 6)[0]
        self.dr.find_element_by_xpath(name_path).send_keys(search_value_name)
        self.dr.find_element_by_xpath(cardid_path).send_keys(search_value_cardid)
        self.dr.find_element_by_xpath(zyzhb_path).send_keys(search_value_zyzbh)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        self.pagination_num(paginal_number, search_value_name, 4)
        self.pagination_num(paginal_number, search_value_cardid, 3)
        self.pagination_num(paginal_number, search_value_zyzbh, 7)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        self.assertEqual('', self.dr.find_element_by_xpath(name_path).get_attribute('value'), '姓名-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(cardid_path).get_attribute('value'), '身份证号-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(zyzhb_path).get_attribute('value'), '作业证编号-重置功能异常')
        print('人口管理-部局七类库-涉爆人员：条件查询功能正常')

    def test06_shebao_details(self):
        self.shebao_search()
        search_value_cardid = sheet.col_values(1, 2, 3)[0]
        cardid_path = sheet.col_values(1, 3, 4)[0]
        self.dr.find_element_by_xpath(cardid_path).send_keys(search_value_cardid)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 3
        self.pagination_num(paginal_number, search_value_cardid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[8]/a').click()
        time.sleep(2)
        self.assertEqual(search_value_cardid,self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').get_attribute('value'),'详情页身份证号校验异常')
        self.assertEqual(sheet.col_values(1,0,1)[0],self.dr.find_element_by_xpath('//*[@id="xm"]').text,'详情页面姓名校验异常')
        self.assertEqual(sheet.col_values(1,4,5)[0],self.dr.find_element_by_xpath('//*[@id="zyzbh"]').get_attribute('value'),'详情页面作业证编号校验异常')
        self.dr.find_element_by_xpath(goback).click()
        self.assertEqual('涉爆人员', self.dr.find_element_by_xpath(page_title).text,'涉爆人员')
        print('人口管理-局部七类库-涉爆人员：详情功能正常')

    def test07_shebao_edit(self):
        self.shebao_search()
        search_value_cardid = sheet.col_values(1, 2, 3)[0]
        cardid_path = sheet.col_values(1, 3, 4)[0]
        self.dr.find_element_by_xpath(cardid_path).send_keys(search_value_cardid)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 3
        self.pagination_num(paginal_number, search_value_cardid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[8]/a').click()
        self.dr.find_element_by_xpath('//*[@id="xjzdz"]').clear()
        self.dr.find_element_by_xpath('//*[@id="xjzdz"]').send_keys(sheet.col_values(2, 6, 7)[0])
        self.dr.find_element_by_xpath('//*[@id="zyzbh"]').clear()
        self.dr.find_element_by_xpath('//*[@id="zyzbh"]').send_keys(sheet.col_values(2, 7, 8)[0])
        self.dr.find_element_by_xpath('//*[@id="gzdw"]').clear()
        self.dr.find_element_by_xpath('//*[@id="gzdw"]').send_keys(sheet.col_values(2, 8, 9)[0])
        option_chioce = Select(self.dr.find_element_by_xpath('//*[@id="sbzt"]'))
        option_chioce.select_by_index(2)
        self.dr.find_element_by_xpath('//*[@id="fzjg"]').clear()
        self.dr.find_element_by_xpath('//*[@id="fzjg"]').send_keys(sheet.col_values(2, 9, 10)[0])
        self.dr.find_element_by_xpath('//*[@id="supervName"]').clear()
        self.dr.find_element_by_xpath('//*[@id="supervName"]').send_keys(sheet.col_values(2, 10, 11)[0])
        self.dr.find_element_by_xpath('//*[@id="supervIdcardNo"]').clear()
        self.dr.find_element_by_xpath('//*[@id="supervIdcardNo"]').send_keys(sheet.col_values(2, 11, 12)[0])
        self.dr.find_element_by_xpath('//*[@id="supervWx"]').clear()
        self.dr.find_element_by_xpath('//*[@id="supervWx"]').send_keys(sheet.col_values(2, 12, 13)[0])
        self.dr.find_element_by_xpath('//*[@id="reportCycle"]').clear()
        self.dr.find_element_by_xpath('//*[@id="reportCycle"]').send_keys(sheet.col_values(2, 13, 14)[0])
        self.dr.find_element_by_xpath('//*[@id="supervBeWx"]').clear()
        self.dr.find_element_by_xpath('//*[@id="supervBeWx"]').send_keys(sheet.col_values(2, 14, 15)[0])
        self.dr.find_element_by_xpath(saveBtn).click()
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        time.sleep(2)
        self.assertEqual(sheet_prompt_message.col_values(1, 1, 2)[0],
                         self.dr.find_element_by_xpath('//*[@id="gritter-item-1"]/div[2]/div[2]/p').text, '编辑成功提示信息校验')
        print('人口管理-局部七类库-涉爆人员：编辑功能正常')


    def test08_shebao_delete(self):
        self.shebao_search()
        search_value_cardid = sheet.col_values(1, 2, 3)[0]
        cardid_path = sheet.col_values(1, 3, 4)[0]
        self.dr.find_element_by_xpath(cardid_path).send_keys(search_value_cardid)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 3
        self.pagination_num(paginal_number, search_value_cardid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]/input').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        time.sleep(2)
        self.dr.switch_to.default_content()
        time.sleep(1)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        time.sleep(1)
        self.assertEqual(sheet_prompt_message.col_values(1,3,4)[0],
                         self.dr.find_element_by_xpath('//*[@id="gritter-item-1"]/div[2]/div[2]/p').text, '校验删除成功提示信息')
        print('人口管理-局部七类库-涉爆人员：删除功能正常')


if __name__ == '__main__':
    unittest.main()