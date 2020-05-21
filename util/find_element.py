# -*- coding: utf-8 -*-

# @File    : 呵呵
# @Date    : 2020-04-01
# @Author  : derek.zhang

from selenium.webdriver.support.ui import WebDriverWait


# def find_element(driver, find_type, value):
#     element = driver.find_element(by=find_type, value=value)
#     print(type(element))
#     return element

def find_element(driver, find_type, value):
    try:
        element = WebDriverWait(driver,20).until(lambda driver: driver.find_element(by=find_type, value=value))
        return element
    except Exception as e:
        raise e








if __name__ =="__main__":
    from selenium import webdriver

    path = r"C:\Users\Administrator\Desktop\公开课资料\chromedriver_win32\chromedriver"
    driver = webdriver.Chrome(path)
    driver.get('https://mail.163.com/')
    driver.maximize_window()

    find_element(driver,'id', 'switchAccountLogin').click()