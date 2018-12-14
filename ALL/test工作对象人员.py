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
from public_package.pubilc_package import sheet_setting, search, reset, currMenupath, page_title, goback, saveBtn,sheet_menu,sheet_prompt_message,work_space
from public_package.pubilc_package import TESTCASE
import xlrd
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

xlsfile=work_space+r'\\'+sheet_menu.col_values(6,20,21)[0]
excel = xlrd.open_workbook(xlsfile)
global sheet
sheet = excel.sheet_by_name('工作对象人员')

class TESTCAST_SANFEI(TESTCASE):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()

    def tearDown(self):
        self.dr.quit()

    def login(self, username, password):
        self.dr.get(url)
        self.dr.find_element_by_id('vv').send_keys(username)
        self.dr.find_element_by_xpath('//*[@id="login_ff"]/div[2]/input').send_keys(password)
        self.dr.find_element_by_xpath('//*[@id="login_ff"]/a').click()

    def gongzuoduixiang_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,20,21)[0]).click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath(currMenupath).text, '人口管理')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,20,21)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,20,21)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('工作对象人员', self.dr.find_element_by_xpath(page_title).text,
                         '工作对象人员')

    def test1_gongzuoduixiang_add(self):
        self.gongzuoduixiang_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        # self.dr.switch_to.default_content()
        # time.sleep(2)
        # self.dr.switch_to.frame('iframeb')
        add_value_cardid=sheet.col_values(1,2,3)[0]
        cardid_path=sheet.col_values(1,3,4)[0]
        self.dr.find_element_by_xpath(cardid_path).send_keys(add_value_cardid)
        self.dr.find_element_by_xpath('//*[@id="workForm"]/div[1]/div[2]/a').click()
        self.dr.implicitly_wait(2)
        self.dr.find_element_by_xpath('//*[@id="bmch"]').send_keys('萱子')
        Select(self.dr.find_element_by_xpath('//*[@id="ajlb"]')).select_by_value('040118')
        self.dr.find_element_by_xpath('//*[@id="sjjzdxz"]').send_keys('重庆市九龙坡区西彭镇大同街29号5-1')
        self.dr.find_element_by_xpath('//*[@id="lgyy"]').send_keys('入室盗窃')
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual('工作对象人员', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '工作对象人员')
        print('人口管理-部局七类库-工作对象人员：新增功能正常')

    def test2_gongzuoduixiang_search_name(self):
        self.gongzuoduixiang_search()
        search_value_name='刘钰萱'
        self.dr.find_element_by_xpath('//*[@id="xm"]').send_keys(search_value_name)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_name, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        self.assertEqual(search_value_name,self.dr.find_element_by_xpath('//*[@id="xm"]').text,'校验详情页面信息')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('工作对象人员', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '工作对象人员')
        print('人口管理-部局七类库-工作对象人员：姓名条件查询功能正常')

    def test3_gongzuoduixiang_search_carid(self):
        self.gongzuoduixiang_search()
        search_value_carid='500107198901218926'
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(search_value_carid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_carid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        self.assertEqual(search_value_carid,self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').get_attribute('value'),'校验详情页面信息')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('工作对象人员', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '工作对象人员')
        print('人口管理-部局七类库-工作对象人员：身份证号条件查询功能正常')

    def test4_gongzuoduixiang_search_lgyy(self):
        self.gongzuoduixiang_search()
        search_value_lgyy='入室盗窃'
        self.dr.find_element_by_xpath('//*[@id="lgyy"]').send_keys(search_value_lgyy)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        # paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        # column = 3
        # self.pagination_num(paginal_number, search_value_lgyy, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        self.assertEqual(search_value_lgyy,self.dr.find_element_by_xpath('//*[@id="lgyy"]').text,'校验详情页面信息')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('工作对象人员', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '工作对象人员')
        print('人口管理-部局七类库-工作对象人员：列管原因条件查询功能正常')

    def test5_gongzuoduixiang_search_age(self):
        self.gongzuoduixiang_search()
        search_value_age='29'
        self.dr.find_element_by_xpath('//*[@id="age"]').send_keys(search_value_age)
        self.dr.find_element_by_xpath('//*[@id="age1"]').send_keys(search_value_age)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 7
        self.pagination_num(paginal_number, search_value_age, column)
        # self.assertEqual(search_value_age,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[7]').text,'校验年龄条件查询')
        print('人口管理-部局七类库-工作对象人员：年龄条件查询功能正常')

    def test6_gongzuoduixiang_wffzjl(self):
        self.gongzuoduixiang_search()
        search_value_carid = '500107198901218926'
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(search_value_carid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_carid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        self.dr.implicitly_wait(3)
        self.dr.find_element_by_xpath('//*[@id="wffzAdd"]').click()
        self.dr.find_element_by_xpath('//*[@id="work_table1"]/tbody/tr/td[3]/span/div/form/div/div[1]/div/input').send_keys('发展大道建设1路')
        # self.dr.find_element_by_xpath('//*[@id="work_table1"]/tbody/tr/td[2]/a').send_keys('1989-06-25')
        # Select(self.dr.find_element_by_xpath('//*[@id="work_table1"]/tbody/tr/td[4]/span/div/form/div/div[1]/div/select')).select_by_value('040118')
        # Select(self.dr.find_element_by_xpath('//*[@id="work_table1"]/tbody/tr/td[5]/span/div/form/div/div[1]/div/select')).select_by_value('2')
        # self.dr.find_element_by_xpath('//*[@id="work_table1"]/tbody/tr/td[6]/span/div/form/div/div[1]/div/input').send_keys('翰林药坊')
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('发展大道建设1路',self.dr.find_element_by_xpath('//*[@id="work_table1"]/tbody/tr/td[3]/a').get_attribute('data-value'),'校验地点')
        # self.assertEqual('1989-06-25',self.dr.find_element_by_xpath('//*[@id="work_table1"]/tbody/tr/td[2]/a').get_attribute('data-value'),'校验时间')
        # self.assertEqual('非法入侵住宅案',self.dr.find_element_by_xpath('//*[@id="work_table1"]/tbody/tr/td[4]/a').text,'校验问题性质')
        # self.assertEqual('监控',self.dr.find_element_by_xpath('//*[@id="work_table1"]/tbody/tr/td[5]/a').text,'校验处理结果')
        # self.assertEqual('翰林药坊',self.dr.find_element_by_xpath('//*[@id="work_table1"]/tbody/tr/td[6]/a').get_attribute('data-value'),'校验处理单位')
        self.dr.find_element_by_xpath('//*[@id="work_table1"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('//*[@id="wffzDel"]').click()
        time.sleep(5)
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录',self.dr.find_element_by_xpath('//*[@id="work_table1"]/tbody/tr/td').text,'校验违法犯罪经历删除功能')
        print('人口管理-部局七类库-工作对象人员：新增和删除违法犯罪经历功能正常')

    def test7_gongzuoduixiang_zyjfry(self):
        self.gongzuoduixiang_search()
        search_value_carid = '500107198901218926'
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(search_value_carid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_carid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        self.dr.implicitly_wait(3)
        self.dr.find_element_by_xpath('//*[@id="jwryAdd"]').click()
        self.dr.find_element_by_xpath('//*[@id="work_table2"]/tbody/tr/td[3]/span/div/form/div/div[1]/div/input').send_keys('马汉')
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('马汉',self.dr.find_element_by_xpath('//*[@id="work_table2"]/tbody/tr/td[3]/a').get_attribute('data-value'),'校验姓名')
        self.dr.find_element_by_xpath('//*[@id="work_table2"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('//*[@id="jwryDel"]').click()
        time.sleep(5)
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录',self.dr.find_element_by_xpath('//*[@id="work_table2"]/tbody/tr/td').text,'校验主要交往人员删除功能')
        print('人口管理-部局七类库-工作对象人员：新增和删除主要交往人员功能正常')

    def test8_gongzuoduixiang_delete(self):
        self.gongzuoduixiang_search()
        search_value_carid = '500107198901218926'
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(search_value_carid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_carid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[2]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(10)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('人口管理-部局七类库-工作对象人员：删除功能正常')

if __name__ == '__main__':
    unittest.main()