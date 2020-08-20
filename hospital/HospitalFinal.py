# 较正医院等级、类型等
import xlrd

from hospital.Builder import buildModel
from hospital.Hospitals import Hospital
# 加载ab-b
from utils.ExcelUtils import ExcelUtils


def loadCommonExcel(hospitalALL, path, code, name, addr, kind):
    data = xlrd.open_workbook(path)
    print(data.sheet_names())
    table = data.sheet_by_name(data.sheet_names()[0])
    row = table.nrows
    for i in range(row):
        hospital = Hospital()
        if (code != -1):
            hospital.code = table.cell(i, code).value
        hospital.name = table.cell(i, name).value.strip()
        if (addr != -1):
            hospital.address = table.cell(i, addr).value.strip()
        hospital.type = '医院'
        if (kind != -1):
            hospital.kind = table.cell(i, kind).value.strip()
        hospitalALL.append(hospital)


hospitall = []
loadCommonExcel(hospitall, 'E:\\work-doc\\项目\\DMS\DOC\\试用阶段遇到问题\\客户抓取对比\\hl-all\\b匹配基础含下方EXCEL\\a.xls', 0, 1, 4, -1)
print(len(hospitall))

hospitalA = []
hospitalB = []
hospitalBLL= []
i = 0
for h in hospitall:
    print(i)
    if i < 13260:
        i += 1
        continue
    h.print()
    buildModel(h, hospitalA, hospitalB)
    hospitalBLL.append(hospitalB)
    ExcelUtils.updateExcel('d:\\a.xls', hospitalA, i-13260)
    hospitalA.clear()
    i += 1

ExcelUtils.writeExcelHospital('d:\\b.xls', hospitalBLL)
