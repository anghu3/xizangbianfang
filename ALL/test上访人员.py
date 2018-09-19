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
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''


def findnum(string):
    comp = re.compile('-?[1-9]\d*')
    list_str = comp.findall(string)
    list_num = []
    for item in list_str:
        item = int(item)
        list_num.append(item)
    return list_num

class TESTCAST_SHANGFANG(unittest.TestCase):
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

    def pagination_num(self,paginal_number,search_value,column):
        number = findnum(paginal_number)[-1]
        tens = int(number / 10)
        single = int(number % 10)
        if tens == 0:
            for j in range(1, single + 1):
                xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
        if tens == 1:
            for j in range(1, 11):
                xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
            page = '/html/body/div[3]/div[2]/div[1]/div/div[4]/div[2]/ul/li[' + str(tens + 3) + ']/a'
            self.dr.find_element_by_xpath(page).click()
            if single == 0:
                print(single)
            else:
                for j in range(1, single + 1):
                    xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                    self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
                    time.sleep(5)
        if tens < 7:
            for i in range(1, tens + 2):
                if i < tens + 1:
                    for j in range(1, 11):
                        xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                        self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
                    page = '/html/body/div[3]/div[2]/div[1]/div/div[4]/div[2]/ul/li[' + str(tens + 3) + ']/a'
                    self.dr.find_element_by_xpath(page).click()
                if i == tens + 1:
                    for j in range(1, single + 1):
                        if single == 0:
                            print(single)
                        else:
                            for j in range(1, single + 1):
                                xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                                self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
                                time.sleep(5)
        if tens > 7:
            for i in range(1, tens + 2):
                if i < tens + 1:
                    for j in range(1, 11):
                        xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                        self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
                    self.dr.find_element_by_xpath(
                        '/html/body/div[3]/div[2]/div[1]/div/div[4]/div[2]/ul/li[9]/a').click()
                if i == tens + 1:
                    for j in range(1, single + 1):
                        if single == 0:
                            print(single)
                        else:
                            for j in range(1, single + 1):
                                xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                                self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
                                time.sleep(5)

    def shangfang_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/a[2]').click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '人口管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[6]/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="565"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('上访人员', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '上访人员')

    def test1_shangfang_search_name(self):
        self.shangfang_search()
        search_value = '丁淼林'
        self.dr.find_element_by_xpath('//*[@id="xm"]').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(10)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 2
        self.pagination_num(paginal_number,search_value,column)
        print('人口管理-部局七类库-上访人员：姓名条件查询')

    def test2_shangfang_search_cardid(self):
        self.shangfang_search()
        search_value = '36031319800217401X'
        self.dr.find_element_by_xpath('//*[@id="sfzh"]').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(10)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 1
        self.pagination_num(paginal_number,search_value,column)
        print('人口管理-部局七类库-上访人员：身份证号条件查询')

if __name__ == '__main__':
    unittest.main()