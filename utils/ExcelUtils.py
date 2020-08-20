import os

import xlrd
import xlwt
from xlutils.copy import copy
import gc


# EXCEL操作类
class ExcelUtils:

    @classmethod
    def writeExcel(self, fileName, AreaList):
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet("sheet1", cell_overwrite_ok=True)
        index = 0
        for area in AreaList:
            sheet.write(index, 0, str(area.code))
            sheet.write(index, 1, area.name)
            sheet.write(index, 2, str(area.parentCode))
            sheet.write(index, 3, area.parentName)
            sheet.write(index, 4, area.type)
            index += 1
        print("正在删除" + fileName)
        os.remove(fileName)
        print("正在创建" + fileName)
        workbook.save(fileName)
        print("创建完成")

    @classmethod
    def updateExcel(self, fileName, hospitalList, index):
        rb = xlrd.open_workbook(fileName)
        wb = copy(rb)  # 利用xlutils.copy下的copy函数复制
        sheet = wb.get_sheet(0)
        for hospital in hospitalList:
            sheet.write(index, 0, hospital.code)
            sheet.write(index, 1, hospital.name)
            sheet.write(index, 2, hospital.oldName)
            sheet.write(index, 3, hospital.privince)
            sheet.write(index, 4, hospital.city)
            sheet.write(index, 5, hospital.address)
            sheet.write(index, 6, hospital.type)
            sheet.write(index, 7, hospital.kind)
            sheet.write(index, 8, hospital.level)
            sheet.write(index, 9, hospital.onlyCode)
            wb.save(fileName)
        del sheet, wb, rb
        gc.collect()
