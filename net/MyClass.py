import os

import xlwt


class Area:
    code = ""
    name = ""
    parentCode = "CHN"
    parentName = "中国"
    type = "省"

    def printing(self):
        print(self.code + "    " + self.name + "    " + self.parentCode + "    " + self.parentName + "    " + self.type)


class ExcelUtils:
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
