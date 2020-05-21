# -*- coding: utf-8 -*-

# @File    : 呵呵
# @Date    : 2020-04-07
# @Author  : derek.zhang
from selenium import webdriver

from objects.LoginPage import LoginPage


class LoginAccount():

    def __init__(self):
        print('----开始登录啦----')

    @staticmethod
    def login(driver, username, password):
        '''登录功能'''
        try:
            login_page = LoginPage(driver)
            login_page.switch_accountlogin()
            login_page.switch_frame()
            login_page.input_username(username)
            login_page.input_passpord(password)
            login_page.click_login()
        except Exception as e:
            raise e


if __name__ == "__main__":
    path = r"C:\Users\Administrator\Desktop\公开课资料\chromedriver_win32\chromedriver"
    driver = webdriver.Chrome(path)
    driver.get('https://mail.163.com')
    driver.maximize_window()


    LoginAccount.login(driver, 'zhangming002', 'zmkmzmkm')
