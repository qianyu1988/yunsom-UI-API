# -*- coding: utf-8 -*-

# @File    : 呵呵
# @Date    : 2020-04-13
# @Author  : derek.zhang
import unittest
import time

from config.VarConfig import reportPath
from lib import HTMLTestRunner
from script.unittest_demo import Login_Test
from script.wirte import Demo

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Login_Test('test_01'))
    # suite.addTest(Login_Test('test_02'))
    # suite.addTest(Demo('test_01'))

    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    fb = open(reportPath + now + '_report.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fb, title='测试报告', description='测试')
    runner.run(suite)
    fb.close()

