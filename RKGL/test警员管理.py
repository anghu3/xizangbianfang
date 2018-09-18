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

class TESTCAST_JINGYUAN(TESTCASE):
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

    def jingyuan_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div/a[2]/div[2]/img[2]').click()
        time.sleep(5)
        self.assertEqual('勤务管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '勤务管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="642"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('警员基础信息列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '警员管理')

    def test1_jingyuan_add(self):
        self.jingyuan_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        add_value_jinghao='0175420'
        self.dr.find_element_by_xpath('//*[@id="manForm"]/div[1]/div[1]/div/input').send_keys(add_value_jinghao)
        self.dr.find_element_by_xpath('//*[@id="affiliationOrg"]').click()
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_span"]').click()
        self.dr.find_element_by_xpath('//*[@id="manForm"]/div[2]/div[1]/div/input').send_keys('欧阳')
        self.dr.find_element_by_xpath('//*[@id="manForm"]/div[2]/div[2]/div/input').send_keys('500107198901218926')
        self.dr.find_element_by_xpath('//*[@id="manForm"]/div[4]/div[1]/div/input').send_keys('2018-09-07')
        self.dr.find_element_by_xpath('//*[@id="manForm"]/div[4]/div[2]/div/input').send_keys('2018-09-07')
        self.dr.find_element_by_xpath('//*[@id="manForm"]/div[5]/div[1]/div/input').send_keys('湖北武汉')
        self.dr.find_element_by_xpath('//*[@id="manForm"]/div[5]/div[2]/div/input').send_keys('湖北武汉')
        self.dr.find_element_by_xpath('//*[@id="manForm"]/div[6]/div[2]/div/input').send_keys('2018-09-07')
        self.dr.find_element_by_xpath('//*[@id="manForm"]/div[7]/div[1]/div/input').send_keys('13587458745')
        self.dr.find_element_by_xpath('//*[@id="manForm"]/div[8]/div/div/input').send_keys('武汉市江岸区沿江大道188号')
        self.dr.find_element_by_xpath('//*[@id="manForm"]/div[9]/div[1]/div/input').send_keys('175')
        self.dr.find_element_by_xpath('//*[@id="manForm"]/div[10]/div[1]/div/input').send_keys('本科')
        self.dr.find_element_by_xpath('//*[@id="manForm"]/div[11]/div/div/textarea').send_keys('武汉市人民政府是武汉市的行政管理机关，是副省级行政机关，位于武汉市江岸区沿江大道188号')
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual(add_value_jinghao,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,'校验新增，返回和默认排序')
        print('勤务管理-警员管理：新增功能正常')

    def test2_jingyuan_search_jinghao(self):
        self.jingyuan_search()
        search_value_jinghao='0175420'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value_jinghao)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_jinghao, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        self.assertEqual(search_value_jinghao,self.dr.find_element_by_xpath('//*[@id="manForm"]/div[1]/div[1]/div/input').get_attribute('value'),'校验详情页面警员编号')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_jinghao, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,
                         '校验返回和默认排序')
        print('勤务管理-警员管理：警员编号条件查询功能正常')

    def test3_jingyuan_search_name(self):
        self.jingyuan_search()
        search_value_name='欧阳'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/div/input').send_keys(search_value_name)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_name, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        self.assertEqual(search_value_name,self.dr.find_element_by_xpath('//*[@id="manForm"]/div[2]/div[1]/div/input').get_attribute('value'),'校验详情页面警员姓名')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_name, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,
                         '校验返回和默认排序')
        print('勤务管理-警员管理：警员姓名条件查询功能正常')

    def test4_jingyuan_search_ssdw(self):
        self.jingyuan_search()
        search_value_ssdw='山南支队'
        self.dr.find_element_by_xpath('//*[@id="affiliationOrg"]').click()
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_span"]').click()
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_ssdw, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        self.assertEqual(search_value_ssdw,self.dr.find_element_by_xpath('//*[@id="affiliationOrg"]').get_attribute('value'),'校验详情页面警员所属单位')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_ssdw, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[5]').text,
                         '校验返回和默认排序')
        print('勤务管理-警员管理：所属单位条件查询功能正常')

    def test5_jingyuan_search_sex(self):
        self.jingyuan_search()
        option_chioce=Select(self.dr.find_element_by_xpath('//*[@id="form"]/div[4]/div/select'))
        option_chioce.select_by_value('2')
        search_value_sex=option_chioce.first_selected_option.text
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 6
        self.pagination_num(paginal_number, search_value_sex, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        self.assertEqual(search_value_sex,self.dr.find_element_by_xpath('//*[@id="manForm"]/div[3]/div[1]/div/select/option[1]').text,'校验详情页面警员性别')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_sex, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[6]').text,
                         '校验返回和默认排序')
        print('勤务管理-警员管理：警员性别条件查询功能正常')

    def test6_jingyuan_search_status(self):
        self.jingyuan_search()
        option_chioce=Select(self.dr.find_element_by_xpath('//*[@id="form"]/div[5]/div/select'))
        option_chioce.select_by_value('1')
        search_value_status=option_chioce.first_selected_option.text
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 10
        self.pagination_num(paginal_number, search_value_status, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        self.assertEqual(search_value_status,self.dr.find_element_by_xpath('//*[@id="manForm"]/div[10]/div[2]/div/select/option[1]').text,'校验详情页面警员状态')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_status, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[10]').text,
                         '校验返回和默认排序')
        print('勤务管理-警员管理：警员状态条件查询功能正常')

    def test7_jingyuan_edit(self):
        self.jingyuan_search()
        search_value_jinghao='0175420'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value_jinghao)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_jinghao, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        edit_value_name='欧阳靖'
        self.dr.find_element_by_xpath('//*[@id="manForm"]/div[2]/div[1]/div/input').clear()
        self.dr.find_element_by_xpath('//*[@id="manForm"]/div[2]/div[1]/div/input').send_keys(edit_value_name)
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual(edit_value_name, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,'校验返回和默认排序')
        print('勤务管理-警员管理：编辑功能正常')

    def test8_jingyuan_delete(self):
        self.jingyuan_search()
        search_value_jinghao = '0175420'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value_jinghao)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_jinghao, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('勤务管理-警员管理：删除功能正常')


if __name__=='__main__':
    unittest.main()