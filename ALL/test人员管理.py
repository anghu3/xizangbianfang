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

class TESTCAST_RKGL(TESTCASE):
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

    def rkgl_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div/a[6]/div[2]/img[2]').click()
        time.sleep(5)
        self.assertEqual('系统管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '系统管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[1]/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="5"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('人员列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '人员管理')

    def rkgl_search_test(self):
        self.login(login_name_test, login_password_test)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div/a[6]/div[2]/img[2]').click()
        time.sleep(5)
        self.assertEqual('系统管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '系统管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[1]/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="5"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('人员列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '人员管理')

    def test1_rkgl_search_name(self):
        self.rkgl_search()
        search_value_name='王学伟'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value_name)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 1
        self.pagination_num(paginal_number, search_value_name, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[6]/a[1]').click()
        self.assertEqual(search_value_name,self.dr.find_element_by_xpath('//*[@id="name"]').get_attribute('value'),'校验详情页面姓名')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('人员列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '校验返回功能')
        print('系统管理-人口管理：姓名条件查询功能正常')

    def test2_rkgl_search_loginId(self):
        self.rkgl_search()
        search_value_loginId='2c8a8a9b29298c6501292a54ca2908b6'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/div/input').send_keys(search_value_loginId)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 2
        self.pagination_num(paginal_number, search_value_loginId, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[6]/a[1]').click()
        self.assertEqual(search_value_loginId,self.dr.find_element_by_xpath('//*[@id="loginId"]').get_attribute('value'),'校验详情页面登录账户')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('人员列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '校验返回功能')
        print('系统管理-人口管理：登录账户条件查询功能正常')

    def test3_rkgl_search_orgName(self):
        self.rkgl_search()
        search_value_orgName='库局派出所'
        self.dr.find_element_by_xpath('//*[@id="orgName"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_46_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_48_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_orgName, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[6]/a[1]').click()
        self.assertEqual(search_value_orgName,self.dr.find_element_by_xpath('//*[@id="orgName"]').get_attribute('value'),'校验详情页面组织机构')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('人员列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '校验返回功能')
        print('系统管理-人口管理：组织机构条件查询功能正常')

    def test4_rkgl_search_duty(self):
        self.rkgl_search()
        search_value_duty='科长'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[4]/div/input').send_keys(search_value_duty)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_duty, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[6]/a[1]').click()
        self.assertEqual(search_value_duty,self.dr.find_element_by_xpath('//*[@id="duty"]').get_attribute('value'),'校验详情页面登录账户')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('人员列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '校验返回功能')
        print('系统管理-人口管理：登录账户条件查询功能正常')

    def test5_rkgl_edit(self):
        self.rkgl_search()
        search_value_loginId='test'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/div/input').send_keys(search_value_loginId)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 2
        self.pagination_num(paginal_number, search_value_loginId, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[6]/a[1]').click()
        self.dr.find_element_by_xpath('//*[@id="phone"]').clear()
        self.dr.find_element_by_xpath('//*[@id="phone"]').send_keys('13585745874')
        self.dr.find_element_by_xpath('//*[@id="duty"]').clear()
        self.dr.find_element_by_xpath('//*[@id="duty"]').send_keys('警员')
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        time.sleep(3)
        # self.dr.delete_all_cookies()
        self.assertEqual('警员',self.dr.find_element_by_xpath('//*[@id="duty"]').get_attribute('value'),'校验编辑功能')
        self.assertEqual('13585745874',self.dr.find_element_by_xpath('//*[@id="phone"]').get_attribute('value'),'校验编辑功能')
        print('系统管理-人口管理：编辑功能正常')

    def test6_rkgl_edit(self):
        self.rkgl_search()
        search_value_loginId='test'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/div/input').send_keys(search_value_loginId)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 2
        self.pagination_num(paginal_number, search_value_loginId, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[6]/a[1]').click()
        self.dr.find_element_by_xpath('//*[@id="phone"]').clear()
        self.dr.find_element_by_xpath('//*[@id="phone"]').send_keys('15874587458')
        self.dr.find_element_by_xpath('//*[@id="duty"]').clear()
        self.dr.find_element_by_xpath('//*[@id="duty"]').send_keys('科长')
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        time.sleep(3)
        # self.dr.delete_all_cookies()
        self.assertEqual('科长',self.dr.find_element_by_xpath('//*[@id="duty"]').get_attribute('value'),'校验编辑功能')
        self.assertEqual('15874587458', self.dr.find_element_by_xpath('//*[@id="phone"]').get_attribute('value'),
                         '校验编辑功能')
        print('系统管理-人口管理：编辑功能正常')

    def test7_rkgl_pwd(self):
        self.rkgl_search()
        search_value_loginId='test'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/div/input').send_keys(search_value_loginId)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 2
        self.pagination_num(paginal_number, search_value_loginId, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[6]/a[2]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.dr.find_element_by_xpath('//*[@id="pwd"]').send_keys(login_password_test2)
        self.dr.find_element_by_xpath('/html/body/div[6]/div[3]/div/button[2]/span').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[4]/a[2]').click()
        self.login(login_name_test,login_password_test2)
        self.assertEqual('用户：test',self.dr.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[3]/div[1]').text,'校验修改密码后登录')
        print('系统管理-人员管理：修改密码功能')

    def test8_rkgl_pwd(self):
        self.rkgl_search()
        search_value_loginId='test'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/div/input').send_keys(search_value_loginId)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 2
        self.pagination_num(paginal_number, search_value_loginId, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[6]/a[2]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.dr.find_element_by_xpath('//*[@id="pwd"]').send_keys(login_password_test)
        self.dr.find_element_by_xpath('/html/body/div[6]/div[3]/div/button[2]/span').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[4]/a[2]').click()
        self.login(login_name_test,login_password_test)
        self.assertEqual('用户：test',self.dr.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[3]/div[1]').text,'校验修改密码后登录')
        print('系统管理-人员管理：修改密码功能')

    # def test9_rkgl_add_juese(self):
    #     # self.rkgl_search()
    #     print('待角色管理中查询功能正常后完成')



if __name__=='__main__':
    unittest.main()