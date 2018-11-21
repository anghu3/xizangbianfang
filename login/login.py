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
import sys
from public_package.pubilc_package import url,login_name,login_name_test,login_password,login_password_test
'''
用例名称：
用例编号：
用例场景：
用例作者：
'''

class TESTCAST_LOGIN(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()

    def tearDown(self):
        print("脚本执行完成")
        self.dr.quit()

    def login(self, username, password):
        self.dr.get(url)
        self.dr.find_element_by_id('vv').send_keys(username)
        self.dr.find_element_by_xpath('//*[@id="login_ff"]/div[2]/input').send_keys(password)
        self.dr.find_element_by_xpath('//*[@id="login_ff"]/a').click()

    def test1_login_success(self):
        self.login(login_name, login_password)
        self.assertEqual('用户：管理员',self.dr.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[3]/div[1]').text,'登录成功')
        print('登录测试-登录成功-admin')

    def test2_login_pwd_error(self):
        self.login(login_name, '83849898')
        self.assertEqual(self.dr.find_element_by_xpath('//*[@id="login_ff"]/div[3]/span').text, '用户名或密码错误','用户名或密码错误')
        print('登录测试-密码错误-admin')

    def test3_login_pwd_null(self):
        self.login(login_name, '')
        self.assertEqual(self.dr.find_element_by_xpath('//*[@id="login_ff"]/div[3]/span').text, '用户名或密码错误','用户名或密码错误')
        print('登录测试-密码为空-amdin')

    def test4_login_user_null(self):
        self.login('', login_password)
        self.assertEqual(self.dr.find_element_by_xpath('//*[@id="login_ff"]/div[3]/span').text, '用户名或密码错误','用户名或密码错误')
        print('登录测试-用户名为空-admin')

    def test5_login_success(self):
        self.login(login_name_test,login_password_test)
        self.assertEqual('用户：test',self.dr.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[3]/div[1]').text,'登录成功')
        print('登录测试-登录成功-test')


if __name__=='__main__':
    unittest.main()