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

class TESTCAST_FAHUI(TESTCASE):
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

    def fahui_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/a[2]').click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '人口管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[7]/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="773"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('法会列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '法会')

    def test1_fahui_add(self):
        self.fahui_search()
        self.dr.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/a[2]').click()
        self.dr.find_element_by_xpath('//*[@id="ceremonyName"]').send_keys('传昭法会')
        self.dr.find_element_by_xpath('//*[@id="ceremonyArea"]').send_keys('大昭寺')
        self.dr.find_element_by_xpath('//*[@id="organizateMonkNum"]').send_keys('264')
        self.dr.find_element_by_xpath('//*[@id="realityMonkNum"]').send_keys('260')
        self.dr.find_element_by_xpath('//*[@id="conscientiousPolice"]').send_keys('马汉')
        self.dr.find_element_by_xpath('//*[@id="telephone"]').send_keys('15474587458')
        self.dr.find_element_by_xpath('//*[@id="remarks"]').send_keys('传昭法会是为纪念释迦牟尼以神变之法大败外道教徒功德而创立的法会，是藏传佛教重要的宗教活动。藏语称“默朗钦摩”，亦称传大昭、祈愿大法会。')
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.assertEqual('法会列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,'验证返回功能')
        print('人口管理-701数据库-法会：新增功能正常')

    def test2_fahui_search_name(self):
        self.fahui_search()
        search_value_name='传昭法会'
        self.dr.find_element_by_xpath('//*[@id="ceremonyName"]').send_keys(search_value_name)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_name, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/a').click()
        self.assertEqual(search_value_name,self.dr.find_element_by_xpath('//*[@id="ceremonyName"]').get_attribute('value'),'校验详情页面的法会名')
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.assertEqual('法会列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text, '验证返回功能')
        print('人口管理-701数据库-法会：法会名称条件查询功能正常')

    def test3_fahui_search_address(self):
        self.fahui_search()
        search_value_address='大昭寺'
        self.dr.find_element_by_xpath('//*[@id="ceremonyArea"]').send_keys(search_value_address)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_address, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/a').click()
        self.assertEqual(search_value_address,self.dr.find_element_by_xpath('//*[@id="ceremonyArea"]').get_attribute('value'),'校验详情页面的法会名')
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.assertEqual('法会列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text, '验证返回功能')
        print('人口管理-701数据库-法会：法会名称条件查询功能正常')

    def test4_fahui_delete(self):
        self.fahui_search()
        search_value_name = '传昭法会'
        self.dr.find_element_by_xpath('//*[@id="ceremonyName"]').send_keys(search_value_name)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_name, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('人口管理-701数据库-法会：删除功能正常')

if __name__=='__main__':
    unittest.main()