import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from hospital.Hospitals import Hospital
#
from utils.ExcelUtils import ExcelUtils

url = 'https://b.qixin.com/login'
userName = 'cuiyingnan@aidoctor.cn'
password = '18612526681'

userName1 = 'tz'
password1 = '12345678'
userName2 = 'mz'
userName3 = 'juk'

userName = userName1
password = password1

# 创建浏览器对象
driver = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
driver.get(url)
time.sleep(5*60*60)

driver.find_element_by_xpath("//input[@placeholder='请输入账号']").send_keys(userName)
driver.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys(password)
driver.find_element_by_xpath("//button[@class='w-100 font-16 font-gray login-button']").click()
time.sleep(5)

#18612526681 用户进来
# driver.find_element_by_xpath(
#     "//body/div[@id='app']/div/div[@class='container-fluid page-content']/div[@class='row page-container']/div[@class='sidebar-container']/div[@class='sidebar-container-wrapper padding-b-1x']/div[@class='sidebar padding-b-2x']/ul[@class='menu el-menu']/li[2]/div[1]/span[1]").click()
# driver.find_element_by_xpath("//li[@class='el-submenu is-opened']//li[1]").click()

driver.find_element_by_xpath(
    "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/div[1]/span[1]").click()
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/ul[1]/li[1]").click()
time.sleep(2)

driver.find_element_by_xpath("//input[@placeholder='请输入关键词']").send_keys("医院")
driver.find_element_by_xpath("//button[@class='btn btn-primary btn-sm']").click()
time.sleep(3)

pageNum = 2339  # 19472 21437
pageNumber = "2339"
values = driver.find_element_by_xpath(
    "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[5]/div[1]/div[1]/span[3]/div[1]/input[1]")
values.clear()
values.send_keys(pageNumber)
driver.find_element_by_xpath(
    "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[5]/div[1]/div[1]/span[3]/div[1]/input[1]").send_keys(
    Keys.ENTER)
time.sleep(3)


# 打开页面获得社会信用代码
def oneSN(driver, hospital):
    time.sleep(2)
    # 全部窗口
    pages = driver.window_handles
    driver.switch_to_window(pages[1])
    hospital.name = driver.find_element_by_xpath(
        "//body/div[@id='app']/div/div[@class='container-fluid page-content']/div[@class='row page-container']/div[@class='content-container']/div[@class='content-container-wrapper bg-gray-lighter']/div[@class='content-container-inner']/div[@id='app-container']/div/div/div[@id='enterpriseHeader']/table[@class='table']/tr/td[@class='padding-h-1x']/div[@class='title']/span[1]").text
    hospital.address = driver.find_element_by_xpath(
        "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/section[1]/div[2]/div[1]/table[1]/tbody[1]/tr[8]/td[2]").text
    hospital.onlyCode = driver.find_element_by_xpath(
        "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/section[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[2]").text
    hospital.kind = driver.find_element_by_xpath(
        "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/section[1]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[2]").text
    driver.close()


ind = 0
for pageNum in range(3000):
    print("进行第" + str(pageNum) + "页")
    for i in range(11):
        if i == 0: continue

        hospitalAll = []
        try:
            pages = driver.window_handles
            driver.switch_to_window(pages[0])
            hospital = Hospital()
            time.sleep(5)
            driver.find_element_by_xpath(
                "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[4]/div[1]/div[" + str(
                    i) + "]/div[1]/div[3]/div[1]/div[1]/a[1]").click()
            oneSN(driver, hospital)
            # hospital.printings(0)
            hospitalAll.append(hospital)
            ExcelUtils.updateExcel('d:\\b.xls', hospitalAll, ind)
            ind += 1
        except Exception as e:
            print(e)
            pages = driver.window_handles
            if pages.__len__() > 1:
                driver.switch_to_window(pages[1])
                driver.close()
            continue

    pages = driver.window_handles
    driver.switch_to_window(pages[0])
    driver.find_element_by_xpath("//i[@class='el-icon el-icon-arrow-right']").click()
    time.sleep(2)

time.sleep(15)
driver.close()
