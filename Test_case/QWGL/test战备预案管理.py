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

class TESTCAST_ZBYA(TESTCASE):
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

    def zbya_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div/a[2]/div[2]/img[2]').click()
        time.sleep(3)
        self.assertEqual('勤务管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '勤务管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="535"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(3)
        self.assertEqual('战备预案列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '战备预案管理')

    def test1_zbya_add(self):
        self.zbya_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        add_value_yamc='林芝县特大洪水预案'
        self.dr.find_element_by_xpath('//*[@id="yamc"]').send_keys(add_value_yamc)
        global codeid
        codeid=self.dr.find_element_by_xpath('//*[@id="code"]').get_attribute('value')
        # print(codeid)
        Select(self.dr.find_element_by_xpath('//*[@id="type"]')).select_by_value('4')
        self.dr.find_element_by_xpath('//*[@id="task"]').send_keys('积极疏散和救援群众，防止人员伤亡！')
        self.dr.find_element_by_xpath('//*[@id="determined"]').send_keys('迅速到达事故地点救援，防止出现人员伤亡！')
        self.dr.find_element_by_xpath('//*[@id="oneMembers_chosen"]/ul').click()
        self.dr.find_element_by_xpath('//*[@id="oneMembers_chosen"]/div/ul/li[3]').click()
        self.dr.find_element_by_xpath('//*[@id="oneDes"]').send_keys('疏散下游可能被危及的乡村群众.')
        self.dr.find_element_by_xpath('//*[@id="twoMembers_chosen"]/ul').click()
        self.dr.find_element_by_xpath('//*[@id="twoMembers_chosen"]/div/ul/li[4]').click()
        self.dr.find_element_by_xpath('//*[@id="twoDes"]').send_keys('搭建群众临时安置点')
        self.dr.find_element_by_xpath('//*[@id="threeMembers_chosen"]/ul').click()
        self.dr.find_element_by_xpath('//*[@id="threeMembers_chosen"]/div/ul/li[5]').click()
        self.dr.find_element_by_xpath('//*[@id="threeDes"]').send_keys('赶赴受害地点进行搜救并尽力挽回群众损失！')
        self.dr.find_element_by_xpath('//*[@id="fourMembers_chosen"]/ul').click()
        self.dr.find_element_by_xpath('//*[@id="fourMembers_chosen"]/div/ul/li[6]').click()
        self.dr.find_element_by_xpath('//*[@id="fourDes"]').send_keys('组织运输和发放救援物资。')
        self.dr.find_element_by_xpath('//*[@id="policeReadiness"]').send_keys('已经安排240名警力参与救援工作，另有120名正在赶往救援地点！')
        self.dr.find_element_by_xpath('//*[@id="friendsCondition"]').send_keys('目前就林芝县下面三个乡村遭遇灾害，灾害重点在林芝县甘林乡！')
        Select(self.dr.find_element_by_xpath('//*[@id="generalDirector"]')).select_by_value('索朗班旦')
        Select(self.dr.find_element_by_xpath('//*[@id="secondDirector"]')).select_by_value('邹青')
        self.dr.find_element_by_xpath('//*[@id="members_chosen"]/ul').click()
        self.dr.find_element_by_xpath('//*[@id="members_chosen"]/div/ul/li[3]').click()
        self.dr.find_element_by_xpath('//*[@id="members_chosen"]/ul').click()
        self.dr.find_element_by_xpath('//*[@id="members_chosen"]/div/ul/li[4]').click()
        self.dr.find_element_by_xpath('//*[@id="members_chosen"]/ul').click()
        self.dr.find_element_by_xpath('//*[@id="members_chosen"]/div/ul/li[5]').click()
        self.dr.find_element_by_xpath('//*[@id="members_chosen"]/ul').click()
        self.dr.find_element_by_xpath('//*[@id="members_chosen"]/div/ul/li[6]').click()
        self.dr.find_element_by_xpath('//*[@id="taskDescription"]').send_keys('积极疏散和救援群众，防止人员伤亡！')
        Select(self.dr.find_element_by_xpath('//*[@id="responseWay"]')).select_by_value('4')
        Select(self.dr.find_element_by_xpath('//*[@id="responseLevel"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="actionContent"]').send_keys('积极响应')
        Select(self.dr.find_element_by_xpath('//*[@id="disposeType"]')).select_by_value('3')
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual(codeid,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,'校验新增、返回和默认排序')
        print('勤务管理-战备预案管理：新增功能正常')

    def test2_zbya_search_codeid(self):
        self.zbya_search()
        search_value_codeid=codeid
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value_codeid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_codeid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        self.assertEqual(search_value_codeid,self.dr.find_element_by_xpath('//*[@id="code"]').get_attribute('value'),'校验详情页面战备预警编号')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_codeid,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,'校验返回和默认排序')
        print('勤务管理-战备预案管理：战备预警编号条件查询功能正常')

    def test3_zbya_search_name(self):
        self.zbya_search()
        search_value_name='林芝县特大洪水预案'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/div/input').send_keys(search_value_name)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_name, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        self.assertEqual(search_value_name,self.dr.find_element_by_xpath('//*[@id="yamc"]').get_attribute('value'),'校验详情页面战备预警编号')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_name,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,'校验返回和默认排序')
        print('勤务管理-战备预案管理：战备预警名称条件查询功能正常')

    def test4_zbya_search_generalDirector(self):
        self.zbya_search()
        search_value_generalDirector='索朗班旦'
        self.dr.find_element_by_xpath('//*[@id="form"]/div[3]/div/input').send_keys(search_value_generalDirector)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 6
        self.pagination_num(paginal_number, search_value_generalDirector, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        self.assertEqual(search_value_generalDirector,self.dr.find_element_by_xpath('//*[@id="generalDirector"]').get_attribute('value'),'校验详情页面战备预警编号')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_generalDirector,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[6]').text,'校验返回和默认排序')
        print('勤务管理-战备预案管理：总指挥条件查询功能正常')

    def test5_zbya_edit(self):
        self.zbya_search()
        search_value_codeid=codeid
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value_codeid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_codeid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[11]/a').click()
        edit_value_name='林芝县特大洪水灾害预案'
        self.dr.find_element_by_xpath('//*[@id="yamc"]').clear()
        self.dr.find_element_by_xpath('//*[@id="yamc"]').send_keys(edit_value_name)
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(edit_value_name, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,
                         '校验返回和默认排序')
        print('勤务管理-战备预案管理：编辑功能正常')

    def test6_zbya_delete(self):
        self.zbya_search()
        search_value_codeid=codeid
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/input').send_keys(search_value_codeid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_codeid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('勤务管理-战备预案管理：删除功能正常')

if __name__=='__main__':
    unittest.main()
