# 临时，不作为通用
import xlrd

from hospital.Hospitals import Hospital


# 加载ab-b
from utils.ExcelUtils import ExcelUtils


def loadB(hospitalB):
    data = xlrd.open_workbook('E:\\work-doc\\项目\\DMS\DOC\\试用阶段遇到问题\\客户抓取对比\\ab-b.xls')
    print(data.sheet_names())
    table = data.sheet_by_name(data.sheet_names()[0])
    row = table.nrows
    for i in range(row):
        hospital = Hospital()
        hospital.code = table.cell(i, 0).value.strip()
        hospital.name = table.cell(i, 1).value.strip()
        hospitalB.append(hospital)



def compared(hospitalALL, hospitalB, hospitalTA, hospitalTB):
    for b in hospitalB:
        flag = True
        for hospital in hospitalALL:
            if (hospital.name.strip() == b.name.strip()):
                hospitalTA.append(hospital)
                flag = False
                continue
        if (flag):
            hospitalTB.append(b)


# 加载全部爬下来的医院
def loadCommonExcel(hospitalALL, path, code, name, addr, kind):
    data = xlrd.open_workbook(path)
    print(data.sheet_names())
    table = data.sheet_by_name(data.sheet_names()[0])
    row = table.nrows
    for i in range(row):
        if (len(table.cell(i, addr).value.strip()) < 7):
            continue
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


def doWork(hospitalALL, hospitalB, hospitalTA, hospitalTB):
    hospitalTA.clear()
    hospitalTB.clear()
    print("基础库:" + str(hospitalALL.__len__()), "匹配前B总共：" + str(hospitalB.__len__()))
    compared(hospitalALL, hospitalB, hospitalTA, hospitalTB)
    print("A中：" + str(hospitalTA.__len__()) + "  B不中：" + str(hospitalTB.__len__()))


hospitalA = []
hospitalB = []
hospitalALL = []
# 暂无匹配中的
hospitalAllTA = []
hospitalTA = []
hospitalTB = []

loadB(hospitalB)
loadCommonExcel(hospitalALL, 'E:\\work-doc\\项目\\DMS\DOC\\试用阶段遇到问题\\客户抓取对比\\initall.xls', 0, 1, 5, -1)
hospitalAllTA.extend(hospitalALL)
doWork(hospitalALL, hospitalB, hospitalTA, hospitalTB)  # 中3
print("基础库总数：" + str(hospitalAllTA.__len__()))

hospitalALL.clear()
hospitalB = hospitalTB.copy()
loadCommonExcel(hospitalALL, 'E:\\work-doc\\项目\\DMS\DOC\\试用阶段遇到问题\\客户抓取对比\\hl-all\\全国医院名录excel版(17341).xls', -1, 1, 2,
                6)
doWork(hospitalALL, hospitalB, hospitalTA, hospitalTB)  # 中11
hospitalAllTA.extend(hospitalTA)
print("基础库总条数：" + str(hospitalAllTA.__len__()))

hospitalALL.clear()
hospitalB = hospitalTB.copy()
loadCommonExcel(hospitalALL, 'E:\\work-doc\\项目\\DMS\DOC\\试用阶段遇到问题\\客户抓取对比\\hl-all\\全国二甲医院和地址名单.xls', -1, 0, 1, 2)
doWork(hospitalALL, hospitalB, hospitalTA, hospitalTB)  # 中1
hospitalAllTA.extend(hospitalTA)
print("基础库总条数：" + str(hospitalAllTA.__len__()))

hospitalALL.clear()
hospitalB = hospitalTB.copy()
loadCommonExcel(hospitalALL, 'E:\\work-doc\\项目\\DMS\DOC\\试用阶段遇到问题\\客户抓取对比\\hl-all\\客户2020-5-19.xls', 0, 1, 2, -1)
doWork(hospitalALL, hospitalB, hospitalTA, hospitalTB)  # 中
hospitalAllTA.extend(hospitalTA)
print("基础库总条数：" + str(hospitalAllTA.__len__()))


hospitalALL.clear()
hospitalB = hospitalTB.copy()
loadCommonExcel(hospitalALL, 'E:\\work-doc\\项目\\DMS\DOC\\试用阶段遇到问题\\客户抓取对比\\hl-all\\K31客户.xls', 0, 1, 2, -1)
doWork(hospitalALL, hospitalB, hospitalTA, hospitalTB)  # 中
hospitalAllTA.extend(hospitalTA)
print("基础库总条数：" + str(hospitalAllTA.__len__()))
print("最后还剩条数：" + str(hospitalTB.__len__()))

ExcelUtils.writeExcelHospital('d:\\a.xls', hospitalAllTA)
ExcelUtils.writeExcelHospital('d:\\b.xls', hospitalTB)