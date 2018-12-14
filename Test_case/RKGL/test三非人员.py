# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 14:11:17 2018

@author: PCCC
"""
import unittest
from selenium import webdriver
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

xlsfile=work_space+r'\\'+sheet_menu.col_values(6,22,23)[0]
excel = xlrd.open_workbook(xlsfile)
global sheet
sheet = excel.sheet_by_name('三非人员')

class TESTCAST_SANFEI(TESTCASE):
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

    def sanfei_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,22,23)[0]).click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath(currMenupath).text, '人口管理')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,22,23)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,22,23)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('三非人员信息列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text,
                         '三非人员')

    def test01_sanfei_add(self):
        self.sanfei_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        add_value_name=sheet.col_values(1,0,1)[0]
        add_value_carid=sheet.col_values(1,4,5)[0]
        self.dr.find_element_by_xpath('//*[@id="personName"]').send_keys(add_value_name)
        Select(self.dr.find_element_by_xpath('//*[@id="personType"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="work"]').send_keys(sheet.col_values(1,18,19)[0])
        self.dr.find_element_by_xpath('//*[@id="workPlace"]').send_keys(sheet.col_values(1,19,20)[0])
        Select(self.dr.find_element_by_xpath('//*[@id="idType"]')).select_by_value('111')
        self.dr.find_element_by_xpath('//*[@id="idNumber"]').send_keys(add_value_carid)
        self.dr.find_element_by_xpath('//*[@id="entryPosition"]').send_keys(sheet.col_values(1,8,9)[0])
        self.dr.find_element_by_xpath('//*[@id="residentialAddress"]').send_keys(sheet.col_values(1,9,10)[0])
        Select(self.dr.find_element_by_xpath('//*[@id="whetherInvolved"]')).select_by_index('0')
        Select(self.dr.find_element_by_xpath('//*[@id="caseType"]')).select_by_value('010101')
        self.dr.find_element_by_xpath('//*[@id="caseNumber"]').send_keys(sheet.col_values(1,10,11)[0])
        self.dr.find_element_by_xpath('//*[@id="caseSummary"]').send_keys(sheet.col_values(1,11,12)[0])
        self.dr.find_element_by_xpath('//*[@id="connectorName"]').send_keys(sheet.col_values(1,12,13)[0])
        self.dr.find_element_by_xpath('//*[@id="connectorIdCard"]').send_keys(sheet.col_values(1,13,14)[0])
        self.dr.find_element_by_xpath('//*[@id="repatriateDate"]').send_keys(sheet.col_values(1,14,15)[0])
        '''责任单位'''
        self.dr.find_element_by_xpath('//*[@id="dutyOrg"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_46_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_48_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="dutyPerson"]').click()
        self.dr.find_element_by_xpath('//*[@id="dutyPerson"]').send_keys(sheet.col_values(1,16,17)[0])
        self.dr.find_element_by_xpath('//*[@id="remark"]').send_keys(sheet.col_values(1,17,18)[0])
        self.dr.find_element_by_xpath(saveBtn).click()
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        time.sleep(1)
        self.assertEqual(sheet_prompt_message.col_values(1, 4, 5)[0],
                         self.dr.find_element_by_xpath('//*[@id="gritter-item-1"]/div[2]/div[2]/p').text, '新增成功提示信息校验')
        print('人口管理-部局七类库-三非人员：新增功能正常')


    def test02_sanfei_search_name(self):
        self.sanfei_search()
        search_value_name=sheet.col_values(1,0,1)[0]
        name_path=sheet.col_values(1,1,2)[0]
        self.dr.find_element_by_xpath(name_path).send_keys(search_value_name)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number=self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        column=3
        self.pagination_num(paginal_number,search_value_name,column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(2)
        self.assertEqual('', self.dr.find_element_by_xpath(name_path).get_attribute('value'), '姓名-重置功能异常')
        print('人口管理-部局七类库-三非人员：姓名条件查询功能正常')

    def test03_sanfei_search_zjlx(self):
        self.sanfei_search()
        search_value_zjlx='居民身份证'
        Select(self.dr.find_element_by_xpath('//*[@id="idType"]')).select_by_value('111')
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number,search_value_zjlx,column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(2)
        self.assertEqual('',self.dr.find_element_by_xpath('//*[@id="idType"]/option[1]').text,'证件类型-重置功能异常')
        print('人口管理-部局七类库-三非人员：证件类型条件查询功能正常')

    def test04_sanfei_search_carid(self):
        self.sanfei_search()
        search_value_carid=sheet.col_values(1,4,5)[0]
        cardid_path=sheet.col_values(1,5,6)[0]
        self.dr.find_element_by_xpath(cardid_path).send_keys(search_value_carid)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        column = 5
        self.pagination_num(paginal_number, search_value_carid, column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(2)
        self.assertEqual('', self.dr.find_element_by_xpath(cardid_path).get_attribute('value'), '身份证号码-重置功能异常')
        print('人口管理-部局七类库-三非人员：证件编号条件查询功能正常')

    def test05_sanfei_search_rylx(self):
        self.sanfei_search()
        search_value_rylx = '非法入境'
        Select(self.dr.find_element_by_xpath('//*[@id="personType"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        column = 6
        self.pagination_num(paginal_number,search_value_rylx,column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(2)
        self.assertEqual('',self.dr.find_element_by_xpath('//*[@id="personType"]/option[1]').text,'人员类型-重置功能异常')
        print('人口管理-部局七类库-三非人员：人员类型条件查询功能正常')

    def test06_sanfei_search_all(self):
        self.sanfei_search()
        search_value_name = sheet.col_values(1, 0, 1)[0]
        name_path = sheet.col_values(1, 1, 2)[0]
        self.dr.find_element_by_xpath(name_path).send_keys(search_value_name)
        search_value_zjlx = '居民身份证'
        Select(self.dr.find_element_by_xpath('//*[@id="idType"]')).select_by_value('111')
        search_value_carid = sheet.col_values(1, 4, 5)[0]
        cardid_path = sheet.col_values(1, 5, 6)[0]
        self.dr.find_element_by_xpath(cardid_path).send_keys(search_value_carid)
        search_value_rylx = '非法入境'
        Select(self.dr.find_element_by_xpath('//*[@id="personType"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        self.pagination_num(paginal_number, search_value_rylx, 6)
        self.pagination_num(paginal_number, search_value_carid, 5)
        self.pagination_num(paginal_number, search_value_zjlx, 4)
        self.pagination_num(paginal_number, search_value_name, 3)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(2)
        self.assertEqual('', self.dr.find_element_by_xpath(name_path).get_attribute('value'), '姓名-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath('//*[@id="idType"]/option[1]').text, '证件类型-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(cardid_path).get_attribute('value'), '身份证号码-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath('//*[@id="personType"]/option[1]').text,
                                      '人员类型-重置功能异常')
        print('人口管理-部局七类库-三非人员：条件查询功能正常')

    def test07_sanfei_search_details(self):
        self.sanfei_search()
        search_value_carid = sheet.col_values(1, 4, 5)[0]
        cardid_path = sheet.col_values(1, 5, 6)[0]
        self.dr.find_element_by_xpath(cardid_path).send_keys(search_value_carid)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 5
        self.pagination_num(paginal_number, search_value_carid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[8]/a').click()
        self.assertEqual(sheet.col_values(1,0,1)[0],self.dr.find_element_by_xpath('//*[@id="personName"]').get_attribute('value'),'详情页面校验姓名异常')
        self.assertEqual(sheet.col_values(1,4,5)[0],self.dr.find_element_by_xpath('//*[@id="idNumber"]').get_attribute('value'),'详情页面校验身份证号码异常')
        time.sleep(1)
        self.dr.find_element_by_xpath(goback).click()
        self.assertEqual('三非人员信息列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text,
                         '三非人员')
        print('人口管理-部局七类库-三非人员：详情页面功能正常')

    def test08_sanfei_edit(self):
        self.sanfei_search()
        search_value_carid = sheet.col_values(1, 4, 5)[0]
        cardid_path = sheet.col_values(1, 5, 6)[0]
        self.dr.find_element_by_xpath(cardid_path).send_keys(search_value_carid)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 5
        self.pagination_num(paginal_number, search_value_carid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[8]/a').click()
        self.dr.find_element_by_xpath('//*[@id="personName"]').clear()
        self.dr.find_element_by_xpath('//*[@id="personName"]').send_keys(sheet.col_values(2,0,1)[0])
        self.dr.find_element_by_xpath('//*[@id="work"]').clear()
        self.dr.find_element_by_xpath('//*[@id="work"]').send_keys(sheet.col_values(2, 18, 19)[0])
        self.dr.find_element_by_xpath('//*[@id="workPlace"]').clear()
        self.dr.find_element_by_xpath('//*[@id="workPlace"]').send_keys(sheet.col_values(2, 19, 20)[0])
        self.dr.find_element_by_xpath('//*[@id="idNumber"]').clear()
        self.dr.find_element_by_xpath('//*[@id="idNumber"]').send_keys(sheet.col_values(2,4,5)[0])
        self.dr.find_element_by_xpath('//*[@id="entryPosition"]').clear()
        self.dr.find_element_by_xpath('//*[@id="entryPosition"]').send_keys(sheet.col_values(2, 8, 9)[0])
        self.dr.find_element_by_xpath('//*[@id="residentialAddress"]').clear()
        self.dr.find_element_by_xpath('//*[@id="residentialAddress"]').send_keys(sheet.col_values(2, 9, 10)[0])
        self.dr.find_element_by_xpath('//*[@id="caseNumber"]').clear()
        self.dr.find_element_by_xpath('//*[@id="caseNumber"]').send_keys(sheet.col_values(2, 10, 11)[0])
        self.dr.find_element_by_xpath('//*[@id="caseSummary"]').clear()
        self.dr.find_element_by_xpath('//*[@id="caseSummary"]').send_keys(sheet.col_values(2, 11, 12)[0])
        self.dr.find_element_by_xpath('//*[@id="connectorName"]').clear()
        self.dr.find_element_by_xpath('//*[@id="connectorName"]').send_keys(sheet.col_values(2, 12, 13)[0])
        self.dr.find_element_by_xpath('//*[@id="connectorIdCard"]').clear()
        self.dr.find_element_by_xpath('//*[@id="connectorIdCard"]').send_keys(sheet.col_values(2, 13, 14)[0])
        self.dr.find_element_by_xpath('//*[@id="repatriateDate"]').clear()
        self.dr.find_element_by_xpath('//*[@id="repatriateDate"]').send_keys(sheet.col_values(2, 14, 15)[0])
        self.dr.find_element_by_xpath('//*[@id="dutyPerson"]').clear()
        self.dr.find_element_by_xpath('//*[@id="dutyPerson"]').send_keys(sheet.col_values(2, 16, 17)[0])
        self.dr.find_element_by_xpath('//*[@id="remark"]').clear()
        self.dr.find_element_by_xpath('//*[@id="remark"]').send_keys(sheet.col_values(2, 17, 18)[0])
        self.dr.find_element_by_xpath(saveBtn).click()
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        time.sleep(1)
        self.assertEqual(sheet_prompt_message.col_values(1, 4, 5)[0],
                         self.dr.find_element_by_xpath('//*[@id="gritter-item-1"]/div[2]/div[2]/p').text, '编辑修改成功提示信息校验')
        print('人口管理-部局七类库-三非人员：编辑修改功能正常')

    def test09_sanfei_delete(self):
        self.sanfei_search()
        search_value_carid = sheet.col_values(2, 4, 5)[0]
        cardid_path = sheet.col_values(1, 5, 6)[0]
        self.dr.find_element_by_xpath(cardid_path).send_keys(search_value_carid)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 5
        self.pagination_num(paginal_number, search_value_carid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[2]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        time.sleep(1)
        self.assertEqual(sheet_prompt_message.col_values(1, 3, 4)[0],
                         self.dr.find_element_by_xpath('//*[@id="gritter-item-1"]/div[2]/div[2]/p').text, '校验删除成功提示信息')
        print('人口管理-部局七类库-三非人员：删除功能正常')

if __name__=='__main__':
    unittest.main()





