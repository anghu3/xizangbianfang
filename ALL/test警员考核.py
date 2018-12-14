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
import HTMLTestRunner
import xlrd
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

xlsfile=work_space+r'\\'+sheet_menu.col_values(6,79,80)[0]
excel = xlrd.open_workbook(xlsfile)
global sheet
sheet = excel.sheet_by_name('警员考核')

class TESTCAST_JYKH(TESTCASE):

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

    def jykh_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,79,80)[0]).click()
        time.sleep(5)
        self.assertEqual('警员绩效考核',self.dr.find_element_by_xpath(currMenupath).text, '警员绩效考核')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,79,80)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,79,80)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('考核指标模板周期列表', self.dr.find_element_by_xpath(page_title).text,
                         '考核指标模板周期列表')

    def test1_jykh_add(self):
        self.jykh_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        self.dr.find_element_by_xpath('//*[@id="templateName"]').send_keys(sheet.col_values(1,0,1)[0])
        self.dr.find_element_by_xpath('//*[@id="assesmentRange"]').send_keys(sheet.col_values(1,2,3)[0])
        self.dr.find_element_by_xpath('//*[@id="assesmentPeriod"]').send_keys(sheet.col_values(1,3,4)[0])
        self.dr.find_element_by_xpath('//*[@id="templateCompactor"]').send_keys(sheet.col_values(1,1,2)[0])
        self.dr.find_element_by_xpath('//*[@id="templateTime"]').click()
        self.dr.find_element_by_xpath('//*[@id="templateTime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="templateTime"]').send_keys(sheet.col_values(1,5,6)[0])
        self.dr.find_element_by_xpath('//*[@id="templateCompactor"]').click()
        Select(self.dr.find_element_by_xpath('//*[@id="available"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="targetStandard"]').send_keys(sheet.col_values(1,4,5)[0])
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('执勤人员考核模板',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[2]').text,'校验新增、返回和默认排序')
        print('社区警务-警员考核：新增功能正常')

    def test2_jykh_search_templateName(self):
        self.jykh_search()
        search_value_templateName='执勤人员考核模板'
        self.dr.find_element_by_xpath('//*[@id="templateName"]').send_keys(search_value_templateName)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 2
        self.pagination_num(paginal_number, search_value_templateName, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[8]/a').click()
        self.assertEqual(search_value_templateName,self.dr.find_element_by_xpath('//*[@id="templateName"]').get_attribute('value'),'校验详情页面模板名称')
        print('社区警务-警员考核：考核模板名称条件查询功能正常')

    def test3_jykh_search_templateCompactor(self):
        self.jykh_search()
        search_value_templateCompactor='包拯'
        self.dr.find_element_by_xpath('//*[@id="templateCompactor"]').send_keys(search_value_templateCompactor)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_templateCompactor, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[8]/a').click()
        self.assertEqual(search_value_templateCompactor,self.dr.find_element_by_xpath('//*[@id="templateCompactor"]').get_attribute('value'),'校验详情页面模板名称')
        print('社区警务-警员考核：考核模板名称条件查询功能正常')

    def test4_jykh_search_templateTime(self):
        self.jykh_search()
        search_value_templateTime='2018-09-13'
        self.dr.find_element_by_xpath('//*[@id="templateTimeA"]').send_keys(search_value_templateTime)
        self.dr.find_element_by_xpath('//*[@id="templateTimeB"]').send_keys(search_value_templateTime)
        self.dr.find_element_by_xpath('//*[@id="templateCompactor"]').click()
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 7
        self.pagination_num(paginal_number, search_value_templateTime, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[8]/a').click()
        self.assertIn(search_value_templateTime,self.dr.find_element_by_xpath('//*[@id="templateTime"]').get_attribute('value'),'校验详情页面模板编制时间')
        print('社区警务-警员考核：模板编制时间条件查询功能正常')

    def test5_jykh_edit(self):
        self.jykh_search()
        search_value_templateName='执勤人员考核模板'
        self.dr.find_element_by_xpath('//*[@id="templateName"]').send_keys(search_value_templateName)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 2
        self.pagination_num(paginal_number, search_value_templateName, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[8]/a').click()
        self.dr.find_element_by_xpath('//*[@id="templateName"]').clear()
        self.dr.find_element_by_xpath('//*[@id="templateName"]').send_keys('执勤警员考核模板')
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        time.sleep(3)
        print('社区警务-警员考核：编辑功能正常')

    def test6_jykh_delete(self):
        self.jykh_search()
        search_value_templateName='执勤警员考核模板'
        self.dr.find_element_by_xpath('//*[@id="templateName"]').send_keys(search_value_templateName)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 2
        self.pagination_num(paginal_number, search_value_templateName, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('社区警务-警员考核：删除功能正常')

if __name__=='__main__':
    unittest.main()