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

class TESTCAST_QFKHGL(TESTCASE):
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

    def qfkhgl_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/a[2]').click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '人口管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[10]/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="603"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('群防群治信息打分列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '群防力量_考核管理')

    def test01_qfkhgl_search_name(self):
        self.qfkhgl_search()
        search_value_name='朱志鹏'
        self.dr.find_element_by_xpath('//*[@id="name"]').send_keys(search_value_name)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 2
        self.pagination_num(paginal_number, search_value_name, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(search_value_name,self.dr.find_element_by_xpath('//*[@id="memberName"]').get_attribute('value'),'校验详情页面姓名')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('群防群治信息打分列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '群防力量_考核管理')
        print('人员管理-群防力量_考核管理：姓名条件查询功能正常')

    def test02_qfkhgl_search_idCard(self):
        self.qfkhgl_search()
        search_value_idCard='511181199010051916'
        self.dr.find_element_by_xpath('//*[@id="idCard"]').send_keys(search_value_idCard)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_idCard, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(search_value_idCard,self.dr.find_element_by_xpath('//*[@id="idCard"]').get_attribute('value'),'校验详情页面身份证号码')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('群防群治信息打分列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '群防力量_考核管理')
        print('人员管理-群防力量_考核管理：身份证号码条件查询功能正常')

    def test03_qfkhgl_search_manageOrgName(self):
        self.qfkhgl_search()
        search_value_manageOrgName='山南支队'
        self.dr.find_element_by_xpath('//*[@id="manageOrgName"]').click()
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_span"]').click()
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(search_value_manageOrgName,self.dr.find_element_by_xpath('//*[@id="manageOrgName"]').get_attribute('value'),'校验详情页面管辖单位')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('群防群治信息打分列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '群防力量_考核管理')
        print('人员管理-群防力量_考核管理：管辖单位条件查询功能正常')

    def test04_qfkhgl_edit_kh(self):
        self.qfkhgl_search()
        search_value_idCard='511181199010051916'
        self.dr.find_element_by_xpath('//*[@id="idCard"]').send_keys(search_value_idCard)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_idCard, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(search_value_idCard,self.dr.find_element_by_xpath('//*[@id="idCard"]').get_attribute('value'),'校验详情页面身份证号码')
        self.dr.find_element_by_xpath('//*[@id="assessmentPeriod"]').clear()
        self.dr.find_element_by_xpath('//*[@id="assessmentPeriod"]').send_keys('2018-09-17')
        Select(self.dr.find_element_by_xpath('//*[@id="result"]')).select_by_value('良好')
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('群防群治信息打分列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '群防力量_考核管理')
        print('人员管理-群防力量_考核管理：身份证号码条件查询功能正常')

    def test05_qfkhgl_search_period(self):
        self.qfkhgl_search()
        search_value_period='2018-09-17'
        self.dr.find_element_by_xpath('//*[@id="assessmentPeriod"]').send_keys(search_value_period)
        self.dr.find_element_by_xpath('//*[@id="name"]').click()
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 7
        self.pagination_num(paginal_number, search_value_period, column)
        print('人员管理-群防力量_考核管理：考核期条件查询功能正常')

    def test06_qfkhgl_search_flag(self):
        self.qfkhgl_search()
        option_chioce=Select(self.dr.find_element_by_xpath('//*[@id="flag"]'))
        for i in range(0,3):
            if i == 0:
                print('是否已考核的查询条件为全部是不检验数据')
            else:
                option_chioce.select_by_index(i)
                search_value_flag=option_chioce.first_selected_option.text
                self.dr.find_element_by_xpath('//*[@id="search"]').click()
                time.sleep(1)
                self.dr.switch_to.default_content()
                time.sleep(3)
                self.dr.switch_to.frame('iframeb')
                paginal_number = self.dr.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
                column = 8
                self.pagination_num(paginal_number, search_value_flag, column)
        print('人员管理-群防力量_考核管理：是否已考核条件查询功能正常')

    def test07_qfkhgl_search_assessmentResult(self):
        self.qfkhgl_search()
        option_chioce=Select(self.dr.find_element_by_xpath('//*[@id="assessmentResult"]'))
        for i in range(0,5):
            if i == 0:
                print('是否已考核的查询条件为全部是不检验数据')
            else:
                option_chioce.select_by_index(i)
                search_value_assessmentResult=option_chioce.first_selected_option.text
                self.dr.find_element_by_xpath('//*[@id="search"]').click()
                time.sleep(1)
                self.dr.switch_to.default_content()
                time.sleep(3)
                self.dr.switch_to.frame('iframeb')
                paginal_number = self.dr.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
                column = 9
                self.pagination_num(paginal_number, search_value_assessmentResult, column)
        print('人员管理-群防力量_考核管理：考核结果条件查询功能正常')


if __name__=='__main__':
    unittest.main()