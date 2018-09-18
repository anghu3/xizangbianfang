#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import requests
import bs4
import json
import mainutils
import pymysql
db=pymysql.connect('localhost','root','1234567','django',charset='utf8' )
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql = """CREATE TABLE EMPLOYEE (
         NAME  CHAR(20) NOT NULL,
         PASSWORD  CHAR(20),
          )"""
# sql1 = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
cursor.execute(sql)
try:
    cursor.execute(sql1)
    db.commit()
except:
    db.rollback()

db.close()



# def dic2sql(dic,sql):
#     sf=''
#     for key in dic:
#         tup = (key,dic[key])
#         sf += (str(tup) + ',')
#         print(tup)
#     sf+=sf.rstrip(',')
#     sql2=sql%sf
#     print(sql2)
#     return sql2
#
# if __name__=='__main__':
#     dic={'张三':'123456','李四':'xx254125'}
#     sql = "insert into users (name ,password) VALUES %s;"
#     ret = dic2sql(dic, sql)
#     print(ret)
#     db = pymysql.connect('localhost', 'root', '1234567', 'django', charset='utf8')
#     cursor = db.cursor()
#     cursor.execute(ret)
#     db.commit()
#     db.close()