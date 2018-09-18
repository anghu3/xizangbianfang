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

class TESTCAST_YONGCHEGUANLI(TESTCASE):
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

    def yongcheguanli_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div/a[2]/div[2]/img[2]').click()
        time.sleep(5)
        self.assertEqual('勤务管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '勤务管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="585"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('用车管理列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '用车管理')

    def test1_yongcheguanli_add(self):
        self.yongcheguanli_search()
        add_value_place='拉萨贡嘎国际机场'
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        self.dr.find_element_by_xpath('//*[@id="useCarDate"]').click()
        self.dr.find_element_by_xpath('//*[@id="usecarForm"]/div[1]/div[1]/div/div[2]/ul/li[2]/table/tbody/tr/td[2]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="usecarForm"]/div[1]/div[2]/div/input').send_keys(add_value_place)
        Select(self.dr.find_element_by_xpath('//*[@id="carNo"]')).select_by_value('藏A02453')
        self.dr.find_element_by_xpath('//*[@id="usecarForm"]/div[1]/div[5]/div/input').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="usecarForm"]/div[1]/div[5]/div/input').clear()
        self.dr.find_element_by_xpath('//*[@id="usecarForm"]/div[1]/div[5]/div/input').send_keys('2018-09-11 08:30:00')
        self.dr.find_element_by_xpath('//*[@id="usecarForm"]/div[1]/div[5]/div/div[2]/ul/li[2]/table/tbody/tr/td[2]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="usecarForm"]/div[1]/div[6]/div/input').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="usecarForm"]/div[1]/div[6]/div/input').clear()
        self.dr.find_element_by_xpath('//*[@id="usecarForm"]/div[1]/div[6]/div/input').send_keys('2018-09-11 18:00:00')
        self.dr.find_element_by_xpath('//*[@id="usecarForm"]/div[1]/div[6]/div/div[2]/ul/li[2]/table/tbody/tr/td[2]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="usecarForm"]/div[2]/div[1]/div/input').send_keys('四名武警')
        self.dr.find_element_by_xpath('//*[@id="usecarForm"]/div[2]/div[2]/div/textarea').send_keys('城关区武警中队-山南市贡嘎县甲竹林镇。')
        self.dr.find_element_by_xpath('//*[@id="usecarForm"]/div[3]/div[1]/div/input').send_keys('马汉')
        Select(self.dr.find_element_by_xpath('//*[@id="usecarForm"]/div[3]/div[2]/div/select')).select_by_value('包拯')
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual('藏A02453',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[5]').text,'校验新增、返回和默认排序')
        print('勤务管理-用车管理：新增功能正常')

    def test2_yongcheguanli_search_place(self):
        self.yongcheguanli_search()
        search_value_place='拉萨贡嘎国际机场'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value_place)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_place, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        self.assertEqual(search_value_place,self.dr.find_element_by_xpath('//*[@id="usecarForm"]/div[1]/div[2]/div/input').get_attribute('value'),'校验详情页面出行地点')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual(search_value_place,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,'校验返回和默认排序')
        print('勤务管理-用车管理：出行地点条件查询功能正常')

    def test3_yongcheguanli_search_carNo(self):
        self.yongcheguanli_search()
        search_value_carNo='藏A02453'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/div/input').send_keys(search_value_carNo)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_carNo, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        self.assertEqual(search_value_carNo,self.dr.find_element_by_xpath('//*[@id="carNo"]').get_attribute('value'),'校验详情页面警车编号')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual(search_value_carNo,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[5]').text,'校验返回和默认排序')
        print('勤务管理-用车管理：警车编号条件查询功能正常')

    def test4_yongcheguanli_search_carType(self):
        self.yongcheguanli_search()
        search_value_carType='巡逻车'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[3]/div/input').send_keys(search_value_carType)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 6
        self.pagination_num(paginal_number, search_value_carType, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        self.assertEqual(search_value_carType,self.dr.find_element_by_xpath('//*[@id="carType"]').get_attribute('value'),'校验详情页面警车型号')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual(search_value_carType,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[6]').text,'校验返回和默认排序')
        print('勤务管理-用车管理：警车型号条件查询功能正常')

    def test5_yongcheguanli_edit(self):
        self.yongcheguanli_search()
        search_value_carNo='藏A02453'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/div/input').send_keys(search_value_carNo)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_carNo, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        edit_value_place='贡嘎国际机场'
        edit_value_carNo='藏A24567'
        self.dr.find_element_by_xpath('//*[@id="usecarForm"]/div[1]/div[2]/div/input').clear()
        self.dr.find_element_by_xpath('//*[@id="usecarForm"]/div[1]/div[2]/div/input').send_keys(edit_value_place)
        Select(self.dr.find_element_by_xpath('//*[@id="carNo"]')).select_by_value('藏A24567')
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        time.sleep(3)
        self.assertEqual(edit_value_place,self.dr.find_element_by_xpath('//*[@id="usecarForm"]/div[1]/div[2]/div/input').get_attribute('value'),'校验编辑功能')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual(edit_value_carNo,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[5]').text,'校验编辑返回和默认排序')
        self.assertEqual(edit_value_place,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,'校验编辑返回和默认排序')
        print('勤务管理-用车管理：编辑功能正常')

    def test6_yongcheguanli_delete(self):
        self.yongcheguanli_search()
        search_value_place='贡嘎国际机场'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value_place)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_place, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('勤务管理-用车管理：删除功能正常')

if __name__=='__main__':
    unittest.main()