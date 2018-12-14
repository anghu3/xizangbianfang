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
from public_package.pubilc_package import sheet_setting, search, reset, currMenupath, page_title, goback, saveBtn,sheet_menu,sheet_prompt_message,work_space
import xlrd
import HTMLTestRunner
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

# xlsfile=work_space+r'\\'+sheet_menu.col_values(6,50,51)[0]
# excel = xlrd.open_workbook(xlsfile)
# global sheet
# sheet = excel.sheet_by_name('矛盾纠纷调解')

class TESTCASE_MDJF(TESTCASE):
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

    def mdjf_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,48,49)[0]).click()
        time.sleep(5)
        self.assertEqual('社区警务',self.dr.find_element_by_xpath(currMenupath).text, '社区警务')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,48,49)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,48,49)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('矛盾纠纷调处列表', self.dr.find_element_by_xpath(page_title).text,
                         '矛盾纠纷调解')

    def test01_mdjf_add(self):
        self.mdjf_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        Select(self.dr.find_element_by_xpath('//*[@id="mdjflx"]')).select_by_value('01')
        Select(self.dr.find_element_by_xpath('//*[@id="mdjfly"]')).select_by_value('01')
        self.dr.find_element_by_xpath('//*[@id="fssjA"]').click()
        self.dr.find_element_by_xpath('//*[@id="fssjA"]').clear()
        self.dr.find_element_by_xpath('//*[@id="fssjA"]').send_keys('2018-09-12 14:30:00')
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="tjsjA"]').click()
        self.dr.find_element_by_xpath('//*[@id="tjsjA"]').clear()
        self.dr.find_element_by_xpath('//*[@id="tjsjA"]').send_keys('2018-09-13 09:30:00')
        self.dr.find_element_by_xpath('//*[@id="tjrxm"]').click()
        Select(self.dr.find_element_by_xpath('//*[@id="tjjg"]')).select_by_value('01')
        self.dr.find_element_by_xpath('//*[@id="tjdwName"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_46_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_51_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="tjrsfzh"]').send_keys('370123198009220510')
        self.dr.find_element_by_xpath('//*[@id="tjrxm"]').send_keys('荆帅')
        self.dr.find_element_by_xpath('//*[@id="tjrlxfs"]').send_keys('15474587458')
        self.dr.find_element_by_xpath('//*[@id="tjqk"]').send_keys('双方已经达成和解')
        self.dr.find_element_by_xpath('//*[@id="sbqk"]').send_keys('双方已经达成和解')
        self.dr.find_element_by_xpath('//*[@id="sbsjA"]').click()
        self.dr.find_element_by_xpath('//*[@id="ssxjgajgName"]').click()
        self.dr.find_element_by_xpath('//*[@id="treeSelect2_45_span"]').click()
        self.dr.find_element_by_xpath('//*[@id="sspcsName"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect3_1_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect3_43_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect3_47_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect3_50_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="ssjwqName"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect4_1_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect4_2_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect4_3_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect4_4_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect4_5_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect4_6_span"]').click()
        self.dr.find_element_by_xpath('//*[@id="saveMadiate"]').click()
        time.sleep(3)
        self.dr.implicitly_wait(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual('荆帅',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[9]').text,'校验新增、返回和默认排序')
        print('社区警务-矛盾纠纷调解：新增功能正常')

    def test02_mdjf_search_mdjflx(self):
        self.mdjf_search()
        option_chioce=Select(self.dr.find_element_by_xpath('//*[@id="mdjflx"]'))
        for i in range(0,3):
            if i==0:
                print('查询全部类型时不校验查询结果')
            else:
                option_chioce.select_by_index(i)
                search_value_mdjflx=option_chioce.first_selected_option.text
                self.dr.find_element_by_xpath('//*[@id="search"]').click()
                self.dr.switch_to.default_content()
                time.sleep(3)
                self.dr.switch_to.frame('iframeb')
                paginal_number = self.dr.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
                column = 3
                self.pagination_num(paginal_number, search_value_mdjflx, column)
        print('社区警务-矛盾纠纷调解：矛盾纠纷类型条件查询功能正常')

    def test03_mdjf_search_mdjfly(self):
        self.mdjf_search()
        option_chioce=Select(self.dr.find_element_by_xpath('//*[@id="mdjfly"]'))
        for i in range(0,3):
            if i==0:
                print('查询全部类型时不校验查询结果')
            else:
                option_chioce.select_by_index(i)
                search_value_mdjfly=option_chioce.first_selected_option.text
                self.dr.find_element_by_xpath('//*[@id="search"]').click()
                self.dr.switch_to.default_content()
                time.sleep(3)
                self.dr.switch_to.frame('iframeb')
                paginal_number = self.dr.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
                column = 4
                self.pagination_num(paginal_number, search_value_mdjfly, column)
        print('社区警务-矛盾纠纷调解：矛盾纠纷来源条件查询功能正常')

    def test04_mdjf_search_fssjA(self):
        self.mdjf_search()
        search_value_fssjA='2018-09-12'
        self.dr.find_element_by_xpath('//*[@id="fssjA"]').send_keys(search_value_fssjA)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_fssjA, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        self.assertIn(search_value_fssjA,self.dr.find_element_by_xpath('//*[@id="fssjA"]').get_attribute('value'),'校验详情页面发生时间')
        print('社区警务-矛盾纠纷调解：发生时间条件查询功能正常')

    def test05_mdjf_search_tjsjA(self):
        self.mdjf_search()
        search_value_tjsjA='2018-09-13'
        self.dr.find_element_by_xpath('//*[@id="tjsjA"]').send_keys(search_value_tjsjA)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]').click()
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 6
        self.pagination_num(paginal_number, search_value_tjsjA, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        self.assertIn(search_value_tjsjA,self.dr.find_element_by_xpath('//*[@id="tjsjA"]').get_attribute('value'),'校验详情页面调解时间')
        print('社区警务-矛盾纠纷调解：调解时间条件查询功能正常')

    def test06_mdjf_search_tjjg(self):
        self.mdjf_search()
        option_chioce=Select(self.dr.find_element_by_xpath('//*[@id="tjjg"]'))
        for i in range(0,5):
            if i==0:
                print('查询全部类型时不校验查询结果')
            else:
                option_chioce.select_by_index(i)
                search_value_tjjg=option_chioce.first_selected_option.text
                self.dr.find_element_by_xpath('//*[@id="search"]').click()
                self.dr.switch_to.default_content()
                time.sleep(3)
                self.dr.switch_to.frame('iframeb')
                paginal_number = self.dr.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
                column = 7
                self.pagination_num(paginal_number, search_value_tjjg, column)
        print('社区警务-矛盾纠纷调解：调解结果条件查询功能正常')

    def test07_mdjf_search_tjdw(self):
        self.mdjf_search()
        search_value_tjdw='吉巴派出所'
        self.dr.find_element_by_xpath('//*[@id="tjdwName"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_46_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_51_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 8
        self.pagination_num(paginal_number, search_value_tjdw, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[12]/a').click()
        self.assertEqual(search_value_tjdw,self.dr.find_element_by_xpath('//*[@id="tjdwName"]').get_attribute('value'),'校验详情页面调解单位')
        print('社区警务-矛盾纠纷调解：调解单位条件查询功能正常')

    def test08_wdjf_sjry(self):
        self.mdjf_search()
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[12]/a').click()
        self.dr.find_element_by_xpath('//*[@id="sjryAdd"]').click()
        Select(self.dr.find_element_by_xpath('//*[@id="rel_items_table"]/tbody/tr/td[2]/span/div/form/div/div[1]/div/select')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="rel_items_table"]/tbody/tr/td[3]/span/div/form/div/div[1]/div/input').send_keys('500107198901218926')
        self.dr.find_element_by_xpath('//*[@id="rel_items_table"]/tbody/tr/td[4]/span/div/form/div/div[1]/div/input').send_keys('刘钰萱')
        self.dr.find_element_by_xpath('//*[@id="saveMadiate"]').click()
        time.sleep(3)
        self.assertEqual('500107198901218926',self.dr.find_element_by_xpath('//*[@id="rel_items_table"]/tbody/tr/td[3]/a').text,'校验涉及人员新增是否成功')
        self.assertEqual('刘钰萱',self.dr.find_element_by_xpath('//*[@id="rel_items_table"]/tbody/tr/td[4]/a').text,'校验涉及人员新增是否成功')
        self.dr.find_element_by_xpath('//*[@id="rel_items_table"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('//*[@id="sjryDelete"]').click()
        self.dr.find_element_by_xpath('//*[@id="saveMadiate"]').click()
        time.sleep(3)
        self.assertEqual('没有找到匹配的记录',self.dr.find_element_by_xpath('//*[@id="rel_items_table"]/tbody/tr/td').text,'校验涉及人员删除是否成功')
        print('社区警务-矛盾纠纷调解：涉及人员表单新增和删除功能正常')

    def test09_wdjf_sjdw(self):
        self.mdjf_search()
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[12]/a').click()
        self.dr.find_element_by_xpath('//*[@id="sjdwAdd"]').click()
        Select(self.dr.find_element_by_xpath('//*[@id="dw_items_table"]/tbody/tr/td[2]/span/div/form/div/div[1]/div/select')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="dw_items_table"]/tbody/tr/td[3]/span/div/form/div/div[1]/div/input').send_keys('翰林药坊')
        self.dr.find_element_by_xpath('//*[@id="dw_items_table"]/tbody/tr/td[4]/span/div/form/div/div[1]/div/input').send_keys('发展大道')
        self.dr.find_element_by_xpath('//*[@id="saveMadiate"]').click()
        time.sleep(3)
        self.assertEqual('翰林药坊',self.dr.find_element_by_xpath('//*[@id="dw_items_table"]/tbody/tr/td[3]/a').text,'校验涉及单位新增是否成功')
        self.assertEqual('发展大道',self.dr.find_element_by_xpath('//*[@id="dw_items_table"]/tbody/tr/td[4]/a').text,'校验涉及单位新增是否成功')
        self.dr.find_element_by_xpath('//*[@id="dw_items_table"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('//*[@id="sjdwDelete"]').click()
        self.dr.find_element_by_xpath('//*[@id="saveMadiate"]').click()
        time.sleep(3)
        self.assertEqual('没有找到匹配的记录',self.dr.find_element_by_xpath('//*[@id="dw_items_table"]/tbody/tr/td').text,'校验涉及人员删除是否成功')
        print('社区警务-矛盾纠纷调解：涉及单位表单新增和删除功能正常')

    def test10_wdjf_delete(self):
        self.mdjf_search()
        search_value_tjdw = '吉巴派出所'
        self.dr.find_element_by_xpath('//*[@id="tjdwName"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_46_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_51_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 8
        self.pagination_num(paginal_number, search_value_tjdw, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('社区警务-矛盾纠纷调解：删除功能正常')

if __name__=='__main__':
    unittest.main()