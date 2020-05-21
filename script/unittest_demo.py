# -*- coding: utf-8 -*-

# @File    : 呵呵
# @Date    : 2020-04-13
# @Author  : derek.zhang

import unittest
import time

from selenium import webdriver

from config.VarConfig import testdataPath
from module import LoginAccount
from util.operateExcel import OperateExcel


class Login_Test(unittest.TestCase):


    def setUp(self):
        self.path = r"C:\Users\Administrator\Desktop\公开课资料\chromedriver_win32\chromedriver"

        self.excel = OperateExcel()
        self.excel.load_workbook(testdataPath)
        self.excel.get_sheet_by_name('login')



    def tearDown(self):
        pass

    def test_02(self):
        self.assertIn('1','123')


    def test_01(self):
        rows_nums =self.excel.get_rows_num()
        row1_values = self.excel.get_row_values(0)
        try:
            for i in range(1, rows_nums):
                row_values = self.excel.get_row_values(i)
                values = dict(zip(row1_values, row_values))
                if values['是否执行'].lower() == 'y':
                    driver = webdriver.Chrome(self.path)
                    username = values['用户名']
                    password = values['密码']

                    driver.get('https://mail.163.com')
                    driver.maximize_window()
                    LoginAccount.LoginAccount.login(driver, username, password)
                    time.sleep(5)

                    self.assertIn(username, driver.page_source)
                    driver.quit()

        except Exception as e:
            raise e

        finally:
            time.sleep(3)

if __name__ == "__main__":
    unittest.main()


