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

class TESTCAST_QUNFANGGUANLI(TESTCASE):
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

    def qunfangxinxiguanli_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/a[2]').click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '人口管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[10]/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="605"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('群防信息管理列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '群防信息管理')

    def test1_qunfangxinxiguanli_add(self):
        self.qunfangxinxiguanli_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        self.dr.find_element_by_xpath('//*[@id="infoCollectIp"]').send_keys('192.168.110.91')
        self.dr.find_element_by_xpath('//*[@id="infoCollectPerson"]').send_keys('林峰')
        self.dr.find_element_by_xpath('//*[@id="infoSort"]').send_keys('宗教场所')
        self.dr.find_element_by_xpath('//*[@id="infoKeyword"]').send_keys('宗教、达赖、涉恐')
        self.dr.find_element_by_xpath('//*[@id="infoLabel"]').send_keys('宗教')
        self.dr.find_element_by_xpath('//*[@id="infoValueEvaluate"]').send_keys('一般')
        self.dr.find_element_by_xpath('//*[@id="infoRemark"]').send_keys('192.168.110.91-林峰')
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual('林峰',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[2]').text,'校验新增、返回和默认排序')
        print('人口管理-群防信息管理：新增功能正常')

    def test2_qunfangxinxiguanli_search_infoLabel(self):
        self.qunfangxinxiguanli_search()
        search_value_infoLabel='宗教'
        self.dr.find_element_by_xpath('//*[@id="infoLabel"]').send_keys(search_value_infoLabel)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 6
        self.pagination_num(paginal_number, search_value_infoLabel, column)
        print('人口管理-群防信息管理：信息标注条件查询功能正常')

    def test3_qunfangxinxiguanli_search_infoKeyword(self):
        self.qunfangxinxiguanli_search()
        search_value_infoKeyword='涉恐'
        self.dr.find_element_by_xpath('//*[@id="infoKeyword"]').send_keys(search_value_infoKeyword)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_infoKeyword, column)
        print('人口管理-群防信息管理：信息关键词条件查询功能正常')

    def test4_qunfangxinxiguanli_search_infoSort(self):
        self.qunfangxinxiguanli_search()
        search_value_infoSort='宗教场所'
        self.dr.find_element_by_xpath('//*[@id="infoSort"]').send_keys(search_value_infoSort)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_infoSort, column)
        print('人口管理-群防信息管理：信息关键词条件查询功能正常')

    def test5_qunfangxinxiguanli_edit(self):
        self.qunfangxinxiguanli_search()
        search_value_infoLabel='宗教'
        self.dr.find_element_by_xpath('//*[@id="infoLabel"]').send_keys(search_value_infoLabel)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 6
        self.pagination_num(paginal_number, search_value_infoLabel, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[7]/a').click()
        self.dr.find_element_by_xpath('//*[@id="infoValueEvaluate"]').clear()
        self.dr.find_element_by_xpath('//*[@id="infoValueEvaluate"]').send_keys('良好')
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual('林峰', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[2]').text, '校验编辑、返回和默认排序')
        self.assertEqual('良好',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,'校验编辑、返回和默认排序')
        print('人口管理-群防信息管理：编辑功能正常')

    def test6_qunfangxinxiguanli_delete(self):
        self.qunfangxinxiguanli_search()
        search_value_infoLabel='宗教'
        self.dr.find_element_by_xpath('//*[@id="infoLabel"]').send_keys(search_value_infoLabel)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 6
        self.pagination_num(paginal_number, search_value_infoLabel, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('人口管理-群防信息管理：删除功能正常')


if __name__=='__main__':
    unittest.main()