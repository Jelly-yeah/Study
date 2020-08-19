# def number_statistics(L, R):
#     _str = ""
#     for i in range(L, R+1):
#         _join = str(i)
#         _str = "{}{}".format(_str, _join)
#     lst = list(_str)
#     times = 0
#     while '2' in lst:
#           lst.pop(lst.index('2'))
#           times += 1
#     return times
#
#
# print(number_statistics(int(input("from: ")), int(input("to: "))))


def number_statistics(L, R):
    count = 0
    for i in range(L, R+1):
        n = i
        while n > 0:
            m = n % 10
            n //= 10
            if m == 2:
                count += 1
    return count


print(number_statistics(int(input("from: ")), int(input("to: "))))
