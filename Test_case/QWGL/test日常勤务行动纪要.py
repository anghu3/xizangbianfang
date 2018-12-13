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
import HTMLTestRunner
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

class TESTCAST_RCQWXDJY(TESTCASE):
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

    def rcqwxdjy_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div/a[2]/div[2]/img[2]').click()
        time.sleep(3)
        self.assertEqual('勤务管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '勤务管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="534"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(3)
        self.assertEqual('日常勤务行动纪要列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '日常勤务行动纪要')

    def test1_rcqwxdjy_add(self):
        self.rcqwxdjy_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        global codeid
        codeid=self.dr.find_element_by_xpath('//*[@id="summaryNo"]').get_attribute('value')
        add_value_name='城东杀人案现场勘察'
        self.dr.find_element_by_xpath('//*[@id="summaryTitle"]').send_keys(add_value_name)
        self.dr.find_element_by_xpath('//*[@id="groupName"]').send_keys('勘察1组')
        Select(self.dr.find_element_by_xpath('//*[@id="summaryType"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="summaryContent"]').send_keys('城东发展大道101号杀人案现场勘察任务')
        self.dr.find_element_by_xpath('//*[@id="serviceTaskNo"]').send_keys('25475635')
        self.dr.find_element_by_xpath('//*[@id="subordinateUnitsName"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_169_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_191_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_192_span"]').click()
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual(codeid, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,
                         '校验新增，返回和默认排序')
        print('勤务管理-日常勤务行动纪要：新增功能正常')

    def test2_rcqwxdjy_search_summaryNo(self):
        self.rcqwxdjy_search()
        search_value_summaryNo=codeid
        self.dr.find_element_by_xpath('//*[@id="summaryNo"]').send_keys(search_value_summaryNo)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_summaryNo, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/a').click()
        self.assertEqual(search_value_summaryNo,self.dr.find_element_by_xpath('//*[@id="summaryNo"]').get_attribute('value'),'校验详情页面纪要编号')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_summaryNo, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,'校验返回和默认排序')
        print('勤务管理-日常勤务行动纪要：纪要编号条件查询功能正常')

    def test3_rcqwxdjy_search_groupName(self):
        self.rcqwxdjy_search()
        search_value_groupName='勘察1组'
        self.dr.find_element_by_xpath('//*[@id="groupName"]').send_keys(search_value_groupName)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 6
        self.pagination_num(paginal_number, search_value_groupName, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/a').click()
        self.assertEqual(search_value_groupName,self.dr.find_element_by_xpath('//*[@id="groupName"]').get_attribute('value'),'校验详情页面编组名称')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_groupName, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[6]').text,'校验返回和默认排序')
        print('勤务管理-日常勤务行动纪要：编组名称条件查询功能正常')

    def test4_rcqwxdjy_search_summaryTitle(self):
        self.rcqwxdjy_search()
        search_value_summaryTitle='城东杀人案现场勘察'
        self.dr.find_element_by_xpath('//*[@id="summaryTitle"]').send_keys(search_value_summaryTitle)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_summaryTitle, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/a').click()
        self.assertEqual(search_value_summaryTitle,self.dr.find_element_by_xpath('//*[@id="summaryTitle"]').get_attribute('value'),'校验详情页面纪要标题')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_summaryTitle, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,'校验返回和默认排序')
        print('勤务管理-日常勤务行动纪要：纪要标题条件查询功能正常')

    def test5_rcqwxdjy_edit(self):
        self.rcqwxdjy_search()
        search_value_summaryNo=codeid
        self.dr.find_element_by_xpath('//*[@id="summaryNo"]').send_keys(search_value_summaryNo)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_summaryNo, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/a').click()
        edit_value_summaryTitle='城东杀人案勘察任务'
        self.dr.find_element_by_xpath('//*[@id="summaryTitle"]').clear()
        self.dr.find_element_by_xpath('//*[@id="summaryTitle"]').send_keys(edit_value_summaryTitle)
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual(edit_value_summaryTitle,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,'校验编辑、返回和默认排序')
        print('勤务管理-日常勤务行动纪要：编辑功能正常')

    def test6_rcqwxdjy_delete(self):
        self.rcqwxdjy_search()
        search_value_summaryNo=codeid
        self.dr.find_element_by_xpath('//*[@id="summaryNo"]').send_keys(search_value_summaryNo)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_summaryNo, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('勤务管理-日常勤务行动纪要：删除功能正常')

if __name__=='__main__':
    unittest.main()