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
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

class TESTCAST_ZHIQINDIAN(TESTCASE):


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

    def zhiqindian_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath(sheet_menu.col_values(1,41,42)[0]).click()
        time.sleep(5)
        self.assertEqual('管理防范',self.dr.find_element_by_xpath(currMenupath).text, '管理防范')
        self.dr.find_element_by_xpath(sheet_menu.col_values(3,41,42)[0]).click()
        self.dr.find_element_by_xpath(sheet_menu.col_values(5,41,42)[0]).click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('执勤点列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text,
                         '执勤点管理')

    def test01_zhiqindian_add(self):
        self.zhiqindian_search()
        self.dr.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/a[2]').click()
        add_value_name='色拉崩坚执勤任务'
        self.dr.find_element_by_xpath('//*[@id="name"]').send_keys(add_value_name)
        global codeid
        codeid=self.dr.find_element_by_xpath('//*[@id="code"]').get_attribute('value')
        self.dr.find_element_by_xpath('//*[@id="location"]').send_keys('拉萨市城关区色拉路1号')
        self.dr.find_element_by_xpath('//*[@id="dailyCheckCount"]').send_keys('999999')
        self.dr.find_element_by_xpath('//*[@id="importantPeriod"]').send_keys('00:00-06:00')
        self.dr.find_element_by_xpath('//*[@id="entryExitPurpose"]').send_keys('拉萨公安民(辅)警彻夜维持秩序，为朝佛民众提供安全有序便利服务。')
        Select(self.dr.find_element_by_xpath('//*[@id="ispassVehicle"]')).select_by_value('1')
        Select(self.dr.find_element_by_xpath('//*[@id="ispassNonvehicle"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="societyChn"]').send_keys('据了解，由于活动持续时间长，沿线设立了12处便民服务点，配置了60辆免费公交车。')
        self.dr.find_element_by_xpath('//*[@id="malitarySocietyVn"]').send_keys('据了解，由于活动持续时间长，沿线设立了12处便民服务点，配置了60辆免费公交车。')
        self.dr.find_element_by_xpath('//*[@id="riskEvaluation"]').send_keys('设立了医疗救护点，为朝佛民众及时提供紧急救助等便利服务。')
        self.dr.find_element_by_xpath('//*[@id="headName"]').send_keys('包涵')
        self.dr.find_element_by_xpath('//*[@id="headIdCard"]').send_keys('500107198901218926')
        self.dr.find_element_by_xpath('//*[@id="contact"]').send_keys('15874748569')
        self.dr.find_element_by_xpath('//*[@id="dutyTel"]').send_keys('13474587458')
        self.dr.find_element_by_xpath('//*[@id="isHaveCensorate"]').send_keys('未')
        self.dr.find_element_by_xpath('//*[@id="zrdw"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_46_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="gxdw"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="gxtreeSelect_45_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="gxtreeSelect_46_span"]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="saveDuty"]').click()
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame('iframeb')
        time.sleep(1)
        self.assertEqual(sheet_prompt_message.col_values(1, 4, 5)[0],
                         self.dr.find_element_by_xpath('//*[@id="gritter-item-1"]/div[2]/div[2]/p').text, '新增成功提示信息校验')
        print('管理防范-执勤点管理：新增功能正常')

    def test02_zhiqindian_search_codeid(self):
        self.zhiqindian_search()
        search_value_codeid=codeid
        # print(search_value_codeid)
        self.dr.find_element_by_xpath('//*[@id="code"]').send_keys(search_value_codeid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_codeid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        self.assertEqual(search_value_codeid,self.dr.find_element_by_xpath('//*[@id="code"]').get_attribute('value'),'校验详情页面的编号')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_codeid, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,'校验返回功能和默认排序')
        print('管理防范-执勤点管理：编号查询功能正常')

    def test03_zhiqindian_search_name(self):
        self.zhiqindian_search()
        search_value_name='色拉崩坚执勤任务'
        self.dr.find_element_by_xpath('//*[@id="name"]').send_keys(search_value_name)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number, search_value_name, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        self.assertEqual(search_value_name,self.dr.find_element_by_xpath('//*[@id="name"]').get_attribute('value'),'校验详情页面名称')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_name, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,'校验返回功能和默认排序')
        print('管理防范-执勤点管理：名称查询功能正常')

    def test04_zhiqindian_search_address(self):
        self.zhiqindian_search()
        search_value_address='拉萨市城关区色拉路1号'
        self.dr.find_element_by_xpath('//*[@id="location"]').send_keys(search_value_address)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number, search_value_address, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        self.assertEqual(search_value_address,self.dr.find_element_by_xpath('//*[@id="location"]').get_attribute('value'),'校验详情页面所在名称和具体方位')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_address, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[5]').text,'校验返回功能和默认排序')
        print('管理防范-执勤点管理：所在名称和具体方位查询功能正常')

    def test05_zhiqindian_search_headName(self):
        self.zhiqindian_search()
        search_value_headName='包涵'
        self.dr.find_element_by_xpath('//*[@id="headName"]').send_keys(search_value_headName)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 8
        self.pagination_num(paginal_number, search_value_headName, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        self.assertEqual(search_value_headName,self.dr.find_element_by_xpath('//*[@id="headName"]').get_attribute('value'),'校验详情页面责任人姓名')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(search_value_headName, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[8]').text,'校验返回功能和默认排序')
        print('管理防范-执勤点管理：责任人姓名查询功能正常')

    def test06_zhiqindian_search_gldw(self):
        self.zhiqindian_search()
        search_value_gldw='错那边防大队'
        self.dr.find_element_by_xpath('//*[@id="gxdw"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="gxtreeSelect_45_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="gxtreeSelect_46_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 9
        self.pagination_num(paginal_number, search_value_gldw, column)
        print('管理防范-执勤点管理：管理单位查询功能正常')

    def test07_zhiqindian_search_zrdw(self):
        self.zhiqindian_search()
        search_value_zrdw='错那边防大队'
        self.dr.find_element_by_xpath('//*[@id="zrdw"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_46_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 10
        self.pagination_num(paginal_number, search_value_zrdw, column)
        print('管理防范-执勤点管理：责任单位查询功能正常')

    def test08_zhiqindian_edit(self):
        self.zhiqindian_search()
        search_value_codeid=codeid
        # print(search_value_codeid)
        self.dr.find_element_by_xpath('//*[@id="code"]').send_keys(search_value_codeid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_codeid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[12]/a').click()
        edit_value_name='色拉崩坚执勤123'
        self.dr.find_element_by_xpath('//*[@id="name"]').clear()
        self.dr.find_element_by_xpath('//*[@id="name"]').send_keys(edit_value_name)
        self.dr.find_element_by_xpath('//*[@id="saveDuty"]').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual(edit_value_name, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,'校验返回功能和默认排序')
        print('管理防范-执勤点管理：编辑功能正常')

    def test09_zhiqindian_delete(self):
        self.zhiqindian_search()
        search_value_codeid=codeid
        # print(search_value_codeid)
        self.dr.find_element_by_xpath('//*[@id="code"]').send_keys(search_value_codeid)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_codeid, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('管理防范-执勤点管理：删除功能正常')

if __name__=='__main__':
    unittest.main()