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
import xlrd
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

xlsfile = r'F:\pythonkeys\自动化测试\lasa\RKGL.xls'
excel = xlrd.open_workbook(xlsfile)
global sheet
sheet = excel.sheet_by_name('群发力量人员管理')

class TESTCAST_QFRYGL(TESTCASE):

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

    def qfrygl_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/a[2]').click()
        time.sleep(5)
        self.assertEqual('人口管理',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '人口管理')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[10]/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="602"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('群防群治信息列表', self.dr.find_element_by_xpath('/html/body/div[1]/div').text,
                         '群防力量_人员管理')

    def test01_qfrygl_add(self):
        self.qfrygl_search()
        add_value_carid=sheet.cell(1,1).value
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        self.dr.find_element_by_xpath('//*[@id="idCard"]').send_keys(add_value_carid)
        self.dr.find_element_by_xpath('//*[@id="telephone"]').click()
        self.dr.find_element_by_xpath('//*[@id="telephone"]').send_keys(sheet.cell(1,2).value)
        self.dr.find_element_by_xpath('//*[@id="controlRange"]').send_keys(sheet.cell(1,3).value)
        self.dr.find_element_by_xpath('//*[@id="dutyOrgName"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_46_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_48_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="dutyRoomTelephone"]').send_keys(sheet.cell(1,4).value)
        self.dr.find_element_by_xpath('//*[@id="dutyPolice"]').send_keys(sheet.cell(1,5).value)
        self.dr.find_element_by_xpath('//*[@id="dutyPoliceContactWay"]').send_keys(sheet.cell(1,6).value)
        self.dr.find_element_by_xpath('//*[@id="manageOrgName"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect2_45_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect2_46_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect2_48_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual(add_value_carid,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,'校验新增、返回和默认排序')
        print('人口管理-群防力量_人员管理：新增功能正常')

    def test02_qfrygl_search_memberName(self):
        self.qfrygl_search()
        self.dr.find_element_by_xpath('//*[@id="memberName"]').send_keys(sheet.cell(1,0).value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, sheet.cell(1,0).value, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(sheet.cell(1,0).value,self.dr.find_element_by_xpath('//*[@id="memberName"]').get_attribute('value'),'校验详情页面姓名')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(sheet.cell(1,0).value,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,'校验返回和默认排序')
        print('人口管理-群防力量_人员管理：姓名条件查询功能正常')

    def test03_qfrygl_search_idCard(self):
        self.qfrygl_search()
        self.dr.find_element_by_xpath('//*[@id="idCard"]').send_keys(sheet.cell(1,1).value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, sheet.cell(1,1).value, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(sheet.cell(1,1).value,
                         self.dr.find_element_by_xpath('//*[@id="idCard"]').get_attribute('value'), '校验详情页面身份证号码')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(sheet.cell(1,1).value,
                         self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text, '校验返回和默认排序')
        print('人口管理-群防力量_人员管理：身份证号码条件查询功能正常')

    def test04_qfrygl_search_telephone(self):
        self.qfrygl_search()
        self.dr.find_element_by_xpath('//*[@id="telephone"]').send_keys(sheet.cell(1,2).value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, sheet.cell(1,2).value, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(sheet.cell(1,2).value,
                         self.dr.find_element_by_xpath('//*[@id="telephone"]').get_attribute('value'), '校验详情页面联系电话')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(sheet.cell(1,2).value ,
                         self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[5]').text, '校验返回和默认排序')
        print('人口管理-群防力量_人员管理：联系电话条件查询功能正常')

    def test05_qfrygl_search_dutyPolice(self):
        self.qfrygl_search()
        self.dr.find_element_by_xpath('//*[@id="dutyPolice"]').send_keys(sheet.cell(1,5).value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 6
        self.pagination_num(paginal_number, sheet.cell(1,5).value, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(sheet.cell(1,5).value,
                         self.dr.find_element_by_xpath('//*[@id="dutyPolice"]').get_attribute('value'), '校验详情页面责任区民警')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(sheet.cell(1,5).value ,
                         self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[6]').text, '校验返回和默认排序')
        print('人口管理-群防力量_人员管理：责任区民警条件查询功能正常')

    def test06_qfrygl_search_manageOrgName(self):
        self.qfrygl_search()
        self.dr.find_element_by_xpath('//*[@id="manageOrgName"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_46_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_48_span"]').click()

        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 8
        self.pagination_num(paginal_number, sheet.cell(1,7).value, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(sheet.cell(1,7).value,
                         self.dr.find_element_by_xpath('//*[@id="manageOrgName"]').get_attribute('value'), '校验详情页面管理单位')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(sheet.cell(1,7).value ,
                         self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[8]').text, '校验返回和默认排序')
        print('人口管理-群防力量_人员管理：管理单位条件查询功能正常')

    def test07_qfrygl_search_all(self):
        self.qfrygl_search()
        self.dr.find_element_by_xpath('//*[@id="memberName"]').send_keys(sheet.cell(1,0).value)
        self.dr.find_element_by_xpath('//*[@id="idCard"]').send_keys(sheet.cell(1,1).value)
        self.dr.find_element_by_xpath('//*[@id="telephone"]').send_keys(sheet.cell(1,2).value)
        self.dr.find_element_by_xpath('//*[@id="dutyPolice"]').send_keys(sheet.cell(1,5).value)
        self.dr.find_element_by_xpath('//*[@id="manageOrgName"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_46_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_48_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(paginal_number, sheet.cell(1,0).value, 3)
        self.pagination_num(paginal_number, sheet.cell(1,1).value, 4)
        self.pagination_num(paginal_number, sheet.cell(1,2).value, 5)
        self.pagination_num(paginal_number, sheet.cell(1,7).value, 8)
        self.pagination_num(paginal_number, sheet.cell(1,5).value, 6)
        print('人口管理-群防力量_人员管理：全条件查询功能正常')


    def test08_qfrygl_edit(self):
        self.qfrygl_search()
        self.dr.find_element_by_xpath('//*[@id="idCard"]').send_keys(sheet.cell(1,1).value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, sheet.cell(1,1).value, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.dr.find_element_by_xpath('//*[@id="dutyPolice"]').clear()
        self.dr.find_element_by_xpath('//*[@id="dutyPolice"]').send_keys('包拯')
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual(sheet.cell(1,1).value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,
                         '校验编辑、返回和默认排序')
        self.assertEqual('包拯',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[6]').text,'校验编辑、返回和默认排序')
        print('人口管理-群防力量_人员管理：编辑功能正常')

    def test09_qfrygl_add_task(self):
        self.qfrygl_search()
        self.dr.find_element_by_xpath('//*[@id="idCard"]').send_keys(sheet.cell(1,1).value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, sheet.cell(1,1).value, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.dr.find_element_by_xpath('//*[@id="prevAdd"]').click()
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]/span/div/form/div/div[1]/div/input').send_keys(sheet.cell(1,8).value)
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        time.sleep(3)
        self.assertEqual(sheet.cell(1,8).value,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]/a').text,'校验新增任务是否成功')
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[10]/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="603"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(3)
        self.assertEqual(sheet.cell(1,1).value,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,'校验任务是否新增成功')
        self.assertEqual(sheet.cell(1,8).value,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[6]').text,'校验任务是否新增成功')
        print('人口管理-群防力量_人员管理：任务新增功能正常')

    def test10_qfrygl_delete_task(self):
        self.qfrygl_search()
        self.dr.find_element_by_xpath('//*[@id="idCard"]').send_keys(sheet.cell(1,1).value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, sheet.cell(1,1).value, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('//*[@id="prevDelete"]').click()
        self.dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
        time.sleep(3)
        self.assertEqual('没有找到匹配的记录',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text,'校验删除任务是否成功')
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li[10]/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="603"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(3)
        self.assertNotEqual(sheet.cell(1,1).value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,
                         '校验任务是否新增成功')
        self.assertNotEqual(sheet.cell(1,8).value, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[6]').text,
                         '校验任务是否新增成功')
        print('人口管理-群防力量_人员管理：任务删除功能正常')

    def test11_qfrygl_delete(self):
        self.qfrygl_search()
        self.dr.find_element_by_xpath('//*[@id="idCard"]').send_keys(sheet.cell(1,1).value)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, sheet.cell(1,1).value, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('人口管理-群防力量_人员管理：删除功能正常')


if __name__=='__main__':
    unittest.main()