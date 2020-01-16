def sum(NumList, target):
    for i in range (0, len(NumList)):
        for j in range (i+1, len(NumList)):
            if (NumList[i] + NumList[j]) == target:
                return [i, j]
    return None

lst = [2, 7, 11, 15]
target = 18

res = sum(lst, target)
print(res)