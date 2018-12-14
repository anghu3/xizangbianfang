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
from public_package.pubilc_package import sheet_setting, search, reset, currMenupath, page_title, goback, saveBtn,sheet_menu,sheet_prompt_message,work_space
import xlrd
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

xlsfile=work_space+r'\\'+sheet_menu.col_values(6,30,31)[0]
excel = xlrd.open_workbook(xlsfile)
global sheet
sheet = excel.sheet_by_name('群防信息采集')

class TESTCAST_QUNFANGCAIJI(TESTCASE):
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

    def qunfangxinxicaiji_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,30,31)[0]).click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath(currMenupath).text, '人口管理')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,30,31)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,30,31)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('群防信息采集列表', self.dr.find_element_by_xpath(page_title).text,
                         '群防信息采集')

    def test01_qunfangxinxicaiji_search_infoCollectIp(self):
        self.qunfangxinxicaiji_search()
        search_value_infoCollectIp=sheet.col_values(1,0,1)[0]
        infoCollectIp_path=sheet.col_values(1,1,2)[0]
        self.dr.find_element_by_xpath(infoCollectIp_path).send_keys(search_value_infoCollectIp)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        column = 2
        self.pagination_num(paginal_number,search_value_infoCollectIp , column)
        self.dr.find_element_by_xpath(reset).click()
        time.sleep(2)
        self.dr.find_element_by_xpath(search).click()
        self.assertEqual('',self.dr.find_element_by_xpath(infoCollectIp_path).get_attribute('value'),'信息采集接口IP-重置功能异常')
        print('人口管理-群防信息采集：信息采集接口IP条件查询功能正常')

    def test02_qunfangxinxicaiji_search_infoSendIp(self):
        self.qunfangxinxicaiji_search()
        search_value_infoSendIp=sheet.col_values(1,2,3)[0]
        infoSendIp_path=sheet.col_values(1,3,4)[0]
        self.dr.find_element_by_xpath(infoSendIp_path).send_keys(search_value_infoSendIp)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        column = 6
        self.pagination_num(paginal_number,search_value_infoSendIp , column)
        self.dr.find_element_by_xpath(reset).click()
        time.sleep(2)
        self.dr.find_element_by_xpath(search).click()
        self.assertEqual('', self.dr.find_element_by_xpath(infoSendIp_path).get_attribute('value'),
                         '信息发送接口IP-重置功能异常')
        print('人口管理-群防信息采集：信息发送接口IP条件查询功能正常')

    def test03_qunfangxinxicaiji_search_caishijian(self):
        self.qunfangxinxicaiji_search()
        search_value_caijishijian=sheet.col_values(1,4,5)[0]
        startTime_path=sheet.col_values(1,5,6)[0]
        self.dr.find_element_by_xpath(startTime_path).send_keys(search_value_caijishijian)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        column = 7
        self.pagination_num(paginal_number,search_value_caijishijian , column)
        self.dr.find_element_by_xpath(reset).click()
        time.sleep(2)
        self.dr.find_element_by_xpath(search).click()
        self.assertEqual('',self.dr.find_element_by_xpath(startTime_path).get_attribute('value'),'采集时间-重置功能异常')
        print('人口管理-群防信息采集：采集时间条件查询功能正常')

    def test04_qunfangxinxicaiji_search_all(self):
        self.qunfangxinxicaiji_search()
        search_value_infoCollectIp = sheet.col_values(1, 0, 1)[0]
        infoCollectIp_path = sheet.col_values(1, 1, 2)[0]
        self.dr.find_element_by_xpath(infoCollectIp_path).send_keys(search_value_infoCollectIp)
        search_value_infoSendIp = sheet.col_values(1, 2, 3)[0]
        infoSendIp_path = sheet.col_values(1, 3, 4)[0]
        self.dr.find_element_by_xpath(infoSendIp_path).send_keys(search_value_infoSendIp)
        search_value_caijishijian = sheet.col_values(1, 4, 5)[0]
        startTime_path = sheet.col_values(1, 5, 6)[0]
        self.dr.find_element_by_xpath(startTime_path).send_keys(search_value_caijishijian)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        self.pagination_num(paginal_number, search_value_caijishijian, 7)
        self.pagination_num(paginal_number, search_value_infoSendIp, 6)
        self.pagination_num(paginal_number, search_value_infoCollectIp, 2)
        self.dr.find_element_by_xpath(reset).click()
        time.sleep(2)
        self.dr.find_element_by_xpath(search).click()
        self.assertEqual('', self.dr.find_element_by_xpath(startTime_path).get_attribute('value'), '采集时间-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(infoCollectIp_path).get_attribute('value'),
                         '信息采集接口IP-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(infoSendIp_path).get_attribute('value'),
                         '信息发送接口IP-重置功能异常')
        print('人口管理-群防信息采集：条件查询功能正常')


if __name__=='__main__':
    unittest.main()