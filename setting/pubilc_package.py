# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 14:11:17 2018

@author: PCCC
"""

import unittest
import re
import time
import xlrd

'''---------------------------------------------脚本基本配置信息-------------------------------------'''

# url='http://192.168.110.65:8081/login'
url='http://192.168.110.198:8081/login'
# url='http://192.168.110.69:8081/login'
# url='http://192.168.110.62:8081/login'
login_name='admin'
login_password='xxhc26330'
login_name_test='test'
login_password_test='xxhc26330'
login_password_test2='xxhc26333'

'''-------------------------------------------目录配置--------------------------------------------------'''
xlsfile=r'F:\pythonkeys\自动化测试\lasa\menu.xlsx'
excel_menu=xlrd.open_workbook(xlsfile)
sheet_menu=excel_menu.sheet_by_name('menu')
sheet_setting=excel_menu.sheet_by_name('setting')
sheet_prompt_message=excel_menu.sheet_by_name('prompt message')
search = sheet_setting.col_values(2, 1, 2)[0]
reset = sheet_setting.col_values(3, 1, 2)[0]
currMenupath = sheet_setting.col_values(0, 1, 2)[0]
page_title = sheet_setting.col_values(1, 1, 2)[0]
goback = sheet_setting.col_values(5, 1, 2)[0]
saveBtn = sheet_setting.col_values(6, 1, 2)[0]

'''---------------------------------------------------------------------------------------------------'''

'''-------------------------------------------公共函数-----------------------------------------------'''
def findnum(string):
    comp = re.compile('-?[1-9]\d*')
    list_str = comp.findall(string)
    list_num = []
    for item in list_str:
        item = int(item)
        list_num.append(item)
    # print(list_num)
    return list_num

'''---------------------------------------------------------------------------------------------------'''

class TESTCASE(unittest.TestCase):

    '''
    查询功能数据校验：hl-胡亮
    paginal_number：“显示第 1 到第 2 条记录，总共 2 条记录”；运用findnum函数取出数据条数
    search_value：查询值，传入函数是为了做查询功能正常与否的校验
    column：校验数据在表单中的列数
    '''
    def pagination_num(self,paginal_number,search_value,column):
        number = findnum(paginal_number)[-1]
        tens = int(number / 10)
        # print(tens)
        single = int(number % 10)
        # print(single)
        if tens == 0:
            for j in range(1, single + 1):
                xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
        if tens == 1:
            if single==0:
                for j in range(1,11):
                    xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                    self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
            else:
                for j in range(1,11):
                    xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                    self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
                page = '/html/body/div[3]/div[2]/div/div[4]/div[2]/ul/li[' + str(tens + 3) + ']/a'
                # page=  '/html/body/div[4]/div[2]/div/div[4]/div[2]/ul/li['+str(tens+3)+']/a'
                self.dr.find_element_by_xpath(page).click()
                time.sleep(2)
                if single == 0:
                    print(single)
                else:
                    for j in range(1, single + 1):
                        xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                        self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
        if 1< tens < 7:
            for i in range(1, tens + 2):
                if single==0:
                    if i < tens + 1:
                        for j in range(1, 11):
                            xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                            self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
                        time.sleep(1)
                        page = '/html/body/div[3]/div[2]/div/div[4]/div[2]/ul/li[' + str(tens + 2) + ']/a'
                        self.dr.find_element_by_xpath(page).click()
                        time.sleep(1)
                    if i == tens + 1:
                        for j in range(1, single + 1):
                            if single == 0:
                                print(single)
                            else:
                                for j in range(1, single + 1):
                                    xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                                    self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
                                    time.sleep(1)
                else:
                    if i < tens + 1:
                        for j in range(1, 11):
                            xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                            self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
                        time.sleep(1)
                        page = '/html/body/div[3]/div[2]/div/div[4]/div[2]/ul/li[' + str(tens + 3) + ']/a'
                        self.dr.find_element_by_xpath(page).click()
                        time.sleep(1)
                    if i == tens + 1:
                        for j in range(1, single + 1):
                            if single == 0:
                                print(single)
                            else:
                                for j in range(1, single + 1):
                                    xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                                    self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
        if tens >= 7:
            for i in range(1, tens + 2):
                if i < tens + 1:
                    for j in range(1, 11):
                        xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                        self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
                        time.sleep(1)
                    self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[2]/ul/li[9]/a').click()
                    time.sleep(3)
                if i == tens + 1:
                    for j in range(1, single + 1):
                        if single == 0:
                            print(single)
                        else:
                            for j in range(1, single + 1):
                                xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                                self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
                                # time.sleep(1)

    '''
        油料数量查询：hl-胡亮
        paginal_number：“显示第 1 到第 2 条记录，总共 2 条记录”；运用findnum函数取出数据条数
        search_value：查询值，传入函数是为了做查询功能正常与否的校验
        column：校验数据在表单中的列数
    '''

    def Getdata_Contrast(self,paginal_number,search_value,column):
        number = findnum(paginal_number)[-1]
        tens = int(number / 10)
        single = int(number % 10)
        less_num=[]
        more_num=[]
        if tens == 0:
            for j in range(1, single + 1):
                xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                if search_value<=self.dr.find_element_by_xpath(xpath).text:
                    less_num.append(self.dr.find_element_by_xpath(xpath).text)
                elif search_value>self.dr.find_element_by_xpath(xpath).text:
                    more_num.append(self.dr.find_element_by_xpath(xpath).text)
            print(less_num)
            print(more_num)
            self.assertIn(search_value,less_num,'校验数据小于查询数目')
        if tens == 1:
            for j in range(1, 11):
                xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                if search_value<=self.dr.find_element_by_xpath(xpath).text:
                    less_num.append(self.dr.find_element_by_xpath(xpath).text)
                elif search_value>self.dr.find_element_by_xpath(xpath).text:
                    more_num.append(self.dr.find_element_by_xpath(xpath).text)
            page='/html/body/div[3]/div[2]/div/div[4]/div[2]/ul/li['+str(tens+3)+']/a'
            self.dr.find_element_by_xpath(page).click()
            time.sleep(2)
            if single == 0:
                print(single)
            else:
                for j in range(1, single + 1):
                    xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                    if search_value <= self.dr.find_element_by_xpath(xpath).text:
                        less_num.append(self.dr.find_element_by_xpath(xpath).text)
                    elif search_value > self.dr.find_element_by_xpath(xpath).text:
                        more_num.append(self.dr.find_element_by_xpath(xpath).text)
            print(less_num)
            print(more_num)
            self.assertIn(search_value,less_num,'校验数据小于查询数目')
        if 1< tens < 7:
            for i in range(1, tens + 2):
                if i < tens + 1:
                    for j in range(1, 11):
                        xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                        if search_value <= self.dr.find_element_by_xpath(xpath).text:
                            less_num.append(self.dr.find_element_by_xpath(xpath).text)
                        elif search_value > self.dr.find_element_by_xpath(xpath).text:
                            more_num.append(self.dr.find_element_by_xpath(xpath).text)
                    page = '/html/body/div[3]/div[2]/div[1]/div/div[4]/div[2]/ul/li[' + str(tens + 3) + ']/a'
                    self.dr.find_element_by_xpath(page).click()
                if i == tens + 1:
                    for j in range(1, single + 1):
                        if single == 0:
                            print(single)
                        else:
                            for j in range(1, single + 1):
                                xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                                if search_value <= self.dr.find_element_by_xpath(xpath).text:
                                    less_num.append(self.dr.find_element_by_xpath(xpath).text)
                                elif search_value > self.dr.find_element_by_xpath(xpath).text:
                                    more_num.append(self.dr.find_element_by_xpath(xpath).text)
            print(less_num)
            print(more_num)
            self.assertIn(search_value, less_num, '校验数据小于查询数目')
        if tens > 7:
            for i in range(1, tens + 2):
                if i < tens + 1:
                    for j in range(1, 11):
                        xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                        if search_value <= self.dr.find_element_by_xpath(xpath).text:
                            less_num.append(self.dr.find_element_by_xpath(xpath).text)
                        elif search_value > self.dr.find_element_by_xpath(xpath).text:
                            more_num.append(self.dr.find_element_by_xpath(xpath).text)
                    self.dr.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[2]/ul/li[9]/a').click()
                    time.sleep(2)
                if i == tens + 1:
                    for j in range(1, single + 1):
                        if single == 0:
                            print(single)
                        else:
                            for j in range(1, single + 1):
                                xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                                if search_value <= self.dr.find_element_by_xpath(xpath).text:
                                    less_num.append(self.dr.find_element_by_xpath(xpath).text)
                                elif search_value > self.dr.find_element_by_xpath(xpath).text:
                                    more_num.append(self.dr.find_element_by_xpath(xpath).text)
            print(less_num)
            print(more_num)
            self.assertIn(search_value, less_num, '校验数据小于查询数目')
