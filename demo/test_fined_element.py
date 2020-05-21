# -*- coding: utf-8 -*-

# @File    : 呵呵
# @Date    : 2020-03-18
# @Author  : derek.zhang

# 1.selenium 1.0  javascript
# 2.selenium 2.0  -- selenium1.0+webdriver
# 3.selenium 3.0 优化

# 1. 通过id 来查找
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
# driver.find_element_by_id('kw').send_keys('haha')
# driver.find_element(by='id',value='kw').send_keys('haha')

# 2.通过name
# driver.find_element_by_name('wd').send_keys('haha')
# driver.find_element(by='name',value='wd').send_keys('haha')
# driver.find_elements_by_name('wd')
# driver.find_elements(by='name',value='wd')

# 3. 通过classname
# driver.find_element_by_class_name('s_ipt').send_keys('haha')
# driver.find_element(by='class name',value='s_ipt').send_keys('haha')
# driver.find_elements_by_class_name('s_ipt')
# driver.find_elements(by='class name',value='s_ipt')

# link_text
# driver.find_element_by_link_text('新闻').click()
# driver.find_element(by='link text',value='新闻').click()

# 通过partial_link_text
# driver.find_element_by_partial_link_text('抗击').click()
# driver.find_element(by='partial link text',value='肺炎').click()

# xpath
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('haha')
# driver.find_element(by='xpath', value='//*[@id="kw"]').send_keys('haha')

# css_selector
# driver.find_element_by_css_selector('#kw').send_keys('haha')
# driver.find_element(by='css selector', value='#kw').send_keys('haha')

# tag name
