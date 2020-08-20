import cpca
import requests
from bs4 import BeautifulSoup


def buildModel(hospital, hospitalA, hospitalB):
    url = "http://www.yixue.com/"
    url += hospital.name
    # print(url)

    # if hospital.name == '深圳市第二人民医院' or hospital.name == '白求恩国际和平医院' or hospital.name == '广州市妇女儿童医疗中心' or hospital.name == '沈阳市妇婴医院' or hospital.name == '南方医科大学' or hospital.name == '和静县人民医院' or hospital.name == '成都市第三人民医院' or hospital.name == '泸州医学院' or hospital.name == '包头市中心医院':
    #     hospitalB.append(hospital)
    #     return

    headers = {'User-Agent':
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}
    html = requests.get(url, headers).text
    soup = BeautifulSoup(html, "html.parser")
    if (soup.text.__contains__('本页面目前没有内容。')):
        hospitalB = hospital
        return
    try:
        hospital.onlyCode = '-'
        # hospital.name = soup.select('#firstHeading')[0].text
        hospital.address = soup.select('div div div div div div ul li')[0].contents[1].replace('：', '').replace('\n', '')
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

        hospital.level = soup.select('div div div div div div ul li')[2].contents[2].contents[0]
        if (hospital.name.find('检验') != -1):
            hospital.type = '检验中心'
        elif (hospital.name.find('妇幼') != -1):
            hospital.type = '妇幼'
        elif (hospital.name.find('儿童') != -1):
            hospital.type = '儿童'
        else:
            hospital.type = '医院'
        hospital.kind = soup.select('div div div div div div ul li')[3].contents[2].contents[0]

        # hospital.print()
        hospitalA.append(hospital)
    except IndexError:
        hospitalB.append(hospital)

# a = "北京市东城区大木仓胡同41号"
# df = cpca.transform([a], cut=True)
# print(df.iat[0, 0])
# print(df.iat[0, 1])
# print(df.iat[0, 2])
# print(df.iat[0, 3])
