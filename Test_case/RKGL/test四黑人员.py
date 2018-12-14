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
from public_package.pubilc_package import sheet_setting, search, reset, currMenupath, page_title, goback, saveBtn,sheet_menu,sheet_prompt_message,work_space
import xlrd
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''
xlsfile=work_space+r'\\'+sheet_menu.col_values(6,21,22)[0]
excel = xlrd.open_workbook(xlsfile)
global sheet
sheet = excel.sheet_by_name('四黑人员')

class TESTCAST_SIHEI(TESTCASE):
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

    def sihei_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,21,22)[0]).click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath(currMenupath).text, '人口管理')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,21,22)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,21,22)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('四黑人员列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text,
                         '四黑人员')

    def test01_sihei_add(self):
        self.sihei_search()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        add_search_carid=sheet.col_values(1,2,3)[0]
        self.dr.find_element_by_xpath('//*[@id="idCard"]').send_keys(add_search_carid)
        Select(self.dr.find_element_by_xpath('//*[@id="personType"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="mainBusiness"]').send_keys(sheet.col_values(1,8,9)[0])
        self.dr.find_element_by_xpath('//*[@id="personName"]').send_keys(sheet.col_values(1,9,10)[0])
        self.dr.find_element_by_xpath('//*[@id="mainTourists"]').send_keys(sheet.col_values(1,10,11)[0])
        self.dr.find_element_by_xpath('//*[@id="activityArea"]').send_keys(sheet.col_values(1,11,12)[0])
        self.dr.find_element_by_xpath('//*[@id="activityTimeSlot"]').send_keys(sheet.col_values(1,12,13)[0])
        self.dr.find_element_by_xpath('//*[@id="startBlackDate"]').send_keys(sheet.col_values(1,13,14)[0])
        self.dr.find_element_by_xpath('//*[@id="dayTraffic"]').click()
        self.dr.find_element_by_xpath('//*[@id="dayTraffic"]').send_keys(sheet.col_values(1,14,15)[0])
        self.dr.find_element_by_xpath('//*[@id="averagePrice"]').send_keys(sheet.col_values(1,15,16)[0])
        self.dr.find_element_by_xpath('//*[@id="riskAssess"]').send_keys(sheet.col_values(1,16,17)[0])
        self.dr.find_element_by_xpath('//*[@id="dutyPerson"]').send_keys(sheet.col_values(1,17,18)[0])
        #责任单位
        self.dr.find_element_by_xpath('//*[@id="dutyOrg"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_46_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_48_span"]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="dayTraffic"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="remark"]').send_keys(sheet.col_values(1,19,20)[0])
        self.dr.find_element_by_xpath(saveBtn).click()
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        time.sleep(1)
        self.assertEqual(sheet_prompt_message.col_values(1, 4, 5)[0],
                         self.dr.find_element_by_xpath('//*[@id="gritter-item-1"]/div[2]/div[2]/p').text, '新增成功提示信息校验')
        print('人口管理-部局七类库-四黑人员：新增功能正常')

    def test02_sihei_search_name(self):
        self.sihei_search()
        search_value_name=sheet.col_values(1,0,1)[0]
        name_path=sheet.col_values(1,1,2)[0]
        self.dr.find_element_by_xpath(name_path).send_keys(search_value_name)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        column = 3
        self.pagination_num(paginal_number,search_value_name,column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(2)
        self.assertEqual('', self.dr.find_element_by_xpath(name_path).get_attribute('value'), '姓名-重置功能异常')
        print('人口管理-部局七类库-四黑人员：姓名条件查询功能正常')

    def test03_sihei_search_cardid(self):
        self.sihei_search()
        search_value_cardid = sheet.col_values(1,2,3)[0]
        cardid_path=sheet.col_values(1,3,4)[0]
        self.dr.find_element_by_xpath(cardid_path).send_keys(search_value_cardid)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        column = 4
        self.pagination_num(paginal_number, search_value_cardid, column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(2)
        self.assertEqual('', self.dr.find_element_by_xpath(cardid_path).get_attribute('value'), '身份证号码-重置功能异常')
        print('人口管理-部局七类库-四黑人员：身份证号条件查询功能正常')

    def test04_sihei_search_dutyPerson(self):
        self.sihei_search()
        search_value_dutyPerson = sheet.col_values(1,4,5)[0]
        dutyPerson_path=sheet.col_values(1,5,6)[0]
        self.dr.find_element_by_xpath('//*[@id="dutyPerson"]').send_keys(search_value_dutyPerson)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        column = 7
        self.pagination_num(paginal_number, search_value_dutyPerson, column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(2)
        self.assertEqual('', self.dr.find_element_by_xpath(dutyPerson_path).get_attribute('value'), '责任人-重置功能异常')
        print('人口管理-部局七类库-四黑人员：责任人条件查询功能正常')

    def test05_sihei_search_personType(self):
        self.sihei_search()
        Select(self.dr.find_element_by_xpath('//*[@id="personType"]')).select_by_value('1')
        # search_value_rylx=self.dr.find_element_by_xpath('//*[@id="personType"]').text
        search_value_personType=sheet.col_values(1,6,7)[0]
        personType_path=sheet.col_values(1,7,8)[0]
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        column = 5
        self.pagination_num(paginal_number, search_value_personType, column)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(2)
        self.assertEqual('', self.dr.find_element_by_xpath('//*[@id="personType"]/option[1]').text, '人员类型-重置功能异常')
        print('人口管理-部局七类库-四黑人员：人员类型条件查询功能正常')

    def test06_sihei_search_all(self):
        self.sihei_search()
        search_value_name = sheet.col_values(1, 0, 1)[0]
        name_path = sheet.col_values(1, 1, 2)[0]
        self.dr.find_element_by_xpath(name_path).send_keys(search_value_name)
        search_value_cardid = sheet.col_values(1, 2, 3)[0]
        cardid_path = sheet.col_values(1, 3, 4)[0]
        self.dr.find_element_by_xpath(cardid_path).send_keys(search_value_cardid)
        search_value_dutyPerson = sheet.col_values(1, 4, 5)[0]
        dutyPerson_path = sheet.col_values(1, 5, 6)[0]
        self.dr.find_element_by_xpath('//*[@id="dutyPerson"]').send_keys(search_value_dutyPerson)
        Select(self.dr.find_element_by_xpath('//*[@id="personType"]')).select_by_value('1')
        # search_value_rylx=self.dr.find_element_by_xpath('//*[@id="personType"]').text
        search_value_personType = sheet.col_values(1, 6, 7)[0]
        personType_path = sheet.col_values(1, 7, 8)[0]
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4,1,2)[0]).text
        self.pagination_num(paginal_number, search_value_personType, 5)
        self.pagination_num(paginal_number, search_value_dutyPerson, 7)
        self.pagination_num(paginal_number, search_value_cardid, 4)
        self.pagination_num(paginal_number, search_value_name, 3)
        self.dr.find_element_by_xpath(reset).click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_xpath(search).click()
        time.sleep(2)
        self.assertEqual('', self.dr.find_element_by_xpath('//*[@id="personType"]/option[1]').text, '人员类型-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(name_path).get_attribute('value'), '姓名-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(cardid_path).get_attribute('value'), '身份证号码-重置功能异常')
        self.assertEqual('', self.dr.find_element_by_xpath(dutyPerson_path).get_attribute('value'), '责任人-重置功能异常')
        print('人口管理-部局七类库-四黑人员：条件查询功能正常')

    def test07_sihei_details(self):
        self.sihei_search()
        search_value_cardid = sheet.col_values(1, 2, 3)[0]
        cardid_path = sheet.col_values(1, 3, 4)[0]
        self.dr.find_element_by_xpath(cardid_path).send_keys(search_value_cardid)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 4
        self.pagination_num(paginal_number, search_value_cardid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/a').click()
        self.assertEqual(sheet.col_values(1,0,1)[0],self.dr.find_element_by_xpath('//*[@id="personName"]').get_attribute('value'),'')
        self.assertEqual(sheet.col_values(1,2,3)[0],self.dr.find_element_by_xpath('//*[@id="idCard"]').get_attribute('value'),'')
        self.assertEqual(sheet.col_values(1,4,5)[0],self.dr.find_element_by_xpath('//*[@id="dutyPerson"]').get_attribute('value'),'')
        time.sleep(1)
        self.dr.find_element_by_xpath(goback).click()
        self.assertEqual('四黑人员列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text,
                         '四黑人员')
        print('人口管理-部局七类库-四黑人员：详情功能正常')

    def test08_sihei_edit(self):
        self.sihei_search()
        search_value_cardid = sheet.col_values(1, 2, 3)[0]
        cardid_path = sheet.col_values(1, 3, 4)[0]
        self.dr.find_element_by_xpath(cardid_path).send_keys(search_value_cardid)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 4
        self.pagination_num(paginal_number, search_value_cardid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/a').click()
        self.dr.find_element_by_xpath('//*[@id="idCard"]').clear()
        self.dr.find_element_by_xpath('//*[@id="idCard"]').send_keys(sheet.col_values(2,2,3)[0])
        self.dr.find_element_by_xpath('//*[@id="mainBusiness"]').clear()
        self.dr.find_element_by_xpath('//*[@id="mainBusiness"]').send_keys(sheet.col_values(2, 8, 9)[0])
        self.dr.find_element_by_xpath('//*[@id="personName"]').clear()
        self.dr.find_element_by_xpath('//*[@id="personName"]').send_keys(sheet.col_values(2, 9, 10)[0])
        self.dr.find_element_by_xpath('//*[@id="mainTourists"]').clear()
        self.dr.find_element_by_xpath('//*[@id="mainTourists"]').send_keys(sheet.col_values(2, 10, 11)[0])
        self.dr.find_element_by_xpath('//*[@id="activityArea"]').clear()
        self.dr.find_element_by_xpath('//*[@id="activityArea"]').send_keys(sheet.col_values(2, 11, 12)[0])
        self.dr.find_element_by_xpath('//*[@id="activityTimeSlot"]').clear()
        self.dr.find_element_by_xpath('//*[@id="activityTimeSlot"]').send_keys(sheet.col_values(2, 12, 13)[0])
        self.dr.find_element_by_xpath('//*[@id="startBlackDate"]').clear()
        self.dr.find_element_by_xpath('//*[@id="startBlackDate"]').send_keys(sheet.col_values(2, 13, 14)[0])
        self.dr.find_element_by_xpath('//*[@id="dayTraffic"]').click()
        self.dr.find_element_by_xpath('//*[@id="dayTraffic"]').clear()
        self.dr.find_element_by_xpath('//*[@id="dayTraffic"]').send_keys(sheet.col_values(2, 14, 15)[0])
        self.dr.find_element_by_xpath('//*[@id="averagePrice"]').clear()
        self.dr.find_element_by_xpath('//*[@id="averagePrice"]').send_keys(sheet.col_values(2, 15, 16)[0])
        self.dr.find_element_by_xpath('//*[@id="riskAssess"]').clear()
        self.dr.find_element_by_xpath('//*[@id="riskAssess"]').send_keys(sheet.col_values(2, 16, 17)[0])
        self.dr.find_element_by_xpath('//*[@id="dutyPerson"]').clear()
        self.dr.find_element_by_xpath('//*[@id="dutyPerson"]').send_keys(sheet.col_values(2, 17, 18)[0])
        self.dr.find_element_by_xpath('//*[@id="remark"]').clear()
        self.dr.find_element_by_xpath('//*[@id="remark"]').send_keys(sheet.col_values(2, 19, 20)[0])
        self.dr.find_element_by_xpath(saveBtn).click()
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        time.sleep(1)
        self.assertEqual(sheet_prompt_message.col_values(1, 4, 5)[0],
                         self.dr.find_element_by_xpath('//*[@id="gritter-item-1"]/div[2]/div[2]/p').text, '编辑修改成功提示信息校验')
        print('人口管理-部局七类库-四黑人员：编辑修改功能正常')

    def test09_sihei_delete(self):
        self.sihei_search()
        search_value_cardid = sheet.col_values(2, 2, 3)[0]
        cardid_path = sheet.col_values(1, 3, 4)[0]
        self.dr.find_element_by_xpath(cardid_path).send_keys(search_value_cardid)
        self.dr.find_element_by_xpath(search).click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath(sheet_setting.col_values(4, 1, 2)[0]).text
        column = 4
        self.pagination_num(paginal_number, search_value_cardid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[2]/div[1]/input').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        # self.dr.switch_to.frame('iframeb')
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        time.sleep(1)
        self.assertEqual(sheet_prompt_message.col_values(1, 3, 4)[0],
                         self.dr.find_element_by_xpath('//*[@id="gritter-item-1"]/div[2]/div[2]/p').text, '校验删除成功提示信息')
        print('人口管理-部局七类库-四黑人员：删除功能正常')

if __name__ == '__main__':
    unittest.main()
