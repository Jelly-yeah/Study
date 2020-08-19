"""
def dagongyin(a, b):
    a_list = []
    for i in range(1, a+1):
        if a % i == 0:
            a_list.append(a // i)
        else:
            continue
    
    b_list = []
    for j in range(1, b+1):
        if b % j == 0:
            b_list.append(b // j)
        else:
            continue

    # x, y = (set(a_list), set(b_list))
    # r = x & y
    # r = list(r)
    # r = sorted(r)
    # r = r[len(r)-1]
    r = max(list(set(a_list) & set(b_list)))
    print(r)

print(dagongyin(12, 8))


def xiaogongbei(x, y):
    if x == y:
        n = x
        print(n)
    if x > y:
        i = x
        x = y
   
    y = i
    a = True
    while a:
        if (y * i) % x == 0:
            print(y*i)
            a = False
        else:
            continue

print(xiaogongbei(12,8))

"""


def dagongyin(x, y):
    z = x % y
    while z != 0:
        z = x % y
        x, y = y, z
    return x


print(dagongyin(24, 16))
