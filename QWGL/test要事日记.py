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

class TESTCAST_YSRJ(TESTCASE):
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

    def ysrj_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div/a[2]/div[2]/img[2]').click()
        time.sleep(3)
        self.assertEqual('勤务管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '勤务管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="538"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(3)
        self.assertEqual('要事日记信息列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '要事日记')

    def test1_ysrj_add(self):
        self.ysrj_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        self.dr.find_element_by_xpath('//*[@id="diaryDate"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="diaryForm"]/div[1]/div[1]/div/div[2]/ul/li[2]/table/tbody/tr/td[2]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="diaryForm"]/div[1]/div[2]/div/input').send_keys('雷阵雨')
        self.dr.find_element_by_xpath('//*[@id="affiliationOrg"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_46_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_48_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="organCadreNum"]').send_keys('99999999')
        self.dr.find_element_by_xpath('//*[@id="organPoliceNum"]').send_keys('99999999')
        self.dr.find_element_by_xpath('//*[@id="existCadreNum"]').send_keys('99999999')
        self.dr.find_element_by_xpath('//*[@id="existPoliceNum"]').send_keys('99999999')
        self.dr.find_element_by_xpath('//*[@id="diaryForm"]/div[4]/div[2]/div/input').send_keys('出勤关注交通事故多发点')
        self.dr.find_element_by_xpath('//*[@id="diaryForm"]/div[4]/div[3]/div/input').send_keys('暂无')
        self.dr.find_element_by_xpath('//*[@id="diaryForm"]/div[4]/div[4]/div/textarea').send_keys('暂无')
        self.dr.find_element_by_xpath('//*[@id="diaryForm"]/div[4]/div[5]/div/textarea').send_keys('注意市内事故和积水路段执勤')
        self.dr.find_element_by_xpath('//*[@id="saveImp"]').click()
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual('库局派出所',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[5]').text,'校验新增、返回和默认排序')
        print('勤务管理-要事日记：新增功能')

    def test2_ysrj_search_date(self):
        self.ysrj_search()
        search_value_date=time.strftime("%Y-%m-%d", time.localtime(time.time()))
        # print(search_value_date)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value_date)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_date, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[6]/a').click()
        self.assertIn(search_value_date,self.dr.find_element_by_xpath('//*[@id="diaryDate"]').get_attribute('value'),'校验详情页面日期')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertIn(search_value_date,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,'校验返回和默认排序')
        print('勤务管理-要事日记：日期条件查询功能正常')

    def test3_ysrj_search_ssdw(self):
        self.ysrj_search()
        search_value_ssdw='库局派出所'
        self.dr.find_element_by_xpath('//*[@id="affiliationOrg"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_46_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_48_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_ssdw, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[6]/a').click()
        self.assertIn(search_value_ssdw,self.dr.find_element_by_xpath('//*[@id="affiliationOrg"]').get_attribute('value'),'校验详情页面日期')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertIn(search_value_ssdw,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[5]').text,'校验返回和默认排序')
        print('勤务管理-要事日记：日期条件查询功能正常')

    def test4_ysrj_search_qwrw(self):
        self.ysrj_search()
        search_value_date=time.strftime("%Y-%m-%d", time.localtime(time.time()))
        # print(search_value_date)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value_date)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_date, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[6]/a').click()
        self.dr.find_element_by_xpath('//*[@id="diaryAdd"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]/span/div/form/div/div[1]/div/div/input').send_keys(search_value_date)
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[4]/span/div/form/div/div[1]/div/input').send_keys('交通执勤任务')
        time.sleep(1)
        Select(self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[5]/span/div/form/div/div[1]/div/select')).select_by_value('02')
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[7]/span/div/form/div/div[1]/div/input').send_keys('24')
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="saveImp"]').click()
        time.sleep(3)
        self.assertEqual('交通执勤任务',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[4]/a').text,'校验勤务任务新增')
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('//*[@id="diaryDelete"]').click()
        self.dr.find_element_by_xpath('//*[@id="saveImp"]').click()
        time.sleep(3)
        self.assertEqual('没有找到匹配的记录',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text,'校验勤务任务删除')
        print('勤务管理-要事日记：勤务或任务执行情况新增删除功能正常')

    def test5_ysrj_delete(self):
        self.ysrj_search()
        search_value_date=time.strftime("%Y-%m-%d", time.localtime(time.time()))
        # print(search_value_date)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value_date)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_date, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('勤务管理-要事日记：删除功能')

if __name__=='__main__':
    unittest.main()
