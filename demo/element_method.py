# -*- coding: utf-8 -*-

# @File    : 呵呵
# @Date    : 2020-03-24
# @Author  : derek.zhang
import time

from selenium import webdriver

driver = webdriver.Chrome()
# 访问网址
driver.get('https://mail.qq.com/')
time.sleep(2)
# driver.get('https://mail.163.com/')
# time.sleep(2)
# # 后退
# driver.back()
# time.sleep(2)
# # 前进
# driver.forward()
# 网页的title
# print(driver.title)
# print('*******************************************')
# # 当前网址
# print(driver.current_url)
# print('*******************************************')
# # 页面源代码
# print(driver.page_source)

# 窗口的最大化
# driver.maximize_window()
# 窗口句柄 --窗口的标识
# now_handle = driver.current_window_handle
# # print(type(now_handle))
# print(now_handle)
# driver.find_element_by_id('kw').send_keys('米兰')
# time.sleep(2)
# driver.find_element_by_id('su').click()
# time.sleep(2)
# driver.find_element_by_partial_link_text('百度百科').click()
# time.sleep(3)
#
# all_handles = driver.window_handles
# print(len(all_handles))
# print(type(all_handles))
# print(all_handles)
# # 切换窗口
# driver.switch_to.window(now_handle)
# time.sleep(3)
# driver.switch_to.window(all_handles[-1])

# driver.find_element_by_id('kw').send_keys('米兰')
# time.sleep(3)
# 情况
# driver.find_element_by_id('kw').clear()
# 获取文本内容
# print(driver.find_element_by_partial_link_text('肺炎').text)
# 获取属性
# print(element.get_attribute('id'))
# element = driver.find_element_by_partial_link_text('肺炎')
# print(element.is_displayed())
# print(element.is_enabled())

driver.maximize_window()
time.sleep(2)

# 鼠标悬停
# from selenium.webdriver.common.action_chains import ActionChains
# ActionChains(driver).move_to_element(driver.find_element_by_link_text('设置')).perform()
# driver.find_element_by_link_text('搜索设置').click()

# 下拉框的操作
# 直接定位

# driver.find_element_by_xpath('//*[@id="nr"]/option[2]').click()

# Select
# from selenium.webdriver.support.select import Select
# select_element = driver.find_element_by_name('NR')
# Select(select_element).select_by_index(2)
# time.sleep(2)
# Select(select_element).select_by_value("20")
# time.sleep(2)
# Select(select_element).select_by_visible_text("每页显示10条")

#

# Frame 切换
driver.switch_to.frame("login_frame")
driver.find_element_by_id('u').send_keys('123')
time.sleep(2)
driver.switch_to.default_content()
driver.find_element_by_link_text('基本版').click()