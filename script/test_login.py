# -*- coding: utf-8 -*-

# @File    : 呵呵
# @Date    : 2020-04-07
# @Author  : derek.zhang
import time

from selenium import webdriver

from config.VarConfig import testdataPath
from module import LoginAccount
from util import Log
from util.operateExcel import OperateExcel

import util.Log



def test_login():
    '''测试登录功能'''
    try:
        # path = r"C:\Users\Administrator\Desktop\公开课资料\chromedriver_win32\chromedriver"
        # driver = webdriver.Chrome(path)
        # driver.get('https://mail.163.com')
        # driver.maximize_window()
        # LoginAccount.LoginAccount.login(driver,'zhangming002', 'zmkmzmkm')

        path = r"C:\Users\Administrator\Desktop\公开课资料\chromedriver_win32\chromedriver"

        Log.debug('开始加载测试数据')
        excel = OperateExcel()
        excel.load_workbook(testdataPath)
        excel.get_sheet_by_name('login')
        rows_nums = excel.get_rows_num()
        row1_values = excel.get_row_values(0)

        # {'用户名':'xxxx','密码':'xxxxx','是否执行':'y'}
        for i in range(1, rows_nums):

            row_values = excel.get_row_values(i)
            values = dict(zip(row1_values,row_values))
            if values['是否执行'].lower() == 'y':
                driver = webdriver.Chrome(path)
                username = values['用户名']
                password = values['密码']
                Log.debug('开始打开网页')
                driver.get('https://mail.163.com')
                driver.maximize_window()
                LoginAccount.LoginAccount.login(driver, username, password)
                time.sleep(3)
                driver.quit()

    except Exception as e:
        raise e
    finally:
        time.sleep(3)
        # driver.quit()










if __name__ =="__main__":
    test_login()

