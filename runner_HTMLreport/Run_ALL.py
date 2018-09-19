# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 14:11:17 2018

@author: PCCC
"""
import unittest
import os
import HTMLTestRunner
import time

def allcase():
    case_dir_rk=r'F:\pythonkeys\自动化测试\lasa\ALL'
    discover=unittest.defaultTestLoader.discover(case_dir_rk,pattern='test*.py',top_level_dir=None)
    return discover

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_path = '../report/' + now + '拉萨边防自动化测试报告.html'
    fp = open(report_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='拉萨边防自动化测试报告', description='用例执行情况：')
    runner.run(allcase())
    fp.close()