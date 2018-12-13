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
import HTMLTestRunner
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

class TESTCAST_YLKCQD(TESTCASE):
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

    def ylkcqd_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div/a[2]/div[2]/img[2]').click()
        time.sleep(5)
        self.assertEqual('勤务管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '勤务管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="584"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('油料库存清单列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '油料库存清单')

    def test1_ylkcqd_add(self):
        self.ylkcqd_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        self.dr.find_element_by_xpath('//*[@id="otype"]/input').send_keys('92')
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        time.sleep(3)
        print('勤务管理-油料库存清单：新增功能正常')

    def test2_ylkcqd_search_oiltype(self):
        self.ylkcqd_search()
        search_value_oiltype='92'
        Select(self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/select')).select_by_value('92')
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number,search_value_oiltype, column)
        global oil_num
        oil_num=self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[4]').text
        print(oil_num)
        print('勤务管理-油料库存清单：油料型号条件查询功能正常')

    def test3_ylkcqd_change_oiltype(self):
        self.ylkcqd_search()
        search_value_oiltype = '92'
        Select(self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/select')).select_by_value('92')
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_oiltype, column)
        edit_value_oiltype='89'
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[7]/a[2]').click()
        self.dr.find_element_by_xpath('//*[@id="otype"]/input').clear()
        self.dr.find_element_by_xpath('//*[@id="otype"]/input').send_keys(edit_value_oiltype)
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        time.sleep(3)
        print('勤务管理-油料库存清单：修改油料型号功能正常')

    def test4_ylkcqd_change_oilnum(self):
        self.ylkcqd_search()
        add_value_num=1000
        snum=int(add_value_num)+int(oil_num)
        self.ylkcqd_search()
        search_value_oiltype = '89'
        Select(self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/select')).select_by_value('89')
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_oiltype, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[7]/a[1]').click()
        self.dr.find_element_by_xpath('//*[@id="snum"]/div/input').clear()
        self.dr.find_element_by_xpath('//*[@id="snum"]/div/input').send_keys(add_value_num)
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        Select(self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/select')).select_by_value('89')
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, str(snum), column)
        print('勤务管理-油料库存清单：增加油料库存功能正常')

    def test5_ylkcqd_add_98(self):
        self.ylkcqd_search()
        add_value_num = 1000
        snum = int(add_value_num) + int(oil_num)
        self.ylkcqd_search()
        search_value_oiltype = '98'
        Select(self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/select')).select_by_value('98')
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_oiltype, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[7]/a[1]').click()
        self.dr.find_element_by_xpath('//*[@id="snum"]/div/input').clear()
        self.dr.find_element_by_xpath('//*[@id="snum"]/div/input').send_keys(add_value_num)
        self.dr.find_element_by_xpath('//*[@id="save"]').click()

    def test6_ylkcqd_search_oilnum(self):
        self.ylkcqd_search()
        search_value_oilnum='1000'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/div/input').send_keys(search_value_oilnum)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.Getdata_Contrast(paginal_number,search_value_oilnum,column)
        print('勤务管理-油料库存清单：库存数量条件功能正常')

    def test7_ylkcqd_delete(self):
        self.ylkcqd_search()
        search_value_oiltype='89'
        Select(self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/select')).select_by_value('89')
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number,search_value_oiltype, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('勤务管理-油料库存清单：删除功能正常')

if __name__=='__main__':
    unittest.main()