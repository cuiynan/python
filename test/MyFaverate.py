

class fi:
    def fibonacci(num):
        a, b = 1, 1
        while a < num:
            print(a)
            a, b = b, a + b

# 后期可以按Fibonacci Sequence产生的数目进行画图
fi.fibonacci(20)
