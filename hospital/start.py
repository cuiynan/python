import xlrd

# 读EXCEL
from hospital import Builder
from hospital.Hospitals import Hospital

# data = xlrd.open_workbook('直销医院（数据准确）A部分.xlsx')
from utils.ExcelUtils import ExcelUtils

data = xlrd.open_workbook('分配单医院（数据待清洗）B部分.xlsx')
# data = xlrd.open_workbook('TMP.xlsx')
print(data.sheet_names())
table = data.sheet_by_name("Sheet1")
row = table.nrows
col = table.ncols

allHospital = []
hospitalA = []
hospitalB = []

# for i in range(row):
#     hos = Hospital()
#     hos.code = table.cell(i, 0).value
#     hos.name = table.cell(i, 1).value
#     allHospital.append(hos)

# -------bbb----
for i in range(row):
    hos = Hospital()
    hos.name = table.cell(i, 0).value
    allHospital.append(hos)

for i in allHospital:
    if i.name == '购货单位' or i.name == '医院':
        continue
    i.print()
    Builder.buildModel(i, hospitalA, hospitalB)

# 爬对应的信息 并组装数据，2部分
print('aaaa')
for A in hospitalA:
    A.print()
print('bbbb')
for A in hospitalB:
    A.print()
# 写EXCEL
ExcelUtils.writeExcelHospital('d:\\a.xls', hospitalA)
ExcelUtils.writeExcelHospital('d:\\b.xls', hospitalB)
