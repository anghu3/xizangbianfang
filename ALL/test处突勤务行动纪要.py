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

class TESTCAST_CTQWXDJY(TESTCASE):
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

    def ctqwxdjy_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div/a[2]/div[2]/img[2]').click()
        time.sleep(3)
        self.assertEqual('勤务管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '勤务管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="536"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(3)
        self.assertEqual('处突勤务行动纪要列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '处突勤务行动纪要')

    def test1_ctqwxdjy_add(self):
        self.ctqwxdjy_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        global codeid
        codeid=self.dr.find_element_by_xpath('//*[@id="taskNo"]').get_attribute('value')
        add_value_taskname='米林县聚众赌博案件'
        self.dr.find_element_by_xpath('//*[@id="taskName"]').send_keys(add_value_taskname)
        self.dr.find_element_by_xpath('//*[@id="dutyDate"]').send_keys('2018-09-10')
        self.dr.find_element_by_xpath('//*[@id="startTime"]').click()
        self.dr.find_element_by_xpath('//*[@id="startTime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="startTime"]').send_keys('14:30:00')
        self.dr.find_element_by_xpath('//*[@id="taskSource"]').click()
        Select(self.dr.find_element_by_xpath('//*[@id="taskSource"]')).select_by_value('1')
        Select(self.dr.find_element_by_xpath('//*[@id="safetyLevel"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="endTime"]').click()
        self.dr.find_element_by_xpath('//*[@id="endTime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="endTime"]').send_keys('18:00:00')
        self.dr.find_element_by_xpath('//*[@id="taskContent"]').click()
        self.dr.find_element_by_xpath('//*[@id="taskContent"]').send_keys('根据电话热线，有人说米林县有人聚众赌博，接到报警立即出警处理。')
        Select(self.dr.find_element_by_xpath('//*[@id="taskSource"]')).select_by_value('1')
        Select(self.dr.find_element_by_xpath('//*[@id="safetyLevel"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="dutyStation"]').send_keys('米林县')
        self.dr.find_element_by_xpath('//*[@id="dutyGroupName"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="dutytreeSelect_1_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="dutytreeSelect_6_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="dutytreeSelect_7_span"]').click()
        time.sleep(1)
        self.assertEqual('包涵',self.dr.find_element_by_xpath('//*[@id="leadingByCadre"]').get_attribute('value'),'校验和部队组成信息管理模块的关联')
        self.dr.find_element_by_xpath('//*[@id="resultRecord"]').send_keys('抓获聚众赌博人员12名，有1人逃脱！')
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual(codeid, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,
                         '校验新增，返回和默认排序')
        print('勤务管理-处突勤务计划管理：新增功能正常')

    def test2_ctqwxdjy_search_date(self):
        self.ctqwxdjy_search()
        search_value_date='2018-09-10'
        self.dr.find_element_by_xpath('//*[@id="zqrq"]').send_keys(search_value_date)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_date, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(search_value_date,self.dr.find_element_by_xpath('//*[@id="dutyDate"]').get_attribute('value'),'校验详情页面日期')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_date, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,'校验返回和默认排序')
        self.assertEqual('米林县聚众赌博案件',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[7]').text,'校验返回和默认排序')
        print('勤务管理-处突勤务计划管理：日期条件查询功能正常')

    def test3_ctqwxdjy_search_codeid(self):
        self.ctqwxdjy_search()
        search_value_codeid=codeid
        self.dr.find_element_by_xpath('//*[@id="taskNo"]').send_keys(search_value_codeid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_codeid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(search_value_codeid,self.dr.find_element_by_xpath('//*[@id="taskNo"]').get_attribute('value'),'校验详情页面任务编号')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_codeid, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,'校验返回和默认排序')
        self.assertEqual('米林县聚众赌博案件',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[7]').text,'校验返回和默认排序')
        print('勤务管理-处突勤务计划管理：任务编号条件查询功能正常')

    def test4_ctqwxdjy_search_safetyLevel(self):
        self.ctqwxdjy_search()
        option_chioce=Select(self.dr.find_element_by_xpath('//*[@id="safetyLevel"]'))
        option_chioce.select_by_value('1')
        search_value_safetyLevel =option_chioce.first_selected_option.text
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_safetyLevel, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(search_value_safetyLevel,self.dr.find_element_by_xpath('//*[@id="safetyLevel"]/option[2]').text,'校验详情页面安全等级')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_safetyLevel, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[5]').text,'校验返回和默认排序')
        self.assertEqual('米林县聚众赌博案件',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[7]').text,'校验返回和默认排序')
        print('勤务管理-处突勤务计划管理：安全等级条件查询功能正常')

    def test5_ctqwxdjy_search_taskname(self):
        self.ctqwxdjy_search()
        search_value_taskname='米林县聚众赌博案件'
        self.dr.find_element_by_xpath('//*[@id="taskName"]').send_keys(search_value_taskname)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 7
        self.pagination_num(paginal_number, search_value_taskname, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(search_value_taskname,self.dr.find_element_by_xpath('//*[@id="taskName"]').get_attribute('value'),'校验详情页面任务名称')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_taskname, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[7]').text,'校验返回和默认排序')
        print('勤务管理-处突勤务计划管理：任务名称条件查询功能正常')

    def test6_ctqwxdjy_search_dutyGroupName(self):
        self.ctqwxdjy_search()
        search_value_dutyGroupName='边防1组'
        self.dr.find_element_by_xpath('//*[@id="dutyGroupName"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="dutytreeSelect_1_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="dutytreeSelect_6_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="dutytreeSelect_7_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 8
        self.pagination_num(paginal_number, search_value_dutyGroupName, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual('BF21001',self.dr.find_element_by_xpath('//*[@id="dutyGroupName"]').get_attribute('value'),'校验详情页面执勤编组')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_dutyGroupName, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[8]').text,'校验返回和默认排序')
        print('勤务管理-处突勤务计划管理：执勤编组条件查询功能正常')

    def test7_ctqwxdjy_edit(self):
        self.ctqwxdjy_search()
        search_value_codeid=codeid
        self.dr.find_element_by_xpath('//*[@id="taskNo"]').send_keys(search_value_codeid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_codeid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        edit_value_taskname='米林县聚众赌博事件'
        self.dr.find_element_by_xpath('//*[@id="taskName"]').clear()
        self.dr.find_element_by_xpath('//*[@id="taskName"]').send_keys(edit_value_taskname)
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        time.sleep(3)
        self.assertEqual(edit_value_taskname,self.dr.find_element_by_xpath('//*[@id="taskName"]').get_attribute('value'),'校验编辑功能')
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(edit_value_taskname,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[7]').text,'校验编辑、返回和默认排序')
        print('勤务管理-处突勤务计划管理：编辑功能正常')

    def test8_ctqwxdjy_delete(self):
        self.ctqwxdjy_search()
        search_value_codeid=codeid
        self.dr.find_element_by_xpath('//*[@id="taskNo"]').send_keys(search_value_codeid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_codeid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('勤务管理-处突勤务计划管理：删除功能正常')

if __name__=='__main__':
    unittest.main()