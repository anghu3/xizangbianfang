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
import xlrd
from public_package.pubilc_package import TESTCASE
from public_package.pubilc_package import sheet_setting, search, reset, currMenupath, page_title, goback, saveBtn,sheet_menu,sheet_prompt_message
import HTMLTestRunner
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

xlsfile = r'F:\pythonkeys\自动化测试\lasa\RKGL.xls'
excel = xlrd.open_workbook(xlsfile)
global sheet
sheet = excel.sheet_by_name('涉枪人员')

class TESTCAST_SHEQIANG(TESTCASE):

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

    def sheqiang_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,12,13)[0]).click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath(currMenupath).text, '人口管理')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,12,13)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,12,13)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('涉枪人员', self.dr.find_element_by_xpath(page_title).text,
                         '涉枪人员')

    def test01_sheqiang_add(self):
        self.sheqiang_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]/span').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        add_value_cardid = sheet.col_values(1,2,3)[0]
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(add_value_cardid)
        self.dr.find_element_by_xpath('//*[@id="gunForm"]/div[1]/div[2]/div/div[1]/div[2]/a').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="cqzbh"]').send_keys(sheet.col_values(1,4,5)[0])
        self.dr.find_element_by_xpath('//*[@id="fzsj"]').send_keys(sheet.col_values(1,6,7)[0])
        self.dr.find_element_by_xpath('//*[@id="szdw"]').send_keys(sheet.col_values(1,7,8)[0])
        self.dr.find_element_by_xpath('//*[@id="supervName"]').send_keys(sheet.col_values(1,8,9)[0])
        self.dr.find_element_by_xpath('//*[@id="supervIdcardNo"]').send_keys(sheet.col_values(1,9,10)[0])
        self.dr.find_element_by_xpath('//*[@id="supervWx"]').send_keys(sheet.col_values(1,10,11)[0])
        self.dr.find_element_by_xpath('//*[@id="reportCycle"]').send_keys(sheet.col_values(1,11,12)[0])
        self.dr.find_element_by_xpath('//*[@id="supervBeWx"]').send_keys(sheet.col_values(1,12,13)[0])
        self.dr.find_element_by_xpath(saveBtn).click()
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        time.sleep(2)
        self.assertEqual(sheet_prompt_message.col_values(1, 0, 1)[0],
                         self.dr.find_element_by_xpath('//*[@id="gritter-item-1"]/div[2]/div[2]/p').text, '新增成功提示信息校验')
        print('人口管理-部局七类库-涉枪人员：新增涉枪人员功能正常')

    def test02_sheqiang_search_name(self):
        self.sheqiang_search()
        search_value_name=sheet.col_values(1,0,1)[0]
        name_path=sheet.col_values(1,1,2)[0]
        self.dr.find_element_by_xpath(name_path).send_keys(search_value_name)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(10)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 4
        self.pagination_num(paginal_number, search_value_name, column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(name_path).get_attribute('value'), '姓名-重置功能异常')
        print('人口管理-部局七类库-涉枪人员：姓名条件查询功能正常')

    def test03_sheqiang_search_cardid(self):
        self.sheqiang_search()
        search_value_cardid =sheet.col_values(1,2,3)[0]
        cardid_path=sheet.col_values(1,3,4)[0]
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(search_value_cardid)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(10)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 3
        self.pagination_num(paginal_number, search_value_cardid, column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(cardid_path).get_attribute('value'), '身份证号-重置功能异常')
        print('人口管理-部局七类库-涉枪人员：身份证号条件查询功能正常')

    def test04_sheqiang_search_cqzbh(self):
        self.sheqiang_search()
        search_value_cqzbh = sheet.col_values(1,4,5)[0]
        cqzbh_path=sheet.col_values(1,5,6)[0]
        self.dr.find_element_by_xpath(cqzbh_path).send_keys(search_value_cqzbh)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(10)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 5
        self.pagination_num(paginal_number, search_value_cqzbh, column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(cqzbh_path).get_attribute('value'), '持枪证编号-重置功能异常')
        print('人口管理-部局七类库-涉枪人员：持枪证编号条件查询功能正常')

    def test05_sheqiang_search_all(self):
        self.sheqiang_search()
        search_value_name = sheet.col_values(1, 0, 1)[0]
        name_path = sheet.col_values(1, 1, 2)[0]
        self.dr.find_element_by_xpath(name_path).send_keys(search_value_name)
        search_value_cardid = sheet.col_values(1, 2, 3)[0]
        cardid_path = sheet.col_values(1, 3, 4)[0]
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(search_value_cardid)
        search_value_cqzbh = sheet.col_values(1, 4, 5)[0]
        cqzbh_path = sheet.col_values(1, 5, 6)[0]
        self.dr.find_element_by_xpath(cqzbh_path).send_keys(search_value_cqzbh)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(10)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        self.pagination_num(paginal_number, search_value_name, 4)
        self.pagination_num(paginal_number, search_value_cardid, 3)
        self.pagination_num(paginal_number, search_value_cqzbh, 5)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(name_path).get_attribute('value'), '姓名-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(cardid_path).get_attribute('value'), '身份证号-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(cqzbh_path).get_attribute('value'), '持枪证编号-重置功能异常')
        print('人口管理-部局七类库-涉枪人员：条件查询功能正常')

    def test06_sheqiang_details(self):
        self.sheqiang_search()
        search_value_cardid = sheet.col_values(1, 2, 3)[0]
        cardid_path = sheet.col_values(1, 3, 4)[0]
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(search_value_cardid)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(10)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 3
        self.pagination_num(paginal_number, search_value_cardid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[8]/a').click()
        time.sleep(2)
        self.assertEqual(search_value_cardid,self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').get_attribute('value'),'详情页面身份证号校验异常')
        self.assertEqual(sheet.col_values(1,0,1)[0],self.dr.find_element_by_xpath('//*[@id="xm"]').text,'详情页面姓名校验异常')
        self.assertEqual(sheet.col_values(1,4,5)[0],self.dr.find_element_by_xpath('//*[@id="cqzbh"]').get_attribute('value'),'详情页面持枪证编号校验异常')
        self.dr.find_element_by_xpath(goback).click()
        self.assertEqual('涉枪人员', self.dr.find_element_by_xpath(page_title).text,'涉枪人员')
        print('人口管理-部局七类库-涉枪人员：详情功能正常')

    def test07_sheqiang_edit(self):
        self.sheqiang_search()
        search_value_cardid = sheet.col_values(1, 2, 3)[0]
        cardid_path = sheet.col_values(1, 3, 4)[0]
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(search_value_cardid)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(10)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 3
        self.pagination_num(paginal_number, search_value_cardid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[8]/a').click()
        self.dr.find_element_by_xpath('//*[@id="cqzbh"]').clear()
        self.dr.find_element_by_xpath('//*[@id="cqzbh"]').send_keys(sheet.col_values(2, 4, 5)[0])
        self.dr.find_element_by_xpath('//*[@id="fzsj"]').clear()
        self.dr.find_element_by_xpath('//*[@id="fzsj"]').send_keys(sheet.col_values(2, 6, 7)[0])
        self.dr.find_element_by_xpath('//*[@id="szdw"]').clear()
        self.dr.find_element_by_xpath('//*[@id="szdw"]').send_keys(sheet.col_values(2, 7, 8)[0])
        self.dr.find_element_by_xpath('//*[@id="supervName"]').clear()
        self.dr.find_element_by_xpath('//*[@id="supervName"]').send_keys(sheet.col_values(2, 8, 9)[0])
        self.dr.find_element_by_xpath('//*[@id="supervIdcardNo"]').clear()
        self.dr.find_element_by_xpath('//*[@id="supervIdcardNo"]').send_keys(sheet.col_values(2, 9, 10)[0])
        self.dr.find_element_by_xpath('//*[@id="supervWx"]').clear()
        self.dr.find_element_by_xpath('//*[@id="supervWx"]').send_keys(sheet.col_values(2, 10, 11)[0])
        self.dr.find_element_by_xpath('//*[@id="reportCycle"]').clear()
        self.dr.find_element_by_xpath('//*[@id="reportCycle"]').send_keys(sheet.col_values(2, 11, 12)[0])
        self.dr.find_element_by_xpath('//*[@id="supervBeWx"]').clear()
        self.dr.find_element_by_xpath('//*[@id="supervBeWx"]').send_keys(sheet.col_values(2, 12, 13)[0])
        self.dr.find_element_by_xpath(saveBtn).click()
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        time.sleep(2)
        self.assertEqual(sheet_prompt_message.col_values(1, 0, 1)[0],
                         self.dr.find_element_by_xpath('//*[@id="gritter-item-1"]/div[2]/div[2]/p').text, '编辑修改成功提示信息校验')
        print('人口管理-局部七类库-涉枪人员：编辑修改功能正常')

    def test08_sheqiang_delete(self):
        self.sheqiang_search()
        search_value_cardid = sheet.col_values(1,2,3)[0]
        cardid_path=sheet.col_values(1,3,4)[0]
        self.dr.find_element_by_xpath(cardid_path).send_keys(search_value_cardid)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(10)
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
        print('人口管理-局部七类库-涉枪人员：删除涉枪人员功能正常')

if __name__ == '__main__':
    unittest.main()