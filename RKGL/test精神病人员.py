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

class TESTCAST_JINGSHENBING(unittest.TestCase):
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

    def pagination_num(self, paginal_number, search_value, column):
        number = findnum(paginal_number)[-1]
        tens = int(number / 10)
        single = int(number % 10)
        if tens == 0:
            for j in range(1, single + 1):
                xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
        if tens == 1:
            for j in range(1, 11):
                xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
            page = '/html/body/div[3]/div[2]/div[1]/div/div[4]/div[2]/ul/li[' + str(tens + 3) + ']/a'
            self.dr.find_element_by_xpath(page).click()
            if single == 0:
                print(single)
            else:
                for j in range(1, single + 1):
                    xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                    self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
                    time.sleep(5)
        if tens < 7:
            for i in range(1, tens + 2):
                if i < tens + 1:
                    for j in range(1, 11):
                        xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                        self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
                    page = '/html/body/div[3]/div[2]/div[1]/div/div[4]/div[2]/ul/li[' + str(tens + 3) + ']/a'
                    self.dr.find_element_by_xpath(page).click()
                if i == tens + 1:
                    for j in range(1, single + 1):
                        if single == 0:
                            print(single)
                        else:
                            for j in range(1, single + 1):
                                xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                                self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
                                time.sleep(5)
        if tens > 7:
            for i in range(1, tens + 2):
                if i < tens + 1:
                    for j in range(1, 11):
                        xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                        self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
                    self.dr.find_element_by_xpath(
                        '/html/body/div[3]/div[2]/div[1]/div/div[4]/div[2]/ul/li[9]/a').click()
                if i == tens + 1:
                    for j in range(1, single + 1):
                        if single == 0:
                            print(single)
                        else:
                            for j in range(1, single + 1):
                                xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                                self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
                                time.sleep(5)

    def jingshenbing_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/a[2]').click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '人口管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[6]/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="330"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('精神病人员', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '精神病人员')

    def test1_jingshenbing_add(self):
        self.jingshenbing_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        add_value = '540123198506025515'
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(add_value)
        self.dr.find_element_by_xpath('//*[@id="mentForm"]/div[1]/div[2]/div/div[1]/div[2]/a').click()
        time.sleep(2)
        Select(self.dr.find_element_by_xpath('//*[@id="sfyjd"]')).select_by_value('1')
        Select(self.dr.find_element_by_xpath('//*[@id="zl"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="zdfbsjd"]').send_keys('16:00-18:00')
        Select(self.dr.find_element_by_xpath('//*[@id="fbswhcd"]')).select_by_value('2')
        #管辖单位
        #责任单位
        self.dr.find_element_by_xpath('//*[@id="zrmj"]').send_keys('马汉')
        self.dr.find_element_by_xpath('//*[@id="mjdha"]').send_keys('15748574587')
        self.dr.find_element_by_xpath('//*[@id="mjdhb"]').send_keys('13574587458')
        self.dr.find_element_by_xpath('//*[@id="sfccjcz"]').send_keys('是')
        self.dr.find_element_by_xpath('//*[@id="supervIdcardNo"]').send_keys('540123198506025515')
        self.dr.find_element_by_xpath('//*[@id="supervName"]').send_keys('王朝')
        self.dr.find_element_by_xpath('//*[@id="reportCycle"]').send_keys('5')
        self.dr.find_element_by_xpath('//*[@id="supervWx"]').send_keys('15748574587')
        self.dr.find_element_by_xpath('//*[@id="supervBeWx"]').send_keys('13574587458')
        self.dr.find_element_by_xpath('//*[@id="jhrXm"]').send_keys('展昭')
        self.dr.find_element_by_xpath('//*[@id="sqgbXm"]').send_keys('包拯')
        self.dr.find_element_by_xpath('//*[@id="jhrDh"]').send_keys('15748574587')
        self.dr.find_element_by_xpath('//*[@id="sqgbDh"]').send_keys('13574587458')
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        time.sleep(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.assertEqual('精神病人员', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '精神病人员')
        print('人口管理-部局七类库-精神病人员：新增功能正常')

    def test2_jingshenbing_search_name(self):
        self.jingshenbing_search()
        search_value = '索朗旺堆'
        self.dr.find_element_by_xpath('//*[@id="xm"]').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,'姓名条件查询')
        # self.dr.find_element_by_xpath('//*[@id="reset"]').click()
        # self.dr.implicitly_wait(10)
        # self.dr.find_element_by_xpath('//*[@id="search"]').click()
        # time.sleep(5)
        # self.assertNotEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text, '重置功能')
        print('人口管理-部局七类库-精神病人员：姓名条件查询功能正常')

    def test3_jingshenbing_search_cardid(self):
        self.jingshenbing_search()
        search_value = '540123198506025515'
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,'身份证号条件查询')
        # self.dr.find_element_by_xpath('//*[@id="reset"]').click()
        # self.dr.implicitly_wait(10)
        # self.dr.find_element_by_xpath('//*[@id="search"]').click()
        # time.sleep(5)
        # self.assertNotEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text, '重置功能')
        print('人口管理-部局七类库-涉枪人员：身份证号条件查询功能正常')

    def test4_jingshenbing_search_zyzbh(self):
        self.jingshenbing_search()
        search_value_1 = '33'
        self.dr.find_element_by_xpath('//*[@id="start"]').send_keys(search_value_1)
        self.dr.find_element_by_xpath('//*[@id="end"]').send_keys(search_value_1)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value_1,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[7]').text,'持枪证编号条件查询')
        # self.dr.find_element_by_xpath('//*[@id="reset"]').click()
        # self.dr.implicitly_wait(10)
        # self.dr.find_element_by_xpath('//*[@id="search"]').click()
        # time.sleep(5)
        # self.assertNotEqual(search_value_1, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text, '重置功能')
        print('人口管理-部局七类库-涉枪人员：持枪证编号条件查询功能正常')

    def test5_jingshengbing_xiangqing(self):
        self.jingshenbing_search()
        search_value = '540123198506025515'
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        name=self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text
        age=self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[7]').text
        self.assertEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,
                         '身份证号条件查询')
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        self.assertEqual(search_value, self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').get_attribute('value'), '详情校验')
        self.assertEqual(name,self.dr.find_element_by_xpath('//*[@id="xm"]').text,'详情校验')
        print('人口管理-部局七类库-精神病人员：详情功能正常')

    def test6_jingshengbing_delete(self):
        self.jingshenbing_search()
        search_value = '540123198506025515'
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,
                         '身份证号条件查询')
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        time.sleep(2)
        self.dr.switch_to.default_content()
        time.sleep(1)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        print('人口管理-部局七类库-涉枪人员：删除功能正常')

if __name__ == '__main__':
    unittest.main()

