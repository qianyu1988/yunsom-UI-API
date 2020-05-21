# -*- coding: utf-8 -*-

# @File    : 呵呵
# @Date    : 2020-04-10
# @Author  : derek.zhang

import os

#  /Users/liuyan/Documents/config/VarConfig.py
parentPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 定位方式配置文件
loacationPath = os.path.join(parentPath, u'config\location.ini')

# 测试数据文件
testdataPath = os.path.join(parentPath, u'testdata\mail.xlsx')

#logging 配置文件
loggingConfigPath = os.path.join(parentPath, u'config\LogConfig.ini')

# 测试报告地址
reportPath = os.path.join(parentPath, u'report\\')

print(reportPath)