"""
What's this?
--it's a homework file
"""
# Homework 1


# def perfect_number(m, n):
#     lst = []
#     for i in range(m, n+1):
#         s = 0
#         for j in range(1, i):
#             if i % j == 0:
#                 s += j
#         if s == i:
#             lst.append(i)
#             print(i)
#     print(lst)
#
#
# perfect_number(5, 200000000000000000000000000000)

# ===============================================

# Homework 2
# import math
#
#
# def is_prime(n):
#     m = math.floor(math.sqrt(n))
#     for i in range(2, m+1):
#         if n % i == 0:
#             return False
#     return True
#
#
# s = 0
# r = int(input("质数范围至："))
# for j in range(2, r+1):
#     if is_prime(j):
#         print("{} , ".format(j), end='')
#         s += 1
#     else:
#         continue
# print("\n\n共有{}个质数".format(s))

# ===============================================

# Homework 3


# def _max(a, b, c):
#     if a < b:
#         a, b = b, a
#     if a < c:
#         a, c = c, a
#     return a
#
#
# def func(a, b, c):
#     return _max(a, b, c) / _max(a+b, b, c) / _max(a, b, b+c)
#
#
# print("max(a, b, c) / [ max(a+b, b, c) * max(a, b, b+c) ] = {}".format(func(int(input("a: ")), int(input("b: ")), int(input("c: ")))))

# ===============================================

# Homework 4


# import math
#
#
# def is_prime(n):
#     m = math.floor(math.sqrt(n))
#     for i in range(2, m+1):
#         if n % i == 0:
#             return False
#     return True
#
#
# def is_absolutely_prime(n):
#     l = [int(x) for x in str(n)]
#     l2 = l[::-1]
#     _str = ''
#     for i in l2:
#         _str += str(i)
#     if is_prime(n) and is_prime(int(_str)):
#         return True
#     else:
#         return False
#
#
# for i in range(10, 100):
#     if is_absolutely_prime(i):
#         print("{}".format(i), end=', ')

# =================================================

# Homework 5


# def factor_sum(n):
#     s = 0
#     for i in range(1, n):
#         if n % i == 0:
#             s += i
#     return s
#
#
# # def friendly_number(a, b):
# #     if factor_sum(a) == b and factor_sum(b) == a:
# #         return True
# #     return False
#
#
# Bol = True
# a = 0
# while Bol:
#     b = factor_sum(a)
#     if factor_sum(b) == a and a != b:
#         print(a, b, sep=', ')
#         Bol = False
#     a += 1

# =========================================

# Homework 6


# import math
#
#
# def is_palindrome(x):
#     x = str(x)
#     if len(x) % 2 == 0:
#
#         _list = []
#         for i in range(len(x) // 2):
#             x = list(x)
#             _list.append(x[i])
#
#         lst = []
#         x = "".join(x)
#         for j in range(len(x) - 1, len(x) // 2 - 1, -1):
#             x = list(x)
#             lst.append(x[j])
#
#         if _list == lst:
#             return True
#         else:
#             return False
#
#     else:
#
#         middle = len(x) // 2
#         x = list(x)
#         x.pop(middle)
#         x = "".join(x)
#
#         _list = []
#         for m in range(len(x) // 2):
#             x = list(x)
#             _list.append(x[m])
#
#         lst = []
#         x = "".join(x)
#         for n in range(len(x) - 1, len(x) // 2 - 1, -1):
#             x = list(x)
#             lst.append(x[n])
#
#         if _list == lst:
#             return True
#         else:
#             return False
#
#
# def is_prime(o):
#     m = math.floor(math.sqrt(o))
#     for i in range(2, m + 1):
#         if o % i == 0:
#             return False
#     return True
#
#
# for i in range(100, 1000):
#     if is_prime(i) and is_palindrome(i):
#         print(i)

