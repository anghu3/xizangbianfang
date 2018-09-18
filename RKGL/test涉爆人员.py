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

class TESTCAST_SHEBAO(unittest.TestCase):
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

    def shebao_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/a[2]').click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '人口管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[6]/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="328"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('涉爆人员', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '涉爆人员')

    def test1_shebao_add(self):
        self.shebao_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        add_value = '540123198506025515'
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(add_value)
        self.dr.find_element_by_xpath('//*[@id="wadeForm"]/div[1]/div[2]/div/div[1]/div[2]/a').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="xjzdz"]').send_keys('西藏自治区尼木县尼木乡尼木村')
        self.dr.find_element_by_xpath('//*[@id="zyzbh"]').send_keys('85587485')
        self.dr.find_element_by_xpath('//*[@id="gzdw"]').send_keys('尼木乡尼木村林场')
        option_chioce = Select(self.dr.find_element_by_xpath('//*[@id="sbzt"]'))
        option_chioce.select_by_index(1)
        self.dr.find_element_by_xpath('//*[@id="fzjg"]').send_keys('尼木乡尼木村林场')
        self.dr.find_element_by_xpath('//*[@id="supervName"]').send_keys('马琳')
        self.dr.find_element_by_xpath('//*[@id="supervIdcardNo"]').send_keys('540123198506025515')
        self.dr.find_element_by_xpath('//*[@id="supervWx"]').send_keys('85274156')
        self.dr.find_element_by_xpath('//*[@id="reportCycle"]').send_keys('5')
        self.dr.find_element_by_xpath('//*[@id="supervBeWx"]').send_keys('85274156')
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        time.sleep(2)
        print('人口管理-局部七类库-涉爆人员：新增涉爆人员')

    def test2_shebao_search_name(self):
        self.shebao_search()
        search_value = '索朗旺堆'
        self.dr.find_element_by_xpath('//*[@id="name"]').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[4]').text,'校验姓名查询功能')
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[8]/a').click()
        self.assertEqual(search_value, self.dr.find_element_by_xpath('//*[@id="xm"]').text, '详情校验')
        print('人口管理-部局七类库-涉爆人员：姓名条件查询功能正常')

    def test3_shebao_search_cardid(self):
        self.shebao_search()
        search_value = '540123198506025515'
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]').text,'校验身份证号查询功能')
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[8]/a').click()
        self.assertEqual(search_value, self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').get_attribute('value'),
                         '详情校验')
        print('人口管理-部局七类库-涉爆人员：身份证号条件查询功能正常')

    def test4_shebao_search_zyzbh(self):
        self.shebao_search()
        search_value = '85587485'
        self.dr.find_element_by_xpath('//*[@id="zyzbh"]').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[7]').text,'校验作业证编号查询功能')
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[8]/a').click()
        self.assertEqual(search_value, self.dr.find_element_by_xpath('//*[@id="zyzbh"]').get_attribute('value'), '详情校验')
        print('人口管理-部局七类库-涉爆人员：作业证编号条件查询功能正常')

    def test5_shebao_delete(self):
        self.shebao_search()
        search_value = '540123198506025515'
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]').text,
                         '校验身份证号查询功能')
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]/input').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        time.sleep(2)
        self.dr.switch_to.default_content()
        time.sleep(1)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        print('人口管理-局部七类库-涉爆人员：删除涉爆人员')


if __name__ == '__main__':
    unittest.main()