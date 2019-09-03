# 说明：
#     本类主要是爬中华人民共和国民政部 县级以上区域
# 来源:
# version: 2019年7月中华人民共和国县以上行政区划代码
# url: http://www.mca.gov.cn/article/sj/xzqh/2019/

# 2019年8月27日
import requests
from bs4 import BeautifulSoup

from net.MyClass import Area, ExcelUtils


def addOther(allArea):
    # 澳门
    area = Area()
    area.parentCode = "820100"
    area.parentName = "澳门特别行政区"
    area.type = "区"
    area.code = "820101"
    area.name = "澳门特别行政区"
    allArea.append(area)
    # 香港区
    area = Area()
    area.parentCode = "810100"
    area.parentName = "香港特别行政区"
    area.type = "区"
    area.code = "810101"
    area.name = "香港特别行政区"
    allArea.append(area)
    # 台湾
    area = Area()
    area.parentCode = "710000"
    area.parentName = "台湾省"
    area.type = "市"
    area.code = "710100"
    area.name = "台湾省"
    allArea.append(area)
    area = Area()
    area.parentCode = "710100"
    area.parentName = "台湾省"
    area.type = "市"
    area.code = "710101"
    area.name = "台湾省"
    allArea.append(area)


url = "http://www.mca.gov.cn/article/sj/xzqh/2019/201908/201908271607.html"
html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")
table = soup.select("body table")[0]

cityCode = 0
cityName = ""
provinceCode = 0
provinceName = ""
allArea = []
# 组装
try:
    for tr in table.findAll("tr"):
        area = Area()
        td = tr.findAll("td")
        spans = td[2].findAll("span")
        txt1 = td[1].text
        txt2 = td[2].text
        if (len(txt1) == 0):
            continue
        tdClass = td[1].attrs['class'][0]

        if (len(spans) > 0):
            if (tdClass == 'xl7010750'):
                # 市
                area.parentCode = provinceCode
                area.parentName = provinceName
                area.type = "市"
                area.code = txt1
                area.name = txt2

                cityCode = txt1
                cityName = txt2
            elif (tdClass == 'xl7110750'):
                # 说明是县或区
                area.parentCode = cityCode
                area.parentName = cityName
                if (txt2.find("区") == -1):
                    area.type = "县"
                else:
                    area.type = "区"
                area.code = txt1
                area.name = txt2
        else:
            # 父集
            if (txt2.find("省") > -1):
                provinceCode = int(txt1)
                provinceName = txt2
                area.parentCode = "CHN"
                area.parentName = "中国"
                area.type = "省"
                area.code = txt1
                area.name = txt2
            else:
                # 为解决三级联动新增省
                area.parentCode = "CHN"
                area.parentName = "中国"
                area.type = "省"
                area.code = txt1
                area.name = txt2
                allArea.append(area)
                provinceCode = int(txt1)
                provinceName = txt2
                # 直辖市
                area = Area()
                area.parentCode = provinceCode
                area.parentName = provinceName
                area.type = "市"
                cityCode = provinceCode + 100
                area.code = cityCode
                area.name = txt2
                cityName = txt2
        allArea.append(area)
except IndexError as e:
    print(e)

addOther(allArea)
# 打印输出
# for area in allArea:
#     area.printing()
ExcelUtils().writeExcel("区域.xls", allArea)
