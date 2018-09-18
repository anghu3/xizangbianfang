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

class TESTCAST_SHEBIANSHEKONG(unittest.TestCase):
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

    def shebian_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/a[2]').click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '人口管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[6]/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="327"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('涉边/涉稳/涉恐/涉外人员', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '涉边/涉稳/涉恐/涉外人员')

    def test1_shebian_add(self):
        self.shebian_search()
        add_value = '542225197601020021'
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(add_value)
        self.dr.find_element_by_xpath('//*[@id="otherForm"]/div[1]/div[2]/div/div[1]/div[2]/a').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="xjdz"]').send_keys('西藏自治区琼结县')
        self.dr.find_element_by_xpath('//*[@id="tmtz"]').send_keys('偏瘦，个子高')
        option_jz = Select(self.dr.find_element_by_xpath('//*[@id="sfyjz"]'))
        option_jz.select_by_index(1)
        self.dr.find_element_by_xpath('//*[@id="jzlx"]').send_keys('C1')
        self.dr.find_element_by_xpath('//*[@id="jzhm"]').send_keys('542225197601020021')
        self.dr.find_element_by_xpath('//*[@id="qk"]').send_keys('否')
        self.dr.find_element_by_xpath('//*[@id="gddh"]').send_keys('13258748569')
        self.dr.find_element_by_xpath('//*[@id="qqorip"]').send_keys('13574857')
        self.dr.find_element_by_xpath('//*[@id="hlwtxhm"]').send_keys('646464875')
        option_gj = Select(self.dr.find_element_by_xpath('//*[@id="gj"]'))
        option_gj.select_by_visible_text('中国')
        self.dr.find_element_by_xpath('//*[@id="hzhm"]').send_keys('741852')
        self.dr.find_element_by_xpath('//*[@id="hdqk"]').send_keys('无')
        self.dr.find_element_by_xpath('//*[@id="sy"]').send_keys('经商')
        self.dr.find_element_by_xpath('//*[@id="fs"]').send_keys('客车')
        self.dr.find_element_by_xpath('//*[@id="jzdlx"]').send_keys('租住')
        self.dr.find_element_by_xpath('//*[@id="zzzh"]').send_keys('暂无')
        # self.dr.find_element_by_xpath('//*[@id="dbdsj"]').click()
        self.dr.find_element_by_xpath('//*[@id="zjhm"]').send_keys('452748574')
        self.dr.find_element_by_xpath('//*[@id="supervIdcardNo"]').send_keys('542225197601020021')
        self.dr.find_element_by_xpath('//*[@id="supervName"]').send_keys('林虎')
        self.dr.find_element_by_xpath('//*[@id="reportCycle"]').send_keys('3')
        self.dr.find_element_by_xpath('//*[@id="supervWx"]').send_keys('无')
        self.dr.find_element_by_xpath('//*[@id="supervBeWx"]').send_keys('无')
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        time.sleep(5)
        print('人口管理-局部七类库-涉爆人员：新增涉边|涉恐|涉稳|涉外人员功能正常')

    def test2_shebian_search_name(self):
        self.shebian_search()
        search_value = '嘎多'
        self.dr.find_element_by_xpath('//*[@id="name"]').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(2)
        self.assertIn(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[4]').text, '校验结果')
        print('涉边|涉恐|涉稳|涉外人员-姓名条件查询功能正常')

    def test3_rkgl_bjqlk_1_search_cardid(self):
        self.shebian_search()
        search_value = '542225197601020021'
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.assertIn(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]').text, '校验结果')
        print('涉边|涉恐|涉稳|涉外人员-身份证号条件查询功能正常')

    def test4_rkgl_bjqlk_1_search_age(self):
        self.shebian_search()
        search_value_1 = 42
        search_value_2 = 42
        self.dr.find_element_by_xpath('//*[@id="start"]').send_keys(search_value_1)
        self.dr.find_element_by_xpath('//*[@id="end"]').send_keys(search_value_2)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.assertEqual(str(search_value_1), self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[7]').text,
                         '校验结果')
        print('涉边|涉恐|涉稳|涉外人员-年龄条件查询')

    def test5_shebian_delete(self):
        self.shebian_search()
        add_value = '542225197601020021'
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(add_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]/input').click()
        # self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]/span').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        time.sleep(2)
        self.dr.switch_to.default_content()
        time.sleep(1)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        print('人口管理-局部七类库-涉爆人员：删除涉边|涉恐|涉稳|涉外人员功能正常')

if __name__ == '__main__':
    unittest.main()