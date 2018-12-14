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
from public_package.pubilc_package import sheet_setting, search, reset, currMenupath, page_title, goback, saveBtn , sheet_menu,sheet_prompt_message,work_space
import xlrd
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

class TESTCAST_WEIBAO(TESTCASE):


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

    def weibao_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,44,45)[0]).click()
        time.sleep(5)
        self.assertEqual('管理防范',self.dr.find_element_by_xpath(currMenupath).text, '管理防范')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,44,45)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,44,45)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('危爆场所列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text,
                         '危爆场所管理')

    def test01_weibao_add(self):
        self.weibao_search()
        add_value_name='米林烟火爆竹工厂'
        self.dr.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/a[2]').click()
        self.dr.find_element_by_xpath('//*[@id="securityCompanyCode"]').send_keys('85745877')
        self.dr.find_element_by_xpath('//*[@id="compCode"]').send_keys('25475657')
        self.dr.find_element_by_xpath('//*[@id="compName"]').send_keys(add_value_name)
        '''生产单位'''
        Select(self.dr.find_element_by_xpath('//*[@id="compType"]')).select_by_value('01')
        '''私有'''
        Select(self.dr.find_element_by_xpath('//*[@id="compCategory"]')).select_by_value('0304')
        self.dr.find_element_by_xpath('//*[@id="orgCode"]').send_keys('26475874')
        '''烟花爆竹加工厂'''
        Select(self.dr.find_element_by_xpath('//*[@id="type"]')).select_by_value('703')
        '''私有'''
        Select(self.dr.find_element_by_xpath('//*[@id="economicProperty"]')).select_by_value('17')
        self.dr.find_element_by_xpath('//*[@id="legalRepresentative"]').send_keys('王小波')
        self.dr.find_element_by_xpath('//*[@id="contactTel"]').send_keys('13247458965')
        self.dr.find_element_by_xpath('//*[@id="detailAddress"]').send_keys('林廓西路21号')
        self.dr.find_element_by_xpath('//*[@id="saveDanger"]').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual(add_value_name,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,'校验新增、返回和默认排序')
        print('管理防范-危爆场所管理：新增功能正常')

    def test02_weibao_search_frdb(self):
        self.weibao_search()
        search_value_frdb='王小波'
        self.dr.find_element_by_xpath('//*[@id="legalRepresentative"]').send_keys(search_value_frdb)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_frdb, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        self.assertEqual(search_value_frdb,self.dr.find_element_by_xpath('//*[@id="legalRepresentative"]').get_attribute('value'),'校验详情页面法人代表')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_frdb,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,'校验返回和默认排序')
        print('管理防范-危爆场所管理：法人代表条件查询功能正常')

    def test03_weibao_search_name(self):
        self.weibao_search()
        search_value_name='米林烟火爆竹工厂'
        self.dr.find_element_by_xpath('//*[@id="compName"]').send_keys(search_value_name)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_name, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        self.assertEqual(search_value_name,self.dr.find_element_by_xpath('//*[@id="compName"]').get_attribute('value'),'校验详情页面单位名称')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_name,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,'校验返回和默认排序')
        print('管理防范-危爆场所管理：单位名称条件查询功能正常')

    def test04_weibao_search_comptype(self):
        self.weibao_search()
        option_chioce=Select(self.dr.find_element_by_xpath('//*[@id="compType"]'))
        option_chioce.select_by_value('01')
        search_value_comptype = option_chioce.first_selected_option.text
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_comptype, column)
        print('管理防范-危爆场所管理：单位类型条件查询功能正常')

    def test05_weibao_search_adress(self):
        self.weibao_search()
        search_value_address='林廓西路21号'
        self.dr.find_element_by_xpath('//*[@id="detailAddress"]').send_keys(search_value_address)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 10
        self.pagination_num(paginal_number, search_value_address, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        self.assertEqual(search_value_address,self.dr.find_element_by_xpath('//*[@id="detailAddress"]').get_attribute('value'),'校验详情页面单位详址')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_address,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[10]').text,'校验返回和默认排序')
        print('管理防范-危爆场所管理：单位详址条件查询功能正常')

    def test06_weibao_edit(self):
        self.weibao_search()
        search_value_name='米林烟火爆竹工厂'
        self.dr.find_element_by_xpath('//*[@id="compName"]').send_keys(search_value_name)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_name, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        edit_value_name='米林烟火爆竹有限公司'
        self.dr.find_element_by_xpath('//*[@id="compName"]').clear()
        self.dr.find_element_by_xpath('//*[@id="compName"]').send_keys(edit_value_name)
        self.dr.find_element_by_xpath('//*[@id="saveDanger"]').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual(edit_value_name, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,'校验返回和默认排序')
        print('管理防范-危爆场所管理：编辑功能正常')

    def test07_weibao_delete(self):
        self.weibao_search()
        search_value_name='米林烟火爆竹有限公司'
        self.dr.find_element_by_xpath('//*[@id="compName"]').send_keys(search_value_name)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_name, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[2]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('管理防范-危爆场所管理：删除功能正常')

if __name__=='__main__':
    unittest.main()