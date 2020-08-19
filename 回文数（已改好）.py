def is_palindrome(x):
        
    if len(x) % 2 == 0:
        
        _list = []
        for i in range(len(x)//2):
            x = list(x)
            _list.append(x[i])

        lst = []
        x = "".join(x)
        for i in range(len(x)-1, len(x)//2-1, -1):
            x = list(x)
            listy.append(x[i])

        if _list == lst:
            return True
        else:
            return False

    else:
        
        middle = len(x)//2
        x = list(x)
        x.pop(middle)
        x = "".join(x)

        _list = []
        for i in range(len(x)//2):
            x = list(x)
            _list.append(x[i])

        lst = []
        x = "".join(x)
        for i in range(len(x)-1, len(x)//2-1, -1):
            x = list(x)
            lst.append(x[i])

        if _list == lst:
            return True
        else:
            return False


a = input()
print(is_palindrome(a))