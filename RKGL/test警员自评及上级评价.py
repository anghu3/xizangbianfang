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

class TESTCAST_JYZP(TESTCASE):
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

    def jyzp_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div/a[3]/div[2]/img[2]').click()
        time.sleep(5)
        self.assertEqual('社区警务',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '社区警务')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[1]/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="1863"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('警员自评及上级评价列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '警员自评及上级评价')

    def test1_jyzp_add(self):
        self.jyzp_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        self.dr.find_element_by_xpath('//*[@id="policeName"]').send_keys('包涵')
        self.dr.find_element_by_xpath('//*[@id="policeNumber"]').send_keys('0375325')
        self.dr.find_element_by_xpath('//*[@id="policeOrgName"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect1_45_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect1_46_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect1_48_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="evaluationDescribe"]').send_keys('本月执勤22天，执勤时间段无任何意外发生，协助破获案件10起，抓获嫌疑人5名。')
        self.dr.find_element_by_xpath('//*[@id="evaluationResult"]').send_keys('B+')
        self.dr.find_element_by_xpath('//*[@id="superiorName"]').send_keys('包拯')
        self.dr.find_element_by_xpath('//*[@id="superiorNumber"]').send_keys('0375420')
        self.dr.find_element_by_xpath('//*[@id="superiorOrgName"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect2_45_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect2_46_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect2_48_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="superiorDescribe"]').send_keys('该警员描述属实，在职期间认真负责，吃苦耐劳！')
        self.dr.find_element_by_xpath('//*[@id="superiorResult"]').send_keys('A')
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual('包涵',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,'校验新增、返回和默认排序')
        print('社区警务-警员自评及上级评价：新增功能正常')

    def test2_jyzp_search_policeName(self):
        self.jyzp_search()
        search_value_policeName = '包涵'
        self.dr.find_element_by_xpath('//*[@id="policeName"]').send_keys(search_value_policeName)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_policeName, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[9]/a').click()
        self.assertEqual(search_value_policeName,
                         self.dr.find_element_by_xpath('//*[@id="policeName"]').get_attribute('value'), '校验详情页面中警员名称')
        print('社区警务-警员自评及上级评价：警员姓名条件功能正常')

    def test3_jyzp_search_policeNumber(self):
        self.jyzp_search()
        search_value_policeNumber='0375325'
        self.dr.find_element_by_xpath('//*[@id="policeNumber"]').send_keys(search_value_policeNumber)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_policeNumber, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[9]/a').click()
        self.assertEqual(search_value_policeNumber,self.dr.find_element_by_xpath('//*[@id="policeNumber"]').get_attribute('value'),'校验详情页面中警员编号')
        print('社区警务-警员自评及上级评价：警员编号条件功能正常')

    def test4_jyzp_edit(self):
        self.jyzp_search()
        search_value_policeNumber='0375325'
        self.dr.find_element_by_xpath('//*[@id="policeNumber"]').send_keys(search_value_policeNumber)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_policeNumber, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[9]/a').click()
        self.assertEqual(search_value_policeNumber,self.dr.find_element_by_xpath('//*[@id="policeNumber"]').get_attribute('value'),'校验详情页面中警员编号')
        edit_value_policeName='马汉'
        self.dr.find_element_by_xpath('//*[@id="policeName"]').clear()
        self.dr.find_element_by_xpath('//*[@id="policeName"]').send_keys(edit_value_policeName)
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual(edit_value_policeName, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text, '校验新增、返回和默认排序')
        print('社区警务-警员自评及上级评价：编辑功能正常')

    def test5_jyzp_delete(self):
        self.jyzp_search()
        search_value_policeNumber='0375325'
        self.dr.find_element_by_xpath('//*[@id="policeNumber"]').send_keys(search_value_policeNumber)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_policeNumber, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('社区警务-警员自评及上级评价：删除功能正常')

if __name__=='__main__':
    unittest.main()