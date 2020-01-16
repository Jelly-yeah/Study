def zhishu(x):
    lst = []
    num = 0
    for i in range(2, x+1, +1):
        for j in range(i, 0, -1):
            if i % j == 0:
                num += 1
        if num < 3:
            lst.append(i)
            num = 0
        else:
            num = 0
    print(lst)


print(zhishu(1000))