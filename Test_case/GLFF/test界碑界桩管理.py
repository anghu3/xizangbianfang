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
from public_package.pubilc_package import sheet_setting, search, reset, currMenupath, page_title, goback, saveBtn , sheet_menu,sheet_prompt_message,work_space
import xlrd
import HTMLTestRunner
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

class TESTCAST_JIEBEIJIEZHUANG(TESTCASE):
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

    def jiebeijiezhuang_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,39,40)[0]).click()
        time.sleep(5)
        self.assertEqual('管理防范',self.dr.find_element_by_xpath(currMenupath).text, '管理防范')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,39,40)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,39,40)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('界碑界桩列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text,
                         '界碑界桩管理')

    def test01_jiebeijiezhuang_add(self):
        self.jiebeijiezhuang_search()
        self.dr.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/a[2]').click()
        add_value_name='陈墉中尼边界245142'
        global codeid
        self.dr.find_element_by_xpath('//*[@id="name"]').send_keys(add_value_name)
        codeid=self.dr.find_element_by_xpath('//*[@id="code"]').get_attribute('value')
        self.dr.find_element_by_xpath('//*[@id="geographiPosition"]').send_keys('陈墉镇')
        self.dr.find_element_by_xpath('//*[@id="societyChn"]').send_keys('陈塘位于喜马拉雅山北麓、珠穆朗玛峰东侧的原始森林地带内，处于中尼边界我国一侧的最南边，与尼泊尔一衣带水，隔河相望。')
        self.dr.find_element_by_xpath('//*[@id="societyChnVietnam"]').send_keys('陈塘位于喜马拉雅山北麓、珠穆朗玛峰东侧的原始森林地带内，处于中尼边界我国一侧的最南边，与尼泊尔一衣带水，隔河相望。')
        self.dr.find_element_by_xpath('//*[@id="isBoundaryWithVn"]').send_keys('陈塘位于喜马拉雅山北麓、珠穆朗玛峰东侧的原始森林地带内，处于中尼边界我国一侧的最南边，与尼泊尔一衣带水，隔河相望。')
        self.dr.find_element_by_xpath('//*[@id="riskEvaluation"]').send_keys('陈塘位于喜马拉雅山北麓、珠穆朗玛峰东侧的原始森林地带内，处于中尼边界我国一侧的最南边，与尼泊尔一衣带水，隔河相望。')
        self.dr.find_element_by_xpath('//*[@id="dutyPolice"]').send_keys('包涵')
        self.dr.find_element_by_xpath('//*[@id="dutyPoliceContact"]').send_keys('15869874587')
        self.dr.find_element_by_xpath('//*[@id="zrdw"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_span"]').click()
        self.dr.find_element_by_xpath('//*[@id="dutyRoomTel"]').send_keys('13574587451')
        self.dr.find_element_by_xpath('//*[@id="gxdw"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="gxtreeSelect_45_span"]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="saveBound"]').click()
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual('界碑界桩列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text,'返回功能校验')
        print('管理防范-界碑界桩管理：新增功能正常')

    def test02_jiebeijiezhuang_search_codeid(self):
        self.jiebeijiezhuang_search()
        search_value_codeid=codeid
        # print(codeid)
        self.dr.find_element_by_xpath('//*[@id="code"]').send_keys(search_value_codeid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_codeid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        self.assertEqual(search_value_codeid,self.dr.find_element_by_xpath('//*[@id="code"]').get_attribute('value'),'校验详情页面的编号')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('界碑界桩列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text, '返回功能校验')
        print('管理防范-界碑界桩管理：编号条件查询功能正常')

    def test03_jiebeijiezhuang_search_name(self):
        self.jiebeijiezhuang_search()
        search_value_name='陈墉中尼边界245142'
        self.dr.find_element_by_xpath('//*[@id="name"]').send_keys(search_value_name)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_name, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        self.assertEqual(search_value_name,self.dr.find_element_by_xpath('//*[@id="name"]').get_attribute('value'),'校验详情页面的名称')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('界碑界桩列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text, '返回功能校验')
        print('管理防范-界碑界桩管理：名称条件查询功能正常')

    def test04_jiebeijiezhuang_search_address(self):
        self.jiebeijiezhuang_search()
        search_value_address = '陈墉镇'
        self.dr.find_element_by_xpath('//*[@id="geographiPosition"]').send_keys(search_value_address)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 6
        self.pagination_num(paginal_number, search_value_address, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        self.assertEqual(search_value_address,
                         self.dr.find_element_by_xpath('//*[@id="geographiPosition"]').get_attribute('value'),
                         '校验详情页面所在名称和具体方位')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('界碑界桩列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text, '返回功能校验')
        print('管理防范-界碑界桩管理：所在名称和具体方位条件查询功能正常')

    def test05_jiebeijiezhuang_search_dutyPolice(self):
        self.jiebeijiezhuang_search()
        search_value_dutyPolice='包涵'
        self.dr.find_element_by_xpath('//*[@id="dutyPolice"]').send_keys(search_value_dutyPolice)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 7
        self.pagination_num(paginal_number, search_value_dutyPolice, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        self.assertEqual(search_value_dutyPolice,self.dr.find_element_by_xpath('//*[@id="dutyPolice"]').get_attribute('value'),'校验详情页面责任民警')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('界碑界桩列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text, '返回功能校验')
        print('管理防范-界碑界桩管理：责任民警条件查询功能正常')

    def test06_jiebeijiezhuang_search_zrdw(self):
        self.jiebeijiezhuang_search()
        search_value_zrdw='山南支队'
        self.dr.find_element_by_xpath('//*[@id="zrdw"]').click()
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_span"]').click()
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 9
        self.pagination_num(paginal_number, search_value_zrdw, column)
        # self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        # self.assertEqual(search_value_zrdw,self.dr.find_element_by_xpath('//*[@id="dutyPolice"]').get_attribute('value'),'校验详情页面责任民警')
        # self.dr.implicitly_wait(5)
        # self.dr.find_element_by_xpath('/html/body/a').click()
        # time.sleep(2)
        # self.assertEqual('界碑界桩列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text, '返回功能校验')
        print('管理防范-界碑界桩管理：责任单位条件查询功能正常')

    def test07_jiebeijiezhuang_search_gldw(self):
        self.jiebeijiezhuang_search()
        search_value_gldw='山南支队'
        self.dr.find_element_by_xpath('//*[@id="gxdw"]').click()
        self.dr.find_element_by_xpath('//*[@id="gxtreeSelect_45_span"]').click()
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 10
        self.pagination_num(paginal_number, search_value_gldw, column)
        # self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        # self.assertEqual(search_value_zrdw,self.dr.find_element_by_xpath('//*[@id="dutyPolice"]').get_attribute('value'),'校验详情页面责任民警')
        # self.dr.implicitly_wait(5)
        # self.dr.find_element_by_xpath('/html/body/a').click()
        # time.sleep(2)
        # self.assertEqual('界碑界桩列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text, '返回功能校验')
        print('管理防范-界碑界桩管理：责任单位条件查询功能正常')

    def test08_jiebeijiezhuang_delete(self):
        self.jiebeijiezhuang_search()
        search_value_codeid = codeid
        # print(codeid)
        self.dr.find_element_by_xpath('//*[@id="code"]').send_keys(search_value_codeid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_codeid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[2]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('管理防范-界碑界桩管理：删除功能正常')

if __name__=='__main__':
    unittest.main()