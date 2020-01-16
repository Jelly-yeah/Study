def change(a):
    lst=[]
    while True:
        if a == 0:
            break
        if a % 2 == 0:
            lst.append(0)
            a = (a - 1)//2
        else:
            lst.append(1)
            a = a //2
    return lst[::-1]

print(change(85))