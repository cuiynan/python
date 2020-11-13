import importlib  # 提供import语句
import sys
import time  # 提供延时功能
import xlrd  # excel文件读取
import os
import xlwt  # excel文件写入

from xlutils.copy import copy  # excel文件复制
from selenium import webdriver  # 浏览器操作库

importlib.reload(sys)

# 伪装成浏览器，防止被识破
option = webdriver.ChromeOptions()
option.add_argument(
    '--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"')
driver = webdriver.Chrome(options=option)

# 打开登录页面
driver.get('https://www.qichacha.com/user_login')
time.sleep(20)  # 等待20s，完成手动登录操作
# 手动登录操作
txt = '海淀妇幼保健院'
# 向搜索框注入文字
driver.find_element_by_id('searchkey').send_keys(txt)
# 单击搜索按钮
srh_btn = driver.find_element_by_xpath('//*[@id="indexSearchForm"]/div/span/input')
srh_btn.click()
try:
    # 获取网页地址，进入
    inner = driver.find_element_by_xpath('//*[@id="search-result"]/tr[1]/td[3]/a').get_attribute("href")
    driver.get(inner)
    time.sleep(2)
    # 弹出框按钮
    try:
        try:
            srh_btn = driver.find_element_by_xpath('//*[@id="firstepdadModal"]/div/div/div[2]/button')
            srh_btn.click()
        except:
            srh_btn = driver.find_element_by_xpath('//*[@id="firstcaseModal"]/div/div/div[2]/button')
            srh_btn.click()
    except:
        pass
    try:
        # 转到企业发展
        tag = driver.find_element_by_xpath('//*[@id="report_title"]')
        tag.click()
        time.sleep(2)
        # 获取首个企业信用码
        try:
            credit_code = driver.find_element_by_xpath('//*[@id="0"]/table[1]/tbody/tr[1]/td[4]').text
        except:
            credit_code = 'none'
    except:
        credit_code = 'none'
except:
    credit_code = 'none'
print(credit_code)
