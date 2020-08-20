s = lambda x, y: x + y
print(s(3, 2))

z = lambda x, y: x if x > 2 else y
print(z(3, 2))
print(z(1, 5655))

# lamda常用于排序
dic = {'z': 2, 'b': 1, 'c': 4}
a = sorted(dic.items())
b = sorted(dic.items(), reverse=True)
print(a, b)  # 原组列表
print({k: v for k, v in a})

dic = {'z': 2, 'b': 1, 'c': 4}
dic1 = sorted(dic.items(), key=lambda x: x[1])
dic2 = sorted(dic.items(), key=lambda x: x[0], reverse=True)
print({k: v for k, v in dic1})  # 原组转字典
print({k: v for k, v in dic2})  # 字典推导式

# list排序
list = [
    {'name': 'joe', 'age': 20},
    {'name': 'tom', 'age': 32},
    {'name': 'jke', 'age': 17}
]
print(list)
x = sorted(list, key=lambda x: x['age'], reverse=True)
y = sorted(list, key=lambda x: x['name'])
print(x)
print(y)
