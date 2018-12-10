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
from public_package.pubilc_package import sheet_setting, search, reset, currMenupath, page_title, goback, saveBtn,sheet_menu,sheet_prompt_message
from public_package.pubilc_package import TESTCASE
import HTMLTestRunner
import xlrd
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

# xlsfile = r'F:\pythonkeys\自动化测试\lasa\QWGL.xlsx'
# excel = xlrd.open_workbook(xlsfile)
# global sheet
# sheet = excel.sheet_by_name('人员请假管理')

class TESTCAST_QJGL(TESTCASE):
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

    def qjgl_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,63,64)[0]).click()
        time.sleep(5)
        self.assertEqual('勤务管理',self.dr.find_element_by_xpath(currMenupath).text, '勤务管理')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,63,64)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,63,64)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('人员请假条列表', self.dr.find_element_by_xpath(page_title).text,
                         '人员请假管理')

    def qjgl_search_test(self):
        self.login(login_name_test, login_password_test)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1, 63, 64)[0]).click()
        time.sleep(5)
        self.assertEqual('勤务管理', self.dr.find_element_by_xpath(currMenupath).text, '勤务管理')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3, 63, 64)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5, 63, 64)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('人员请假条列表', self.dr.find_element_by_xpath(page_title).text,
                         '人员请假管理')

    def test01_qjgl_add(self):
        self.qjgl_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        global add_value_user
        add_value_user=self.dr.find_element_by_xpath('//*[@id="proposer"]').get_attribute('value')
        self.dr.find_element_by_xpath('//*[@id="startTime"]').click()
        self.dr.find_element_by_xpath('//*[@id="startTime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="startTime"]').send_keys('2018-09-13 08:00:00')
        self.dr.find_element_by_xpath('//*[@id="endTime"]').click()
        self.dr.find_element_by_xpath('//*[@id="endTime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="endTime"]').send_keys('2018-09-13 18:00:00')
        self.dr.find_element_by_xpath('//*[@id="totalTime"]').click()
        self.dr.find_element_by_xpath('//*[@id="totalTime"]').send_keys('8')
        Select(self.dr.find_element_by_xpath('//*[@id="wad"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="reason"]').send_keys('家中老人生病，需要请假到医院陪同看病！')
        self.dr.find_element_by_xpath('//*[@id="urgentTel"]').send_keys('15874574587')
        self.dr.find_element_by_xpath('//*[@id="director"]').send_keys('包拯')
        self.dr.find_element_by_xpath('//*[@id="approval"]').send_keys('情况属实，予以批准')
        self.dr.find_element_by_xpath('//*[@id="approvalOpinion"]').send_keys('包拯')
        self.dr.find_element_by_xpath('//*[@id="approvalTime"]').click()
        Select(self.dr.find_element_by_xpath('//*[@id="approvalResult"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        time.sleep(1)
        self.assertEqual(sheet_prompt_message.col_values(1, 4, 5)[0],
                         self.dr.find_element_by_xpath('//*[@id="gritter-item-1"]/div[2]/div[2]/p').text, '新增成功提示信息校验')
        print('勤务管理-人员请假管理：新增功能正常')

    def test02_qjgl_add_test(self):
        self.qjgl_search_test()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        global add_value_user_test
        add_value_user_test=self.dr.find_element_by_xpath('//*[@id="proposer"]').get_attribute('value')
        self.dr.find_element_by_xpath('//*[@id="startTime"]').click()
        self.dr.find_element_by_xpath('//*[@id="startTime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="startTime"]').send_keys('2018-09-13 08:00:00')
        self.dr.find_element_by_xpath('//*[@id="endTime"]').click()
        self.dr.find_element_by_xpath('//*[@id="endTime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="endTime"]').send_keys('2018-09-13 18:00:00')
        self.dr.find_element_by_xpath('//*[@id="totalTime"]').click()
        self.dr.find_element_by_xpath('//*[@id="totalTime"]').send_keys('8')
        Select(self.dr.find_element_by_xpath('//*[@id="wad"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="reason"]').send_keys('家中老人生病，需要请假到医院陪同看病！')
        self.dr.find_element_by_xpath('//*[@id="urgentTel"]').send_keys('15874574587')
        self.dr.find_element_by_xpath('//*[@id="director"]').send_keys('包拯')
        self.dr.find_element_by_xpath('//*[@id="approval"]').send_keys('情况属实，予以批准')
        self.dr.find_element_by_xpath('//*[@id="approvalOpinion"]').send_keys('包拯')
        self.dr.find_element_by_xpath('//*[@id="approvalTime"]').click()
        Select(self.dr.find_element_by_xpath('//*[@id="approvalResult"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        time.sleep(1)
        self.assertEqual(sheet_prompt_message.col_values(1, 4, 5)[0],
                         self.dr.find_element_by_xpath('//*[@id="gritter-item-1"]/div[2]/div[2]/p').text, '新增成功提示信息校验')
        print('勤务管理-人员请假管理：新增功能正常')

    def test03_qjgl_search_proposer(self):
        self.qjgl_search()
        search_value_proposer='test'
        self.dr.find_element_by_xpath('//*[@id="proposer"]').send_keys(search_value_proposer)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_proposer, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[10]/a').click()
        self.assertEqual(search_value_proposer,self.dr.find_element_by_xpath('//*[@id="proposer"]').get_attribute('value'),'校验详情页面申请人')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('人员请假条列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '人员请假管理')
        print('勤务管理-人员请假管理：申请人条件查询功能正常')

    def test04_qjgl_search_urgentTel(self):
        self.qjgl_search()
        search_value_urgentTel='15874574587'
        self.dr.find_element_by_xpath('//*[@id="urgentTel"]').send_keys(search_value_urgentTel)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 7
        self.pagination_num(paginal_number, search_value_urgentTel, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[10]/a').click()
        self.assertEqual(search_value_urgentTel,self.dr.find_element_by_xpath('//*[@id="urgentTel"]').get_attribute('value'),'校验详情紧急联系电话')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('人员请假条列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '人员请假管理')
        print('勤务管理-人员请假管理：紧急联系电话条件查询功能正常')

    def test05_qjgl_search_approvalOpinion(self):
        self.qjgl_search()
        search_value_approvalOpinion='包拯'
        '''审批人'''
        self.dr.find_element_by_xpath('//*[@id="approvalOpinion"]').send_keys(search_value_approvalOpinion)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 8
        self.pagination_num(paginal_number, search_value_approvalOpinion, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[10]/a').click()
        self.assertEqual(search_value_approvalOpinion,self.dr.find_element_by_xpath('//*[@id="approvalOpinion"]').get_attribute('value'),'校验详情页面审批人')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('人员请假条列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '人员请假管理')
        print('勤务管理-人员请假管理：审批人条件查询功能正常')

    '''请假开始时间和结束时间查询由于不是精准查询并且时间对比支撑函数尚未完成，脚本暂时搁置！'''

    def test06_qjgl_search_approvalTime1(self):
        self.qjgl_search()
        search_value_approvalTime1=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        '''审批时间'''
        self.dr.find_element_by_xpath('//*[@id="approvalTime1"]').send_keys(search_value_approvalTime1)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 9
        self.pagination_num(paginal_number, search_value_approvalTime1, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[10]/a').click()
        self.assertIn(search_value_approvalTime1,self.dr.find_element_by_xpath('//*[@id="approvalTime"]').get_attribute('value'),'校验详情页面审批时间')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('人员请假条列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '人员请假管理')
        print('勤务管理-人员请假管理：审批时间条件查询功能正常')

    def test07_qjgl_search_totalTime(self):
        self.qjgl_search()
        search_value_totalTime='8'
        self.dr.find_element_by_xpath('//*[@id="totalTime"]').send_keys(search_value_totalTime)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 6
        self.pagination_num(paginal_number, search_value_totalTime, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[10]/a').click()
        self.assertEqual(search_value_totalTime,self.dr.find_element_by_xpath('//*[@id="totalTime"]').get_attribute('value'),'校验详情合计小时数')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('人员请假条列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '人员请假管理')
        print('勤务管理-人员请假管理：合计小时数条件查询功能正常')

    def test08_qjgl_edit(self):
        self.qjgl_search()
        search_value_proposer='test'
        self.dr.find_element_by_xpath('//*[@id="proposer"]').send_keys(search_value_proposer)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_proposer, column)
        edit_value_totalTime='16'
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[10]/a').click()
        self.dr.find_element_by_xpath('//*[@id="totalTime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="totalTime"]').send_keys(edit_value_totalTime)
        self.dr.find_element_by_xpath('//*[@id="save"]').click()
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="proposer"]').send_keys(search_value_proposer)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual(edit_value_totalTime,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[6]').text,'校验编辑功能')
        print('勤务管理-人员请假管理：编辑功能正常')

    def test09_qjgl_delete(self):
        self.qjgl_search()
        search_value_proposer='test'
        self.dr.find_element_by_xpath('//*[@id="proposer"]').send_keys(search_value_proposer)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_proposer, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('勤务管理-人员请假管理：删除功能正常')

if __name__=='__main__':
    unittest.main()