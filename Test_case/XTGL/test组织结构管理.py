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
from public_package.pubilc_package import sheet_setting, search, reset, currMenupath, page_title, goback, saveBtn,sheet_menu,sheet_prompt_message
from public_package.pubilc_package import TESTCASE
import HTMLTestRunner
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

class TESTCAST_ZZJGGL(TESTCASE):
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

    def zzjggl_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('//*[@id="next"]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,65,66)[0]).click()
        time.sleep(5)
        self.assertEqual('系统管理',self.dr.find_element_by_xpath(currMenupath).text, '系统管理')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,65,66)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,65,66)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('组织机构人员列表', self.dr.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/p').text,
                         '组织机构管理')

    def test1_search_zzjg(self):
        self.zzjggl_search()
        search_value_zzjg='错那边防大队'
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_46_span"]').click()
        time.sleep(1)
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_zzjg, column)
        print('系统管理-组织结构管理：组织机构查询功能正常')

    def test2_search_zzjg(self):
        self.zzjggl_search()
        search_value_zzjg='库局派出所'
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_46_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_48_span"]').click()
        time.sleep(1)
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_zzjg, column)
        print('系统管理-组织结构管理：组织机构查询功能正常')

    def test3_search_zzjg(self):
        self.zzjggl_search()
        search_value_zzjg='贡日派出所'
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_46_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_53_span"]').click()
        time.sleep(1)
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_zzjg, column)
        print('系统管理-组织结构管理：组织机构查询功能正常')



if __name__=='__main__':
    unittest.main()