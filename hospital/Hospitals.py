class Hospital:
    code = ""
    name = ""
    oldName = ""
    privince = ""
    city = ""
    address = ""
    type = ""
    kind = ""
    level = ""
    onlyCode = ""

    def print(self):
        print(
            self.code + "    " + self.name + "    " + self.oldName + "    " + self.privince + "    " +
            self.city + self.address + "    " + self.type + "    " + self.kind + "    " + self.level + "    " + self.onlyCode)


