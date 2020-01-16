def isPalindrome(x, y=0):
    
    for i in range (len(x),0 , -1): # suan'fa'wen'ti(xia'main)
        y = ( int(x) - ( int(x) % ( 10 ** ( len(x) - ( i - 2 ) ) ) ) ) / ( 10 ** ( len(x) - ( i ) ) ) + y
    print(y)
    if x == y:
        return True
    elif x != y:    
        return False

print(isPalindrome("121"))