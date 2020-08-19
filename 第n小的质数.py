"""
def prime_number(n):
    prime_number_list = [2]
    i = 3
    _i = i
    lst = [2]
    bol = True
    while len(prime_number_list) < n:
        for k in lst:
            if (i + 1) % k == 0:
                bol = False
                break
            else:
                bol = True
                continue
        if bol:
            prime_number_list.append(i)
        else:
            lst.append(i)
            i += 1
    prime_number_list = prime_number_list[::-1]
    return prime_number_list[0]


print(prime_number(int(input("::"))))
"""
import math


def is_prime_number(n):
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            return False
        else:
            continue
    return True


s = input("第几个质数? :")
j = 0
t = 2
while j <= s:
    if is_prime_number(t):
        j += 1
    if j == s:
        break
print(j)
