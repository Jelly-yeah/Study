# def LuckyChristian(m):
#     lst = []
#     if m % 9 == 0:
#         if len(lst)>m:
#             lst.pop(m)
#         else:
#             lst.pop[9%len(lst)]
#     else:
#         return LuckyChristian()
def joseph(n, k):
    persons= [True]*n
    counter, index, number=0,0,0
    while counter < n-1:
        if persons[index]:
            number += 1
            if number == k:
                persons[index]=False
                counter+= 1
        number=0
        print(index)
        index += 1
        if index == n:
            index = 0
        # index =30
    for person in persons:
        print('Lucky  ' if person else 'unLucky  ',end='')

joseph(123, 50)