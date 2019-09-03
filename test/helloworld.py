# class Test:
#     a = 1;

from numpy import *
a = array([1,1,1])
b = array([1,1,1])
print(a * b)

# a = [1,2,3]
# b = [1,2,3]
# c = [3,2,1]
#
# for x in zip(a,b,c):
#     print(x * 2)

# 局部变更
# def scope_test():
#     def do_local():
#         spam = "local spam"
#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"
#     def do_global():
#         global spam
#         spam = "global spam"
#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)
#
# scope_test()
# print("In global scope:", spam)



# from MyFaverate import *
#
# dir  fibonacci

# with open("d:/a.txt") as file:
#     for f in file:
#         print(f)
#
# # 预处理
# for line in open("d:/a.txt"):
#     print(line)

# 异常处理
# try:
#     if 1==1:
#         raise ValueError("xxx")
# except ValueError:
#     print("sdfa")

# print('hello\'s world')
#
# for x in range(0,10,2):
#     print(x)

# def a(a,L=[]):
#     L.append(a)
#     print(L)
#     return L
#
#
# a(1)
# a(3)

#
# a = [1,2,3]
# b = [1,2,4]
# if a < b:
#     print('yes')


# string1, string2, string3 = '1', '0', '1'
# print(string1 or string2 and string3)
# print(string1 < string2 == string3)

# questions = ['name', 'quest', 'favorite color']
# answers = ['cc', '111', 'red']
#
# for q, a in zip(questions, answers):
#     print('what\'s you {}? It is {}.'.format(q,a))

s = ['za','b','c']
# for x in reversed(s):
#     print(x)
#
# print(s)
# r = reversed(s)
# for x in r:
#     print(x)

# s.sort()
# print(s)


# from collections import deque
# q = deque(s)
# q.append('sdfas')
# q.append('sdfa12341234s')
# q.appendleft("1")
# print(q)
#
# a = range(100)
# print(a)