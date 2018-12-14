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
from public_package.pubilc_package import sheet_setting, search, reset, currMenupath, page_title, goback, saveBtn , sheet_menu,sheet_prompt_message,work_space
import xlrd
import HTMLTestRunner
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

class TESTCAST_HANGYECHANGSUO(TESTCASE):
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

    def hangyechangsuo_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,38,39)[0]).click()
        time.sleep(5)
        self.assertEqual('管理防范',self.dr.find_element_by_xpath(currMenupath).text, '管理防范')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,38,39)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,38,39)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('行业管理列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text,
                         '行业场所管理')

    def test01_hangyechangsuo_add(self):
        self.hangyechangsuo_search()
        self.dr.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/a[2]').click()
        self.dr.find_element_by_xpath('//*[@id="localityName"]').click()
        self.dr.find_element_by_xpath('//*[@id="dqtreeSelect_1_switch"]').click()
        self.dr.find_element_by_xpath('//*[@id="dqtreeSelect_2_span"]').click()
        self.dr.find_element_by_xpath('//*[@id="pcs"]').click()
        self.dr.find_element_by_xpath('//*[@id="pcstreeSelect_1_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="pcstreeSelect_2_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="pcstreeSelect_9_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="pcstreeSelect_10_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="locatedPoliceAreaName"]').click()
        self.dr.find_element_by_xpath('//*[@id="jqtreeSelect_1_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="jqtreeSelect_2_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="jqtreeSelect_3_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="jqtreeSelect_4_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="jqtreeSelect_5_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="jqtreeSelect_6_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="policeAreaContactTel"]').send_keys('15874587458')
        '''选择行业类型'''
        self.dr.find_element_by_xpath('//*[@id="zprxm2"]').click()
        self.dr.find_element_by_xpath('//*[@id="treeSelect2_52_switch"]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="treeSelect2_53_span"]').click()
        time.sleep(1)
        '''选择企业性质'''
        Select(self.dr.find_element_by_xpath('//*[@id="character"]')).select_by_value('16')
        '''输入企业注册名称'''
        self.dr.find_element_by_xpath('//*[@id="registrationName"]').send_keys('精伦电子')
        self.dr.find_element_by_xpath('//*[@id="actualBusinessName"]').send_keys('精伦电子股份有限公司')
        self.dr.find_element_by_xpath('//*[@id="compEngName"]').send_keys('Routon Electronic Co., Ltd.')
        self.dr.find_element_by_xpath('//*[@id="legalRepresentative"]').send_keys('张学阳')
        self.dr.find_element_by_xpath('//*[@id="rigisteredCapital"]').send_keys('3000')
        self.dr.find_element_by_xpath('//*[@id="openningDate"]').send_keys('2018-08-05')
        Select(self.dr.find_element_by_xpath('//*[@id="businessStatus"]')).select_by_value('02')
        self.dr.find_element_by_xpath('//*[@id="businessAddress"]').send_keys('江苏路101号')
        '''点击保存'''
        self.dr.find_element_by_xpath('//*[@id="saveIndus"]').click()
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        time.sleep(1)
        self.assertEqual(sheet_prompt_message.col_values(1, 4, 5)[0],
                         self.dr.find_element_by_xpath('//*[@id="gritter-item-1"]/div[2]/div[2]/p').text, '新增成功提示信息校验')
        print('管理防范-行业场所管理：新增功能正常')

    def test02_hangyechangsuo_search_farendaibiao(self):
        self.hangyechangsuo_search()
        search_value_farendaibiao='张学阳'
        self.dr.find_element_by_xpath('//*[@id="legalRepresentative"]').send_keys(search_value_farendaibiao)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_farendaibiao, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        self.assertEqual(search_value_farendaibiao,self.dr.find_element_by_xpath('//*[@id="legalRepresentative"]').get_attribute('value'),
                         '校验详情页面法人代表')
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.assertEqual('行业管理列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text,'校验返回功能')
        print('管理防范-行业场所管理：法人代表条件查询功能正常')

    def test03_hangyechangsuo_search_registrationName(self):
        self.hangyechangsuo_search()
        search_value_registrationName='精伦电子'
        self.dr.find_element_by_xpath('//*[@id="registrationName"]').send_keys(search_value_registrationName)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_registrationName, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        self.assertEqual(search_value_registrationName,self.dr.find_element_by_xpath('//*[@id="registrationName"]').get_attribute('value'),
                         '校验详情页面企业名称')
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.assertEqual('行业管理列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text,'校验返回功能')
        print('管理防范-行业场所管理：企业名称条件查询功能正常')

    def test04_hangyechangsuo_search_hangyeleibie(self):
        self.hangyechangsuo_search()
        search_value_zprxm='其他'
        self.dr.find_element_by_xpath('//*[@id="zprxm"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_52_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_53_span"]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 6
        self.pagination_num(paginal_number, search_value_zprxm, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        self.assertEqual(search_value_zprxm,self.dr.find_element_by_xpath('//*[@id="zprxm2"]').get_attribute('value'),
                         '校验详情页面行业类别')
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.assertEqual('行业管理列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text,'校验返回功能')
        print('管理防范-行业场所管理：行业类别条件查询功能正常')

    def test05_hangyechangsuo_search_businessAddress(self):
        self.hangyechangsuo_search()
        search_value_businessAddress='江苏路101号'
        self.dr.find_element_by_xpath('//*[@id="businessAddress"]').send_keys(search_value_businessAddress)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 9
        self.pagination_num(paginal_number, search_value_businessAddress, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        self.assertEqual(search_value_businessAddress,self.dr.find_element_by_xpath('//*[@id="businessAddress"]').get_attribute('value'),
                         '校验详情页面经营地址')
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.assertEqual('行业管理列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text,'校验返回功能')
        print('管理防范-行业场所管理：经营地址条件查询功能正常')

    def test06_hangyechangsuo_deleet(self):
        self.hangyechangsuo_search()
        search_value_registrationName = '精伦电子'
        self.dr.find_element_by_xpath('//*[@id="registrationName"]').send_keys(search_value_registrationName)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_registrationName, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[2]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(10)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('管理防范-行业场所管理：删除功能正常')

if __name__=='__main__':
    unittest.main()