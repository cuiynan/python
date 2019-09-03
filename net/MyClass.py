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
            sheet.write(index, 0, area.code)
            sheet.write(index, 1, area.name)
            sheet.write(index, 2, area.parentCode)
            sheet.write(index, 3, area.parentName)
            sheet.write(index, 4, area.type)
            index += 1
        os.remove(fileName)
        workbook.save(fileName)
