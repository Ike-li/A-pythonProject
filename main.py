# s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#
# # 每隔2个字母取一个
# print(s[::3])  # 输出: ADGJMPSVY
#
# # 从索引1开始，每隔3个字母取一个
# print(s[1::4])  # 输出: BFJNRVZ
#
# # 反向每隔1个字母取一个
# print(s[::-2])  # 输出: ZXVTQOMKIGECA
#
# s1 = "北 上 广 深"
# ls1 = s1.split(" ")
# print(ls1)  # 输出: ['北', '上', '广', '深']
# print(",".join(ls1))
# print(s1.replace(" ", ","))  # 输出: 北京深圳

# print(1 and 2)
# print(1 or 2)

# s1 = "ZXVTQOMKIGECA"
# s2 = "123"
# print(s1 + s2)  # 输出: ZXVTQOMKIGECA123
# # 把 s1 转换为列表
# ls1 = list(s1)
# ls2 = list(s2)
# print(ls1 + ls2)
# print(ls1)
# print(ls1[::-2])


# l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print([j for i in l for j in i])

# s = "ABCDEFGHIAAABBBRRRR"
# print(set(s))  # 输出: {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'R'}
# print({i: s.count(i) for i in set(s)})
# print({i: s.count(i) for i in s})

l0 = [1, 2, 3]
l1 = []
for i in l0:
    for j in l0:
        for k in l0:
            if i != j and i != k and j != k:
                l1.append(int(str(i) + str(j) + str(k)))


cols = set(l1)
print(cols)
print(len(cols))
print(l1)
print(len(l1))
