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
sheet = excel.sheet_by_name('精神病人员')

class TESTCAST_JINGSHENBING(TESTCASE):

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

    def jingshenbing_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,13,14)[0]).click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath(currMenupath).text, '人口管理')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,13,14)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,13,14)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('精神病人员', self.dr.find_element_by_xpath(page_title).text,
                         '精神病人员')

    def test01_jingshenbing_add(self):
        self.jingshenbing_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        add_value_cardid =sheet.col_values(1,2,3)[0]
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(add_value_cardid)
        self.dr.find_element_by_xpath('//*[@id="mentForm"]/div[1]/div[2]/div/div[1]/div[2]/a').click()
        time.sleep(2)
        Select(self.dr.find_element_by_xpath('//*[@id="sfyjd"]')).select_by_value('1')
        Select(self.dr.find_element_by_xpath('//*[@id="zl"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="zdfbsjd"]').send_keys(sheet.col_values(1,8,9)[0])
        Select(self.dr.find_element_by_xpath('//*[@id="fbswhcd"]')).select_by_value('2')
        self.dr.find_element_by_xpath('//*[@id="zrmj"]').send_keys(sheet.col_values(1,9,10)[0])
        # print(sheet.col_values(1,10,11)[0])
        self.dr.find_element_by_xpath('//*[@id="mjdha"]').send_keys(sheet.col_values(1,10,11)[0])
        self.dr.find_element_by_xpath('//*[@id="mjdhb"]').send_keys(sheet.col_values(1,11,12)[0])
        self.dr.find_element_by_xpath('//*[@id="sfccjcz"]').send_keys(sheet.col_values(1,12,13)[0])
        self.dr.find_element_by_xpath('//*[@id="supervIdcardNo"]').send_keys(sheet.col_values(1,13,14)[0])
        self.dr.find_element_by_xpath('//*[@id="supervName"]').send_keys(sheet.col_values(1,14,15)[0])
        self.dr.find_element_by_xpath('//*[@id="reportCycle"]').send_keys(sheet.col_values(1,15,16)[0])
        self.dr.find_element_by_xpath('//*[@id="supervWx"]').send_keys(sheet.col_values(1,16,17)[0])
        self.dr.find_element_by_xpath('//*[@id="supervBeWx"]').send_keys(sheet.col_values(1,17,18)[0])
        self.dr.find_element_by_xpath('//*[@id="jhrXm"]').send_keys(sheet.col_values(1,18,19)[0])
        self.dr.find_element_by_xpath('//*[@id="sqgbXm"]').send_keys(sheet.col_values(1,19,20)[0])
        self.dr.find_element_by_xpath('//*[@id="jhrDh"]').send_keys(sheet.col_values(1,20,21)[0])
        self.dr.find_element_by_xpath('//*[@id="sqgbDh"]').send_keys(sheet.col_values(1,21,22)[0])
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        time.sleep(2)
        self.assertEqual(sheet_prompt_message.col_values(1, 0, 1)[0],
                         self.dr.find_element_by_xpath('//*[@id="gritter-item-1"]/div[2]/div[2]/p').text, '新增成功提示信息校验')
        print('人口管理-部局七类库-精神病人员：新增功能正常')

    def test02_jingshenbing_search_name(self):
        self.jingshenbing_search()
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
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(name_path).get_attribute('value'), '姓名-重置功能异常')
        print('人口管理-部局七类库-精神病人员：姓名条件查询功能正常')

    def test03_jingshenbing_search_cardid(self):
        self.jingshenbing_search()
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
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(cardid_path).get_attribute('value'), '身份证号-重置功能异常')
        print('人口管理-部局七类库-精神病人员：身份证号条件查询功能正常')

    def test04_jingshenbing_search_age(self):
        self.jingshenbing_search()
        search_value_1 = sheet.col_values(1,4,5)[0]
        search_value_2=sheet.col_values(1,6,7)[0]
        self.dr.find_element_by_xpath(sheet.col_values(1,5,6)[0]).send_keys(search_value_1)
        self.dr.find_element_by_xpath(sheet.col_values(1,7,8)[0]).send_keys(search_value_2)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 7
        self.pagination_num(paginal_number, search_value_1, column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1,5,6)[0]).get_attribute('value'), '重置功能')
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1, 7, 8)[0]).get_attribute('value'), '重置功能')
        print('人口管理-部局七类库-精神病人员：年龄段条件查询功能正常')

    def test05_jingshengbing_type(self):
        self.jingshenbing_search()
        option_chioce=Select(self.dr.find_element_by_xpath('//*[@id="zl"]'))
        for i in range(1,3):
            option_chioce.select_by_index(i)
            search_value_type=option_chioce.all_selected_options[0].text
            self.dr.find_element_by_xpath(search).click()
            self.dr.switch_to.default_content()
            time.sleep(2)
            self.dr.switch_to.frame('iframeb')
            self.dr.find_element_by_xpath(reset).click()
            self.dr.implicitly_wait(10)
            self.dr.find_element_by_xpath(search).click()
            self.assertEqual('--全部--',self.dr.find_element_by_xpath('//*[@id="zl"]/option[1]').get_attribute('text'),'种类-重置功能异常')
        print('人口管理-部局七类库-精神病人员：种类条件查询功能正常')

    def test06_jingshengbing_details(self):
        self.jingshenbing_search()
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
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        self.assertEqual(search_value_cardid, self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').get_attribute('value'), '详情校验')
        self.assertEqual(sheet.col_values(1,0,1)[0],self.dr.find_element_by_xpath('//*[@id="xm"]').text,'详情校验')
        time.sleep(2)
        self.dr.find_element_by_xpath(goback).click()
        self.assertEqual('精神病人员', self.dr.find_element_by_xpath(page_title).text,'精神病人员')
        print('人口管理-部局七类库-精神病人员：详情功能正常')

    def test07_jingshengbing_edit(self):
        self.jingshenbing_search()
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
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        self.dr.find_element_by_xpath('//*[@id="zdfbsjd"]').clear()
        self.dr.find_element_by_xpath('//*[@id="zdfbsjd"]').send_keys(sheet.col_values(2, 8, 9)[0])
        Select(self.dr.find_element_by_xpath('//*[@id="fbswhcd"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="zrmj"]').clear()
        self.dr.find_element_by_xpath('//*[@id="zrmj"]').send_keys(sheet.col_values(2, 9, 10)[0])
        self.dr.find_element_by_xpath('//*[@id="mjdha"]').clear()
        self.dr.find_element_by_xpath('//*[@id="mjdha"]').send_keys(sheet.col_values(2, 10, 11)[0])
        self.dr.find_element_by_xpath('//*[@id="mjdhb"]').clear()
        self.dr.find_element_by_xpath('//*[@id="mjdhb"]').send_keys(sheet.col_values(2, 11, 12)[0])
        self.dr.find_element_by_xpath('//*[@id="sfccjcz"]').clear()
        self.dr.find_element_by_xpath('//*[@id="sfccjcz"]').send_keys(sheet.col_values(2, 12, 13)[0])
        self.dr.find_element_by_xpath('//*[@id="supervIdcardNo"]').clear()
        self.dr.find_element_by_xpath('//*[@id="supervIdcardNo"]').send_keys(sheet.col_values(2, 13, 14)[0])
        self.dr.find_element_by_xpath('//*[@id="supervName"]').clear()
        self.dr.find_element_by_xpath('//*[@id="supervName"]').send_keys(sheet.col_values(2, 14, 15)[0])
        self.dr.find_element_by_xpath('//*[@id="reportCycle"]').clear()
        self.dr.find_element_by_xpath('//*[@id="reportCycle"]').send_keys(sheet.col_values(2, 15, 16)[0])
        self.dr.find_element_by_xpath('//*[@id="supervWx"]').clear()
        self.dr.find_element_by_xpath('//*[@id="supervWx"]').send_keys(sheet.col_values(2, 16, 17)[0])
        self.dr.find_element_by_xpath('//*[@id="supervBeWx"]').clear()
        self.dr.find_element_by_xpath('//*[@id="supervBeWx"]').send_keys(sheet.col_values(2, 17, 18)[0])
        self.dr.find_element_by_xpath('//*[@id="jhrXm"]').clear()
        self.dr.find_element_by_xpath('//*[@id="jhrXm"]').send_keys(sheet.col_values(2, 18, 19)[0])
        self.dr.find_element_by_xpath('//*[@id="sqgbXm"]').clear()
        self.dr.find_element_by_xpath('//*[@id="sqgbXm"]').send_keys(sheet.col_values(2, 19, 20)[0])
        self.dr.find_element_by_xpath('//*[@id="jhrDh"]').clear()
        self.dr.find_element_by_xpath('//*[@id="jhrDh"]').send_keys(sheet.col_values(2, 20, 21)[0])
        self.dr.find_element_by_xpath('//*[@id="sqgbDh"]').clear()
        self.dr.find_element_by_xpath('//*[@id="sqgbDh"]').send_keys(sheet.col_values(2, 21, 22)[0])
        self.dr.find_element_by_xpath(saveBtn).click()
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        time.sleep(2)
        self.assertEqual(sheet_prompt_message.col_values(1, 0, 1)[0],
                         self.dr.find_element_by_xpath('//*[@id="gritter-item-1"]/div[2]/div[2]/p').text, '编辑修改成功提示信息校验')
        print('人口管理-部局七类库-精神病人员：编辑修改功能正常')

    def test08_jingshengbing_delete(self):
        self.jingshenbing_search()
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
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        time.sleep(2)
        self.dr.switch_to.default_content()
        time.sleep(1)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        time.sleep(1)
        self.assertEqual(sheet_prompt_message.col_values(1, 3, 4)[0],
                         self.dr.find_element_by_xpath('//*[@id="gritter-item-1"]/div[2]/div[2]/p').text, '校验删除成功提示信息')
        print('人口管理-部局七类库-涉枪人员：删除功能正常')

if __name__ == '__main__':
    unittest.main()

