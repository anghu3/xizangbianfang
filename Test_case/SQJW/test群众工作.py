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

class TESTCAST_QZGZ(TESTCASE):
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

    def qzgz_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div/a[3]/div[2]/img[2]').click()
        time.sleep(5)
        self.assertEqual('社区警务',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '社区警务')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[1]/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="947"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('群众工作列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '群众工作')

    def test1_qzgz_add(self):
        self.qzgz_search()
        times = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        self.dr.find_element_by_xpath('//*[@id="kzrqkssjA"]').click()
        self.dr.find_element_by_xpath('//*[@id="kzrqkssjA"]').clear()
        self.dr.find_element_by_xpath('//*[@id="kzrqkssjA"]').send_keys(times)
        self.dr.find_element_by_xpath('//*[@id="kzrqjssjA"]').click()
        self.dr.find_element_by_xpath('//*[@id="kzrqjssjA"]').clear()
        self.dr.find_element_by_xpath('//*[@id="kzrqjssjA"]').send_keys(times)
        Select(self.dr.find_element_by_xpath('//*[@id="gzlb"]')).select_by_value('01')
        self.dr.find_element_by_xpath('//*[@id="gzkzqk"]').send_keys(
            '健全完善党员干部直接联系群众制度。先后组织开展了“放下架子进万家门、沉下身子知万家情、'
            '想出法子解万家难”为主要内容的“3个万家”活动和“去官气、做公仆”大讨论等主题实践活动，'
            '认真落实领导干部基层联系点、调查研究、定期接访、谈心谈话等8项制度，以了解群众困难、征'
            '求群众意见、解答群众疑问、化解民生难题。')
        self.dr.find_element_by_xpath('//*[@id="jwqmjssdwName"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_46_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_48_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="jwqmjxm"]').send_keys('包涵')
        self.dr.find_element_by_xpath('//*[@id="saveMass"]').click()
        self.dr.implicitly_wait(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('群众工作列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '校验返回功能')
        print('社区警务-群众工作：新增功能正常')

    def test2_qzgz_search_date(self):
        self.qzgz_search()
        search_value_date=time.strftime("%Y-%m-%d", time.localtime(time.time()))
        self.dr.find_element_by_xpath('//*[@id="kzrqkssjA"]').send_keys(search_value_date)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_date, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[8]/a').click()
        self.assertIn(search_value_date,self.dr.find_element_by_xpath('//*[@id="kzrqkssjA"]').get_attribute('value'),'校验详情页面开展日期')
        print('社区警务-群众工作：开展日期条件查询功能正常')

    def test3_qzgz_search_gzlb(self):
        self.qzgz_search()
        option_chioce=Select(self.dr.find_element_by_xpath('//*[@id="gzlb"]'))
        for i in range(0,3):
            if i==0:
                print('查询条件为空时不对数据进行校验')
            else:
                option_chioce.select_by_index(i)
                search_value_date = option_chioce.first_selected_option.text
                self.dr.find_element_by_xpath('//*[@id="search"]').click()
                self.dr.switch_to.default_content()
                time.sleep(5)
                self.dr.switch_to.frame('iframeb')
                paginal_number = self.dr.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
                column = 4
                self.pagination_num(paginal_number, search_value_date, column)
        print('社区警务-群众工作：开展日期条件查询功能正常')

    def test4_qzgz_search_jwqmjxm(self):
        self.qzgz_search()
        search_value_jwqmjxm = '包涵'
        self.dr.find_element_by_xpath('//*[@id="jwqmjxm"]').send_keys(search_value_jwqmjxm)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_jwqmjxm, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[8]/a').click()
        self.assertIn(search_value_jwqmjxm,
                      self.dr.find_element_by_xpath('//*[@id="jwqmjxm"]').get_attribute('value'), '校验详情页面警务区民警姓名')
        print('社区警务-群众工作：警务区民警条件查询功能正常')

    def test5_qzgz_search_ssdw(self):
        self.qzgz_search()
        search_value_ssdw='库局派出所'
        self.dr.find_element_by_xpath('//*[@id="jwqmjssdwName"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_46_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_48_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 6
        self.pagination_num(paginal_number, search_value_ssdw, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[8]/a').click()
        self.assertIn(search_value_ssdw,
                      self.dr.find_element_by_xpath('//*[@id="jwqmjssdwName"]').get_attribute('value'), '校验详情页面所属单位')
        print('社区警务-群众工作：所属单位条件查询功能正常')

    def test6_qzgz_edit(self):
        self.qzgz_search()
        search_value_jwqmjxm = '包涵'
        self.dr.find_element_by_xpath('//*[@id="jwqmjxm"]').send_keys(search_value_jwqmjxm)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_jwqmjxm, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[8]/a').click()
        edit_value_name='包拯'
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="jwqmjxm"]').clear()
        self.dr.find_element_by_xpath('//*[@id="jwqmjxm"]').send_keys(edit_value_name)
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="saveMass"]').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(edit_value_name,
                      self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[5]').text, '校验编辑功能')
        print('社区警务-群众工作：编辑功能正常')

    def test7_qzgz_delete(self):
        self.qzgz_search()
        search_value_jwqmjxm = '包拯'
        self.dr.find_element_by_xpath('//*[@id="jwqmjxm"]').send_keys(search_value_jwqmjxm)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_jwqmjxm, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('社区警务-群众工作：删除功能正常')

if __name__=='__main__':
    unittest.main()