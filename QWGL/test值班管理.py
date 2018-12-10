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

# xlsfile = r'F:\pythonkeys\自动化测试\lasa\QWGL.xlsx'
# excel = xlrd.open_workbook(xlsfile)
# global sheet
# sheet = excel.sheet_by_name('值班管理')

class TESTCAST_ZHIBANGUANLI(TESTCASE):
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

    def zhibanguanli_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,62,63)[0]).click()
        time.sleep(5)
        self.assertEqual('勤务管理',self.dr.find_element_by_xpath(currMenupath).text, '勤务管理')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,62,63)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,62,63)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('值班管理列表', self.dr.find_element_by_xpath(page_title).text,
                         '值班管理')

    def test01_zhibanguanli_add(self):
        self.zhibanguanli_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        time_now=now = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        self.dr.find_element_by_xpath('//*[@id="dutyDate"]').click()
        self.dr.find_element_by_xpath('//*[@id="dutyDate"]').send_keys(time_now)
        self.dr.find_element_by_xpath('//*[@id="dutyArea"]').click()
        option_choice=Select(self.dr.find_element_by_xpath('//*[@id="dutyType"]'))
        option_choice.select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="dutyArea"]').send_keys('拉萨市实验中学')
        self.dr.find_element_by_xpath('//*[@id="dutyPerson"]').send_keys('包涵')
        self.dr.find_element_by_xpath('//*[@id="dutyPersonCharge"]').send_keys('林峰')
        self.dr.find_element_by_xpath('//*[@id="telephone"]').send_keys('15874587474')
        self.dr.find_element_by_xpath('//*[@id="dutyContent"]').send_keys('中学上学和放学时间段周边情况执勤')
        self.dr.find_element_by_xpath('//*[@id="saveDutyManage"]').click()
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual('值班管理列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '值班管理')
        print('勤务管理-值班管理：新增功能正常')

    def test02_zhibanguanli_search_date(self):
        self.zhibanguanli_search()
        time_now = now = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        self.dr.find_element_by_xpath('//*[@id="dutyDates"]').send_keys(time_now)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, time_now, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[9]/a').click()
        self.assertIn(time_now,self.dr.find_element_by_xpath('//*[@id="dutyDate"]').get_attribute('value'),'校验详情页的日期')
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual('值班管理列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,'值班管理')
        print('勤务管理-值班管理：时间条件查询功能正常')

    def test03_zhibanguanli_search_dutyType(self):
        self.zhibanguanli_search()
        option_chioce=Select(self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/div/select'))
        option_chioce.select_by_value('1')
        option_chioce_value=option_chioce.first_selected_option.text
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, option_chioce_value, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[9]/a').click()
        self.assertIn(option_chioce_value,self.dr.find_element_by_xpath('//*[@id="dutyType"]/option[2]').text,'校验详情页值班类型')
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual('值班管理列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,'值班管理')
        print('勤务管理-值班管理：值班类型条件查询功能正常')

    def test04_zhibanguanli_search_all(self):
        self.zhibanguanli_search()
        option_chioce = Select(self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/div/select'))
        option_chioce.select_by_value('1')
        option_chioce_value = option_chioce.first_selected_option.text
        time_now = now = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        self.dr.find_element_by_xpath('//*[@id="dutyDates"]').send_keys(time_now)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        self.pagination_num(paginal_number, option_chioce_value, 5)
        self.pagination_num(paginal_number, time_now, 4)
        self.dr.find_element_by_xpath(reset).click()
        time.sleep(1)
        self.dr.find_element_by_xpath(search).click()
        self.assertEqual('',self.dr.find_element_by_xpath('//*[@id="dutyDates"]').get_attribute('value'),'日期-重置功能异常')
        self.assertEqual('全部',self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/div/select/option[1]').text,'值班类型-重置功能异常')
        print('勤务管理-值班管理：查询功能正常')

    def test05_zhibanguanli_delete(self):
        self.zhibanguanli_search()
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('值班管理列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,'值班管理')
        print('勤务管理-值班管理：新增功能正常')

if __name__=='__main__':
    unittest.main()