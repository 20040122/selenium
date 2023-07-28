from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("http://127.0.0.1/")
driver.maximize_window()
driver.find_element_by_xpath("//a[text()='登录']").click() # 点击登录按钮
time.sleep(2)
driver.find_element_by_xpath("//input[@id='username']").send_keys(13555985732)# 用户名输入框
time.sleep(2)
driver.find_element_by_xpath("//input[@id='password']").send_keys(123456)# 密码输入框
time.sleep(2)
driver.find_element_by_xpath("//input[@id='verify_code']").send_keys(8888)# 验证码输入框
time.sleep(2)
driver.find_element_by_xpath("//a[@name='sbtbutton']").click() # 点击登录按钮
