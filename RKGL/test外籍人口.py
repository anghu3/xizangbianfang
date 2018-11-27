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
from public_package.pubilc_package import TESTCASE
import xlrd
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

class TESTCAST_WJRK(unittest.TestCase):

    dir = os.getcwd()
    xlsfile = dir + '.xls'
    excel = xlrd.open_workbook(xlsfile)
    sheet_name = excel.sheet_names()[0]
    global sheet_menu
    sheet_menu = excel.sheet_by_name('menu')
    global sheet
    sheet = excel.sheet_by_name('暂住人口')
    global sheet_setting, search, reset, add, delete, currMenupath, page_title
    sheet_setting = excel.sheet_by_name('setting')
    search = sheet_setting.col_values(2, 1, 2)[0]
    reset = sheet_setting.col_values(3, 1, 2)[0]
    currMenupath = sheet_setting.col_values(0, 1, 2)[0]
    page_title = sheet_setting.col_values(1, 1, 2)[0]

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
        self.pagination_num(paginal_number,name_path,column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(5)
        self.assertEqual('', self.dr.find_element_by_xpath(name_path).get_attribute('value'),
                            '中文名-重置功能异常')
        print('人口管理-人员基本信息-外籍人口:姓名条件查询功能正常')

    def test2_wjrk_search_gj(self):
        self.wjrk_search()
        print("人口管理-人员基本信息-外籍人口：由于国际选择控件无法选择到，该查询后续实现自动化")


    def test3_wjrk_search_cardid(self):
        self.wjrk_search()
        search_value = 'ZJ0002'
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[3]/div/input').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[6]').text,
                         '证件号码条件查询')
        self.dr.find_element_by_xpath('//*[@id="reset"]').click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.assertNotEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[6]').text,
                            '重置功能')
        print('人口管理-人员基本信息-外籍人口:证件号码条件查询功能正常')

    def test4_wjrk_search_yingwenxing(self):
        self.wjrk_search()
        search_value_yingwenxing = 'L'
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[4]/div/input').send_keys(search_value_yingwenxing)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value_yingwenxing, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text,
                         '英文姓条件查询')
        self.dr.find_element_by_xpath('//*[@id="reset"]').click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.assertNotEqual(search_value_yingwenxing, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text,
                            '重置功能')
        print('人口管理-人员基本信息-外籍人口:英文姓条件查询功能正常')

    def test5_wjrk_search_yingwenming(self):
        self.wjrk_search()
        search_value_yingwenming = 'sam'
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[5]/div/input').send_keys(search_value_yingwenming)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value_yingwenming, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]').text,
                         '英文名条件查询')
        self.dr.find_element_by_xpath('//*[@id="reset"]').click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.assertNotEqual(search_value_yingwenming, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]').text,
                            '重置功能')
        print('人口管理-人员基本信息-外籍人口:英文名条件查询功能正常')

    def test6_wjrk_search_xiangqing(self):
        self.wjrk_search()
        search_value_yingwenming = 'sam'
        self.dr.implicitly_wait(30)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[5]/div/input').send_keys(search_value_yingwenming)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value_yingwenming, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]').text,
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
        self.assertIn(search_value_yingwenming,self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div[3]/div/div[2]').text,'校验详情页面英文名')
        print('人口管理-人员基本信息-外籍人口:详情功能正常')

    def test7_wjrk_search_zhixiqingshu(self):
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