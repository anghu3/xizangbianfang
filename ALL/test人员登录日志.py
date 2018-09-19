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
from public_package.pubilc_package import url,login_name,login_name_test,login_password,login_password_test,login_password_test2
from public_package.pubilc_package import TESTCASE
import HTMLTestRunner
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

class TESTCAST_RYDLRZ(TESTCASE):
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

    def rydlrz_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div/a[6]/div[2]/img[2]').click()
        time.sleep(5)
        self.assertEqual('系统管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '系统管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[3]/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="11"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('人员日志管理', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '人员登录日志')

    def test1_rydlrz_search_loginId(self):
        self.rydlrz_search()
        search_value_loginId='test11'
        self.dr.find_element_by_xpath('//*[@id="detachment"]').send_keys(search_value_loginId)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 1
        self.pagination_num(paginal_number, search_value_loginId, column)
        print('系统管理-人员登录日志：登录账户条件查询功能正常')

    def test2_rydlrz_search_loginstatus(self):
        self.rydlrz_search()
        option_chioce=Select(self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/div/select'))
        for i in range(0,3):
            if i==0:
                print('状态查询条件为全部时不校验数据')
            else:
                print(i)
                option_chioce.select_by_index(i)
                search_value_state=option_chioce.first_selected_option.text
                search_value_loginId = 'test11'
                self.dr.find_element_by_xpath('//*[@id="detachment"]').clear()
                self.dr.find_element_by_xpath('//*[@id="detachment"]').send_keys(search_value_loginId)
                self.dr.find_element_by_xpath('//*[@id="search"]').click()
                self.dr.switch_to.default_content()
                time.sleep(3)
                self.dr.switch_to.frame('iframeb')
                paginal_number = self.dr.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
                column = 3
                self.pagination_num(paginal_number, search_value_state, column)
        print('系统管理-人员登录日志：状态条件查询功能正常')

if __name__=='__main__':
    unittest.main()