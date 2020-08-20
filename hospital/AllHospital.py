# 按省份获得全部医院列表

import requests
from bs4 import BeautifulSoup

from hospital.Hospitals import Hospital
from utils.ExcelUtils import ExcelUtils


def buildModel(province, allHospital):
    url = "http://www.yixue.com/" + province + "医院列表"
    print(url)

    headers = {'User-Agent':
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}
    html = requests.get(url, headers).text
    soup = BeautifulSoup(html, "html.parser")
    try:
        num = soup.select('#mw-content-text ul li b a').__len__()
        for i in range(num):
            hospital = Hospital()
            hospital.name = soup.select('#mw-content-text ul li b a')[i].contents[0]
            hospital.address = soup.select('#mw-content-text ul li ul')[i].contents[0].contents[1].replace('：',
                                                                                                           '').replace(
                '\n', '')
            hospital.level = soup.select('#mw-content-text ul li ul')[i].contents[2].contents[1].replace('：',
                                                                                                         '').replace(
                '\n', '')
            hospital.type = '医院'
            hospital.kind = ''
            allHospital.append(hospital)

            hospital.print()
    except IndexError:
        hospital.print()


allHospital = []
provinces = ['北京市', '天津市', '河北省', '山西省', '内蒙古自治区', '辽宁省', '吉林省', '黑龙江省', '上海市', '江苏省', '浙江省', '安徽省', '福建省', '江西省',
             '山东省', '河南省', '湖北省', '湖南省', '广东省', '广西壮族自治区', '海南省', '重庆市', '四川省', '贵州省', '云南省', '西藏自治区', '陕西省', '甘肃省',
             '青海省', '宁夏回族自治区', '新疆维吾尔自治区', '台湾省', '香港特别行政区', '澳门特别行政区']
for i in provinces:
    buildModel(i, allHospital)
    # buildModel('天津市', allHospital)

ExcelUtils.writeExcelHospital('d:\\all.xls', allHospital)

