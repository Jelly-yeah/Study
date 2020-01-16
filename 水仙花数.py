import copy
def ArmstrongNumber(x):
    z = copy.deepcopy(x)
    x = str(x)
    x = list(x)
    y = []
    for i in x:
        i = int(i)
        y.append(i)
    _sum = 0
    for i in y:
        _sum = _sum + (i**3)
    if _sum == z:
        # print("This is a ArmstrongNumber")
        return True
    else:
        # print("This isn't a ArmstrongNumber")
        return False

lst = []
for i in range(0, 10000):
    if ArmstrongNumber(i) == True:
        lst.append(i)
    else:
        continue

print(lst)