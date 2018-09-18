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

class TESTCAST_JINGCHE(TESTCASE):
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

    def jingche_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div/a[2]/div[2]/img[2]').click()
        time.sleep(5)
        self.assertEqual('勤务管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '勤务管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="643"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('警车基本信息列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '警车管理')

    def test1_jingche_add(self):
        self.jingche_search()
        add_value_carNo='藏A24577'
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        self.dr.find_element_by_xpath('//*[@id="carNo"]').send_keys(add_value_carNo)
        self.dr.find_element_by_xpath('//*[@id="carType"]').send_keys('勘察车')
        self.dr.find_element_by_xpath('//*[@id="affiliationOrgName"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_58_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_62_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="carUse"]').send_keys('勘察现场')
        self.dr.find_element_by_xpath('//*[@id="carCondition"]').send_keys('车辆使用两年，每年按时保养，使用正常！最近发生一次交通事故，正在维修！')
        Select(self.dr.find_element_by_xpath('//*[@id="status"]')).select_by_value('2')
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual(add_value_carNo,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,'校验新增，返回和默认排序')
        print('勤务管理-警车管理：新增功能正常')

    def test2_jingche_search_carNo(self):
        self.jingche_search()
        search_value_carNo='藏A24577'
        self.dr.find_element_by_xpath('//*[@id="carNo"]').send_keys(search_value_carNo)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_carNo, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/a').click()
        self.assertEqual(search_value_carNo,self.dr.find_element_by_xpath('//*[@id="carNo"]').get_attribute('value'),'校验详情页面的警车编号')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_carNo, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,
                         '校验返回和默认排序')
        print('勤务管理-警车管理：警车编号条件查询功能正常')

    def test3_jingche_search_carType(self):
        self.jingche_search()
        search_value_carType='勘察车'
        self.dr.find_element_by_xpath('//*[@id="carType"]').send_keys(search_value_carType)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_carType, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/a').click()
        self.assertEqual(search_value_carType,self.dr.find_element_by_xpath('//*[@id="carType"]').get_attribute('value'),'校验详情页面的警车型号')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_carType, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,
                         '校验返回和默认排序')
        print('勤务管理-警车管理：警车型号条件查询功能正常')

    def test4_jingche_search_ssdw(self):
        self.jingche_search()
        search_value_ssdw='扎日派出所'
        self.dr.find_element_by_xpath('//*[@id="affiliationOrgName"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_58_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_62_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_ssdw, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/a').click()
        self.assertEqual(search_value_ssdw,self.dr.find_element_by_xpath('//*[@id="affiliationOrgName"]').get_attribute('value'),'校验详情页面的所属单位')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_ssdw, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[5]').text,
                         '校验返回和默认排序')
        print('勤务管理-警车管理：所属单位条件查询功能正常')

    def test5_jingche_search_carUse(self):
        self.jingche_search()
        search_value_carUse='勘察现场'
        self.dr.find_element_by_xpath('//*[@id="carUse"]').send_keys(search_value_carUse)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 6
        self.pagination_num(paginal_number, search_value_carUse, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/a').click()
        self.assertEqual(search_value_carUse,self.dr.find_element_by_xpath('//*[@id="carUse"]').get_attribute('value'),'校验详情页面的警车用途')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_carUse, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[6]').text,
                         '校验返回和默认排序')
        print('勤务管理-警车管理：警车用途条件查询功能正常')

    def test6_jingche_search_status(self):
        self.jingche_search()
        option_chioce=Select(self.dr.find_element_by_xpath('//*[@id="status"]'))
        option_chioce.select_by_value('2')
        search_value_status=option_chioce.first_selected_option.text
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 7
        self.pagination_num(paginal_number, search_value_status, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/a').click()
        self.assertEqual(search_value_status,self.dr.find_element_by_xpath('//*[@id="status"]/option[3]').text,'校验详情页面的警车状态')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_status, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[7]').text,
                         '校验返回和默认排序')
        print('勤务管理-警车管理：警车状态条件查询功能正常')

    def test7_jingche_edit(self):
        self.jingche_search()
        search_value_carNo='藏A24577'
        self.dr.find_element_by_xpath('//*[@id="carNo"]').send_keys(search_value_carNo)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_carNo, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/a').click()
        edit_value_caruse='出勤巡查'
        edit_value_cartype='勤务车'
        self.dr.find_element_by_xpath('//*[@id="carType"]').clear()
        self.dr.find_element_by_xpath('//*[@id="carType"]').send_keys(edit_value_cartype)
        self.dr.find_element_by_xpath('//*[@id="carUse"]').clear()
        self.dr.find_element_by_xpath('//*[@id="carUse"]').send_keys(edit_value_caruse)
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual(edit_value_cartype,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,'校验编辑功能和默认排序')
        self.assertEqual(edit_value_caruse,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[6]').text,'校验编辑功能和默认排序')
        print('勤务管理-警车管理：编辑功能正常')

    def test8_jingche_delete(self):
        self.jingche_search()
        search_value_carNo='藏A24577'
        self.dr.find_element_by_xpath('//*[@id="carNo"]').send_keys(search_value_carNo)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_carNo, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[2]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('勤务管理-警车管理：删除功能正常')

if __name__=='__main__':
    unittest.main()