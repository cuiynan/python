import xlrd

from hospital.Builder import buildModel
from hospital.Hospitals import Hospital
# 加载ab-b
from utils.ExcelUtils import ExcelUtils
from utils.mysql import mysql, selectOne

host = "58.87.88.74"
userName = "root"
passWord = "Zhuoyuew@killhacker*94@"
dbName = "dms_bh"


def loadCommonExcel(hospitalALL, path):

    data = xlrd.open_workbook(path)
    print(data.sheet_names())
    table = data.sheet_by_name(data.sheet_names()[0])
    row = table.nrows
    for i in range(row):
        if i == 0:
            continue
        hospital = Hospital()
        hospital.oldName = table.cell(i, 0).value.strip()
        hospital.name = table.cell(i, 2).value.strip()
        hospital.privince = table.cell(i, 4).value
        hospital.city = table.cell(i, 5).value
        # 区
        hospital.area = table.cell(i, 3).value
        hospital.address = table.cell(i, 6).value
        hospital.kind = table.cell(i, 7).value
        hospital.level = table.cell(i, 9).value

        if (hospital.name.find('检验') != -1):
            hospital.type = '检验中心'
        elif (hospital.name.find('妇幼') != -1):
            hospital.type = '妇幼'
        elif (hospital.name.find('儿童') != -1):
            hospital.type = '儿童'
        else:
            hospital.type = '综合'

        hospitalALL[hospital.name] = hospital
       # hospitalALL.append(hospital)


def selectarea(province):
    sql = "SELECT LEFT(CODE,2) FROM b_region WHERE NAME = '" + province + "' AND TYPE=  '省'"
    data = selectOne(host, userName, passWord, dbName, sql)
    return data


def initMap(map):
    sql = "SELECT NAME FROM b_region WHERE   TYPE=  '省'"
    data = mysql(host, userName, passWord, dbName, sql)
    for i in data:
        map[i] = 1


hospitalALL = {}
loadCommonExcel(hospitalALL, 'C:\\Users\\cuiyingnan\\Desktop\\lastVersion.xls')

map = {}
initMap(map)
# for i in map:
#     print(i)
#     print(map[i])

for h in hospitalALL:
    code = ""
    for i in map:
        hos = hospitalALL[h]
        if hos.privince == i[0]:
            # print(map[i])
            area = selectarea(hos.privince)
            if hos.name.find('检测') != -1 or hos.name.find('检测') != -1:
                code += "JC"
            else:
                code += "HP"
            code += area[0]
            code += str(map[i]).zfill(4)
            hos.code = code
            hos.printings(map[i])
            map[i] = map[i] + 1
            break
