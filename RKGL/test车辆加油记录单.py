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

class TESTCAST_CLJYJL(TESTCASE):
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

    def cljyjl_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div/a[2]/div[2]/img[2]').click()
        time.sleep(5)
        self.assertEqual('勤务管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '勤务管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="588"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('车辆加油记录单列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '车辆加油记录单')

    def test1_cljyjl_add(self):
        self.cljyjl_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        global codeid
        codeid=self.dr.find_element_by_xpath('//*[@id="reForm"]/div[1]/div[1]/div/input[1]').get_attribute('value')
        add_value_carNo='藏A24567'
        self.dr.find_element_by_xpath('//*[@id="reForm"]/div[1]/div[2]/div/input').send_keys(add_value_carNo)
        Select(self.dr.find_element_by_xpath('//*[@id="oilType"]')).select_by_visible_text('98')
        self.dr.find_element_by_xpath('//*[@id="actualOilAmount"]').send_keys('100')
        self.dr.find_element_by_xpath('//*[@id="reForm"]/div[1]/div[5]/div/input').send_keys('王朝')
        self.dr.find_element_by_xpath('//*[@id="reForm"]/div[1]/div[6]/div/input').click()
        self.dr.find_element_by_xpath('//*[@id="reForm"]/div[1]/div[6]/div/div[2]/ul/li[2]/table/tbody/tr/td[2]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="approver"]').send_keys('包涵')
        self.dr.find_element_by_xpath('//*[@id="approvalTime"]').click()
        self.dr.find_element_by_xpath('//*[@id="approvalTime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="approvalTime"]').send_keys('2018-09-11 16:00:00')
        self.dr.find_element_by_xpath('//*[@id="reForm"]/div[1]/div[8]/div/div[2]/ul/li[2]/table/tbody/tr/td[2]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="reForm"]/div[1]/div[9]/div/input').send_keys('包拯')
        self.dr.find_element_by_xpath('//*[@id="reForm"]/div[1]/div[10]/div/input').click()
        self.dr.find_element_by_xpath('//*[@id="reForm"]/div[1]/div[10]/div/input').clear()
        self.dr.find_element_by_xpath('//*[@id="reForm"]/div[1]/div[10]/div/input').send_keys('2018-09-11 17:00:00')
        self.dr.find_element_by_xpath('//*[@id="reForm"]/div[1]/div[10]/div/div[2]/ul/li[2]/table/tbody/tr/td[1]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual(codeid,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,'校验新增，返回和默认排序')
        print('勤务管理-车辆加油记录单：新增功能正常')

    def test2_cljyjl_search_carNo(self):
        self.cljyjl_search()
        search_value_carNo='藏A24567'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value_carNo)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number,search_value_carNo,column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[11]/a').click()
        self.assertEqual(search_value_carNo,self.dr.find_element_by_xpath('//*[@id="reForm"]/div[1]/div[2]/div/input').get_attribute('value'),'校验详情页面警车编号')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_carNo,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,'校验返回和默认排序')
        print('勤务管理-车辆加油记录单：警车编号条件查询功能正常')

    def test3_cljyjl_search_oiltype(self):
        self.cljyjl_search()
        search_value_oiltype='98'
        Select(self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/div/select')).select_by_visible_text('98')
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number,search_value_oiltype,column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[11]/a').click()
        self.assertEqual(search_value_oiltype,self.dr.find_element_by_xpath('//*[@id="oilType"]/option[4]').text,'校验详情页面油料型号')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_oiltype,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[5]').text,'校验返回和默认排序')
        print('勤务管理-车辆加油记录单：油料型号条件查询功能正常')

    def test4_cljyjl_search_driver(self):
        self.cljyjl_search()
        search_value_driver='王朝'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[3]/div/input').send_keys(search_value_driver)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 7
        self.pagination_num(paginal_number,search_value_driver,column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[11]/a').click()
        self.assertEqual(search_value_driver,self.dr.find_element_by_xpath('//*[@id="reForm"]/div[1]/div[5]/div/input').get_attribute('value'),'校验详情页面驾驶员')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_driver,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[7]').text,'校验返回和默认排序')
        print('勤务管理-车辆加油记录单：驾驶员条件查询功能正常')

    def test5_cljyjl_search_date(self):
        self.cljyjl_search()
        search_value_date=time.strftime("%Y-%m-%d", time.localtime(time.time()))
        self.dr.find_element_by_xpath('//*[@id="form"]/div[4]/div/input').send_keys(search_value_date)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 8
        self.pagination_num(paginal_number,search_value_date,column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[11]/a').click()
        self.assertIn(search_value_date,self.dr.find_element_by_xpath('//*[@id="reForm"]/div[1]/div[6]/div/input').get_attribute('value'),'校验详情页面加油时间')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertIn(search_value_date,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[8]').text,'校验返回和默认排序')
        print('勤务管理-车辆加油记录单：加油时间条件查询功能正常')

    def test6_cljyjl_edit(self):
        self.cljyjl_search()
        search_value_carNo = '藏A24567'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value_carNo)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_carNo, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[11]/a').click()
        self.dr.find_element_by_xpath('//*[@id="reForm"]/div[1]/div[2]/div/input').clear()
        self.dr.find_element_by_xpath('//*[@id="reForm"]/div[1]/div[2]/div/input').send_keys('藏A24566')
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('藏A24566',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,'校验编辑、返回和默认排序')
        print('勤务管理-车辆加油记录单：警车编号条件查询功能正常')

    def test7_cljyjl_delete(self):
        self.cljyjl_search()
        search_value_carNo = '藏A24566'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value_carNo)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_carNo, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('勤务管理-车辆加油记录单：删除功能正常')


if __name__=='__main__':
    unittest.main()