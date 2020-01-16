def PerfectNumber(x):
    Factor_list = []
    for i in range(x, 1, -1):
        if x % i == 0:
            Factor_list.append(x // i)
        else:
            continue
    if sum(Factor_list) == x:
        return True
    else:
        return False

lst = []
for i in range(10 ** 4):
    if PerfectNumber(i) == True:
        lst.append(i)
    else:
        continue
print(lst)