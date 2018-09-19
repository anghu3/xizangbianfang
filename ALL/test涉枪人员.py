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
import HTMLTestRunner
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

class TESTCAST_SHEQIANG(unittest.TestCase):
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

    def sheqiang_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/a[2]').click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '人口管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[6]/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="329"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('涉枪人员', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '涉枪人员')

    def test1_sheqiang_add(self):
        self.sheqiang_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]/span').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        add_value = '540123198506025515'
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(add_value)
        self.dr.find_element_by_xpath('//*[@id="gunForm"]/div[1]/div[2]/div/div[1]/div[2]/a').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="cqzbh"]').send_keys('85815565')
        self.dr.find_element_by_xpath('//*[@id="fzsj"]').send_keys('2018-08-28')
        self.dr.find_element_by_xpath('//*[@id="szdw"]').send_keys('马林农场')
        self.dr.find_element_by_xpath('//*[@id="supervName"]').send_keys('马林')
        self.dr.find_element_by_xpath('//*[@id="supervIdcardNo"]').send_keys(add_value)
        self.dr.find_element_by_xpath('//*[@id="supervWx"]').send_keys('15474587458')
        self.dr.find_element_by_xpath('//*[@id="reportCycle"]').send_keys('5')
        self.dr.find_element_by_xpath('//*[@id="supervBeWx"]').send_keys('13654857458')
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        print('人口管理-部局七类库-涉枪人员：新增涉枪人员功能正常')

    def test2_sheqiang_search_name(self):
        self.sheqiang_search()
        search_value = '索朗旺堆'
        self.dr.find_element_by_xpath('//*[@id="residentpopulation.xm"]').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(10)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,'姓名条件查询')
        self.dr.find_element_by_xpath('//*[@id="reset"]').click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.assertNotEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text, '重置功能')
        print('人口管理-部局七类库-涉枪人员：姓名条件查询功能正常')

    def test3_sheqiang_search_cardid(self):
        self.sheqiang_search()
        search_value = '540123198506025515'
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(10)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,'身份证号条件查询')
        self.dr.find_element_by_xpath('//*[@id="reset"]').click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.assertNotEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text, '重置功能')
        print('人口管理-部局七类库-涉枪人员：身份证号条件查询功能正常')

    def test4_sheqiang_search_zyzbh(self):
        self.sheqiang_search()
        search_value = '85815565'
        self.dr.find_element_by_xpath('//*[@id="cqzbh"]').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(10)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[5]').text,'持枪证编号条件查询')
        self.dr.find_element_by_xpath('//*[@id="reset"]').click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(5)
        self.assertNotEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text, '重置功能')
        print('人口管理-部局七类库-涉枪人员：持枪证编号条件查询功能正常')

    def test5_sheqiang_delete(self):
        self.sheqiang_search()
        search_value = '540123198506025515'
        self.dr.find_element_by_xpath('//*[@id="gmsfhm"]').send_keys(search_value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(10)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(search_value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,
                         '身份证号条件查询')
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        time.sleep(2)
        self.dr.switch_to.default_content()
        time.sleep(1)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        print('人口管理-局部七类库-涉枪人员：删除涉枪人员功能正常')

if __name__ == '__main__':
    unittest.main()
    # suite = unittest.makeSuite(TESTCAST_SHEQIANG)
    # filename = r'..\report\testresult.html'
    # with open(filename, 'wb') as fp:
    #     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行详情：')
    #     runner.run(suite)
