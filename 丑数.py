def uglyNumber(n):
    if n%2 != 0 or n%3 !=0 or n%4 !=0:
        return False
    else:
        for i in [2,3,5]:
            if n % i == 0:
                while True:
                    n //= i
                    if n % i != 0:
                        break
        # if n % 3 == 0:
        #     while True:
        #         n //= 3
        #         if n % 3 != 0:
        #             break
        # if n % 5 == 0:
        #     while True:
        #         n //= 5
        #         if n % 5 != 0:
                    # break
        if n == 1:
            return True
        else:
            return False

print(uglyNumber(14))