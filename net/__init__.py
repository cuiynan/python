from net.MyClass import ExcelUtils, Area

area = Area()
allArea = []

area.parentCode = "CHN"
area.parentName = "中国"
area.type = "省"
allArea.append(area)
ExcelUtils().writeExcel("d:\\xx.xls",allArea)