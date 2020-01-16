def cjengfabiao(x):
    for i in range(1,x+1):
        _str = ""
        for j in range(1,x+1):
            if i >= j:
                if (i == 3 and j == 3) or (i == 4 and j == 3):
                    _str = _str + "   {} * {} = {}".format(j,i,i*j)
                else:
                    _str = _str + "  {} * {} = {}".format(j,i,i*j)
        print(_str)

print(cjengfabiao(9))