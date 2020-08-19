# def LuckyChristian(m):
#     lst = []
#     if m % 9 == 0:
#         if len(lst)>m:
#             lst.pop(m)
#         else:
#             lst.pop[9%len(lst)]
#     else:
#         return LuckyChristian()


# def joseph(n, k):
#     persons = [True]*n
#     counter, index, number = 0, 0, 0
#     while counter < n-1:
#         if persons[index]:
#             number += 1
#             if number == k:
#                 persons[index] = False
#                 counter += 1
#         number = 0
#         print(index)
#         index += 1
#         if index == n:
#             index = 0
#         # index =30
#     for person in persons:
#         print('Lucky  ' if person else 'unLucky  ', end='')
#
#
# joseph(123, 50)
from typing import List

n = int(input("约瑟夫环人数"))
m = int(input("报数周期(报到最后一个数的人出列): "))
# ---------------------------------------------

persons: List[bool] = [False for i in range(0, n+1)]
counter, number, k = 0, 0, 0
# ---------------------------------------------

while counter < n:
    number += 1

    if number > n:
        number = 1
    if persons[number]:
        continue

    k += 1
    if k > m:
        k = 1

    if k == m:
        persons[number] = True
        counter += 1
        print(number)


