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

class TESTCAST_PWJC(TESTCASE):
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

    def pwjc_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div/a[3]/div[2]/img[2]').click()
        time.sleep(5)
        self.assertEqual('社区警务',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '社区警务')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[1]/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="949"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('盘问检查基本信息列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '盘问检查')

    def test1_pwjc_add(self):
        self.pwjc_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        self.dr.find_element_by_xpath('//*[@id="pwkssjA"]').click()
        date1=time.strftime('%Y-%m-%d 08:30:00')
        self.dr.find_element_by_xpath('//*[@id="pwkssjA"]').clear()
        self.dr.find_element_by_xpath('//*[@id="pwkssjA"]').send_keys(date1)
        self.dr.find_element_by_xpath('//*[@id="questForm"]/div[1]/div[1]/div/div[2]/ul/li[2]/table/tbody/tr/td[2]/a/span').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="pwjssjA"]').click()
        date2=time.strftime('%Y-%m-%d 12:00:00')
        self.dr.find_element_by_xpath('//*[@id="pwjssjA"]').clear()
        self.dr.find_element_by_xpath('//*[@id="pwjssjA"]').send_keys(date2)
        self.dr.find_element_by_xpath('//*[@id="questForm"]/div[1]/div[2]/div/div[2]/ul/li[2]/table/tbody/tr/td[2]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="sfzhm"]').send_keys('370123198009220510')
        self.dr.find_element_by_xpath('//*[@id="xm"]').send_keys('荆帅')
        self.dr.find_element_by_xpath('//*[@id="lxfs"]').send_keys('15745874587')
        self.dr.find_element_by_xpath('//*[@id="pwjcqk"]').send_keys('运输货物较多,检查时发现盘问人情绪可疑，但未发现可疑物品。')
        Select(self.dr.find_element_by_xpath('//*[@id="pwjg"]')).select_by_value('02')
        self.dr.find_element_by_xpath('//*[@id="pwjcmjssdwName"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_58_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_62_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="pwjcmjxm"]').send_keys('包涵')
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        self.dr.implicitly_wait(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual('370123198009220510', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[6]').text,
                         '检验新增、返回和默认排序')
        print('社区警务-盘问检查：新增功能正常')

    def test2_pwjc_search_date(self):
        self.pwjc_search()
        search_value_date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        self.dr.find_element_by_xpath('//*[@id="pwkssjA"]').send_keys(search_value_date)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_date, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        self.assertIn(search_value_date,self.dr.find_element_by_xpath('//*[@id="pwkssjA"]').get_attribute('value'),'校验详情页面的盘问时间')
        # self.assertIn(search_value_date,self.dr.find_element_by_xpath('//*[@id="pwjssjA"]').get_attribute('value'),'校验详情页面的盘问时间')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('370123198009220510', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[6]').text,
                         '检验返回和默认排序')
        print('社区警务-盘问检查：盘问时间条件查询功能正常')

    def test3_pwjc_search_name(self):
        self.pwjc_search()
        search_value_name='荆帅'
        self.dr.find_element_by_xpath('//*[@id="xm"]').send_keys(search_value_name)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_name, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        self.assertIn(search_value_name,self.dr.find_element_by_xpath('//*[@id="xm"]').get_attribute('value'),'校验详情页面的被盘问人姓名')
        # self.assertIn(search_value_date,self.dr.find_element_by_xpath('//*[@id="pwjssjA"]').get_attribute('value'),'校验详情页面的盘问时间')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_name, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[5]').text,
                         '检验返回和默认排序')
        print('社区警务-盘问检查：被盘问人姓名条件查询功能正常')

    def test4_pwjc_search_carID(self):
        self.pwjc_search()
        search_value_carid='370123198009220510'
        self.dr.find_element_by_xpath('//*[@id="sfzhm"]').send_keys(search_value_carid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 6
        self.pagination_num(paginal_number, search_value_carid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        self.assertIn(search_value_carid,self.dr.find_element_by_xpath('//*[@id="sfzhm"]').get_attribute('value'),'校验详情页面的被盘问人身份证号码')
        # self.assertIn(search_value_date,self.dr.find_element_by_xpath('//*[@id="pwjssjA"]').get_attribute('value'),'校验详情页面的盘问时间')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_carid, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[6]').text,
                         '检验返回和默认排序')
        print('社区警务-盘问检查：被盘问人身份证号码条件查询功能正常')

    def test5_pwjc_search_pwjg(self):
        self.pwjc_search()
        option_chioce=Select(self.dr.find_element_by_xpath('//*[@id="pwjg"]'))
        for i in range(0, 4):
            if i == 0:
                print('查询全部数据时不校验查询结果')
            else:
                option_chioce.select_by_index(i)
                search_value_pwjg=option_chioce.first_selected_option.text
                self.dr.find_element_by_xpath('//*[@id="search"]').click()
                self.dr.switch_to.default_content()
                time.sleep(5)
                self.dr.switch_to.frame('iframeb')
                paginal_number = self.dr.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
                column = 7
                self.pagination_num(paginal_number, search_value_pwjg, column)
        print('社区警务-盘问检查：盘问结果条件查询功能正常')

    def test6_pwjc_search_pwjcmjxm(self):
        self.pwjc_search()
        search_value_pwjcmjxm='包涵'
        self.dr.find_element_by_xpath('//*[@id="pwjcmjxm"]').send_keys(search_value_pwjcmjxm)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 8
        self.pagination_num(paginal_number, search_value_pwjcmjxm, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[11]/a').click()
        self.assertEqual(search_value_pwjcmjxm,self.dr.find_element_by_xpath('//*[@id="pwjcmjxm"]').get_attribute('value'),'校验详情页面民警姓名')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_pwjcmjxm, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[8]').text,
                         '检验返回和默认排序')
        print('社区警务-盘问检查：盘问检查民警姓名条件查询功能正常')

    def test7_pwjc_search_pwjcmjssdwName(self):
        self.pwjc_search()
        search_value_pwjcmjssdwName='扎日派出所'
        self.dr.find_element_by_xpath('//*[@id="pwjcmjssdwName"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_58_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_62_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 9
        self.pagination_num(paginal_number, search_value_pwjcmjssdwName, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[11]/a').click()
        self.assertEqual(search_value_pwjcmjssdwName,self.dr.find_element_by_xpath('//*[@id="pwjcmjssdwName"]').get_attribute('value'),'校验详情页面民警所属单位')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_pwjcmjssdwName, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[9]').text,
                         '检验返回和默认排序')
        print('社区警务-盘问检查：盘问检查民警所属单位条件查询功能正常')

    def test8_pwjc_edit(self):
        self.pwjc_search()
        search_value_carid='370123198009220510'
        self.dr.find_element_by_xpath('//*[@id="sfzhm"]').send_keys(search_value_carid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 6
        self.pagination_num(paginal_number, search_value_carid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        Select(self.dr.find_element_by_xpath('//*[@id="pwjg"]')).select_by_value('01')
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        self.dr.implicitly_wait(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_carid, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[6]').text,
                         '检验返回和默认排序')
        self.assertEqual('排除嫌疑', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[7]').text,
                         '检验返回和默认排序')
        print('社区警务-盘问检查：编辑功能正常')

    def test9_pwjc_delete(self):
        self.pwjc_search()
        search_value_carid='370123198009220510'
        self.dr.find_element_by_xpath('//*[@id="sfzhm"]').send_keys(search_value_carid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 6
        self.pagination_num(paginal_number, search_value_carid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('社区警务-盘问检查：删除功能正常')

if __name__=='__main__':
    unittest.main()