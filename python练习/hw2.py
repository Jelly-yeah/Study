import random


# =============================每次的判断部分===============================
def guessing(g, r):
    try:
        ret = list(r)[:]
        if g == r:
            return "猜对了"
        elif len(g) == len(r):
            j = 0
            for i in ret:
                if g[:(j+1)] != i:
                    ret[j] = 'x'
                j += 1
            ret = ''.join(ret)
            return ret
        elif len(g) > len(r):
            return "数位猜多了（正确答案的数位比这个少）"
        elif len(g) < len(r):
            return "数位猜少了（正确答案的数位比这个多）"
    except TypeError as e:
        return "输入不符合规则!"


# =========================文字提示与准备部分==============================
def guess_hello():
    print("猜数游戏")
    print('============================================================')
    print("游戏规则", "当使用者手动输入猜测的四位数字后程序将这四位数字中猜对的位数以真实数字显示出来", "没猜对的位数用表示",
          "使用者则继续输入自己猜测的四位数", "输入直到使用者将四位数字全部猜对", "程序则恭喜使用者猜对了",
          "并提示使用者一共用了几次猜对数字的。", sep=",\n", end="\n")
    print()
    print('============================================================')
    _max = int(input("请输入范围上限:"))
    _min = int(input("请输入范围下限:"))
    guess_number(_min, _max)


# =============================程序正文==================================
def guess_number(_min, _max):
    rand = str(random.randint(_min, _max))
    print("提示:它是{}位数".format(len(rand)))
    i = 0
    while True:
        guess = input("请猜数:")
        print(guessing(guess, rand))
        if guessing(guess, rand) == "猜对了":
            print("一共猜了{}次".format(i))
            break
        i += 1


# ==============================主函数==================================
if __name__ == "__main__":
    guess_hello()
