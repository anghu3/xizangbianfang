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
    dir_file = os.getcwd()
    case_dir = dir_file + r'\..\Test_case\CLGL\\'
    discover=unittest.defaultTestLoader.discover(case_dir,pattern='test*.py',top_level_dir=None)
    print(discover)
    return discover

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    dir_report = os.getcwd()
    report_path = dir_report + r'\..\report\\' + now+ '拉萨边防-车辆管理自动化测试报告.html'
    fp = open(report_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='拉萨边防-车辆管理自动化测试报告', description='用例执行情况：')
    runner.run(allcase())
    fp.close()