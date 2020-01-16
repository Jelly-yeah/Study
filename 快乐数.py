# def happyNum(b):
#     b = list(str(b))
#     _sum = 0
#     a = []
#     for n in b :
#         a.append(int(n))
#     num = 0
#     _sm = 0
#     # while _sum!=4 or _sum!=37 or _sum!=58 or _sum!=89 or _sum!=145:
#     while True:
#         if num<1:
#             x = []
#             for i in a :
#                 x.append(i**2)
#             for j in x :
#                 _sum += j
#             if _sum==1:
#                 return True
#             if _sum==4 or _sum==37 or _sum==58 or _sum==89 or _sum==145:
#                 return False
#         if num<2:
#             x, s = [], []
#             u = list(str(_sum))
#             for n in u :
#                 s.append(int(n))
#             for i in s :
#                 x.append(i**2)
#             for j in x :
#                 _sm += j
#             if _sm==1:
#                 return True
#             if _sm==4 or _sm==37 or _sm==58 or _sm==89 or _sm==145:
#                 return False
#             m = x[0]
#             d = []
#             c = list(str(m))
#             for n in c :
#                 d.append(int(n))
#         else :
#             x, s = [], []
#             for n in d :
#                 s.append(int(n))
#             for i in s :
#                 x.append(i**2)
#             for j in x :
#                 _sm += j
#             if _sm==1:
#                 return True
#             if _sm==4 or _sm==37 or _sm==58 or _sm==89 or _sm==145:
#                 return False
#             m = x[0]
#             d = []
#             c = list(str(m))
#             for n in c :
#                 d.append(int(n))
#         num += 1
#         _sm = 0

# lst = []
# for i in range(1, 10000):
#     print(i)
#     if happyNum(i) == True:
#         lst.append(i)
#     else:
#         continue
# print(lst)
def isHappy(n):
        numList = [n]
        while n!=1:
            _sum=0
            for i in str(n):
                _sum += int(i)**2
            if _sum not in numList:
                numList.append(_sum)
            else: 
                return False
            n = sum
        return True
print(isHappy(19))