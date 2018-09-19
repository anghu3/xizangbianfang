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

class TESTCAST_ZIDINGYI(TESTCASE):
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

    def zidingyi_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/a[2]').click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '人口管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[8]/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="331"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('自定义人员监控', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '自定义人员')

    def test1_zidingyi_add(self):
        self.zidingyi_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        add_value = '540123198506025515'
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(add_value)
        self.dr.find_element_by_xpath('//*[@id="customForm"]/div[1]/div[2]/div/div[1]/div[2]/a').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="personsType"]').send_keys('盗窃惯犯')
        self.dr.find_element_by_xpath('//*[@id="credentials"]').send_keys('98574857')
        self.dr.find_element_by_xpath('//*[@id="livingPlace"]').send_keys('西藏自治区聂拉木县聂拉木镇充堆村')
        option_bz = Select(self.dr.find_element_by_xpath('//*[@id="isLimit"]'))
        option_bz.select_by_index(1)
        # js = "$('input[id=txtBeginDate]').attr('readonly','')"
        # self.dr.execute_script(js)
        # self.dr.find_element_by_xpath('//*[@id="starttime"]').send_keys('2018-08-01')
        # self.dr.find_element_by_xpath('//*[@id="endtime"]').send_keys('2018-08-01')
        option_ts = Select(self.dr.find_element_by_xpath('//*[@id="isAttention"]'))
        option_ts.select_by_index(2)
        self.dr.find_element_by_xpath('//*[@id="recognitionInfo"]').send_keys('盗窃惯犯')
        self.dr.find_element_by_xpath('//*[@id="monitorReason"]').send_keys('盗窃惯犯')
        option_tb = Select(self.dr.find_element_by_xpath('//*[@id="isNotify"]'))
        option_tb.select_by_index(2)
        self.dr.find_element_by_xpath('//*[@id="processingScheme"]').send_keys('监控')
        self.dr.find_element_by_xpath('//*[@id="note"]').send_keys('重点监控')
        self.dr.find_element_by_xpath('//*[@id="supervIdcardNo"]').send_keys(add_value)
        self.dr.find_element_by_xpath('//*[@id="supervName"]').send_keys('林峰')
        self.dr.find_element_by_xpath('//*[@id="supervWx"]').send_keys('13247859687')
        self.dr.find_element_by_xpath('//*[@id="supervBeWx"]').send_keys('13247859687')
        self.dr.find_element_by_xpath('//*[@id="reportCycle"]').send_keys('5')
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        time.sleep(5)
        # self.assertEqual(add_value,self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').get_attribute('value'),'校验保存是否会清空表单')
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('自定义人员监控', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '校验返回功能是否正常')
        print('人口管理-自定义人员：新增功能正常')

    def test2_zidingyi_search_name(self):
        self.zidingyi_search()
        search_value = '索朗旺堆'
        self.dr.find_element_by_xpath('//*[@id="xm"]').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number,search_value,column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        self.assertEqual(search_value, self.dr.find_element_by_xpath('//*[@id="xm"]').text, '校验详细信息-姓名')
        print('人口管理-自定义人员：姓名条件查询')

    def test3_zidingyi_search_cardid(self):
        self.zidingyi_search()
        search_value = '540123198506025515'
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(10)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number,search_value,column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        self.assertEqual(search_value, self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').get_attribute('value'),
                         '校验详细信息-身份证号')
        print('人口管理-自定义人员：身份证号条件查询')

    def test4_zidingyi_search_age(self):
        self.zidingyi_search()
        search_value = '33'
        self.dr.find_element_by_xpath('//*[@id="start"]').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="end"]').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(10)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 7
        self.pagination_num(paginal_number,search_value,column)
        print('人口管理-自定义人员：年龄条件查询')

    # def test5_zidingyi_search_namecaridage(self):
    #     self.zidingyi_search()
    #     search_value_age = '33'
    #     search_value_name='索朗旺堆'
    #     search_value_carid='540123198506025515'
    #     self.dr.find_element_by_xpath('//*[@id="xm"]').send_keys(search_value_name)
    #     self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(search_value_carid)
    #     self.dr.find_element_by_xpath('//*[@id="start"]').send_keys(search_value_age)
    #     self.dr.find_element_by_xpath('//*[@id="end"]').send_keys(search_value_age)
    #     self.dr.find_element_by_xpath('//*[@id="search"]').click()
    #     self.dr.switch_to.default_content()
    #     time.sleep(10)
    #     self.dr.switch_to.frame('iframeb')
    #     paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
    #     column = 7
    #     self.pagination_num(paginal_number,search_value_age,column)
    #     print('人口管理-自定义人员：多条件组合查询')

    def test5_zidingyi_delete(self):
        self.zidingyi_search()
        search_value = '540123198506025515'
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(10)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        time.sleep(2)
        self.dr.switch_to.default_content()
        time.sleep(1)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        print('人口管理-自定义人员：删除功能正常')

if __name__ == '__main__':
    unittest.main()