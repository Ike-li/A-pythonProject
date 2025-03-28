def fibo_1(n):
    # 打印 n 以前的波那契数列
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b


fibo_1(100)
print()


def fibo_2(n):
    # 打印 n 个斐波那契数列
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


fibo_2(12)


print()


def fibo_3(n):
    # 递归生成斐波那契数列
    if n <= 1:
        return n

    return fibo_3(n - 1) + fibo_3(n - 2)


for i in range(12):
    print(fibo_3(i), end=" ")
