import cpca
import requests
import xlrd
from bs4 import BeautifulSoup
import re
import pandas as pd

from hospital.Hospitals import Hospital
from utils.ExcelUtils import ExcelUtils


def baidu(key, hospitalNew, hospitalBLL):
    # key = "成县妇幼保健院"
    url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=" + key + "&rsv_pq=c975914300115949&rsv_t=e7f3%2FJ8sovjmaqT%2B6p6ID4KVYbFRyG9dPQjqKtszA7eNO7jE0ynUBwuzYek&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=3&rsv_sug1=3&rsv_sug7=101&rsv_sug2=0&inputT=2503&rsv_sug4=4616&rsv_sug=2&&usm=3&rsv_idx=2&rsv_page=1"
    # 上面这行代码是在百度首页查询python关键字，将此网站赋值给url
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0"}  # 设置网站请求头
    params = {
        'kw': key
    }

    response = requests.get(url, headers=headers, params=params)  # 对网站进行get请求，并伪装成浏览器进行请求
    response.encoding = "utf-8"  # 设置网页编码格式为utf-8
    # 3、打印浏览器解析的内容
    html = response.text  # 将网页源代码的文本文件赋值给html
    content = response.content  # 将网页源代码的二进制文件赋值给content
    print(html)  # 打印网页源代码的文本文件
    print(content)  # 打印二进制源码文件
    print("response.status_code:", response.status_code)  # 打印状态码，结果为200时表示请求成功
    print("headers:", response.headers)  # 打印网页的头部headers信息
    soup = BeautifulSoup(html, "lxml")
    # 4、打印查找到的标题信息
    print(soup.findAll("h3"))  # 经查实所有的标题信息在h3标签里，故打印h3标签的内容
    list1 = []
    hospital = Hospital()
    hospital.onlyCode = key
    try:
        searchName = soup.findAll("h3")[0].text.replace("_百度地图", "").strip()
        searchAddress = soup.select(".op-map-singlepoint-info-right")[0].text
        print(searchName, searchAddress)
        hospital.name = searchName

        hospital.address = searchAddress
        if len(hospital.address) > 6:
            df = cpca.transform([hospital.address], cut=False)
            hospital.code = hospital.address
            hospital.name = hospital.name
            hospital.oldName = df.iat[0, 2]
            hospital.privince = df.iat[0, 0]
            hospital.city = df.iat[0, 1]
            hospital.address = df.iat[0, 3]
        else:
            hospital.code = hospital.address
            hospital.name = hospital.name
            hospital.oldName = ''
            hospital.privince = ''
            hospital.city = ''
            hospital.address = hospital.address
        if (hospital.name.find('检验') != -1):
            hospital.type = '检验中心'
        elif (hospital.name.find('妇幼') != -1):
            hospital.type = '妇幼'
        elif (hospital.name.find('儿童') != -1):
            hospital.type = '儿童'
        else:
            hospital.type = '医院'
        hospital.level = ""
        hospitalNew.append(hospital)
    except:
        hospital.code = ""
        hospital.name = key
        hospital.oldName = ""
        hospital.privince = ""
        hospital.city = ""
        hospital.address = ""
        hospital.type = ""
        hospital.kind = ""
        hospital.level = ""
        hospital.onlyCode = ""
        hospitalBLL.append(hospital)
        print("eerrrorrr")
    # for title in soup.findAll("h3"):  # 遍历h3标签里的title内容
    #     print(title.text)


# 加载全部爬下来的医院
def loadCommonExcel(hospitalALL, path, code, name, addr, kind):
    data = xlrd.open_workbook(path)
    print(data.sheet_names())
    table = data.sheet_by_name(data.sheet_names()[0])
    row = table.nrows
    for i in range(row):
        hospital = Hospital()
        hospital.code = table.cell(i, code).value
        hospital.name = table.cell(i, name).value.strip()
        hospitalALL.append(hospital)


hospitalALL = []
hospitalBLL = []
loadCommonExcel(hospitalALL, 'E:\\work-doc\\项目\\DMS\DOC\\试用阶段遇到问题\\客户抓取对比\\hl-all\\b匹配基础含下方EXCEL\\b.xls', 0, 1, -1, -1)
i = 0
m = 0
n = 0
for hospital in hospitalALL:
    hospitalNew = []
    key = hospital.name
    baidu(key, hospitalNew, hospitalBLL)
    if len(hospitalNew) > 0:
        ExcelUtils.updateExcel('d:\\a.xls', hospitalNew, m)
        m += 1
    elif len(hospitalBLL) > 0:
        ExcelUtils.updateExcel('d:\\b.xls', hospitalBLL,n)
        n += 1
    i += 1
