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


def findnum(string):
    comp = re.compile('-?[1-9]\d*')
    list_str = comp.findall(string)
    list_num = []
    for item in list_str:
        item = int(item)
        list_num.append(item)
    return list_num

class TESTCAST_SIHEI(TESTCASE):
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

    def sihei_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/a[2]').click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '人口管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[6]/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="772"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('四黑人员列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text,
                         '四黑人员')

    def test1_sihei_add(self):
        self.sihei_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        add_search_carid='540123198506025515'
        add_search_yw='导游'
        add_search_name='王晓水'
        self.dr.find_element_by_xpath('//*[@id="idCard"]').send_keys(add_search_carid)
        Select(self.dr.find_element_by_xpath('//*[@id="personType"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="mainBusiness"]').send_keys(add_search_yw)
        self.dr.find_element_by_xpath('//*[@id="personName"]').send_keys(add_search_name)
        self.dr.find_element_by_xpath('//*[@id="mainTourists"]').send_keys('旅行社')
        self.dr.find_element_by_xpath('//*[@id="activityArea"]').send_keys('各大旅游景点')
        self.dr.find_element_by_xpath('//*[@id="activityTimeSlot"]').send_keys('7:30-18:30')
        self.dr.find_element_by_xpath('//*[@id="startBlackDate"]').send_keys('2018-08-08')
        self.dr.find_element_by_xpath('//*[@id="dayTraffic"]').send_keys('24')
        self.dr.find_element_by_xpath('//*[@id="averagePrice"]').send_keys('200')
        self.dr.find_element_by_xpath('//*[@id="riskAssess"]').send_keys('容易被宰客')
        self.dr.find_element_by_xpath('//*[@id="dutyPerson"]').send_keys('马汉')
        #责任单位
        self.dr.find_element_by_xpath('//*[@id="remark"]').send_keys('各大旅游景点')
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        time.sleep(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.assertEqual('四黑人员列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text,
                         '四黑人员')
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(add_search_name,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,'校验新增是否成功，默认排序')
        self.assertEqual(add_search_carid,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,'校验新增是否成功，默认排序')
        print('人口管理-部局七类库-四黑人员：新增功能正常')

    def test2_sihei_search_name(self):
        self.sihei_search()
        search_value_name='王晓水'
        self.dr.find_element_by_xpath('//*[@id="personName"]').send_keys(search_value_name)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number,search_value_name,column)
        # self.assertEqual(search_value_name,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]').text,'校验姓名条件查询')
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/a').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value_name,self.dr.find_element_by_xpath('//*[@id="personName"]').get_attribute('value'),'校验详情')
        print('人口管理-部局七类库-四黑人员：姓名条件查询功能正常')


    def test3_sihei_search_carid(self):
        self.sihei_search()
        search_value_carid = '540123198506025515'
        self.dr.find_element_by_xpath('//*[@id="idCard"]').send_keys(search_value_carid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_carid, column)
        # self.assertEqual(search_value_carid, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[4]').text,
        #                  '校验身份证号条件查询')
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/a').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value_carid,
                         self.dr.find_element_by_xpath('//*[@id="idCard"]').get_attribute('value'), '校验详情')
        print('人口管理-部局七类库-四黑人员：身份证号条件查询功能正常')

    def test4_sihei_search_zrr(self):
        self.sihei_search()
        search_value_zrr = '马汉'
        self.dr.find_element_by_xpath('//*[@id="dutyPerson"]').send_keys(search_value_zrr)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 7
        self.pagination_num(paginal_number, search_value_zrr, column)
        # self.assertEqual(search_value_zrr, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[7]').text,
        #                  '校验身份证号条件查询')
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/a').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value_zrr,
                         self.dr.find_element_by_xpath('//*[@id="dutyPerson"]').get_attribute('value'), '校验详情')
        print('人口管理-部局七类库-四黑人员：身份证号条件查询功能正常')

    def test5_sihei_search_rylx(self):
        self.sihei_search()
        Select(self.dr.find_element_by_xpath('//*[@id="personType"]')).select_by_value('1')
        # search_value_rylx=self.dr.find_element_by_xpath('//*[@id="personType"]').text
        search_value_rylx='黑导游'
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_rylx, column)
        print('人口管理-部局七类库-四黑人员：人员类型条件查询功能正常')

    def test6_sihei_delete(self):
        self.sihei_search()
        search_value_name = '王晓水'
        self.dr.find_element_by_xpath('//*[@id="personName"]').send_keys(search_value_name)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value_name, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]').text,
                         '校验姓名条件查询')
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[2]/div[1]/input').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        # self.dr.switch_to.frame('iframeb')
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('人口管理-部局七类库-四黑人员：删除功能正常')

if __name__ == '__main__':
    unittest.main()
