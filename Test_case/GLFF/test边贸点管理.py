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
from public_package.pubilc_package import sheet_setting, search, reset, currMenupath, page_title, goback, saveBtn , sheet_menu,sheet_prompt_message,work_space
import xlrd
import HTMLTestRunner
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

class TESTCAST_BIANMAODIAN(TESTCASE):


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

    def bianmaodian_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,42,43)[0]).click()
        time.sleep(5)
        self.assertEqual('管理防范',self.dr.find_element_by_xpath(currMenupath).text, '管理防范')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,42,43)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,42,43)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('边贸点管理', self.dr.find_element_by_xpath('/html/body/div[1]/p').text,
                         '边贸点管理')

    def test01_bianmaodian_add(self):
        self.bianmaodian_search()
        self.dr.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/a[2]').click()
        add_value_name='基隆口岸'
        global codeid
        codeid=self.dr.find_element_by_xpath('//*[@id="code"]').get_attribute('value')
        self.dr.find_element_by_xpath('//*[@id="name"]').send_keys(add_value_name)
        self.dr.find_element_by_xpath('//*[@id="location"]').send_keys('西藏自治区吉隆县吉隆镇热索村')
        self.dr.find_element_by_xpath('//*[@id="dailyCheckCount"]').send_keys('999999')
        self.dr.find_element_by_xpath('//*[@id="importantPeriod"]').send_keys('8:30-18:00')
        self.dr.find_element_by_xpath('//*[@id="entryExitPurpose"]').send_keys('贸易')
        self.dr.find_element_by_xpath('//*[@id="tradeCrossingDistChn"]').send_keys('999999')
        self.dr.find_element_by_xpath('//*[@id="tradeCrossingDistVn"]').send_keys('999999')
        Select(self.dr.find_element_by_xpath('//*[@id="ispassVehicle"]')).select_by_value('1')
        Select(self.dr.find_element_by_xpath('//*[@id="ispassNonvehicle"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="societyChn"]').send_keys('吉隆口岸：是中尼边境贸易的通道，位于日喀则地区吉隆县吉隆镇热索村境内')
        self.dr.find_element_by_xpath('//*[@id="malitarySocietyVn"]').send_keys('吉隆口岸：是中尼边境贸易的通道，位于日喀则地区吉隆县吉隆镇热索村境内')
        self.dr.find_element_by_xpath('//*[@id="riskEvaluation"]').send_keys('吉隆口岸：是中尼边境贸易的通道，位于日喀则地区吉隆县吉隆镇热索村境内')
        self.dr.find_element_by_xpath('//*[@id="headName"]').send_keys('马汉')
        self.dr.find_element_by_xpath('//*[@id="headIdCard"]').send_keys('500107198901218926')
        self.dr.find_element_by_xpath('//*[@id="contact"]').send_keys('15847478578')
        self.dr.find_element_by_xpath('//*[@id="dutyTel"]').send_keys('13574587458')
        self.dr.find_element_by_xpath('//*[@id="isHaveCensorate"]').send_keys('吉隆口岸边贸组')
        self.dr.find_element_by_xpath('//*[@id="zrdw"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_360_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_369_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="gxdw"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="gxtreeSelect_360_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="gxtreeSelect_369_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="saveTrade"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual(add_value_name,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,'校验新增、返回和默认排序功能')
        print('管理防范-边贸点管理：新增功能正常')

    def test02_bianmaodian_search_codeid(self):
        self.bianmaodian_search()
        search_value_codeid=codeid
        self.dr.find_element_by_xpath('//*[@id="code"]').send_keys(search_value_codeid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_codeid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        self.assertEqual(search_value_codeid,self.dr.find_element_by_xpath('//*[@id="code"]').get_attribute('value'),'校验详情页面编号')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_codeid,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,'校验返回功能和默认排序')
        print('管理防范-边贸点管理：编号条件查询功能正常')

    def test03_bianmaodian_search_name(self):
        self.bianmaodian_search()
        search_value_name='基隆口岸'
        self.dr.find_element_by_xpath('//*[@id="name"]').send_keys(search_value_name)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_name, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        self.assertEqual(search_value_name,self.dr.find_element_by_xpath('//*[@id="name"]').get_attribute('value'),'校验详情页面名称')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_name,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,'校验返回功能和默认排序')
        print('管理防范-边贸点管理：名称条件查询功能正常')

    def test04_bianmaodian_search_address(self):
        self.bianmaodian_search()
        search_value_address='西藏自治区吉隆县吉隆镇热索村'
        self.dr.find_element_by_xpath('//*[@id="location"]').send_keys(search_value_address)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_address, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        self.assertEqual(search_value_address,self.dr.find_element_by_xpath('//*[@id="location"]').get_attribute('value'),'校验详情页面所在地名和具体方位')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_address,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[5]').text,'校验返回功能和默认排序')
        print('管理防范-边贸点管理：所在地名和具体方位条件查询功能正常')

    def test05_bianmaodian_search_headName(self):
        self.bianmaodian_search()
        search_value_headName='马汉'
        self.dr.find_element_by_xpath('//*[@id="headName"]').send_keys(search_value_headName)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 8
        self.pagination_num(paginal_number, search_value_headName, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        self.assertEqual(search_value_headName,self.dr.find_element_by_xpath('//*[@id="headName"]').get_attribute('value'),'校验详情页面责任人姓名')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_headName,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[8]').text,'校验返回功能和默认排序')
        print('管理防范-边贸点管理：责任人姓名条件查询功能正常')

    def test06_bianmaodian_search_gldw(self):
        self.bianmaodian_search()
        search_value_gldw='执勤业务一科'
        self.dr.find_element_by_xpath('//*[@id="gxdw"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="gxtreeSelect_360_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="gxtreeSelect_369_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 9
        self.pagination_num(paginal_number, search_value_gldw, column)
        print('管理防范-边贸点管理：管理单位条件查询功能正常')

    def test07_bianmaodian_search_zrdw(self):
        self.bianmaodian_search()
        search_value_zrdw='执勤业务一科'
        self.dr.find_element_by_xpath('//*[@id="zrdw"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_360_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_369_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 10
        self.pagination_num(paginal_number, search_value_zrdw, column)
        print('管理防范-边贸点管理：责任单位条件查询功能正常')

    def test08_bianmaodian_edit(self):
        self.bianmaodian_search()
        search_value_codeid=codeid
        self.dr.find_element_by_xpath('//*[@id="code"]').send_keys(search_value_codeid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_codeid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        edit_value_name='基隆边贸'
        self.dr.find_element_by_xpath('//*[@id="name"]').clear()
        self.dr.find_element_by_xpath('//*[@id="name"]').send_keys(edit_value_name)
        self.dr.find_element_by_xpath('//*[@id="saveTrade"]').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual(edit_value_name, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,'校验编辑、返回和默认排序')
        print('管理防范-边贸点管理：编辑功能正常')

    def test09_bianmaodian_delete(self):
        self.bianmaodian_search()
        search_value_codeid=codeid
        self.dr.find_element_by_xpath('//*[@id="code"]').send_keys(search_value_codeid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_codeid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('管理防范-边贸点管理：删除功能正常')

if __name__=='__main__':
    unittest.main()