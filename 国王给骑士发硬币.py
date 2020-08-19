def coins(end_day):
    s = 0
    for i in range(1, end_day+1):
        for j in range(1, i+1):
            s += i
    return s


print(coins(int(input("days:"))))
