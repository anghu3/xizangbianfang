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

class TESTCAST_SIMIAO(TESTCASE):
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

    def simiao_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/a[2]').click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '人口管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[7]/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="702"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('寺庙列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '寺庙')

    def test1_simiao_add(self):
        self.simiao_search()
        search_add_name='仓姑寺'
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        self.dr.find_element_by_xpath('//*[@id="name"]').send_keys(search_add_name)
        self.dr.find_element_by_xpath('//*[@id="location"]').send_keys('林廓南路29号')
        Select(self.dr.find_element_by_xpath('//*[@id="category"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="compilingCount"]').send_keys('100')
        Select(self.dr.find_element_by_xpath('//*[@id="rank"]')).select_by_value('2')
        self.dr.find_element_by_xpath('//*[@id="realCount"]').send_keys('87')
        Select(self.dr.find_element_by_xpath('//*[@id="police"]')).select_by_value('包拯')
        self.dr.find_element_by_xpath('//*[@id="contact"]').send_keys('13548574785')
        self.dr.find_element_by_xpath('//*[@id="remark"]').send_keys('仓姑寺的定员编制是100名僧尼，但现有87名出家僧尼。阿尼拉们大部分是从山南、林芝、达孜等地慕名前来学法。寺里给每位阿尼拉每月400元人民币。')
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.assertEqual('寺庙列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,'校验返回功能')
        print('人口管理-701数据库-寺庙：新增功能正常')

    def test2_simiao_search_name(self):
        self.simiao_search()
        search_value_name='仓姑寺'
        self.dr.find_element_by_xpath('//*[@id="name"]').send_keys(search_value_name)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 2
        self.pagination_num(paginal_number, search_value_name, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/a').click()
        time.sleep(2)
        self.assertEqual(search_value_name,self.dr.find_element_by_xpath('//*[@id="name"]').get_attribute('value'))
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.assertEqual('寺庙列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text, '校验返回功能')
        print('人口管理-701数据库-寺庙：姓名条件查询功能正常')

    def test3_simiao_search_address(self):
        self.simiao_search()
        search_value_address = '林廓南路29号'
        self.dr.find_element_by_xpath('//*[@id="location"]').send_keys(search_value_address)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_address, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/a').click()
        time.sleep(2)
        self.assertEqual(search_value_address, self.dr.find_element_by_xpath('//*[@id="location"]').get_attribute('value'))
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.assertEqual('寺庙列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text, '校验返回功能')
        print('人口管理-701数据库-寺庙：所在地条件查询功能正常')

    def test4_simiao_search_category(self):
        self.simiao_search()
        # Select_category=Select(self.dr.find_element_by_xpath('//*[@id="category"]'))
        # options=Select_category.options
        # search_value_category=options[1]
        search_value_category = '格鲁派寺庙'
        Select(self.dr.find_element_by_xpath('//*[@id="category"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 6
        self.pagination_num(paginal_number, search_value_category, column)
        # self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/a').click()
        # time.sleep(2)
        # self.assertEqual(search_value_category, self.dr.find_element_by_xpath('//*[@id="location"]').get_attribute('value'))
        # self.dr.find_element_by_xpath('/html/body/a').click()
        # self.assertEqual('寺庙列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text, '校验返回功能')
        print('人口管理-701数据库-寺庙：教派类别条件查询功能正常')

    def test5_simiao_search_rank(self):
        self.simiao_search()
        # search_value_category=Select(self.dr.find_element_by_xpath('//*[@id="category"]')).
        search_value_rank = '正科级'
        Select(self.dr.find_element_by_xpath('//*[@id="rank"]')).select_by_value('2')
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 7
        self.pagination_num(paginal_number, search_value_rank, column)
        # self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/a').click()
        # time.sleep(2)
        # self.assertEqual(search_value_category, self.dr.find_element_by_xpath('//*[@id="location"]').get_attribute('value'))
        # self.dr.find_element_by_xpath('/html/body/a').click()
        # self.assertEqual('寺庙列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text, '校验返回功能')
        print('人口管理-701数据库-寺庙：寺管会级别条件查询功能正常')

    def test6_simiao_delete(self):
        self.simiao_search()
        search_value_name = '仓姑寺'
        self.dr.find_element_by_xpath('//*[@id="name"]').send_keys(search_value_name)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 2
        self.pagination_num(paginal_number, search_value_name, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('人口管理-701数据库-寺庙：删除功能正常')

if __name__=='__main__':
    unittest.main()