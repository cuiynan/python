class Hospital:
    code = ""
    name = ""
    oldName = ""
    privince = ""
    city = ""
    address = ""
    area = ""
    type = ""
    kind = ""
    level = ""
    onlyCode = ""

    def printings(self, num):
        print(
            "0" +
            "	" + self.code + "	" + self.name + "	" + self.address + "	" + self.privince + "	" +
            self.city + "	" + self.area + "	" + self.oldName + "	" + self.kind + "	" + self.type + "	" + self.level + "	" + self.onlyCode + "	" + str(
                num))
