# -*- coding: utf-8 -*-

# @File    : 呵呵
# @Date    : 2020-03-30
# @Author  : derek.zhang
import time

from util.find_element import find_element

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://mail.163.com/')
driver.maximize_window()

# driver.find_element_by_id("switchAccountLogin").click()
# # driver.switch_to.frame("x-URS-iframe1585316015217.1082")
# iframe = driver.find_element_by_tag_name('iframe')
# driver.switch_to.frame(iframe)
# driver.find_element_by_name('email').send_keys('zhangming002')
# driver.find_element_by_name('password').send_keys('zmkmzmkm')
# driver.find_element_by_id("dologin").click()

find_element(driver, 'id', 'switchAccountLogin').click()
iframe = find_element(driver,'tag name', 'iframe')
driver.switch_to.frame(iframe)

find_element(driver, 'name', 'email').send_keys('zhangming002')
find_element(driver, 'name', 'password').send_keys('zmkmzmkm')
find_element(driver, 'id', 'dologin').click()


#page object PO
# 一个页面，看做事一个类，我们通过对象提供的API,找到元素，

# 自动化脚本分成三层
# 1. 对象层  用于存放页面元素定位和 控件操作
# 2. 逻辑层  封装一些常用的功能模块，登录功能
# 3. 业务层  真正的测试用例操作部分















time.sleep(3)
# 写信
driver.find_element_by_xpath('//*[@id="_mail_component_19_19"]/span[1]/b').click()
time.sleep(2)

# 收件人
driver.find_element_by_class_name('nui-editableAddr-ipt').send_keys('923770317@qq.com')
# 主题
driver.find_elements_by_class_name('nui-ipt-input')[2].send_keys('test')

#切换frame
i_frame = driver.find_element_by_class_name('APP-editor-iframe')
driver.switch_to.frame(i_frame)
# 输入文本
driver.find_element_by_class_name('nui-scroll').send_keys('hahahaha')

# 发送
# driver.switch_to.default_content()
driver.find_element_by_id('_mail_icon_42_215').click()