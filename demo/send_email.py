# -*- coding: utf-8 -*-

# @File    : 呵呵
# @Date    : 2020-03-29
# @Author  : derek.zhang

import time

from selenium import webdriver

driver = webdriver.Chrome()
# 访问网址
driver.get('https://mail.163.com/')
driver.maximize_window()

# 点击密码登录
driver.find_element_by_id('switchAccountLogin').click()


#切换frame
i_frame = driver.find_element_by_tag_name('iframe')
driver.switch_to.frame(i_frame)


# 用户名输入
driver.find_element_by_name('email').send_keys('zhangming002')

# 密码输入
driver.find_element(by='name',value='password').send_keys('zmkmzmkm')

# 点击登录按钮
driver.find_element_by_id('dologin').click()
time.sleep(2)

# 点击写信
driver.find_element_by_xpath('//*[@id="_mail_component_19_19"]/span[2]').click()

# 收件人
driver.find_element_by_class_name('nui-editableAddr-ipt').send_keys('923770317@qq.com')
driver.find_elements_by_class_name('nui-ipt-input')[2].send_keys('test')

# 切换frame
j_frame = driver.find_element_by_class_name('APP-editor-iframe')
driver.switch_to.frame(j_frame)

# 文本框输入
driver.find_element_by_class_name('nui-scroll').send_keys('hello!!!!')

# 返回
driver.switch_to.default_content()
driver.find_elements_by_class_name('nui-btn-text')[2].click()