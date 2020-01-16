import hashlib
def hash(n):
    n = str(n)
    m = hashlib.md5(n.encode(encoding='utf-8')).hexdigest()
    print(m)
    return m

# rainbow_list = []
# x_list = [0, 0, 0, 0]
# y_list = []
# z_list = []
# a = 0
# b = 0

# while True:
#     if a == 4:
#         break
#     if b % 10 == 0:
#         a += 1
#     for i in x_list:
#         y_list.append(i)
#     for i in x_list:
#         z_list.append(hash(i))
#     print("{} : hash({})".format(y_list, z_list))
#     one = x_list[a-1]
#     one += a+1
#     x_list.insert(a, one)
#     x_list.pop(a-1)
#     b += 1