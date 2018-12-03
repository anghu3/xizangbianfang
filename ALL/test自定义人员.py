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
sheet = excel.sheet_by_name('自定义人员')

class TESTCAST_ZIDINGYI(TESTCASE):
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

    def zidingyi_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,26,27)[0]).click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath(currMenupath).text, '人口管理')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,26,27)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,26,27)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('自定义人员监控', self.dr.find_element_by_xpath(page_title).text,
                         '自定义人员')

    def test01_zidingyi_add(self):
        self.zidingyi_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        add_value_cardid = sheet.col_values(1,2,3)[0]
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(add_value_cardid)
        self.dr.find_element_by_xpath('//*[@id="customForm"]/div[1]/div[2]/div/div[1]/div[2]/a').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="personsType"]').send_keys(sheet.col_values(1,8,9)[0])
        self.dr.find_element_by_xpath('//*[@id="credentials"]').send_keys(sheet.col_values(1,9,10)[0])
        self.dr.find_element_by_xpath('//*[@id="livingPlace"]').send_keys(sheet.col_values(1,10,11)[0])
        Select(self.dr.find_element_by_xpath('//*[@id="isLimit"]')).select_by_value('0')
        # js = "$('input[id=txtBeginDate]').attr('readonly','')"
        # self.dr.execute_script(js)
        self.dr.find_element_by_xpath('//*[@id="endtime"]').send_keys(sheet.col_values(1, 21, 22)[0])
        self.dr.find_element_by_xpath('//*[@id="livingPlace"]').click()
        self.dr.find_element_by_xpath('//*[@id="starttime"]').send_keys(sheet.col_values(1,20,21)[0])
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="livingPlace"]').click()
        Select(self.dr.find_element_by_xpath('//*[@id="isAttention"]')).select_by_value('0')
        self.dr.find_element_by_xpath('//*[@id="recognitionInfo"]').send_keys(sheet.col_values(1,11,12)[0])
        self.dr.find_element_by_xpath('//*[@id="monitorReason"]').send_keys(sheet.col_values(1,12,13)[0])
        Select(self.dr.find_element_by_xpath('//*[@id="isNotify"]')).select_by_value('0')
        self.dr.find_element_by_xpath('//*[@id="processingScheme"]').send_keys(sheet.col_values(1,13,14)[0])
        self.dr.find_element_by_xpath('//*[@id="note"]').send_keys(sheet.col_values(1,14,15)[0])
        self.dr.find_element_by_xpath('//*[@id="supervIdcardNo"]').send_keys(sheet.col_values(1,15,16)[0])
        self.dr.find_element_by_xpath('//*[@id="supervName"]').send_keys(sheet.col_values(1,16,17)[0])
        self.dr.find_element_by_xpath('//*[@id="supervWx"]').send_keys(sheet.col_values(1,17,18)[0])
        self.dr.find_element_by_xpath('//*[@id="supervBeWx"]').send_keys(sheet.col_values(1,18,19)[0])
        self.dr.find_element_by_xpath('//*[@id="reportCycle"]').send_keys(sheet.col_values(1,19,20)[0])
        self.dr.find_element_by_xpath(saveBtn).click()
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        time.sleep(2)
        self.assertEqual(sheet_prompt_message.col_values(1, 1, 2)[0],
                         self.dr.find_element_by_xpath('//*[@id="gritter-item-1"]/div[2]/div[2]/p').text, '新增成功提示信息校验')
        print('人口管理-自定义人员：新增功能正常')

    def test02_zidingyi_search_name(self):
        self.zidingyi_search()
        search_value_name=sheet.col_values(1,0,1)[0]
        name_path=sheet.col_values(1,1,2)[0]
        self.dr.find_element_by_xpath(name_path).send_keys(search_value_name)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        column = 5
        self.pagination_num(paginal_number,search_value_name,column)
        self.dr.find_element_by_xpath(reset).click()
        time.sleep(2)
        self.dr.find_element_by_xpath(search).click()
        self.assertEqual('',self.dr.find_element_by_xpath(name_path).get_attribute('value'),'姓名-重置功能异常')
        print('人口管理-自定义人员：姓名条件查询')

    def test03_zidingyi_search_cardid(self):
        self.zidingyi_search()
        search_value_cardid = sheet.col_values(1,2,3)[0]
        cardid_path=sheet.col_values(1,3,4)[0]
        self.dr.find_element_by_xpath(cardid_path).send_keys(search_value_cardid)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(10)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        column = 4
        self.pagination_num(paginal_number,search_value_cardid,column)
        self.dr.find_element_by_xpath(reset).click()
        time.sleep(2)
        self.dr.find_element_by_xpath(search).click()
        self.assertEqual('',self.dr.find_element_by_xpath(cardid_path).get_attribute('value'),'身份证-重置功能异常')
        print('人口管理-自定义人员：身份证号条件查询')

    def test04_zidingyi_search_age(self):
        self.zidingyi_search()
        search_value_age1 = sheet.col_values(1,4,5)[0]
        search_value_age2=sheet.col_values(1,6,7)[0]
        self.dr.find_element_by_xpath(sheet.col_values(1,5,6)[0]).send_keys(search_value_age1)
        self.dr.find_element_by_xpath(sheet.col_values(1,7,8)[0]).send_keys(search_value_age2)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(10)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        column = 7
        self.pagination_num(paginal_number,search_value_age1,column)
        self.dr.find_element_by_xpath(reset).click()
        time.sleep(2)
        self.dr.find_element_by_xpath(search).click()
        self.assertEqual('',self.dr.find_element_by_xpath(sheet.col_values(1,5,6)[0]).get_attribute('value'),'年龄段-重置功能异常')
        self.assertEqual('',self.dr.find_element_by_xpath(sheet.col_values(1,7,8)[0]).get_attribute('value'),'年龄段-重置功能异常')
        print('人口管理-自定义人员：年龄条件查询')

    def test05_zidingyi_search_all(self):
        self.zidingyi_search()
        search_value_name = sheet.col_values(1, 0, 1)[0]
        name_path = sheet.col_values(1, 1, 2)[0]
        self.dr.find_element_by_xpath(name_path).send_keys(search_value_name)
        search_value_cardid = sheet.col_values(1, 2, 3)[0]
        cardid_path = sheet.col_values(1, 3, 4)[0]
        self.dr.find_element_by_xpath(cardid_path).send_keys(search_value_cardid)
        search_value_age1 = sheet.col_values(1, 4, 5)[0]
        search_value_age2 = sheet.col_values(1, 6, 7)[0]
        self.dr.find_element_by_xpath(sheet.col_values(1, 5, 6)[0]).send_keys(search_value_age1)
        self.dr.find_element_by_xpath(sheet.col_values(1, 7, 8)[0]).send_keys(search_value_age2)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(paginal_number,search_value_age1,7)
        self.pagination_num(paginal_number, search_value_cardid, 4)
        self.pagination_num(paginal_number, search_value_name, 5)
        self.dr.find_element_by_xpath(reset).click()
        time.sleep(2)
        self.dr.find_element_by_xpath(search).click()
        self.assertEqual('', self.dr.find_element_by_xpath(name_path).get_attribute('value'), '姓名-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(cardid_path).get_attribute('value'), '身份证-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1, 5, 6)[0]).get_attribute('value'),
                         '年龄段-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1, 7, 8)[0]).get_attribute('value'),
                         '年龄段-重置功能异常')
        print('人口管理-自定义人员：多条件组合查询')

    def test06_zidingyi_details(self):
        self.zidingyi_search()
        search_value_cardid = sheet.col_values(1, 2, 3)[0]
        cardid_path = sheet.col_values(1, 3, 4)[0]
        self.dr.find_element_by_xpath(cardid_path).send_keys(search_value_cardid)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(10)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 4
        self.pagination_num(paginal_number, search_value_cardid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        self.assertEqual(search_value_cardid,self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').get_attribute('value'),'详情页面校验身份证号异常')
        self.assertEqual(sheet.col_values(1,0,1)[0],self.dr.find_element_by_xpath('//*[@id="xm"]').text,'详情页面校验姓名异常')
        self.assertEqual(sheet.col_values(1,8,9)[0],self.dr.find_element_by_xpath('//*[@id="personsType"]').get_attribute('value'),'详情页面校验类别异常')
        self.dr.find_element_by_xpath(goback).click()
        self.assertEqual('自定义人员监控', self.dr.find_element_by_xpath(page_title).text,
                         '自定义人员')
        print('人口管理-自定义人员：详情功能正常')

    def test07_zidingyi_eidt(self):
        self.zidingyi_search()
        self.zidingyi_search()
        search_value_cardid = sheet.col_values(1, 2, 3)[0]
        cardid_path = sheet.col_values(1, 3, 4)[0]
        self.dr.find_element_by_xpath(cardid_path).send_keys(search_value_cardid)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(10)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 4
        self.pagination_num(paginal_number, search_value_cardid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').clear()
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(sheet.col_values(2,2,3)[0])
        self.dr.find_element_by_xpath('//*[@id="customForm"]/div[1]/div[2]/div/div[1]/div[2]/a').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="personsType"]').clear()
        self.dr.find_element_by_xpath('//*[@id="personsType"]').send_keys(sheet.col_values(1, 8, 9)[0])
        self.dr.find_element_by_xpath('//*[@id="credentials"]').clear()
        self.dr.find_element_by_xpath('//*[@id="credentials"]').send_keys(sheet.col_values(1, 9, 10)[0])
        self.dr.find_element_by_xpath('//*[@id="livingPlace"]').clear()
        self.dr.find_element_by_xpath('//*[@id="livingPlace"]').send_keys(sheet.col_values(1, 10, 11)[0])
        Select(self.dr.find_element_by_xpath('//*[@id="isLimit"]')).select_by_value('1')
        # js = "$('input[id=txtBeginDate]').attr('readonly','')"
        # self.dr.execute_script(js)
        self.dr.find_element_by_xpath('//*[@id="endtime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="endtime"]').send_keys(sheet.col_values(1, 21, 22)[0])
        self.dr.find_element_by_xpath('//*[@id="livingPlace"]').click()
        self.dr.find_element_by_xpath('//*[@id="starttime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="starttime"]').send_keys(sheet.col_values(1, 20, 21)[0])
        self.dr.find_element_by_xpath('//*[@id="livingPlace"]').click()
        Select(self.dr.find_element_by_xpath('//*[@id="isAttention"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="recognitionInfo"]').clear()
        self.dr.find_element_by_xpath('//*[@id="recognitionInfo"]').send_keys(sheet.col_values(1, 11, 12)[0])
        self.dr.find_element_by_xpath('//*[@id="monitorReason"]').clear()
        self.dr.find_element_by_xpath('//*[@id="monitorReason"]').send_keys(sheet.col_values(1, 12, 13)[0])
        Select(self.dr.find_element_by_xpath('//*[@id="isNotify"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="processingScheme"]').clear()
        self.dr.find_element_by_xpath('//*[@id="processingScheme"]').send_keys(sheet.col_values(1, 13, 14)[0])
        self.dr.find_element_by_xpath('//*[@id="note"]').clear()
        self.dr.find_element_by_xpath('//*[@id="note"]').send_keys(sheet.col_values(1, 14, 15)[0])
        self.dr.find_element_by_xpath('//*[@id="supervIdcardNo"]').clear()
        self.dr.find_element_by_xpath('//*[@id="supervIdcardNo"]').send_keys(sheet.col_values(1, 15, 16)[0])
        self.dr.find_element_by_xpath('//*[@id="supervName"]').clear()
        self.dr.find_element_by_xpath('//*[@id="supervName"]').send_keys(sheet.col_values(1, 16, 17)[0])
        self.dr.find_element_by_xpath('//*[@id="supervWx"]').clear()
        self.dr.find_element_by_xpath('//*[@id="supervWx"]').send_keys(sheet.col_values(1, 17, 18)[0])
        self.dr.find_element_by_xpath('//*[@id="supervBeWx"]').clear()
        self.dr.find_element_by_xpath('//*[@id="supervBeWx"]').send_keys(sheet.col_values(1, 18, 19)[0])
        self.dr.find_element_by_xpath('//*[@id="reportCycle"]').clear()
        self.dr.find_element_by_xpath('//*[@id="reportCycle"]').send_keys(sheet.col_values(1, 19, 20)[0])
        self.dr.find_element_by_xpath(saveBtn).click()
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        time.sleep(2)
        self.assertEqual(sheet_prompt_message.col_values(1, 1, 2)[0],
                         self.dr.find_element_by_xpath('//*[@id="gritter-item-1"]/div[2]/div[2]/p').text, '编辑修改提示信息校验')
        print('人口管理-自定义人员：编辑修改功能正常')


    def test08_zidingyi_delete(self):
        self.zidingyi_search()
        search_value_cardid = sheet.col_values(2, 2, 3)[0]
        cardid_path = sheet.col_values(1, 3, 4)[0]
        self.dr.find_element_by_xpath(cardid_path).send_keys(search_value_cardid)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(15)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 4
        self.pagination_num(paginal_number, search_value_cardid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        time.sleep(2)
        self.dr.switch_to.default_content()
        time.sleep(1)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        print('人口管理-自定义人员：删除功能正常')

if __name__ == '__main__':
    unittest.main()