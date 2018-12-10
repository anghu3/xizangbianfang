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
import xlrd
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

xlsfile = r'F:\pythonkeys\自动化测试\lasa\XTGL.xlsx'
excel = xlrd.open_workbook(xlsfile)
global sheet
sheet = excel.sheet_by_name('人员管理')

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
        self.dr.find_element_by_xpath('//*[@id="next"]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,64,65)[0]).click()
        time.sleep(5)
        self.assertEqual('系统管理',self.dr.find_element_by_xpath(currMenupath).text, '系统管理')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,64,65)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,64,65)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('人员列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '人员管理')

    def rkgl_search_test(self):
        self.login(login_name_test, login_password_test)
        self.dr.find_element_by_xpath('//*[@id="next"]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,64,65)[0]).click()
        time.sleep(5)
        self.assertEqual('系统管理',self.dr.find_element_by_xpath(currMenupath).text, '系统管理')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,64,65)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,64,65)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('人员列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '人员管理')

    def test01_rkgl_add(self):
        self.rkgl_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="loginId"]').send_keys(sheet.col_values(1,2,3)[0])
        self.dr.find_element_by_xpath('//*[@id="ukeyLoginId"]').send_keys(sheet.col_values(1,10,11)[0])
        self.dr.find_element_by_xpath('//*[@id="name"]').send_keys(sheet.col_values(1,0,1)[0])
        self.dr.find_element_by_xpath('//*[@id="orgName"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_2_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_34_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_44_span"]').click()
        self.dr.find_element_by_xpath('//*[@id="phone"]').send_keys(sheet.col_values(1,11,12)[0])
        self.dr.find_element_by_xpath('//*[@id="duty"]').send_keys(sheet.col_values(1,6,7)[0])
        self.dr.find_element_by_xpath(saveBtn).click()
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        time.sleep(1)
        self.assertEqual('登陆账号已存在！',
                         self.dr.find_element_by_xpath('//*[@id="gritter-item-1"]/div[2]/div[2]/p').text, '新增成功提示信息校验')
        print('系统管理-人口管理：人员新增功能正常')

    def test02_rkgl_search_name(self):
        self.rkgl_search()
        search_value_name=sheet.col_values(1,0,1)[0]
        name_path=sheet.col_values(1,1,2)[0]
        self.dr.find_element_by_xpath(name_path).send_keys(search_value_name)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        column = 2
        self.pagination_num(paginal_number, search_value_name, column)
        self.dr.find_element_by_xpath(reset).click()
        time.sleep(1)
        self.dr.find_element_by_xpath(search).click()
        self.assertEqual('',self.dr.find_element_by_xpath(name_path).get_attribute('value'),'姓名-重置功能异常')
        print('系统管理-人口管理：姓名条件查询功能正常')

    def test03_rkgl_search_loginId(self):
        self.rkgl_search()
        search_value_loginId=sheet.col_values(1,2,3)[0]
        loginId_path=sheet.col_values(1,3,4)[0]
        self.dr.find_element_by_xpath(loginId_path).send_keys(search_value_loginId)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        column = 3
        self.pagination_num(paginal_number, search_value_loginId, column)
        self.dr.find_element_by_xpath(reset).click()
        time.sleep(1)
        self.dr.find_element_by_xpath(search).click()
        self.assertEqual('',self.dr.find_element_by_xpath(loginId_path).get_attribute('value'),'登录账号-重置功能异常')
        print('系统管理-人口管理：登录账户条件查询功能正常')

    def test04_rkgl_search_orgName(self):
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
        column = 5
        self.pagination_num(paginal_number, search_value_orgName, column)
        self.dr.find_element_by_xpath(reset).click()
        time.sleep(1)
        self.dr.find_element_by_xpath(search).click()
        self.assertEqual('', self.dr.find_element_by_xpath('//*[@id="orgName"]').get_attribute('value'), '登录账号-重置功能异常')
        print('系统管理-人口管理：组织机构条件查询功能正常')

    def test05_rkgl_search_duty(self):
        self.rkgl_search()
        search_value_duty=sheet.col_values(1,6,7)[0]
        duty_path=sheet.col_values(1,7,8)[0]
        self.dr.find_element_by_xpath(duty_path).send_keys(search_value_duty)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        column = 6
        self.pagination_num(paginal_number, search_value_duty, column)
        self.dr.find_element_by_xpath(reset).click()
        time.sleep(1)
        self.dr.find_element_by_xpath(search).click()
        self.assertEqual('',self.dr.find_element_by_xpath(duty_path).get_attribute('value'),'职务-重置功能异常')
        print('系统管理-人口管理：登录账户条件查询功能正常')

    def test06_rkgl_edit(self):
        self.rkgl_search()
        search_value_loginId='test'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/div/input').send_keys(search_value_loginId)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_loginId, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[8]/a[2]').click()
        self.dr.find_element_by_xpath('//*[@id="phone"]').clear()
        self.dr.find_element_by_xpath('//*[@id="phone"]').send_keys(sheet.col_values(1,11,12)[0])
        self.dr.find_element_by_xpath('//*[@id="duty"]').clear()
        self.dr.find_element_by_xpath('//*[@id="duty"]').send_keys(sheet.col_values(1,6,7)[0])
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        time.sleep(3)
        # self.dr.delete_all_cookies()
        self.assertEqual('科员',self.dr.find_element_by_xpath('//*[@id="duty"]').get_attribute('value'),'校验编辑功能')
        self.assertEqual('15247456354',self.dr.find_element_by_xpath('//*[@id="phone"]').get_attribute('value'),'校验编辑功能')
        print('系统管理-人口管理：编辑功能正常')

    def test07_rkgl_pwd(self):
        self.rkgl_search()
        search_value_loginId='test'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/div/input').send_keys(search_value_loginId)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_loginId, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[8]/a[1]').click()
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

    def test08_rkgl_pwd(self):
        self.rkgl_search()
        search_value_loginId='test'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/div/input').send_keys(search_value_loginId)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_loginId, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[8]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.dr.find_element_by_xpath('//*[@id="pwd"]').send_keys(login_password_test)
        self.dr.find_element_by_xpath('/html/body/div[6]/div[3]/div/button[2]/span').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[4]/a[2]').click()
        self.login(login_name_test,login_password_test)
        self.assertEqual('用户：test',self.dr.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[3]/div[1]').text,'校验修改密码后登录')
        print('系统管理-人员管理：修改密码功能')

if __name__=='__main__':
    unittest.main()