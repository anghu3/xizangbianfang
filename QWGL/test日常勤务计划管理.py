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

class TESTCAST_RCQWJHGL(TESTCASE):
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

    def rcqwjhgl_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div/a[2]/div[2]/img[2]').click()
        time.sleep(3)
        self.assertEqual('勤务管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '勤务管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="533"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(3)
        self.assertEqual('日常勤务计划列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '日常勤务计划管理')

    def test1_rcqwjhgl_add(self):
        self.rcqwjhgl_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        add_value_name='贡嘎国际机场执勤任务'
        global codeid
        codeid=self.dr.find_element_by_xpath('//*[@id="taskId"]').get_attribute('value')
        print(codeid)
        self.dr.find_element_by_xpath('//*[@id="dutyDate"]').send_keys('2018-09-10')
        self.dr.find_element_by_xpath('//*[@id="startTime"]').click()
        self.dr.find_element_by_xpath('//*[@id="startTime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="startTime"]').send_keys('08:00:00')
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="endTime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="endTime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="endTime"]').send_keys('21:30:00')
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="dutyPlace"]').click()
        self.dr.find_element_by_xpath('//*[@id="dutyPlace"]').send_keys('拉萨贡嘎国际机场')
        self.dr.find_element_by_xpath('//*[@id="taskName"]').send_keys(add_value_name)
        self.dr.find_element_by_xpath('//*[@id="taskContent"]').send_keys('拉萨贡嘎国际机场定点定期执勤任务，防止意外突发情况造成人员伤亡和公民财产损失。')
        self.dr.find_element_by_xpath('//*[@id="dutyGroupName"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="dutytreeSelect_1_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="dutytreeSelect_6_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="dutytreeSelect_7_span"]').click()
        time.sleep(2)
        self.assertEqual('包涵',self.dr.find_element_by_xpath('//*[@id="leadingCadre"]').get_attribute('value'),'校验和部队组成信息管理模块的关联')
        self.assertEqual('山南支队',self.dr.find_element_by_xpath('//*[@id="subordinateUnitsName"]').get_attribute('value'),'校验和部队组成信息管理模块的关联')
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual(codeid,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,'校验新增，返回和默认排序')
        print('勤务管理-日常勤务计划管理：新增功能正常')

    def test2_rcqwjhgl_search_codeid(self):
        self.rcqwjhgl_search()
        search_value_codeid=codeid
        self.dr.find_element_by_xpath('//*[@id="taskId"]').send_keys(search_value_codeid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_codeid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(search_value_codeid,self.dr.find_element_by_xpath('//*[@id="taskId"]').get_attribute('value'),'校验详情页面任务编号')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_codeid,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,'校验返回和默认排序')
        print('勤务管理-日常勤务计划管理：任务编号条件查询功能正常')

    def test3_rcqwjhgl_search_dutyPlace(self):
        self.rcqwjhgl_search()
        search_value_dutyPlace='拉萨贡嘎国际机场'
        self.dr.find_element_by_xpath('//*[@id="dutyPlace"]').send_keys(search_value_dutyPlace)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_dutyPlace, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(search_value_dutyPlace,self.dr.find_element_by_xpath('//*[@id="dutyPlace"]').get_attribute('value'),'校验详情页面任务编号')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_dutyPlace,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,'校验返回和默认排序')
        print('勤务管理-日常勤务计划管理：任务编号条件查询功能正常')

    def test4_rcqwjhgl_search_ssdw(self):
        self.rcqwjhgl_search()
        search_value_ssdw='山南支队'
        self.dr.find_element_by_xpath('//*[@id="subordinateUnitsName"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_ssdw, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(search_value_ssdw,self.dr.find_element_by_xpath('//*[@id="subordinateUnitsName"]').get_attribute('value'),'校验详情页面任务编号')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_ssdw,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[5]').text,'校验返回和默认排序')
        print('勤务管理-日常勤务计划管理：任务编号条件查询功能正常')

    def test5_rcqwjhgl_search_dutyGroupName(self):
        self.rcqwjhgl_search()
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
        column = 9
        self.pagination_num(paginal_number, search_value_dutyGroupName, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(search_value_dutyGroupName,self.dr.find_element_by_xpath('//*[@id="dutyGroupName"]').get_attribute('value'),'校验详情页面任务编号')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_dutyGroupName,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[9]').text,'校验返回和默认排序')
        print('勤务管理-日常勤务计划管理：任务编号条件查询功能正常')

    def test6_rcqwjhgl_search_taskName(self):
        self.rcqwjhgl_search()
        search_value_taskName='贡嘎国际机场执勤任务'
        self.dr.find_element_by_xpath('//*[@id="taskName"]').send_keys(search_value_taskName)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 6
        self.pagination_num(paginal_number, search_value_taskName, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(search_value_taskName,self.dr.find_element_by_xpath('//*[@id="taskName"]').get_attribute('value'),'校验详情页面任务编号')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_taskName,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[6]').text,'校验返回和默认排序')
        print('勤务管理-日常勤务计划管理：任务编号条件查询功能正常')

    def test7_rcqwjhgl_edit(self):
        self.rcqwjhgl_search()
        search_value_codeid=codeid
        self.dr.find_element_by_xpath('//*[@id="taskId"]').send_keys(search_value_codeid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_codeid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        edit_value_taskname='贡嘎机场执勤任务'
        edit_value_taskplace='拉萨贡嘎机场'
        self.dr.find_element_by_xpath('//*[@id="dutyPlace"]').clear()
        self.dr.find_element_by_xpath('//*[@id="dutyPlace"]').send_keys(edit_value_taskplace)
        self.dr.find_element_by_xpath('//*[@id="taskName"]').clear()
        self.dr.find_element_by_xpath('//*[@id="taskName"]').send_keys(edit_value_taskname)
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual(edit_value_taskplace,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text, '校验编辑、返回和默认排序')
        self.assertEqual(edit_value_taskname, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[6]').text,'校验编辑、返回和默认排序')
        print('勤务管理-日常勤务计划管理：编辑功能正常')

    def test8_rcqwjhgl_delete(self):
        self.rcqwjhgl_search()
        search_value_codeid=codeid
        self.dr.find_element_by_xpath('//*[@id="taskId"]').send_keys(search_value_codeid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_codeid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('勤务管理-日常勤务计划管理：删除功能正常')

if __name__=='__main__':
    unittest.main()