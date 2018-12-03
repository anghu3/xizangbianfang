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

class TESTCAST_JCJDJ(TESTCASE):
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

    def jcjdj_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div/a[3]/div[2]/img[2]').click()
        time.sleep(5)
        self.assertEqual('社区警务',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '社区警务')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[2]/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="943"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('接处警登记列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '接处警登记')

    def test01_jcjdj_add(self):
        self.jcjdj_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        self.dr.find_element_by_xpath('//*[@id="alarmTimeA"]').click()
        self.dr.find_element_by_xpath('//*[@id="alarmTimeA"]').clear()
        times=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
        self.dr.find_element_by_xpath('//*[@id="alarmTimeA"]').send_keys(times)
        self.dr.find_element_by_xpath('//*[@id="alarmpeopleTel"]').send_keys('15874587458')
        Select(self.dr.find_element_by_xpath('//*[@id="reportalarmType"]')).select_by_value('2')
        self.dr.find_element_by_xpath('//*[@id="alarmpeople"]').send_keys('马腾')
        self.dr.find_element_by_xpath('//*[@id="unitAddress"]').send_keys('北京中路24号')
        Select(self.dr.find_element_by_xpath('//*[@id="alertType"]')).select_by_value('5')
        self.dr.find_element_by_xpath('//*[@id="alertAddress"]').send_keys('北京中路与康昂多南路十字路口')
        self.dr.find_element_by_xpath('//*[@id="contentValidity"]').send_keys('北京中路与康昂多南路十字路口发生交通肇事逃逸，目前摩托车被撞2名人员倒地不起，肇事车辆直接驶离现场')
        self.dr.find_element_by_xpath('//*[@id="disposeSituation"]').send_keys('立即出警救援，并已拨打120救援车赶往现场。')
        self.dr.find_element_by_xpath('//*[@id="disposePerson"]').send_keys('马辰')
        self.dr.find_element_by_xpath('//*[@id="disposeTimeA"]').click()
        self.dr.find_element_by_xpath('//*[@id="disposeTimeA"]').clear()
        self.dr.find_element_by_xpath('//*[@id="disposeTimeA"]').send_keys(times)
        self.dr.find_element_by_xpath('//*[@id="dutyLeader"]').click()
        self.dr.find_element_by_xpath('//*[@id="dutyLeader"]').send_keys('包拯')
        Select(self.dr.find_element_by_xpath('//*[@id="result"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="resultRemark"]').send_keys('通过录像查看到肇事车辆车牌号为藏A25478，已经开始抓捕。')
        self.dr.find_element_by_xpath('//*[@id="hurtNum"]').send_keys('2')
        self.dr.find_element_by_xpath('//*[@id="deathToll"]').send_keys('0')
        self.dr.find_element_by_xpath('//*[@id="economicsLoss"]').send_keys('24000')
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual('马腾',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[5]').text,'校验新增，返回和默认排序')
        print('社区警务-接处警登记：新增功能正常')

    def test02_jcjdj_search_alarmTimeA(self):
        self.jcjdj_search()
        search_value_alarmTimeA=time.strftime("%Y-%m-%d", time.localtime(time.time()))
        self.dr.find_element_by_xpath('//*[@id="alarmTimeA"]').send_keys(search_value_alarmTimeA)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_alarmTimeA, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[14]/a').click()
        self.assertIn(search_value_alarmTimeA,self.dr.find_element_by_xpath('//*[@id="alarmTimeA"]').get_attribute('value'),'校验详情页面接警时间')
        print('社区警务-接处警登记：接警时间条件查询功能正常')

    def test03_jcjdj_search_reportalarmType(self):
        self.jcjdj_search()
        option_chioce=Select(self.dr.find_element_by_xpath('//*[@id="reportalarmType"]'))
        option_chioce.select_by_value('2')
        search_value_reportalarmType=option_chioce.first_selected_option.text
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_reportalarmType, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[14]/a').click()
        self.assertIn(search_value_reportalarmType,
                      self.dr.find_element_by_xpath('//*[@id="reportalarmType"]/option[3]').text, '校验详情页面报警形式')
        print('社区警务-接处警登记：报警形式条件查询功能正常')

    def test04_jcjdj_search_alarmpeople(self):
        self.jcjdj_search()
        search_value_alarmpeople='马腾'
        self.dr.find_element_by_xpath('//*[@id="alarmpeople"]').send_keys(search_value_alarmpeople)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_alarmpeople, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[14]/a').click()
        self.assertIn(search_value_alarmpeople,self.dr.find_element_by_xpath('//*[@id="alarmpeople"]').get_attribute('value'),'校验详情页面接警时间')
        print('社区警务-接处警登记：接警时间条件查询功能正常')

    def test05_jcjdj_search_unitAddress(self):
        self.jcjdj_search()
        search_value_unitAddress='北京中路24号'
        self.dr.find_element_by_xpath('//*[@id="unitAddress"]').send_keys(search_value_unitAddress)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 6
        self.pagination_num(paginal_number, search_value_unitAddress, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[14]/a').click()
        self.assertIn(search_value_unitAddress,self.dr.find_element_by_xpath('//*[@id="unitAddress"]').get_attribute('value'),'校验详情页面单位详址')
        print('社区警务-接处警登记：单位详址条件查询功能正常')

    def test06_jcjdj_search_alertType(self):
        self.jcjdj_search()
        option_chioce=Select(self.dr.find_element_by_xpath('//*[@id="alertType"]'))
        option_chioce.select_by_value('5')
        search_value_alertType='交通肇事'
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 7
        self.pagination_num(paginal_number, search_value_alertType, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[14]/a').click()
        self.assertIn(search_value_alertType,self.dr.find_element_by_xpath('//*[@id="alertType"]/option[6]').text,'校验详情页面警情类型')
        print('社区警务-接处警登记：警情类型条件查询功能正常')

    def test07_jcjdj_search_disposePerson(self):
        self.jcjdj_search()
        search_value_disposePerson='马辰'
        self.dr.find_element_by_xpath('//*[@id="disposePerson"]').send_keys(search_value_disposePerson)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 8
        self.pagination_num(paginal_number, search_value_disposePerson, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[14]/a').click()
        self.assertIn(search_value_disposePerson,self.dr.find_element_by_xpath('//*[@id="disposePerson"]').get_attribute('value'),'校验详情页面处警人员姓名')
        print('社区警务-接处警登记：处警人员姓名条件查询功能正常')

    def test08_jcjdj_search_disposeTimeA(self):
        self.jcjdj_search()
        search_value_disposeTimeA=time.strftime("%Y-%m-%d", time.localtime(time.time()))
        self.dr.find_element_by_xpath('//*[@id="disposeTimeA"]').send_keys(search_value_disposeTimeA)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 9
        self.pagination_num(paginal_number, search_value_disposeTimeA, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[14]/a').click()
        self.assertIn(search_value_disposeTimeA,self.dr.find_element_by_xpath('//*[@id="disposeTimeA"]').get_attribute('value'),'校验详情页面处警时间')
        print('社区警务-接处警登记：处警时间条件查询功能正常')

    def test09_jcjdj_search_result(self):
        self.jcjdj_search()
        search_value_result='报立刑事案件'
        Select(self.dr.find_element_by_xpath('//*[@id="result"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 10
        self.pagination_num(paginal_number, search_value_result, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[14]/a').click()
        self.assertIn(search_value_result,self.dr.find_element_by_xpath('//*[@id="result"]/option[2]').text,'校验详情页面处警结果')
        print('社区警务-接处警登记：处警结果条件查询功能正常')

    def test10_jcjdj_edit(self):
        self.jcjdj_search()
        search_value_alarmpeople='马腾'
        self.dr.find_element_by_xpath('//*[@id="alarmpeople"]').send_keys(search_value_alarmpeople)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_alarmpeople, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[14]/a').click()
        self.dr.find_element_by_xpath('//*[@id="unitAddress"]').clear()
        self.dr.find_element_by_xpath('//*[@id="unitAddress"]').send_keys('北京中路2号')
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual('马腾', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[5]').text, '校验编辑和默认排序')
        self.assertEqual('北京中路2号',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[6]').text,'校验编辑和默认排序')
        print('社区警务-接处警登记：编辑功能正常')

    def test11_jcjdj_delete(self):
        self.jcjdj_search()
        search_value_alarmpeople='马腾'
        self.dr.find_element_by_xpath('//*[@id="alarmpeople"]').send_keys(search_value_alarmpeople)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_alarmpeople, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('社区警务-接处警登记：删除功能正常')

if __name__=='__main__':
    unittest.main()