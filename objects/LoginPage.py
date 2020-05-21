# -*- coding: utf-8 -*-

# @File    : 呵呵
# @Date    : 2020-04-07
# @Author  : derek.zhang
from util import Log
from util.configparse import ConfigFileParse
from util.find_element import find_element


class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.parse = ConfigFileParse()

    def switch_accountlogin(self):
        '''切换登录方式'''
        # find_element(self.driver, 'id', 'switchAccountLogin').click()
        # Log.debug('切换登录方式')
        login_type, value = self.parse.getOptionValue('163mail_login','login_page.switchbutton').split(":")
        find_element(self.driver, login_type, value).click()

    def switch_frame(self):
        '''切换frame'''
        # i_frame = find_element(self.driver, 'tag name', 'iframe')
        # Log.debug('切换frame')
        login_type, value = self.parse.getOptionValue('163mail_login', 'login_page.frame').split(":")
        i_frame = find_element(self.driver, login_type, value)
        self.driver.switch_to.frame(i_frame)

    def input_username(self, username):
        '''输入用户名'''
        # find_element(self.driver, 'name', 'email').send_keys(username)
        login_type, value = self.parse.getOptionValue('163mail_login', 'login_page.username').split(":")
        find_element(self.driver, login_type, value).send_keys(username)

    def input_passpord(self, password):
        '''输入密码'''
        # find_element(self.driver, 'name', 'password').send_keys(password)
        login_type, value = self.parse.getOptionValue('163mail_login', 'login_page.password').split(":")
        find_element(self.driver, login_type, value).send_keys(password)


    def click_login(self):
        '''点击登录按钮'''
        # find_element(self.driver, 'id', 'dologin').click()
        login_type, value = self.parse.getOptionValue('163mail_login', 'login_page.loginbutton').split(":")
        find_element(self.driver, login_type, value).click()


if __name__ == "__main__":
    from selenium import webdriver

    path = r"C:\Users\Administrator\Desktop\公开课资料\chromedriver_win32\chromedriver"
    driver = webdriver.Chrome(path)
    driver.get('https://mail.163.com/')
    driver.maximize_window()

    login_page = LoginPage(driver)
    login_page.switch_accountlogin()
    login_page.switch_frame()
    login_page.input_username('zhangming')
    login_page.input_passpord('zmkmzmkm')
    login_page.click_login()
