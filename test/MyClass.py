

# while True:
#     x = input("please enter num:")
#     print(x)
#     x = int(x)
#     if x == 8:
#         print("haha")
#         print("haha zhong")
#     else:
#         print("wo x")

# import os
# print(os.getenv("java_home"))

# import zlib
# s = b"dkfja;kljf;alksdjf;lakdjf;lkadj13241234123j4k123j4k123j4fl;kasjdfasdf"
# print(len(s))
# t = zlib.compress(s)
# print(len(t))
# print(zlib.decompress(t))

# for key in {"name":"cui","age":11}:
#     print(key)

# 置后实现
# class T:
#     pass
#
# x = T
# x.name = "dfaf"
# x.age = 11
# print(x)

# class Test:
#     """Here is test"""
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
# z = Test(1, 2)
# print(z)
#
# class Dog:
#     kind = 'canine'
#     t = []
#     def __init__(self,name):
#         self.name = name
#         self.t.append(name)
#
#
# d = Dog("fido")
# e = Dog("shirlly")
# print(e.t)
#
# print(d.kind)
# print(d.name)
# print(e.kind)
# print(e.name)


# class b:
#     __c = "sfadf"
#     def __init__(self,name):
#         self.name = name
#     def click(self):
#         print("..adf.adf" + self.name)
#
# x = b("aaaaaaaaaaaaaa")
# # print(x.c)
# print(x._b.__c)


class Father:
    def hello(self):
        print("father")
class Son(Father):
    def hello(self):
        print("son")

s = Son();
s.hello()