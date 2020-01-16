import random

def GuessNumber(x):
    answer = random.randint(0, x)
    _sum = 1
    while True:
        _in = None
        try:
            _in = int(input("please input a integer:"))
        except TypeError as ex:
            print("type error!")
            _in = int(input("please input a integer:"))
        if answer < _in:
            print("The true answer is smaller than this number!(smaller)")
        elif answer > _in:
            print("The true answer is bigger than this number!(bigger)")
        else:
            if _sum > 7:
                print("You win, but you are stupid! You guessed {} times".format(_sum))
            elif _sum > 5 and _sum <= 7:
                print("You win, and you are normal! You guessed {} times".format(_sum))
            else:
                print("You win, and you are very smart! You guessed {} times".format(_sum))
            break
        _sum += 1

a = True
while a:
    try:
        a = False
        x = int(input("please input the scope: "))
        GuessNumber(x)
    except:
        pass