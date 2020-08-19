# def func(n):
#     m = []
#     while n != 1:
#         for i in range(2, int(n + 1)):
#             if n % i == 0:
#                 m.append(str(i))
#                 n = n / i
#         if n == 1:
#             break
#     m.sort()
#     res = m[::-1][0]
#     return res
#
#
# print(func(21))

import math
n = int(input("质因数分解: "))
m = math.floor(math.sqrt(n))
for i in range(2, m+1):
    if n % i == 0:
        print(n // i)
        break
