from chinaArea.MyClass import Area
from utils.ExcelUtils import ExcelUtils

area = Area()
allArea = []

area.parentCode = "CHN"
area.parentName = "中国"
area.type = "省"
allArea.append(area)
ExcelUtils().writeExcel("d:\\xx.xls", allArea)
