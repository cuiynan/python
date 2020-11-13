# 与 ChinaArea.py 配对使用
import os

import xlwt


# 定义的区域对象
class Area:
    code = ""
    name = ""
    parentCode = "CHN"
    parentName = "中国"
    type = "省"

    def printing(self):
        print(self.code + "		" + self.name + "    " + self.parentCode + "    " + self.parentName + "    " + self.type)

