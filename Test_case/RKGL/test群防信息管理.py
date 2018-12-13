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
sheet = excel.sheet_by_name('群防信息管理')

class TESTCAST_QUNFANGGUANLI(TESTCASE):
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

    def qunfangxinxiguanli_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,31,32)[0]).click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath(currMenupath).text, '人口管理')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,31,32)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,31,32)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('群防信息管理列表', self.dr.find_element_by_xpath(page_title).text,
                         '群防信息管理')

    def test01_qunfangxinxiguanli_add(self):
        self.qunfangxinxiguanli_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        self.dr.find_element_by_xpath('//*[@id="infoCollectIp"]').send_keys(sheet.col_values(1,6,7)[0])
        self.dr.find_element_by_xpath('//*[@id="infoCollectPerson"]').send_keys(sheet.col_values(1,7,8)[0])
        self.dr.find_element_by_xpath('//*[@id="infoSort"]').send_keys(sheet.col_values(1,8,9)[0])
        self.dr.find_element_by_xpath('//*[@id="infoKeyword"]').send_keys(sheet.col_values(1,9,10)[0])
        self.dr.find_element_by_xpath('//*[@id="infoLabel"]').send_keys(sheet.col_values(1,10,11)[0])
        self.dr.find_element_by_xpath('//*[@id="infoValueEvaluate"]').send_keys(sheet.col_values(1,11,12)[0])
        self.dr.find_element_by_xpath('//*[@id="infoRemark"]').send_keys(sheet.col_values(1,12,13)[0])
        self.dr.find_element_by_xpath(saveBtn).click()
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        time.sleep(2)
        self.assertEqual(sheet_prompt_message.col_values(1, 4, 5)[0],
                         self.dr.find_element_by_xpath('//*[@id="gritter-item-1"]/div[2]/div[2]/p').text, '新增成功提示信息校验')
        print('人口管理-群防信息管理：新增功能正常')

    def test02_qunfangxinxiguanli_search_infoLabel(self):
        self.qunfangxinxiguanli_search()
        search_value_infoLabel=sheet.col_values(1,0,1)[0]
        infoLabel_path=sheet.col_values(1,1,2)[0]
        self.dr.find_element_by_xpath(infoLabel_path).send_keys(search_value_infoLabel)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        column = 6
        self.pagination_num(paginal_number, search_value_infoLabel, column)
        self.dr.find_element_by_xpath(reset).click()
        time.sleep(2)
        self.dr.find_element_by_xpath(search).click()
        self.assertEqual('',self.dr.find_element_by_xpath(infoLabel_path).get_attribute('value'),'信息标注-重置功能异常')
        print('人口管理-群防信息管理：信息标注条件查询功能正常')

    def test03_qunfangxinxiguanli_search_infoKeyword(self):
        self.qunfangxinxiguanli_search()
        search_value_infoKeyword=sheet.col_values(1,2,3)[0]
        infoKeyword_path=sheet.col_values(1,3,4)[0]
        self.dr.find_element_by_xpath(infoKeyword_path).send_keys(search_value_infoKeyword)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        column = 5
        self.pagination_num(paginal_number, search_value_infoKeyword, column)
        self.dr.find_element_by_xpath(reset).click()
        time.sleep(2)
        self.dr.find_element_by_xpath(search).click()
        self.assertEqual('',self.dr.find_element_by_xpath(infoKeyword_path).get_attribute('value'),'信息关键词-重置功能异常')
        print('人口管理-群防信息管理：信息关键词条件查询功能正常')

    def test04_qunfangxinxiguanli_search_infoSort(self):
        self.qunfangxinxiguanli_search()
        search_value_infoSort=sheet.col_values(1,4,5)[0]
        infoSort_path=sheet.col_values(1,5,6)[0]
        self.dr.find_element_by_xpath(infoSort_path).send_keys(search_value_infoSort)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        column = 4
        self.pagination_num(paginal_number, search_value_infoSort, column)
        self.dr.find_element_by_xpath(reset).click()
        time.sleep(2)
        self.dr.find_element_by_xpath(search).click()
        self.assertEqual('',self.dr.find_element_by_xpath(infoSort_path).get_attribute('value'),'信息类别-重置功能异常')
        print('人口管理-群防信息管理：信息关键词条件查询功能正常')

    def test05_qunfangxinxiguanli_search_infoValueEvaluate(self):
        self.qunfangxinxiguanli_search()
        search_value_infoValueEvaluate = sheet.col_values(1, 13, 14)[0]
        infoValueEvaluate_path=sheet.col_values(1,14,15)[0]
        self.dr.find_element_by_xpath(infoValueEvaluate_path).send_keys(search_value_infoValueEvaluate)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 3
        self.pagination_num(paginal_number, search_value_infoValueEvaluate, column)
        self.dr.find_element_by_xpath(reset).click()
        time.sleep(2)
        self.dr.find_element_by_xpath(search).click()
        self.assertEqual('',self.dr.find_element_by_xpath(infoValueEvaluate_path).get_attribute('value'),'信息价值评估-重置功能异常')
        print('人口管理-群防信息管理：信息价值评估-条件查询功能正常')

    def test06_qunfangxinxiguanli_search_all(self):
        self.qunfangxinxiguanli_search()
        search_value_infoLabel = sheet.col_values(1, 0, 1)[0]
        infoLabel_path = sheet.col_values(1, 1, 2)[0]
        self.dr.find_element_by_xpath(infoLabel_path).send_keys(search_value_infoLabel)
        search_value_infoKeyword = sheet.col_values(1, 2, 3)[0]
        infoKeyword_path = sheet.col_values(1, 3, 4)[0]
        self.dr.find_element_by_xpath(infoKeyword_path).send_keys(search_value_infoKeyword)
        search_value_infoSort = sheet.col_values(1, 4, 5)[0]
        infoSort_path = sheet.col_values(1, 5, 6)[0]
        self.dr.find_element_by_xpath(infoSort_path).send_keys(search_value_infoSort)
        search_value_infoValueEvaluate = sheet.col_values(1, 13, 14)[0]
        infoValueEvaluate_path = sheet.col_values(1, 14, 15)[0]
        self.dr.find_element_by_xpath(infoValueEvaluate_path).send_keys(search_value_infoValueEvaluate)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        self.pagination_num(paginal_number, search_value_infoValueEvaluate, 3)
        self.pagination_num(paginal_number, search_value_infoSort, 4)
        self.pagination_num(paginal_number, search_value_infoKeyword, 5)
        self.pagination_num(paginal_number, search_value_infoLabel, 6)
        self.dr.find_element_by_xpath(reset).click()
        time.sleep(2)
        self.dr.find_element_by_xpath(search).click()
        self.assertEqual('', self.dr.find_element_by_xpath(infoValueEvaluate_path).get_attribute('value'),
                         '信息价值评估-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(infoSort_path).get_attribute('value'), '信息类别-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(infoKeyword_path).get_attribute('value'), '信息关键词-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(infoLabel_path).get_attribute('value'), '信息标注-重置功能异常')
        print('人口管理-群防信息管理：条件查询功能正常')

    def test07_qunfangxinxiguanli_edit(self):
        self.qunfangxinxiguanli_search()
        search_value_infoLabel = sheet.col_values(1, 0, 1)[0]
        infoLabel_path = sheet.col_values(1, 1, 2)[0]
        self.dr.find_element_by_xpath(infoLabel_path).send_keys(search_value_infoLabel)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 6
        self.pagination_num(paginal_number, search_value_infoLabel, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[7]/a').click()
        self.dr.find_element_by_xpath('//*[@id="infoValueEvaluate"]').clear()
        self.dr.find_element_by_xpath('//*[@id="infoValueEvaluate"]').send_keys('良好')
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual('林峰', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[2]').text, '校验编辑、返回和默认排序')
        self.assertEqual('良好',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,'校验编辑、返回和默认排序')
        print('人口管理-群防信息管理：编辑功能正常')

    def test08_qunfangxinxiguanli_delete(self):
        self.qunfangxinxiguanli_search()
        search_value_infoLabel='宗教'
        search_value_infoLabel = sheet.col_values(1, 0, 1)[0]
        infoLabel_path = sheet.col_values(1, 1, 2)[0]
        self.dr.find_element_by_xpath(infoLabel_path).send_keys(search_value_infoLabel)
        search_value_infoKeyword = sheet.col_values(1, 2, 3)[0]
        infoKeyword_path = sheet.col_values(1, 3, 4)[0]
        self.dr.find_element_by_xpath(infoKeyword_path).send_keys(search_value_infoKeyword)
        search_value_infoSort = sheet.col_values(1, 4, 5)[0]
        infoSort_path = sheet.col_values(1, 5, 6)[0]
        self.dr.find_element_by_xpath(infoSort_path).send_keys(search_value_infoSort)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        self.pagination_num(paginal_number, search_value_infoSort, 4)
        self.pagination_num(paginal_number, search_value_infoKeyword, 5)
        self.pagination_num(paginal_number, search_value_infoLabel, 6)
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
        print('人口管理-群防信息管理：删除功能正常')


if __name__=='__main__':
    unittest.main()