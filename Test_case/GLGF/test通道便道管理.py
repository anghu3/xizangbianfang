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

class TESTCAST_TONGDAOBIANDAO(TESTCASE):


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

    def tongdaobiandong_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div/a[1]/div[2]/img[2]').click()
        time.sleep(5)
        self.assertEqual('管理防范',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '管理防范')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="957"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('通道便道列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text,
                         '通道便道管理')

    def test1_tongdaobiandao_add(self):
        self.tongdaobiandong_search()
        self.dr.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/a[2]').click()
        add_value_name='陈墉镇中尼通道'
        global codeid
        self.dr.find_element_by_xpath('//*[@id="name"]').send_keys(add_value_name)
        codeid=self.dr.find_element_by_xpath('//*[@id="code"]').get_attribute('value')
        self.dr.find_element_by_xpath('//*[@id="location"]').send_keys('陈墉镇')
        self.dr.find_element_by_xpath('//*[@id="geographicalDist"]').send_keys('陈塘位于喜马拉雅山北麓、珠穆朗玛峰东侧的原始森林地带内')
        self.dr.find_element_by_xpath('//*[@id="crossingDistChn"]').send_keys('999999')
        self.dr.find_element_by_xpath('//*[@id="crossingDistVn"]').send_keys('999999')
        Select(self.dr.find_element_by_xpath('//*[@id="ispassVehicle"]')).select_by_value('1')
        Select(self.dr.find_element_by_xpath('//*[@id="ispassNonvehicle"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="societyChn"]').send_keys('陈塘位于喜马拉雅山北麓、珠穆朗玛峰东侧的原始森林地带内，处于中尼边界我国一侧的最南边，与尼泊尔一衣带水，隔河相望。')
        self.dr.find_element_by_xpath('//*[@id="riskEvaluation"]').send_keys('陈塘位于喜马拉雅山北麓、珠穆朗玛峰东侧的原始森林地带内，处于中尼边界我国一侧的最南边，与尼泊尔一衣带水，隔河相望。')
        self.dr.find_element_by_xpath('//*[@id="importantPeriod"]').send_keys('8;30-18:00')
        self.dr.find_element_by_xpath('//*[@id="zrdw"]').click()
        self.dr.find_element_by_xpath('//*[@id="treeSelect_108_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_148_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_151_span"]').click()
        self.dr.find_element_by_xpath('//*[@id="gxdw"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="gxtreeSelect_108_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="gxtreeSelect_148_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="gxtreeSelect_151_span"]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="saveChannel"]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual('通道便道列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text,'校验返回功能')
        print('管理防范-通道便道管理：新增功能正常')

    def test2_tongdaobiandao_search_bianhao(self):
        self.tongdaobiandong_search()
        search_value_biaoham=codeid
        self.dr.find_element_by_xpath('//*[@id="code"]').send_keys(search_value_biaoham)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number,search_value_biaoham,column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(search_value_biaoham,self.dr.find_element_by_xpath('//*[@id="code"]').get_attribute('value'),'校验详情页面编号')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('通道便道列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text, '校验返回功能')
        print('管理防范-通道便道管理：编号条件查询功能正常')

    def test3_tongdaobiandao_search_name(self):
        self.tongdaobiandong_search()
        search_value_name='陈墉镇中尼通道'
        self.dr.find_element_by_xpath('//*[@id="name"]').send_keys(search_value_name)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 4
        self.pagination_num(paginal_number,search_value_name,column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(search_value_name,self.dr.find_element_by_xpath('//*[@id="name"]').get_attribute('value'),'校验详情页面名称')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('通道便道列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text, '校验返回功能')
        print('管理防范-通道便道管理：名称条件查询功能正常')

    def test4_tongdaobiandao_search_gldw(self):
        self.tongdaobiandong_search()
        search_value_gldw='扎西岗边防派出所'
        self.dr.find_element_by_xpath('//*[@id="gxdw"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="gxtreeSelect_108_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="gxtreeSelect_148_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="gxtreeSelect_151_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 5
        self.pagination_num(paginal_number,search_value_gldw,column)
        print('管理防范-通道便道管理：管理单位条件查询功能正常')

    def test5_tongdaobiandao_search_zrdw(self):
        self.tongdaobiandong_search()
        search_value_zrdw='扎西岗边防派出所'
        self.dr.find_element_by_xpath('//*[@id="zrdw"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_108_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_148_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="treeSelect_151_span"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 6
        self.pagination_num(paginal_number,search_value_zrdw,column)
        print('管理防范-通道便道管理：管理单位条件查询功能正常')

    def test6_tongdaobiandao_search_address(self):
        self.tongdaobiandong_search()
        search_value_address='陈墉镇'
        self.dr.find_element_by_xpath('//*[@id="location"]').send_keys(search_value_address)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 7
        self.pagination_num(paginal_number,search_value_address,column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        self.assertEqual(search_value_address,self.dr.find_element_by_xpath('//*[@id="location"]').get_attribute('value'),'校验详情页面所在地名和具体位置')
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual('通道便道列表', self.dr.find_element_by_xpath('/html/body/div[1]/p').text, '校验返回功能')
        print('管理防范-通道便道管理：所在地名和具体位置条件查询功能正常')

    def test7_tongdaobianhao_edit(self):
        self.tongdaobiandong_search()
        search_value_biaoham = codeid
        self.dr.find_element_by_xpath('//*[@id="code"]').send_keys(search_value_biaoham)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, search_value_biaoham, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/a').click()
        edit_value_name='陈墉镇中尼通道123'
        self.dr.find_element_by_xpath('//*[@id="name"]').clear()
        self.dr.find_element_by_xpath('//*[@id="name"]').send_keys(edit_value_name)
        self.dr.find_element_by_xpath('//*[@id="saveChannel"]').click()
        self.dr.implicitly_wait(5)
        self.dr.find_element_by_xpath('/html/body/a').click()
        time.sleep(2)
        self.assertEqual(edit_value_name,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text,'校验编辑功能是否正常')
        print('管理防范-通道便道管理：编辑功能正常')

    def test8_tongdaobiandao_delete(self):
        self.tongdaobiandong_search()
        search_value_biaohao=codeid
        self.dr.find_element_by_xpath('//*[@id="code"]').send_keys(search_value_biaohao)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number,search_value_biaohao,column)
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[2]/div[1]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/a[1]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(3)
        self.dr.switch_to.frame('iframeb')
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除是否成功')
        print('管理防范-通道便道管理：删除功能正常')

if __name__=='__main__':
    unittest.main()