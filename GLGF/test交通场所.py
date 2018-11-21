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
from selenium.webdriver.common.keys import Keys
import HTMLTestRunner
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

class TESTCAST_JIAOTONG(TESTCASE):


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

    def jiaotong_search(self):
        self.login(login_name, login_password)
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div/a[1]/div[2]/img[2]').click()
        time.sleep(5)
        self.assertEqual('管理防范',self.dr.find_element_by_xpath('//*[@id="currMenu"]').text, '管理防范')
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/ul/li/p[2]').click()
        self.dr.find_element_by_xpath('//*[@id="961"]').click()
        self.dr.switch_to.frame('iframeb')
        time.sleep(5)
        self.assertEqual('交通场所管理', self.dr.find_element_by_xpath('/html/body/div[1]/p').text,
                         '交通场所管理')

    def jiaotong_add(self):
        self.jiaotong_search()
        self.dr.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/a[2]').click()
        time.sleep(2)

    # def test01_jiaotong_add_esc(self):
    #     self.jiaotong_add()
    #     self.dr.find_element_by_xpath('/html/body/div[7]/div[3]/div/button[1]').click()
    #     time.sleep(1)
    #     self.assertFalse(self.dr.find_element_by_xpath('//*[@id="ui-id-1"]').text, '校验选择交通场所类型框是否关闭')
    #     print('管理防范-交通场所管理：新增时选择场所类型框的关闭按键')
    #
    # def test02_jiaotong_add_airfield(self):
    #     self.jiaotong_add()
    #     Select(self.dr.find_element_by_xpath('//*[@id="dtypeNew"]')).select_by_value('3')
    #     self.dr.find_element_by_xpath('/html/body/div[7]/div[3]/div/button[2]/span').click()
    #     global codeid_airfield
    #     codeid_airfield=self.dr.find_element_by_xpath('//*[@id="stationCode"]').get_attribute('value')
    #     add_value_airfield='拉萨贡嘎国际机场'
    #     self.dr.find_element_by_xpath('//*[@id="stationName"]').send_keys(add_value_airfield)
    #     self.dr.find_element_by_xpath('//*[@id="position"]').send_keys('西藏自治区山南市贡嘎县甲竹林镇')
    #     self.dr.find_element_by_xpath('//*[@id="passengerAvg"]').send_keys('666666')
    #     self.dr.find_element_by_xpath('//*[@id="isCheck"]').send_keys('拉萨贡嘎边检站')
    #     self.dr.find_element_by_xpath('//*[@id="describe"]').send_keys('在雅江南岸的河谷地带，北方有雅江的几个分叉河道，两边都是高山。')
    #     self.dr.find_element_by_xpath('//*[@id="risk"]').send_keys('拉萨贡嘎国际机场是世界上海拔最高的军民合用机场之一。')
    #     self.dr.find_element_by_xpath('//*[@id="timeInterval"]').send_keys('24小时')
    #     self.dr.find_element_by_xpath('//*[@id="intercom"]').send_keys('15874587458')
    #     self.dr.find_element_by_xpath('//*[@id="ctrlRoomTel"]').send_keys('13574587456')
    #     self.dr.find_element_by_xpath('//*[@id="zrdw"]').click()
    #     self.dr.find_element_by_xpath('//*[@id="treeSelect_45_span"]').click()
    #     self.dr.find_element_by_xpath('//*[@id="headName"]').send_keys('包拯')
    #     self.dr.find_element_by_xpath('//*[@id="identitycard"]').send_keys('500107198901218926')
    #     self.dr.find_element_by_xpath('//*[@id="linkWay"]').send_keys('13474587458')
    #     self.dr.find_element_by_xpath('//*[@id="saveAirport"]').click()
    #     time.sleep(3)
    #     self.dr.find_element_by_xpath('/html/body/a').click()
    #     self.dr.implicitly_wait(2)
    #     self.assertEqual(codeid_airfield,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,'校验新增、返回和默认排序')
    #     print('管理防范-交通场所管理：新增飞机场功能正常')
    #
    # def test03_jiaotong_add_trainstation(self):
    #     self.jiaotong_add()
    #     Select(self.dr.find_element_by_xpath('//*[@id="dtypeNew"]')).select_by_value('2')
    #     self.dr.find_element_by_xpath('/html/body/div[7]/div[3]/div/button[2]/span').click()
    #     global codeid_trainstation
    #     codeid_trainstation=self.dr.find_element_by_xpath('//*[@id="stationCode"]').get_attribute('value')
    #     add_value_trainstation='拉萨火车站'
    #     self.dr.find_element_by_xpath('//*[@id="stationName"]').send_keys(add_value_trainstation)
    #     self.dr.find_element_by_xpath('//*[@id="position"]').send_keys('西藏拉萨西南的柳梧新区')
    #     self.dr.find_element_by_xpath('//*[@id="passengerAvg"]').send_keys('999999')
    #     self.dr.find_element_by_xpath('//*[@id="isCheck"]').send_keys('999999')
    #     Select(self.dr.find_element_by_xpath('//*[@id="isTraffic"]')).select_by_value('1')
    #     Select(self.dr.find_element_by_xpath('//*[@id="isFreight"]')).select_by_value('1')
    #     self.dr.find_element_by_xpath('//*[@id="describe"]').send_keys(
    #         '拉萨站主站房矗立在广场南侧，依山而立。车站设计为两层斜体建筑，站房建筑面积2.36万平方米，高度22.9米。海拔3641米。')
    #     self.dr.find_element_by_xpath('//*[@id="risk"]').send_keys(
    #         '拉萨站主站房矗立在广场南侧，依山而立。车站设计为两层斜体建筑，站房建筑面积2.36万平方米，高度22.9米。海拔3641米。')
    #     self.dr.find_element_by_xpath('//*[@id="timeInterval"]').send_keys('8:30-21:30')
    #     self.dr.find_element_by_xpath('//*[@id="intercom"]').send_keys('15874587474')
    #     self.dr.find_element_by_xpath('//*[@id="ctrlRoomTel"]').send_keys('15474587458')
    #     self.dr.find_element_by_xpath('//*[@id="zrdw"]').click()
    #     time.sleep(1)
    #     self.dr.find_element_by_xpath('//*[@id="treeSelect_45_span"]').click()
    #     time.sleep(1)
    #     self.dr.find_element_by_xpath('//*[@id="headName"]').send_keys('林峰')
    #     self.dr.find_element_by_xpath('//*[@id="identitycard"]').send_keys('500107198901218926')
    #     self.dr.find_element_by_xpath('//*[@id="linkWay"]').send_keys('13474587458')
    #     self.dr.find_element_by_xpath('//*[@id="saveTrainSta"]').click()
    #     time.sleep(3)
    #     self.dr.find_element_by_xpath('/html/body/a').click()
    #     self.dr.implicitly_wait(2)
    #     self.assertEqual(codeid_trainstation, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,
    #                      '校验新增、返回和默认排序')
    #     print('管理防范-交通场所管理：新增火车站场所功能正常')

    def test04_jiaotong_add_busstation(self):
        self.jiaotong_add()
        Select(self.dr.find_element_by_xpath('//*[@id="dtypeNew"]')).select_by_value('1')
        self.dr.find_element_by_xpath('/html/body/div[7]/div[3]/div/button[2]/span').click()
        global codeid_busstation
        codeid_busstation=self.dr.find_element_by_xpath('//*[@id="stationCode"]').get_attribute('value')
        add_value_busstation='拉萨东郊客运站'
        self.dr.find_element_by_xpath('//*[@id="stationName"]').send_keys(add_value_busstation)
        self.dr.find_element_by_xpath('//*[@id="position"]').send_keys('西藏自治区拉萨市城关区江苏东路3号')
        self.dr.find_element_by_xpath('//*[@id="owerCount"]').send_keys('999999')
        self.dr.find_element_by_xpath('//*[@id="oppositeCount"]').send_keys('999999')
        Select(self.dr.find_element_by_xpath('//*[@id="ispassVehicle"]')).select_by_value('1')
        Select(self.dr.find_element_by_xpath('//*[@id="ispassNonvehicle"]')).select_by_value('1')
        self.dr.find_element_by_xpath('//*[@id="social"]').send_keys('西藏自治区拉萨市城关区江苏东路3号')
        self.dr.find_element_by_xpath('//*[@id="warsituation"]').send_keys('西藏自治区拉萨市城关区江苏东路3号')
        self.dr.find_element_by_xpath('//*[@id="risk"]').send_keys('西藏自治区拉萨市城关区江苏东路3号')
        js = "var q=document.documentElement.scrollTop=70000"
        self.dr.execute_script(js)
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="timeInterval"]').send_keys('8:30-21:30')
        self.dr.find_element_by_xpath('//*[@id="isCheck"]').send_keys('否')
        self.dr.find_element_by_xpath('//*[@id="headName"]').send_keys('马腾')
        self.dr.find_element_by_xpath('//*[@id="identitycard"]').send_keys('500107198901218926')
        self.dr.find_element_by_xpath('//*[@id="linkWay"]').send_keys('15745874574')
        self.dr.find_element_by_xpath('//*[@id="intercom"]').send_keys('15874587458')
        self.dr.find_element_by_xpath('//*[@id="zrdw"]').click()
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_span"]').click()
        self.dr.find_element_by_xpath('//*[@id="gxdw"]').click()
        self.dr.find_element_by_xpath('//*[@id="gxtreeSelect_45_span"]').click()
        self.dr.find_element_by_xpath('//*[@id="saveBusSta"]').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/a').click()
        self.dr.implicitly_wait(2)
        self.assertEqual(codeid_busstation, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text,
                             '校验新增、返回和默认排序')
        print('管理防范-交通场所管理：新增汽车站场所功能正常')

    # def test05_jiaotong_search_stationCode(self):
    #     self.jiaotong_search()
    #     self.dr.find_element_by_xpath('//*[@id="stationCode"]').send_keys(codeid_airfield)
    #     self.dr.find_element_by_xpath('//*[@id="search"]').click()
    #     self.dr.switch_to.default_content()
    #     time.sleep(2)
    #     self.dr.switch_to.frame('iframeb')
    #     paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
    #     column = 3
    #     self.pagination_num(paginal_number, codeid_airfield, column)
    #     self.dr.find_element_by_xpath('//*[@id="stationCode"]').clear()
    #     self.dr.find_element_by_xpath('//*[@id="stationCode"]').send_keys(codeid_trainstation)
    #     self.dr.find_element_by_xpath('//*[@id="search"]').click()
    #     self.dr.switch_to.default_content()
    #     time.sleep(2)
    #     self.dr.switch_to.frame('iframeb')
    #     paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
    #     column = 3
    #     self.pagination_num(paginal_number, codeid_trainstation, column)
    #     self.dr.find_element_by_xpath('//*[@id="stationCode"]').clear()
    #     self.dr.find_element_by_xpath('//*[@id="stationCode"]').send_keys(codeid_busstation)
    #     self.dr.find_element_by_xpath('//*[@id="search"]').click()
    #     self.dr.switch_to.default_content()
    #     time.sleep(2)
    #     self.dr.switch_to.frame('iframeb')
    #     paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
    #     column = 3
    #     self.pagination_num(paginal_number, codeid_busstation, column)
    #     print('管理防范-交通场所管理：编号条件查询功能正常')
    #
    # def test06_jiaotong_search_stationName(self):
    #     self.jiaotong_search()
    #     search_value_stationName='拉萨贡嘎国际机场'
    #     self.dr.find_element_by_xpath('//*[@id="stationName"]').send_keys(search_value_stationName)
    #     self.dr.find_element_by_xpath('//*[@id="search"]').click()
    #     self.dr.switch_to.default_content()
    #     time.sleep(2)
    #     self.dr.switch_to.frame('iframeb')
    #     paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
    #     column = 4
    #     self.pagination_num(paginal_number, search_value_stationName, column)
    #     print('管理防范-交通场所管理：名称条件查询功能正常')
    #
    # def test07_jiaotong_search_position(self):
    #     self.jiaotong_search()
    #     search_value_position='西藏自治区拉萨市城关区江苏东路3号'
    #     self.dr.find_element_by_xpath('//*[@id="position"]').send_keys(search_value_position)
    #     self.dr.find_element_by_xpath('//*[@id="search"]').click()
    #     self.dr.switch_to.default_content()
    #     time.sleep(2)
    #     self.dr.switch_to.frame('iframeb')
    #     paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
    #     column = 5
    #     self.pagination_num(paginal_number, search_value_position, column)
    #     print('管理防范-交通场所管理：所在地名和具体方位条件查询功能正常')
    #
    # def test08_jiaotong_search_gxdw(self):
    #     self.jiaotong_search()
    #     search_value_gxdw='山南支队'
    #     self.dr.find_element_by_xpath('//*[@id="gxdw"]').click()
    #     time.sleep(1)
    #     self.dr.find_element_by_xpath('//*[@id="gxtreeSelect_45_span"]').click()
    #     time.sleep(1)
    #     self.dr.find_element_by_xpath('//*[@id="stationName"]').click()
    #     self.dr.find_element_by_xpath('//*[@id="search"]').click()
    #     self.dr.switch_to.default_content()
    #     time.sleep(2)
    #     self.dr.switch_to.frame('iframeb')
    #     paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
    #     column = 8
    #     self.pagination_num(paginal_number, search_value_gxdw, column)
    #     print('管理防范-交通场所管理：管理单位条件查询功能正常')
    #
    # def test09_jiaotong_search_zrdw(self):
    #     self.jiaotong_search()
    #     search_value_zrdw='山南支队'
    #     self.dr.find_element_by_xpath('//*[@id="zrdw"]').click()
    #     self.dr.find_element_by_xpath('//*[@id="treeSelect_45_span"]').click()
    #     self.dr.find_element_by_xpath('//*[@id="search"]').click()
    #     self.dr.switch_to.default_content()
    #     time.sleep(2)
    #     self.dr.switch_to.frame('iframeb')
    #     paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
    #     column = 9
    #     self.pagination_num(paginal_number, search_value_zrdw, column)
    #     print('管理防范-交通场所管理：责任单位条件查询功能正常')
    #
    # def test10_jiaotong_search_headName(self):
    #     self.jiaotong_search()
    #     search_value_headName='包拯'
    #     self.dr.find_element_by_xpath('//*[@id="headName"]').send_keys(search_value_headName)
    #     self.dr.find_element_by_xpath('//*[@id="search"]').click()
    #     self.dr.switch_to.default_content()
    #     time.sleep(2)
    #     self.dr.switch_to.frame('iframeb')
    #     paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
    #     column = 10
    #     self.pagination_num(paginal_number, search_value_headName, column)
    #     print('管理防范-交通场所管理：责任人名称条件查询功能正常')
    #
    # def test10_jiaotong_search_headName(self):
    #     self.jiaotong_search()
    #     option_chioce=Select(self.dr.find_element_by_xpath('//*[@id="dtype"]'))
    #     for i in range(0,4):
    #         if i==0:
    #             print('场所类型查询条件为空时不校验数据')
    #         else:
    #             option_chioce.select_by_index(i)
    #             search_value_dtype=option_chioce.first_selected_option.text
    #             self.dr.find_element_by_xpath('//*[@id="search"]').click()
    #             self.dr.switch_to.default_content()
    #             time.sleep(2)
    #             self.dr.switch_to.frame('iframeb')
    #             paginal_number = self.dr.find_element_by_xpath(
    #                 '/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
    #             column = 12
    #             self.pagination_num(paginal_number, search_value_dtype, column)
    #     print('管理防范-交通场所管理：责任人名称条件查询功能正常')
    #
    # def test11_jiaotong_airfield_panorama(self):
    #     self.jiaotong_search()
    #     self.dr.find_element_by_xpath('//*[@id="stationCode"]').send_keys(codeid_airfield)
    #     self.dr.find_element_by_xpath('//*[@id="search"]').click()
    #     self.dr.switch_to.default_content()
    #     time.sleep(2)
    #     self.dr.switch_to.frame('iframeb')
    #     paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
    #     column = 3
    #     self.pagination_num(paginal_number, codeid_airfield, column)
    #     self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[13]/a').click()
    #     js = "var q=document.documentElement.scrollTop=100000"
    #     self.dr.execute_script(js)
    #     self.dr.find_element_by_xpath('//*[@id="qjAdd"]').click()
    #     self.dr.find_element_by_xpath('/html/body/div[5]/div[3]/div/button[1]').click()
    #     self.dr.find_element_by_xpath('//*[@id="qjAdd"]').click()
    #     time.sleep(2)
    #     self.dr.find_element_by_xpath('//*[@id="xycoordinates"]').send_keys('98.142474,24.142547')
    #     self.dr.find_element_by_xpath('//*[@id="qjpanoramaPoint"]').send_keys('南大门')
    #     self.dr.find_element_by_xpath('//*[@id="qjdescribe"]').send_keys('南大门')
    #     self.dr.find_element_by_xpath('/html/body/div[5]/div[3]/div/button[2]').click()
    #     self.dr.find_element_by_xpath('//*[@id="saveAirport"]').click()
    #     time.sleep(3)
    #     self.assertEqual('98.142474,24.142547',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text,'校验新增全景列表功能')
    #     self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
    #     self.dr.find_element_by_xpath('//*[@id="qjDelete"]').click()
    #     self.dr.find_element_by_xpath('//*[@id="saveAirport"]').click()
    #     time.sleep(3)
    #     self.assertEqual('没有找到匹配的记录',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text,'校验删除全景列表功能')
    #     print('管理防范-交通场所管理：飞机场场所新增和删除全景功能正常')
    #
    # def test12_jiaotong_airfield_flight(self):
    #     self.jiaotong_search()
    #     self.dr.find_element_by_xpath('//*[@id="stationCode"]').send_keys(codeid_airfield)
    #     self.dr.find_element_by_xpath('//*[@id="search"]').click()
    #     self.dr.switch_to.default_content()
    #     time.sleep(2)
    #     self.dr.switch_to.frame('iframeb')
    #     paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
    #     column = 3
    #     self.pagination_num(paginal_number, codeid_airfield, column)
    #     self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[13]/a').click()
    #     js = "var q=document.documentElement.scrollTop=100000"
    #     self.dr.execute_script(js)
    #     self.dr.find_element_by_xpath('//*[@id="hbAdd"]').click()
    #     self.dr.switch_to.default_content()
    #     time.sleep(3)
    #     self.dr.switch_to.frame('iframeb')
    #     self.dr.find_element_by_xpath('//*[@id="listFj"]/tbody/tr/td[2]/span/div/form/div/div[1]/div/input').click()
    #     self.dr.find_element_by_xpath('//*[@id="listFj"]/tbody/tr/td[2]/span/div/form/div/div[1]/div/input').send_keys(
    #         'MU2336')
    #     self.dr.find_element_by_xpath('//*[@id="listFj"]/tbody/tr/td[3]/span/div/form/div/div[1]/div/input').send_keys(
    #         '西藏民航')
    #     self.dr.find_element_by_xpath('//*[@id="listFj"]/tbody/tr/td[4]/span/div/form/div/div[1]/div/input').send_keys(
    #         '拉萨')
    #     self.dr.find_element_by_xpath('//*[@id="listFj"]/tbody/tr/td[5]/span/div/form/div/div[1]/div/input').send_keys(
    #         '西安')
    #     self.dr.find_element_by_xpath('//*[@id="listFj"]/tbody/tr/td[6]/span/div/form/div/div[1]/div/input').send_keys(
    #         '上海')
    #     self.dr.find_element_by_xpath('//*[@id="listFj"]/tbody/tr/td[8]/span/div/form/div/div[1]/div/input').send_keys(
    #         'T3')
    #     self.dr.find_element_by_xpath('//*[@id="listFj"]/tbody/tr/td[9]/span/div/form/div/div[1]/div/input').send_keys(
    #         '空客319')
    #     self.dr.find_element_by_xpath('//*[@id="listFj"]/tbody/tr/td[10]/span/div/form/div/div[1]/div/input').send_keys(
    #         '240')
    #     self.dr.find_element_by_xpath('//*[@id="saveAirport"]').click()
    #     time.sleep(3)
    #     self.assertEqual('MU2336',self.dr.find_element_by_xpath('//*[@id="listFj"]/tbody/tr/td[2]/a').text,'校验新增航班功能')
    #     self.dr.find_element_by_xpath('//*[@id="listFj"]/thead/tr/th[1]/div[1]/input').click()
    #     self.dr.find_element_by_xpath('//*[@id="hbDelete"]').click()
    #     self.dr.find_element_by_xpath('//*[@id="saveAirport"]').click()
    #     time.sleep(3)
    #     self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="listFj"]/tbody/tr/td').text, '校验删除全景列表功能')
    #     print('管理防范-交通场所管理：飞机场场所新增和删除航班功能正常')
    #
    # def test13_jiaotong_trainstation_panorama(self):
    #     self.jiaotong_search()
    #     self.dr.find_element_by_xpath('//*[@id="stationCode"]').send_keys(codeid_trainstation)
    #     self.dr.find_element_by_xpath('//*[@id="search"]').click()
    #     self.dr.switch_to.default_content()
    #     time.sleep(2)
    #     self.dr.switch_to.frame('iframeb')
    #     paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
    #     column = 3
    #     self.pagination_num(paginal_number, codeid_trainstation, column)
    #     self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[13]/a').click()
    #     js = "var q=document.documentElement.scrollTop=100000"
    #     self.dr.execute_script(js)
    #     self.dr.find_element_by_xpath('//*[@id="qjAdd"]').click()
    #     time.sleep(2)
    #     self.dr.find_element_by_xpath('//*[@id="xycoordinates"]').send_keys('98.142474,24.142547')
    #     self.dr.find_element_by_xpath('//*[@id="qjpanoramaPoint"]').send_keys('南大门')
    #     self.dr.find_element_by_xpath('//*[@id="qjdescribe"]').send_keys('南大门')
    #     self.dr.find_element_by_xpath('/html/body/div[5]/div[3]/div/button[2]').click()
    #     self.dr.find_element_by_xpath('//*[@id="saveTrainSta"]').click()
    #     time.sleep(3)
    #     self.assertEqual('98.142474,24.142547', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text,
    #                      '校验新增全景列表功能')
    #     self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
    #     self.dr.find_element_by_xpath('//*[@id="qjDelete"]').click()
    #     self.dr.find_element_by_xpath('//*[@id="saveTrainSta"]').click()
    #     time.sleep(3)
    #     self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除全景列表功能')
    #     print('管理防范-交通场所管理：火车站场所新增和删除全景功能正常')
    #
    # def test14_jiaotong_trainstation_trainnumber(self):
    #     self.jiaotong_search()
    #     self.dr.find_element_by_xpath('//*[@id="stationCode"]').send_keys(codeid_trainstation)
    #     self.dr.find_element_by_xpath('//*[@id="search"]').click()
    #     self.dr.switch_to.default_content()
    #     time.sleep(2)
    #     self.dr.switch_to.frame('iframeb')
    #     paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
    #     column = 3
    #     self.pagination_num(paginal_number, codeid_trainstation, column)
    #     self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[13]/a').click()
    #     js = "var q=document.documentElement.scrollTop=100000"
    #     self.dr.execute_script(js)
    #     self.dr.find_element_by_xpath('//*[@id="ccAdd"]').click()
    #     self.dr.find_element_by_xpath('//*[@id="listTrain"]/tbody/tr/td[2]/span/div/form/div/div[1]/div/input').send_keys('T221/4次')
    #     self.dr.find_element_by_xpath('//*[@id="listTrain"]/tbody/tr/td[3]/span/div/form/div/div[1]/div/input').send_keys('拉萨')
    #     self.dr.find_element_by_xpath('//*[@id="listTrain"]/tbody/tr/td[4]/span/div/form/div/div[1]/div/input').send_keys('重庆北')
    #     self.dr.find_element_by_xpath('//*[@id="listTrain"]/tbody/tr/td[6]/span/div/form/div/div[1]/div/select').click()
    #     Select(self.dr.find_element_by_xpath('//*[@id="listTrain"]/tbody/tr/td[6]/span/div/form/div/div[1]/div/select')).select_by_value('火车')
    #     self.dr.find_element_by_xpath('//*[@id="saveTrainSta"]').click()
    #     time.sleep(3)
    #     self.assertEqual('T221/4次',self.dr.find_element_by_xpath('//*[@id="listTrain"]/tbody/tr/td[2]/a').text,'校验新增车次功能')
    #     self.dr.find_element_by_xpath('//*[@id="listTrain"]/thead/tr/th[1]/div[1]/input').click()
    #     self.dr.find_element_by_xpath('//*[@id="ccDelete"]').click()
    #     self.dr.find_element_by_xpath('//*[@id="saveTrainSta"]').click()
    #     time.sleep(3)
    #     self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="listTrain"]/tbody/tr/td').text, '校验删除全景列表功能')
    #     print('管理防范-交通场所管理：火车站场所新增和删除车次功能正常')
    #
    # def test15_jiaotong_busstation_panorama(self):
    #     self.jiaotong_search()
    #     self.dr.find_element_by_xpath('//*[@id="stationCode"]').send_keys(codeid_busstation)
    #     self.dr.find_element_by_xpath('//*[@id="search"]').click()
    #     self.dr.switch_to.default_content()
    #     time.sleep(2)
    #     self.dr.switch_to.frame('iframeb')
    #     paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
    #     column = 3
    #     self.pagination_num(paginal_number, codeid_busstation, column)
    #     self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[13]/a').click()
    #     js = "var q=document.documentElement.scrollTop=100000"
    #     self.dr.execute_script(js)
    #     self.dr.find_element_by_xpath('//*[@id="qjAdd"]').click()
    #     time.sleep(2)
    #     self.dr.find_element_by_xpath('//*[@id="xycoordinates"]').send_keys('98.142474,24.142547')
    #     self.dr.find_element_by_xpath('//*[@id="qjpanoramaPoint"]').send_keys('南大门')
    #     self.dr.find_element_by_xpath('//*[@id="qjdescribe"]').send_keys('南大门')
    #     self.dr.find_element_by_xpath('/html/body/div[4]/div[3]/div/button[2]').click()
    #     self.dr.find_element_by_xpath('//*[@id="saveBusSta"]').click()
    #     time.sleep(3)
    #     self.assertEqual('98.142474,24.142547', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text,
    #                      '校验新增全景列表功能')
    #     self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
    #     self.dr.find_element_by_xpath('//*[@id="qjDelete"]').click()
    #     self.dr.find_element_by_xpath('//*[@id="saveBusSta"]').click()
    #     time.sleep(3)
    #     self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text, '校验删除全景列表功能')
    #     print('管理防范-交通场所管理：汽车站场所新增和删除全景功能正常')

    def test16_jiaotong_busstation_cars(self):
        self.jiaotong_search()
        self.dr.find_element_by_xpath('//*[@id="stationCode"]').send_keys(codeid_busstation)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        paginal_number = self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[4]/div[1]/span[1]').text
        column = 3
        self.pagination_num(paginal_number, codeid_busstation, column)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[13]/a').click()
        js = "var q=document.documentElement.scrollTop=100000"
        self.dr.execute_script(js)
        self.dr.find_element_by_xpath('//*[@id="busAdd"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame('iframeb')
        self.dr.find_element_by_xpath('//*[@id="plateNumber"]').send_keys('藏A54745')
        self.dr.find_element_by_xpath('//*[@id="motorcycleType"]').send_keys('大型客车')
        self.dr.find_element_by_xpath('//*[@id="seats"]').send_keys('45')
        self.dr.find_element_by_xpath('//*[@id="carryingCapacity"]').send_keys('2.5')
        self.dr.find_element_by_xpath('//*[@id="driver"]').send_keys('马汉')
        self.dr.find_element_by_xpath('//*[@id="driverContactWay"]').send_keys('15748745745')
        self.dr.find_element_by_xpath('//*[@id="crewMember"]').send_keys('王朝')
        self.dr.find_element_by_xpath('//*[@id="crewMemberContactWay"]').send_keys('15748747896')
        self.dr.find_element_by_xpath('//*[@id="principal"]').send_keys('包拯')
        self.dr.find_element_by_xpath('//*[@id="principalContactWay"]').send_keys('13574587458')
        self.dr.find_element_by_xpath('//*[@id="controlledCompany"]').send_keys('拉萨客运')
        self.dr.find_element_by_xpath('//*[@id="monitoringContactWay"]').send_keys('13474587452')
        js1 = "var q=document.documentElement.scrollTop=100000"
        self.dr.execute_script(js1)
        self.dr.find_element_by_xpath('//*[@id="busccAdd"]').click()
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]/span/div/form/div/div[1]/div/input').send_keys('12:45')
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]/span/div/form/div/div[1]/div/input').send_keys('14:36')
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[4]/span/div/form/div/div[1]/div/input').send_keys('18:15')
        self.dr.find_element_by_xpath('//*[@id="createTime"]').click()
        time.sleep(2)
        self.dr.delete_all_cookies()
        self.dr.find_element_by_xpath('//*[@id="busbaseForm"]/div[3]/button[1]').send_keys(Keys.ENTER)
        self.assertEqual('藏A54745',self.dr.find_element_by_xpath('//*[@id="listBus"]/tbody/tr/td[2]').text,'校验车辆新增功能')
        self.dr.find_element_by_xpath('//*[@id="listBus"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('//*[@id="busDelete"]').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]/span').click()
        time.sleep(3)
        self.assertEqual('没有找到匹配的记录',self.dr.find_element_by_xpath('//*[@id="listBus"]/tbody/tr/td').text,'校验车辆删除功能')
        print('管理防范-交通场所管理：汽车站场所新增和删除车辆功能正常')


if __name__=='__main__':
    unittest.main()