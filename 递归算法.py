import numpy
def pord(x):
    if x == 1:
        return 1
    else:
        return float(x) * pord(x-1)
print("pord: +"+str(pord(159)))

def Gcd(x, y):
    if y > x:
        x, y = y, x
    if x % y == 0:
        return y
    else:
        return Gcd(y, x % y)

print("Gcd: "+str(Gcd(24,16)))

def Fib(n): 
    if n == 1 or n == 2:
        return 1
    else:
        return Fib(n-1) + Fib(n-2)
for i in range(1, 32):
    print("{}   fib: {}".format(i, Fib(i)))

import os
import time
def main():
    a = input("Please input the string: ")
    b = input("Please input the roll speed (scond): ")
    while True:
        os.system("cls")
        print(a)
        time.sleep(b)
        a = a[1:] + a[0]

main()