def prime(p):
    if '&' in p:
        p = p.replace('&', '')
    if int(p) <= 1:
        return False
    if p == 2:
        return True
    else:
        for i in range(2, int(p)):
            if int(p) % i == 0:
                return False
        return True


def have_3():
    lst = []
    for i in range(1, 1001):
        if '3' in str(i):
            lst.append(str(i))
    have_double_3(lst)


def have_double_3(lst):
    times = 0
    for i in lst:
        if '33' in i:
            lst[times] = '&' + lst[times]
        times += 1
    is_prime(lst)


def is_prime(lst):
    times = 0
    for i in lst:
        if prime(i):
            lst[times] += '*'
        times += 1
    print(lst)


if __name__ == "__main__":
    have_3()
