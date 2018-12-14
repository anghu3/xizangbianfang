# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 14:11:17 2018

@author: PCCC
"""
import unittest
from selenium import webdriver
import selenium.webdriver.support.ui as ui
import time
import os
import re
from public_package.pubilc_package import url,login_name,login_name_test,login_password,login_password_test
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''
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
import sys
from public_package.pubilc_package import url,login_name,login_name_test,login_password,login_password_test
from public_package.pubilc_package import sheet_setting, search, reset, currMenupath, page_title, goback, saveBtn,sheet_menu,sheet_prompt_message,work_space
from public_package.pubilc_package import TESTCASE
import xlrd
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

xlsfile=work_space+r'\\'+sheet_menu.col_values(6,7,8)[0]
excel = xlrd.open_workbook(xlsfile)
global sheet
sheet = excel.sheet_by_name('外籍人口')

class TESTCAST_WJRK(TESTCASE):

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

    def wjrk_search(self):
        self.login(login_name,login_password)
        time.sleep(5)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,7,8)[0]).click()
        time.sleep(2)
        self.assertEqual('人口管理', self.dr.find_element_by_xpath(currMenupath).text, '人口管理')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,7,8)[0]).click()
        time.sleep(2)
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,7,8)[0]).click()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('外籍人口列表', self.dr.find_element_by_xpath(page_title).text,
                         '外籍人口')

    def test01_wjrk_search_name(self):
        self.wjrk_search()
        search_value_name = sheet.col_values(1,0,1)[0]
        name_path=sheet.col_values(1,1,2)[0]
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath(sheet.col_values(1,1,2)[0]).send_keys(search_value_name)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 1
        self.pagination_num(paginal_number,search_value_name,column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(name_path).get_attribute('value'),
                            '中文姓名-重置功能异常')
        print('人口管理-人员基本信息-外籍人口:姓名条件查询功能正常')

    def test02_wjrk_search_gj(self):
        self.wjrk_search()
        search_value_gj=sheet.col_values(1,2,3)[0]
        self.dr.find_element_by_xpath('//*[@id="citizenship_chosen"]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="citizenship_chosen"]/div/ul/li[44]').click()
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 5
        self.pagination_num(paginal_number, search_value_gj, column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('请选择', self.dr.find_element_by_xpath('//*[@id="citizenship_chosen"]/a/span').text,
                         '国籍-重置功能异常')
        print("人口管理-人员基本信息-外籍人口：国籍条件查询功能正常")


    def test03_wjrk_search_cardid(self):
        self.wjrk_search()
        search_value_cardid = sheet.col_values(1,4,5)[0]
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath(sheet.col_values(1,5,6)[0]).send_keys(search_value_cardid)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 6
        self.pagination_num(paginal_number,search_value_cardid, column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1,5,6)[0]).get_attribute('value'),
                            '证件号码-重置功能异常')
        print('人口管理-人员基本信息-外籍人口:证件号码条件查询功能正常')

    def test04_wjrk_search_yingwenxing(self):
        self.wjrk_search()
        search_value_yingwenxing = sheet.col_values(1,6,7)[0]
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath(sheet.col_values(1,7,8)[0]).send_keys(search_value_yingwenxing)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 2
        self.pagination_num(paginal_number, search_value_yingwenxing, column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1,7,8)[0]).get_attribute('value'),
                            '英文姓-重置功能异常')
        print('人口管理-人员基本信息-外籍人口:英文姓条件查询功能正常')

    def test05_wjrk_search_yingwenming(self):
        self.wjrk_search()
        search_value_yingwenming = sheet.col_values(1,8,9)[0]
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath(sheet.col_values(1,9,10)[0]).send_keys(search_value_yingwenming)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 3
        self.pagination_num(paginal_number, search_value_yingwenming, column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1,9,10)[0]).get_attribute('value'),
                            '英文名-重置功能异常')
        print('人口管理-人员基本信息-外籍人口:英文名条件查询功能正常')

    def test06_wjrk_search_all(self):
        self.wjrk_search()
        search_value_name = sheet.col_values(1, 0, 1)[0]
        name_path = sheet.col_values(1, 1, 2)[0]
        search_value_gj = sheet.col_values(1, 2, 3)[0]
        search_value_cardid = sheet.col_values(1, 4, 5)[0]
        search_value_yingwenxing = sheet.col_values(1, 6, 7)[0]
        search_value_yingwenming = sheet.col_values(1, 8, 9)[0]
        self.dr.find_element_by_xpath(name_path).send_keys(search_value_name)
        self.dr.find_element_by_xpath('//*[@id="citizenship_chosen"]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="citizenship_chosen"]/div/ul/li[44]').click()
        self.dr.find_element_by_xpath(sheet.col_values(1, 5, 6)[0]).send_keys(search_value_cardid)
        self.dr.find_element_by_xpath(sheet.col_values(1, 7, 8)[0]).send_keys(search_value_yingwenxing)
        self.dr.find_element_by_xpath(sheet.col_values(1, 9, 10)[0]).send_keys(search_value_yingwenming)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        self.pagination_num(paginal_number, search_value_name, 1)
        self.pagination_num(paginal_number,search_value_gj,5)
        self.pagination_num(paginal_number,search_value_cardid,6)
        self.pagination_num(paginal_number,search_value_yingwenxing,2)
        self.pagination_num(paginal_number,search_value_yingwenming,3)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        self.assertEqual('', self.dr.find_element_by_xpath(name_path).get_attribute('value'),
                         '中文姓名-重置功能异常')
        self.assertEqual('请选择', self.dr.find_element_by_xpath('//*[@id="citizenship_chosen"]/a/span').text,
                         '国籍-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1, 5, 6)[0]).get_attribute('value'),
                         '证件号码-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1, 7, 8)[0]).get_attribute('value'),
                         '英文姓-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(sheet.col_values(1, 9, 10)[0]).get_attribute('value'),
                         '英文名-重置功能异常')
        print('人口管理-人员基本信息-外籍人口:英文名条件查询功能正常')



    def test07_wjrk_xiangqing(self):
        self.wjrk_search()
        search_value_cardid = sheet.col_values(1,4,5)[0]
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath(sheet.col_values(1,5,6)[0]).send_keys(search_value_cardid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value_cardid, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[6]').text,
                         '英文名条件查询')
        search_value_name=self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[1]').text
        search_value_carid=self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[6]').text
        search_value_guoji=self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[5]').text
        search_value_yingwenxing=self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        time.sleep(5)
        self.assertIn(search_value_name,self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/div[2]').text,'校验详情页面中文姓名')
        self.assertIn(search_value_carid,self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div[10]/div/div[2]').text,'校验详情页面证件号码')
        self.assertIn(search_value_guoji,self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div[5]/div/div[2]').text,'校验详情页面国籍')
        self.assertIn(search_value_yingwenxing,self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]').text,'校验详情页面英文姓')
        self.assertIn(sheet.col_values(1,8,9)[0],self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div[3]/div/div[2]').text,'校验详情页面英文名')
        print('人口管理-人员基本信息-外籍人口:详情功能正常')

    def test08_wjrk_zhixiqingshu(self):
        self.wjrk_search()
        search_value_yingwenming = 'sam'
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[5]/div/input').send_keys(search_value_yingwenming)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value_yingwenming, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]').text,
                         '新增直系亲属')
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        time.sleep(5)
        '''新增输入'''
        self.dr.find_element_by_xpath('//*[@id="addRow"]').click()
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]/span/div/form/div/div[1]/div/input').send_keys('萨博')
        option_chioce2=Select(self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[4]/span/div/form/div/div[1]/div/select'))
        option_chioce2.select_by_value('1')
        option_chioce_3 = Select(self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[5]/span/div/form/div/div[1]/div/select'))
        option_chioce_3.select_by_value('22')
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[6]/span/div/form/div/div[1]/div/input').send_keys('15874587458')
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[7]/span/div/form/div/div[1]/div/input').send_keys('发展大道建设1路101号')
        Select(self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[8]/span/div/form/div/div[1]/div/select')).select_by_value('1')
        '''保存'''
        self.dr.find_element_by_xpath('//*[@id="fpdSave"]').click()
        '''返回'''
        self.dr.find_element_by_xpath('/html/body/a').click()
        '''查询'''
        self.dr.find_element_by_xpath('//*[@id="form"]/div[5]/div/input').send_keys(search_value_yingwenming)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value_yingwenming, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]').text,
                         '新增直系亲属')
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        time.sleep(5)
        self.assertIn('萨博',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]/a').text,'校验新增是否正常')
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[1]/input').click()
        '''删除'''
        self.dr.find_element_by_xpath('//*[@id="delRow"]').click()
        self.dr.find_element_by_xpath('//*[@id="fpdSave"]').click()
        print('人口管理-人员基本信息-外籍人口:直系亲属新增删除功能正常')

if __name__ == '__main__':
    unittest.main()