""""""
from functools import reduce

"""
python 实现列表翻转
"""


def reverse_list_1(lst):
    return lst[::-1]


print(reverse_list_1([1, 2, 3, 4]))


def reverse_list_2(lst):
    lst1 = []
    for i in lst:
        lst1 = [i] + lst1
    return lst1


print(reverse_list_2([1, 2, 3, 4]))


def reverse_list_3(lst):
    lst.reverse()
    return lst


print(reverse_list_3([1, 2, 3, 4]))


"""
python 实现字符串翻转
"""


def reverse_string_1(string):
    return string[::-1]


print(reverse_string_1("ABCD"))


def reverse_string_2(string):
    str1 = ""
    for i in string:
        str1 = i + str1
    return str1


print(reverse_string_2("ABCD"))

s1 = reversed("ABCD")
print("".join(s1))

"""
python 实现len函数
"""


def python_len_1(string):
    return len(string)


print(python_len_1("ABCD"))


def python_len_2(string):
    count = 0
    for i in string:
        count += 1
    return count


print(python_len_2("ABCD"))


def python_len_3(string):
    count = 0
    while string[count:]:
        count += 1
    return count


print(python_len_3("ABCD"))


def python_len_4(string):
    return sum(1 for i in string)


print(python_len_4("ABCD"))


def python_len_6(string):
    return reduce(lambda x, y: x + 1, string)


"""
python 实现字符串去重
"""


def remove_duplicates_1(string):
    return "".join(set(string))


print(remove_duplicates_1("ABCDABCD"))


def remove_duplicates_2(string):
    lst = []
    for i in string:
        if i not in lst:
            lst.append(i)
    return "".join(lst)


print(remove_duplicates_2("ABCDABCD"))


def remove_duplicates_3(string):
    return "".join(dict.fromkeys(string))


print(remove_duplicates_3("ABCDABCD"))


def remove_duplicates_4(string):
    return "".join({}.fromkeys(string).keys())


print(remove_duplicates_4("ABCDABCD"))


def remove_duplicates_5(string):
    return "".join({}.fromkeys(string))


print(remove_duplicates_5("ABCDABCD"))


"""
python 实现返回数字的绝对值
"""
print(abs(-100))


def python_abs_1(number):
    if number > 0:
        return number
    else:
        return -number


print(python_abs_1(-100))


def python_abs_2(number):
    if number >= 0:
        return number

    return int(str(number)[1:])


print(python_abs_2(-100))

"""
python 实现求和
"""


def python_sum_1(lst):
    return sum(lst)


print(python_sum_1([1, 2, 3, 4]))


def python_sum_2(lst):
    total = 0
    for i in lst:
        total += i
    return total


print(python_sum_2([1, 2, 3, 4]))


def python_sum_3(lst):
    return reduce(lambda x, y: x + y, lst)


print(python_sum_3([1, 2, 3, 4]))
print(isinstance("a", (int, float)))

"""
python 实现返回最小值
"""

print(min([1, 2, 3, 4]))


def python_min_1(lst):
    min_number = lst[0]
    for i in lst[1:]:
        if i < min_number:
            min_number = i

    return min_number


print(python_min_1([1, 2, 3, 4]))

"""
python 实现返回最大值
"""
print(max([1, 2, 3, 4]))


def find_max(lst):
    max_value = lst[0]
    for i in lst[1:]:
        if max_value < i:
            max_value = i
    return max_value


print(find_max([1, 2, 3, 4]))


def find_max_value(lst):
    max_value = lst[0].lower()
    for i in lst[1:]:
        if max_value < i:
            max_value = i
    return max_value


print(find_max_value(["apple", "Banana", "cherry"]))

# def test_find_max_value():
#     assert find_max_value(["apple", "Banana", "cherry"]) == "cherry"

"""
python 实现四舍五入
"""
print(round(10.1))
print(round(2.5))
print(round(-2.7))


def python_round(number, ndigits=None):
    if ndigits is None:
        return int(number + 0.5) if number > 0 else int(number - 0.5)
    else:
        factor = 10**ndigits
        temp = number * factor
        rounded = int(temp + 0.5) if temp >= 0 else int(temp - 0.5)
        return rounded / factor


print(python_round(10.1))
print(python_round(10.9))
print(python_round(10.15))
print(python_round(10.5))


"""
python 实现幂运算
"""
print(pow(2, 3))


def python_pow(base, exp):
    return base**exp


print(python_pow(2, 3))


def python_pow_2(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result


print(python_pow_2(2, 3))

"""
实现字符串的大小写转换
"""


def python_swapcase(string):
    return string.swapcase()
