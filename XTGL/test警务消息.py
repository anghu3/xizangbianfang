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
from public_package.pubilc_package import url,login_name,login_name_test,login_password,login_password_test,login_password_test2
from public_package.pubilc_package import sheet_setting, search, reset, currMenupath, page_title, goback, saveBtn,sheet_menu,sheet_prompt_message
from public_package.pubilc_package import TESTCASE
import HTMLTestRunner
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

class TESTCAST_JWXX(TESTCASE):
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

    def jwxx_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('//*[@id="next"]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,77,78)[0]).click()
        time.sleep(5)
        self.assertEqual('系统管理',self.dr.find_element_by_xpath(currMenupath).text, '系统管理')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,77,78)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,77,78)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('移动警务信息管理列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '警务消息')

    def test1_jwxx_add(self):
        self.jwxx_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        self.dr.find_element_by_xpath('//*[@id="tsbt"]').send_keys('边防缉毒')
        self.dr.find_element_by_xpath('//*[@id="JwxxtsForm"]/div[1]/div[2]/div/div[2]/label[1]/input').click()
        self.dr.find_element_by_xpath('//*[@id="JwxxtsForm"]/div[1]/div[2]/div/div[2]/label[2]/input').click()
        self.dr.find_element_by_xpath('//*[@id="xxnr"]').send_keys('据线人举报有毒贩在该次航班运毒，请仔细排查！')
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertIn('举报有毒贩',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[5]').text,'校验新增、返回和默认排序')
        print('系统管理-警务消息：新增功能正常')

    def test2_jwxx_search_tslx(self):
        self.jwxx_search()
        option_chioce=Select(self.dr.find_element_by_xpath('//*[@id="tslx"]'))
        for i in range(0,3):
            if i==0:
                print('推送类型查询条件为空时不校验数据')
            else:
                option_chioce.select_by_index(i)
                search_value_tslx=option_chioce.first_selected_option.text
                self.dr.find_element_by_xpath('//*[@id="search"]').click()
                self.dr.switch_to.default_content()
                time.sleep(5)
                self.dr.switch_to.frame('iframeb')
                paginal_number = self.dr.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
                column = 6
                self.pagination_num(paginal_number, search_value_tslx, column)
        print('系统管理-警务消息：推送类型条件查询功能正常')

    def test3_jwxx_search_xxnr(self):
        self.jwxx_search()
        search_value_xxnr='毒贩'
        self.dr.find_element_by_xpath('//*[@id="xxnr"]').send_keys(search_value_xxnr)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_xxnr, column)
        print('系统管理-警务消息：信息内容条件查询功能正常')

    def test4_jwxx_search_edittime(self):
        self.jwxx_search()
        search_value_edittime=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        # print(search_value_edittime)
        self.dr.find_element_by_xpath('//*[@id="provideTimeA"]').send_keys(search_value_edittime)
        self.dr.find_element_by_xpath('//*[@id="provideTimeB"]').send_keys(search_value_edittime)
        self.dr.find_element_by_xpath('//*[@id="xxnr"]').click()
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 7
        self.pagination_num(paginal_number, search_value_edittime, column)
        print('系统管理-警务消息：修改时间条件查询功能正常')

    def test5_jwxx_tsdx(self):
        self.jwxx_search()
        search_value_xxnr = '毒贩'
        self.dr.find_element_by_xpath('//*[@id="xxnr"]').send_keys(search_value_xxnr)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_xxnr, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[8]/a').click()
        self.dr.find_element_by_xpath('//*[@id="tsAdd"]').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_1784_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_1785_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_1786_check"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('/html/body/div[4]/div[3]/div/button[2]/span').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        time.sleep(8)
        self.assertEqual('徐利',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]').text,'校验推送对象新增功能')
        self.assertEqual('错那边防大队', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text, '校验推送对象新增功能')
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('//*[@id="tsDelete"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        time.sleep(3)
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验推送对象删除功能')
        print('系统管理-警务消息：新增和删除推送对象功能正常')

    def test6_jwxx_delete(self):
        self.jwxx_search()
        search_value_xxnr = '毒贩'
        self.dr.find_element_by_xpath('//*[@id="xxnr"]').send_keys(search_value_xxnr)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_xxnr, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('系统管理-警务消息：删除功能正常')

if __name__=='__main__':
    unittest.main()