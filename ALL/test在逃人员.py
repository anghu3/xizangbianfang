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
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

class TESTCAST_ZAITAO(TESTCASE):
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

    def zaitaorenyuan_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/a[2]').click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '人口管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[9]/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="564"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('在逃人员列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '在逃人员')

    def test1_zaitaorenyuan_search_name(self):
        self.zaitaorenyuan_search()
        search_value = '周世东'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        # paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        # column = 2
        # self.pagination_num(paginal_number,search_value, column)

        time.sleep(5)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/a').click()
        self.assertEqual(search_value, self.dr.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div[1]/div[2]').text,
                         '校验详细信息-姓名')
        print('人口管理-在逃人员：姓名条件查询功能正常')

    def test2_zaitaorenyuan_search_cardid(self):
        self.zaitaorenyuan_search()
        search_value = '120105197104124814'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/div/input').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(180)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number,search_value,column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[9]/a').click()
        time.sleep(5)
        self.assertEqual(search_value, self.dr.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div[1]/div[2]').text,
                         '校验详细信息-身份证号')
        print('人口管理-在逃人员：身份证号条件查询功能正常')

    def test3_zaitaorenyuan_search_rybh(self):
        self.zaitaorenyuan_search()
        search_value = 'T1201090289992012110013'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[3]/div/input').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 6
        self.pagination_num(paginal_number,search_value,column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[9]/a').click()
        time.sleep(5)
        self.assertEqual(search_value, self.dr.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div[6]/div[2]').text,
                         '校验详细信息-身份证号')
        print('人口管理-在逃人员：人员编号条件查询功能正常')

    def test4_zaitaorenyuan_search_rybh(self):
        self.zaitaorenyuan_search()
        search_value = 'A1201099991052011080007'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[4]/div/input').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 7
        self.pagination_num(paginal_number,search_value,column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[9]/a').click()
        time.sleep(5)
        self.assertEqual(search_value, self.dr.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div[7]/div[2]').text,
                         '校验详细信息-身份证号')
        print('人口管理-在逃人员：人员编号条件查询功能正常')


if __name__ == '__main__':
    unittest.main()