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
import HTMLTestRunner
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

# xlsfile=work_space+r'\\'+sheet_menu.col_values(6,50,51)[0]
# excel = xlrd.open_workbook(xlsfile)
# global sheet
# sheet = excel.sheet_by_name('线索登记')

class TESTCASE_XSDJ(TESTCASE):
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

    def xsdj_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,46,47)[0]).click()
        time.sleep(5)
        self.assertEqual('社区警务',self.dr.find_element_by_xpath(currMenupath).text, '社区警务')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,46,47)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,46,47)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('线索登记列表', self.dr.find_element_by_xpath(page_title).text,
                         '线索登记')

    def test1_xsdj_add(self):
        self.xsdj_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        add_value_clueName='航空酒店入室盗窃'
        self.dr.find_element_by_xpath('//*[@id="clueName"]').send_keys(add_value_clueName)
        Select(self.dr.find_element_by_xpath('//*[@id="clueType"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="provideTime"]').send_keys('2018-09-13')
        self.dr.find_element_by_xpath('//*[@id="clueContent"]').send_keys('15:43电话有人就航空酒店入室盗窃案提供线索，据目击者描述昨晚发现有人晚上在案发地点踩点')
        self.dr.find_element_by_xpath('//*[@id="providesIdCard"]').send_keys('370123198009220510')
        self.dr.find_element_by_xpath('//*[@id="providesName"]').send_keys('荆帅')
        Select(self.dr.find_element_by_xpath('//*[@id="providesSex"]')).select_by_value('2')
        self.dr.find_element_by_xpath('//*[@id="providesZzxz"]').send_keys('拉萨城关区康昂东路14号')
        self.dr.find_element_by_xpath('//*[@id="providesContactWay"]').send_keys('15747457458')
        self.dr.find_element_by_xpath('//*[@id="providesUnit"]').send_keys('翰林药坊')
        self.dr.find_element_by_xpath('//*[@id="policeUnitName"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_46_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_48_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="policeName"]').send_keys('王朝')
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        self.dr.implicitly_wait(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual('线索登记列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '校验返回功能')
        print('社区警务-线索登记：新增功能正常')

    def test2_xsdj_search_clueName(self):
        self.xsdj_search()
        search_value_clueName='航空酒店入室盗窃'
        self.dr.find_element_by_xpath('//*[@id="clueName"]').send_keys(search_value_clueName)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_clueName, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[11]/a').click()
        self.assertEqual(search_value_clueName,self.dr.find_element_by_xpath('//*[@id="clueName"]').get_attribute('value'),'校验详情页面线索名称')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('线索登记列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '校验返回功能')
        print('社区警务-线索登记：线索名称条件查询功能正常')

    def test3_xsdj_search_clueType(self):
        self.xsdj_search()
        option_chioce=Select(self.dr.find_element_by_xpath('//*[@id="clueType"]'))
        option_chioce.select_by_value('1')
        search_value_clueType=option_chioce.first_selected_option.text
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_clueType, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[11]/a').click()
        self.assertEqual(search_value_clueType,self.dr.find_element_by_xpath('//*[@id="clueType"]/option[2]').text,'校验详情页面线索类型')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('线索登记列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '校验返回功能')
        print('社区警务-线索登记：线索类型条件查询功能正常')

    def test4_xsdj_search_clueContent(self):
        self.xsdj_search()
        search_value_clueContent='航空酒店入室盗窃案'
        self.dr.find_element_by_xpath('//*[@id="clueContent"]').send_keys(search_value_clueContent)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        # paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        # column = 3
        # self.pagination_num(paginal_number, search_value_clueContent, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[11]/a').click()
        self.assertIn(search_value_clueContent,self.dr.find_element_by_xpath('//*[@id="clueContent"]').text,'校验详情页面线索内容')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('线索登记列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '校验返回功能')
        print('社区警务-线索登记：线索内容条件查询功能正常')

    def test5_xsdj_search_provideTime(self):
        self.xsdj_search()
        search_value_provideTime='2018-09-13'
        self.dr.find_element_by_xpath('//*[@id="provideTimeA"]').send_keys(search_value_provideTime)
        self.dr.find_element_by_xpath('//*[@id="provideTimeB"]').send_keys(search_value_provideTime)
        self.dr.find_element_by_xpath('//*[@id="providesName"]').click()
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_provideTime, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[11]/a').click()
        self.assertEqual(search_value_provideTime,self.dr.find_element_by_xpath('//*[@id="provideTime"]').get_attribute('value'),'校验详情页面线索提供时间')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('线索登记列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '校验返回功能')
        print('社区警务-线索登记：线索提供时间条件查询功能正常')

    def test6_xsdj_search_providesName(self):
        self.xsdj_search()
        search_value_providesName='荆帅'
        self.dr.find_element_by_xpath('//*[@id="providesName"]').send_keys(search_value_providesName)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 6
        self.pagination_num(paginal_number, search_value_providesName, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[11]/a').click()
        self.assertEqual(search_value_providesName,self.dr.find_element_by_xpath('//*[@id="providesName"]').get_attribute('value'),'校验详情页面线索名称')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('线索登记列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '校验返回功能')
        print('社区警务-线索登记：线索名称条件查询功能正常')

    def test7_xsdj_search_policeName(self):
        self.xsdj_search()
        search_value_policeName='王朝'
        self.dr.find_element_by_xpath('//*[@id="policeName"]').send_keys(search_value_policeName)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 9
        self.pagination_num(paginal_number, search_value_policeName, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[11]/a').click()
        self.assertEqual(search_value_policeName,self.dr.find_element_by_xpath('//*[@id="policeName"]').get_attribute('value'),'校验详情页面线索名称')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('线索登记列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '校验返回功能')
        print('社区警务-线索登记：线索名称条件查询功能正常')

    def test8_xsdj_edit(self):
        self.xsdj_search()
        search_value_clueName='航空酒店入室盗窃'
        self.dr.find_element_by_xpath('//*[@id="clueName"]').send_keys(search_value_clueName)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_clueName, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[11]/a').click()
        edit_value_clueName='航空酒店盗窃案'
        self.dr.find_element_by_xpath('//*[@id="clueName"]').clear()
        self.dr.find_element_by_xpath('//*[@id="clueName"]').send_keys(edit_value_clueName)
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        self.dr.implicitly_wait(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('线索登记列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '校验返回功能')
        print('社区警务-线索登记：编辑功能正常')

    def test9_xsdj_delete(self):
        self.xsdj_search()
        search_value_clueName='航空酒店盗窃案'
        self.dr.find_element_by_xpath('//*[@id="clueName"]').send_keys(search_value_clueName)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_clueName, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('社区警务-线索登记：删除功能正常')

if __name__=='__main__':
    unittest.main()