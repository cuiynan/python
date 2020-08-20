# 临时对比A表，不作为通用
# 所有A-a B-a表排重后放入 医院基本信息表a
import xlrd

from hospital.Hospitals import Hospital


# 加载ab-b
from utils.ExcelUtils import ExcelUtils

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
        hospital = Hospital()
        if (code != -1):
            hospital.code = table.cell(i, code).value
        hospital.name = table.cell(i, name).value.strip()
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

loadCommonExcel(hospitalALL, 'E:\\work-doc\\项目\\DMS\DOC\\试用阶段遇到问题\\客户抓取对比\\hl-all\\b匹配基础含下方EXCEL\\a.xls',0,1,5,-1)
loadCommonExcel(hospitalB, 'E:\\work-doc\\项目\\DMS\DOC\\试用阶段遇到问题\\客户抓取对比\\hl-all\\aa.xls',0,1,6,8)
hospitalAllTA.extend(hospitalALL)
doWork(hospitalALL, hospitalB, hospitalTA, hospitalTB)  # 中3
hospitalAllTA.extend(hospitalTB)
print("基础库总数：" + str(hospitalAllTA.__len__()))

ExcelUtils.writeExcelHospital('d:\\a.xls', hospitalAllTA)