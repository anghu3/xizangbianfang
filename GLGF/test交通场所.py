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
        self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[2]').click()
        time.sleep(2)

    # def test1_jiaotong_add_esc(self):
    #     self.jiaotong_add()
    #     self.dr.find_element_by_xpath('/html/body/div[6]/div[3]/div/button[1]').click()
    #     time.sleep(1)
    #     self.assertFalse(self.dr.find_element_by_xpath('//*[@id="ui-id-1"]').text, '校验选择交通场所类型框是否关闭')
    #     print('管理防范-交通场所管理：新增时选择场所类型框的关闭按键')

    def test2_jiaotong_add_fjc(self):
        self.jiaotong_add()
        Select(self.dr.find_element_by_xpath('//*[@id="dtypeNew"]')).select_by_value('3')
        self.dr.find_element_by_xpath('/html/body/div[6]/div[3]/div/button[2]/span').click()
        global codeid
        codeid=self.dr.find_element_by_xpath('//*[@id="stationCode"]').get_attribute('value')
        add_value_name='拉萨贡嘎国际机场'
        self.dr.find_element_by_xpath('//*[@id="stationName"]').send_keys(add_value_name)
        self.dr.find_element_by_xpath('//*[@id="position"]').send_keys('西藏自治区山南市贡嘎县甲竹林镇')
        self.dr.find_element_by_xpath('//*[@id="passengerAvg"]').send_keys('666666')
        self.dr.find_element_by_xpath('//*[@id="isCheck"]').send_keys('拉萨贡嘎边检站')
        self.dr.find_element_by_xpath('//*[@id="describe"]').send_keys('在雅江南岸的河谷地带，北方有雅江的几个分叉河道，两边都是高山。')
        self.dr.find_element_by_xpath('//*[@id="risk"]').send_keys('拉萨贡嘎国际机场是世界上海拔最高的军民合用机场之一。')
        self.dr.find_element_by_xpath('//*[@id="timeInterval"]').send_keys('24小时')
        self.dr.find_element_by_xpath('//*[@id="intercom"]').send_keys('15874587458')
        self.dr.find_element_by_xpath('//*[@id="ctrlRoomTel"]').send_keys('13574587456')
        self.dr.find_element_by_xpath('//*[@id="zrdw"]').click()
        self.dr.find_element_by_xpath('//*[@id="treeSelect_45_span"]').click()
        self.dr.find_element_by_xpath('//*[@id="headName"]').send_keys('包拯')
        self.dr.find_element_by_xpath('//*[@id="identitycard"]').send_keys('500107198901218926')
        self.dr.find_element_by_xpath('//*[@id="linkWay"]').send_keys('13474587458')
        '''新增全景列表'''
        self.dr.find_element_by_xpath('//*[@id="qjAdd"]').click()
        self.dr.find_element_by_xpath('/html/body/div[5]/div[3]/div/button[1]').click()
        self.dr.find_element_by_xpath('//*[@id="qjAdd"]').click()
        self.dr.find_element_by_xpath('//*[@id="xycoordinates"]').send_keys('98.142474,24.142547')
        self.dr.find_element_by_xpath('//*[@id="qjpanoramaPoint"]').send_keys('南大门')
        self.dr.find_element_by_xpath('//*[@id="qjdescribe"]').send_keys('南大门')
        self.dr.find_element_by_xpath('/html/body/div[5]/div[3]/div/button[2]').click()
        '''航班管理列表'''
        self.dr.find_element_by_xpath('//*[@id="hbAdd"]')
        self.dr.switch_to.default_content()
        time.sleep(5)
        self.dr.switch_to.frame('iframeb')
        self.dr.find_element_by_xpath('//*[@id="listFj"]/tbody/tr/td[2]/span/div/form/div/div[1]/div/input').click()
        time.sleep(5)
        self.dr.find_element_by_xpath('//*[@id="listFj"]/tbody/tr/td[2]/span/div/form/div/div[1]/div/input').send_keys('MU2336')
        self.dr.find_element_by_xpath('//*[@id="listFj"]/tbody/tr/td[3]/span/div/form/div/div[1]/div/input').send_keys('西藏民航')
        self.dr.find_element_by_xpath('//*[@id="listFj"]/tbody/tr/td[4]/span/div/form/div/div[1]/div/input').send_keys('拉萨')
        self.dr.find_element_by_xpath('//*[@id="listFj"]/tbody/tr/td[5]/span/div/form/div/div[1]/div/input').send_keys('西安')
        self.dr.find_element_by_xpath('//*[@id="listFj"]/tbody/tr/td[6]/span/div/form/div/div[1]/div/input').send_keys('上海')
        self.dr.find_element_by_xpath('//*[@id="listFj"]/tbody/tr/td[8]/span/div/form/div/div[1]/div/input').send_keys('T3')
        self.dr.find_element_by_xpath('//*[@id="listFj"]/tbody/tr/td[9]/span/div/form/div/div[1]/div/input').send_keys('空客319')
        self.dr.find_element_by_xpath('//*[@id="listFj"]/tbody/tr/td[10]/span/div/form/div/div[1]/div/input').send_keys('240')
        self.dr.find_element_by_xpath('//*[@id="saveAirport"]').click()
        print('管理防范-交通场所管理：新增飞机场功能正常')


if __name__=='__main__':
    unittest.main()