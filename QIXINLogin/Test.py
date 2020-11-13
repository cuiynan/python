import time
from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
driver.get("https://www.baidu.com")

driver.execute_script("window.open('https://news.163.com')")

pages = driver.window_handles
print(pages)
driver.switch_to_window(pages[0])
time.sleep(2)

