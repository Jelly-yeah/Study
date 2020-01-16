def isPalindrome(x):
        
    if len(x)%2==0:
        
        listx = []
        for i in range(len(x)//2):
            x = list(x)
            listx.append(x[i])

        listy = []
        x = "".join(x)
        for i in range(len(x)-1, len(x)//2-1, -1):
            x = list(x)
            listy.append(x[i])

        if listx == listy:
            return True
        else:
            return False

    else:
        
        middle = len(x)//2
        x = list(x)
        x.pop(middle)
        x = "".join(x)

        listx = []
        for i in range(len(x)//2):
            x = list(x)
            listx.append(x[i])

        listy = []
        x = "".join(x)
        for i in range(len(x)-1, len(x)//2-1, -1):
            x = list(x)
            listy.append(x[i])

        if listx == listy:
            return True
        else:
            return False

a = input()
print(isPalindrome(a))