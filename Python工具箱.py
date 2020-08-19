# -*- coding: utf-8 -*-
import tkinter
import tkinter.messagebox
import hashlib
import os
import time
# import pyperclip
import random


def read_pwd_in_memory(key):
    try:
        if os.path.exists(File):
            _f = open(File, "r", encoding='utf-8')
            read = _f.read()
    except Exception as e:
        tkinter.messagebox.showerror("ERROR","Something was error!({})".format(e))
        if _f:
            _f.close()



def show_pwd(_win):
    _win.withdraw()
    win = tkinter.Tk()
    win.title(" 查看密码条 ")
    width = 500
    height = 50
    x = (win.winfo_screenwidth()-width) // 2
    y = (win.winfo_screenheight()-height) // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    label1 = tkinter.Label(win, text=" 密码条名称: ")
    entry1 = tkinter.Entry(win, width=24)
    button1 = tkinter.Button(win, text=" 搜索密码 ", command=lambda:read_pwd_in_memory(entry1.get()))
    button2 = tkinter.Button(win, text=" 返回 ", command=lambda:EXIT(win, _win))
    label1.pack(side=tkinter.LEFT)
    entry1.pack(side=tkinter.LEFT)
    button1.pack(side=tkinter.LEFT)
    button2.pack(side=tkinter.RIGHT)
    win.mainloop()


def add_pwd_in_memory(key, value):
    value = list(value)
    enc_key = random.randint(0,10)
    for _ in range(enc_key):
        value.append(value[0])
        value.pop(0)            # 利用凯撒加密，enc_key是从右往左的滚动量
    _value = "".join(value)
    add_in = {'name': key, 'pwd': _value, 'enc_key': enc_key}
    File = "X:\\Files\\pwd.txt"
    try:
        if os.path.exists(File):
            _f = open(File, "r", encoding='utf-8')
            read = _f.read()
            _f.close()
            _f2 = open(File, "w", encoding='utf-8')
            read = eval(read)
            write_in = read.append(add_in)
            _f2.write("".join(write_in))
            _f2.close()
        elif os.path.exists(File) == False:
            f = open(File, "w", encoding='utf-8')
            a = str([add_in])
            f.write(a)
            f.close()
        tkinter.messagebox.showinfo("成功", "成功加入密码")
    except Exception as e:
        tkinter.messagebox.showerror("ERROR","Something was error!({})".format(e))
        if _f:
            _f.close()


def add_pwd(_win):
    _win.withdraw()
    win = tkinter.Tk()
    win.title(" 添加密码条 ")
    width = 500
    height = 50
    x = (win.winfo_screenwidth()-width) // 2
    y = (win.winfo_screenheight()-height) // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    label2 = tkinter.Label(win, text=" 密码条名称: ")
    entry1 = tkinter.Entry(win, width=24)
    label1 = tkinter.Label(win, text=" 密码: ")
    entry2 = tkinter.Entry(win, width=12)
    button1 = tkinter.Button(win, text=" 存储密码 ", command=lambda:add_pwd_in_memory(entry1.get(), entry2.get()))
    button2 = tkinter.Button(win, text=" 返回 ", command=lambda:EXIT(win, _win))
    label2.pack(side=tkinter.LEFT)
    entry1.pack(side=tkinter.LEFT)
    label1.pack(side=tkinter.LEFT)
    entry2.pack(side=tkinter.LEFT)
    button1.pack(side=tkinter.LEFT)
    button2.pack(side=tkinter.RIGHT)
    win.mainloop()


def pwd_box(_win):
    _win.withdraw()
    win = tkinter.Tk()
    win.title(" 密码盒 ")
    width = 450
    height = 50
    x = (win.winfo_screenwidth()-width) // 2
    y = (win.winfo_screenheight()-height) // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    button0 = tkinter.Button(win, text=" 查看密码条 ", command=lambda:show_pwd(win))
    button1 = tkinter.Button(win, text=" 添加密码条 ", command=lambda:add_pwd(win))
    button2 = tkinter.Button(win, text=" 返回 ", command=lambda:EXIT(win, _win))
    button0.pack(side=tkinter.LEFT)
    button1.pack(side=tkinter.LEFT)
    button2.pack(side=tkinter.RIGHT)
    win.mainloop()


def ind(_win):
    _win.withdraw()
    win = tkinter.Tk()
    win.title(" xⁿ ")
    width = 450
    height = 50
    x = (win.winfo_screenwidth()-width) // 2
    y = (win.winfo_screenheight()-height) // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    label2 = tkinter.Label(win, text="  ")
    entry1 = tkinter.Entry(win, width=12)
    label1 = tkinter.Label(win, text=" ^ ")
    entry2 = tkinter.Entry(win, width=12)
    button1 = tkinter.Button(win, text=" 获取结果 ", command=lambda:exp(win, entry1.get(), entry2.get()))
    button2 = tkinter.Button(win, text=" 返回 ", command=lambda:EXIT(win, _win))
    label2.pack(side=tkinter.LEFT)
    entry1.pack(side=tkinter.LEFT)
    label1.pack(side=tkinter.LEFT)
    entry2.pack(side=tkinter.LEFT)
    button1.pack(side=tkinter.LEFT)
    button2.pack(side=tkinter.RIGHT)
    win.mainloop()


def exp(_win, m, n):
    try:
        n = int(n)
        m = int(m)
        s = m ** n
        _win.withdraw()
        win = tkinter.Tk()
        win.title(" 结果 ")
        width = 330
        height = 30
        x = (win.winfo_screenwidth()-width) // 2
        y = (win.winfo_screenheight()-height) // 2
        win.geometry("{}x{}+{}+{}".format(width, height, x, y))
        label1 = tkinter.Label(win, text="  结果为:{}    ".format(s))
        button1 = tkinter.Button(win, text="  确定 ", command=lambda:EXIT(win, _win))
        button2 = tkinter.Button(win, text=" 复制计算结果 ", command=lambda:copy(s))
        label1.pack(side=tkinter.LEFT)
        button1.pack(side=tkinter.LEFT)
        button2.pack(side=tkinter.RIGHT)
        win.mainloop()
    except:
        tkinter.messagebox.showerror("错误", "输入不正确!")


def BeforeSetQue(_win):
    File = "X:\\Files\\SafetyQuetions.txt"
    '''if os.path.exists(File):
        que(_win)
    else:
        reg(_win)
        tkinter.messagebox.showwarning("请尽快设置安全问题!")'''
    SetQue(_win)


def GetSetQue(q, a):
    try:
        File = "X:\\Files\\SafetyQuetions.txt"
        a_md5 = hashlib.md5(a.encode(encoding="utf-8")).hexdigest()
        _f = open(File, "w")
        user_dict = {"que":q, "ans":a_md5}
        _f.write(str(user_dict))
        _f.close()
        tkinter.messagebox.showinfo("massage", "设置成功!")
    except:
        tkinter.messagebox.showerror("ERROR", "文件已被占用, 请重试!")


def SetQue(_win):
    _win.withdraw()
    win = tkinter.Tk()
    win.title("设置安全问题")
    width = 700
    height = 50
    x = (win.winfo_screenwidth()-width) // 2
    y = (win.winfo_screenheight()-height) // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    label2 = tkinter.Label(win, text="  问题: ")
    entry1 = tkinter.Entry(win, width=30)
    label1 = tkinter.Label(win, text="  答案(仅英文字母): ")
    entry2 = tkinter.Entry(win, width=24)
    button1 = tkinter.Button(win, text="  设置  ", command=lambda:GetSetQue(entry1.get(), entry2.get()))
    button2 = tkinter.Button(win, text=" 返回 ", command=lambda:EXIT(win, _win))
    label2.pack(side=tkinter.LEFT)
    entry1.pack(side=tkinter.LEFT)
    label1.pack(side=tkinter.LEFT)
    entry2.pack(side=tkinter.LEFT)
    button1.pack(side=tkinter.LEFT)
    button2.pack(side=tkinter.RIGHT)
    win.mainloop()

def div(_win):
    _win.withdraw()
    win = tkinter.Tk()
    win.title(" ÷ ")
    width = 700
    height = 50
    x = (win.winfo_screenwidth()-width) // 2
    y = (win.winfo_screenheight()-height) // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    label2 = tkinter.Label(win, text="  ")
    entry1 = tkinter.Entry(win, width=12)
    label1 = tkinter.Label(win, text=" ÷ ")
    entry2 = tkinter.Entry(win, width=12)
    button1 = tkinter.Button(win, text=" 获取商 ", command=lambda:GetQuotient(win, entry1.get(), entry2.get(), entry3.get()))
    label3 = tkinter.Label(win, text="  四舍五入后的小数位数(默认两位)(最大54位):")
    entry3 = tkinter.Entry(win, width=10)
    button2 = tkinter.Button(win, text=" 返回 ", command=lambda:EXIT(win, _win))
    label2.pack(side=tkinter.LEFT)
    entry1.pack(side=tkinter.LEFT)
    label1.pack(side=tkinter.LEFT)
    entry2.pack(side=tkinter.LEFT)
    button1.pack(side=tkinter.LEFT)
    label3.pack(side=tkinter.LEFT)
    entry3.pack(side=tkinter.LEFT)
    button2.pack(side=tkinter.RIGHT)
    win.mainloop()

def GetQuotient(_win, n, m, k):
    a = True
    try:
        n = int(n)
        m = int(m)
        if k == '':
            k = 2
        k = int(k)
        if m == 0 and n > 0:
            s = "∞"
        elif m == 0 and n < 0:
            s = "-∞"
        elif m == 0 and n == 0:
            tkinter.messagebox.showerror("错误", "输入不正确!")
            a = False
        else:
            s = ("%.{}f".format(k) % (n/m))
        if a:
            _win.withdraw()
            win = tkinter.Tk()
            win.title(" 商 ")
            width = 330+k
            height = 30
            x = (win.winfo_screenwidth()-width) // 2
            y = (win.winfo_screenheight()-height) // 2
            win.geometry("{}x{}+{}+{}".format(width, height, x, y))
            label1 = tkinter.Label(win, text="  商为: {}    ".format(s))
            button1 = tkinter.Button(win, text="  确定 ", command=lambda:EXIT(win, _win))
            button2 = tkinter.Button(win, text=" 复制计算结果 ", command=lambda:copy(s))
            label1.pack(side=tkinter.LEFT)
            button1.pack(side=tkinter.LEFT)
            button2.pack(side=tkinter.RIGHT)
            win.mainloop()
    except:
        tkinter.messagebox.showerror("错误", "输入不正确!")

def mul(_win):
    _win.withdraw()
    win = tkinter.Tk()
    win.title(" × ")
    width = 380
    height = 50
    x = (win.winfo_screenwidth()-width) // 2
    y = (win.winfo_screenheight()-height) // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    label2 = tkinter.Label(win, text="  ")
    entry1 = tkinter.Entry(win, width=12)
    label1 = tkinter.Label(win, text=" × ")
    entry2 = tkinter.Entry(win, width=12)
    button1 = tkinter.Button(win, text=" 获取积 ", command=lambda:GetProduct(win, entry1.get(), entry2.get()))
    button2 = tkinter.Button(win, text=" 返回 ", command=lambda:EXIT(win, _win))
    label2.pack(side=tkinter.LEFT)
    entry1.pack(side=tkinter.LEFT)
    label1.pack(side=tkinter.LEFT)
    entry2.pack(side=tkinter.LEFT)
    button1.pack(side=tkinter.LEFT)
    button2.pack(side=tkinter.RIGHT)
    win.mainloop()

def GetProduct(_win, n, m):
    try:
        n = int(n)
        m = int(m)
        s = m * n
        _win.withdraw()
        win = tkinter.Tk()
        win.title(" 积 ")
        width = 330
        height = 30
        x = (win.winfo_screenwidth()-width) // 2
        y = (win.winfo_screenheight()-height) // 2
        win.geometry("{}x{}+{}+{}".format(width, height, x, y))
        label1 = tkinter.Label(win, text="  积为:{}    ".format(s))
        button1 = tkinter.Button(win, text="  确定 ", command=lambda:EXIT(win, _win))
        button2 = tkinter.Button(win, text=" 复制计算结果 ", command=lambda:copy(s))
        label1.pack(side=tkinter.LEFT)
        button1.pack(side=tkinter.LEFT)
        button2.pack(side=tkinter.RIGHT)
        win.mainloop()
    except:
        tkinter.messagebox.showerror("错误", "输入不正确!")

def sub(_win):
    _win.withdraw()
    win = tkinter.Tk()
    win.title(" － ")
    width = 380
    height = 50
    x = (win.winfo_screenwidth()-width) // 2
    y = (win.winfo_screenheight()-height) // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    label2 = tkinter.Label(win, text="  ")
    entry1 = tkinter.Entry(win, width=12)
    label1 = tkinter.Label(win, text=" － ")
    entry2 = tkinter.Entry(win, width=12)
    button1 = tkinter.Button(win, text=" 获取差 ", command=lambda:GetDiff(win, entry1.get(), entry2.get()))
    button2 = tkinter.Button(win, text=" 返回 ", command=lambda:EXIT(win, _win))
    label2.pack(side=tkinter.LEFT)
    entry1.pack(side=tkinter.LEFT)
    label1.pack(side=tkinter.LEFT)
    entry2.pack(side=tkinter.LEFT)
    button1.pack(side=tkinter.LEFT)
    button2.pack(side=tkinter.RIGHT)
    win.mainloop()

def GetDiff(_win, n, m):
    try:
        n = int(n)
        m = int(m)
        s = n - m
        _win.withdraw()
        win = tkinter.Tk()
        win.title(" 差 ")
        width = 330
        height = 30
        x = (win.winfo_screenwidth()-width) // 2
        y = (win.winfo_screenheight()-height) // 2
        win.geometry("{}x{}+{}+{}".format(width, height, x, y))
        label1 = tkinter.Label(win, text="  差为:{}    ".format(s))
        button1 = tkinter.Button(win, text="  确定 ", command=lambda:EXIT(win, _win))
        button2 = tkinter.Button(win, text=" 复制计算结果 ", command=lambda:copy(s))
        label1.pack(side=tkinter.LEFT)
        button1.pack(side=tkinter.LEFT)
        button2.pack(side=tkinter.RIGHT)
        win.mainloop()
    except:
        tkinter.messagebox.showerror("错误", "输入不正确!")

def copy(obj):
    pyperclip.copy(obj)

def GetSum(_win, n, m):
    try:
        n = int(n)
        m = int(m)
        s = n + m
        _win.withdraw()
        win = tkinter.Tk()
        win.title(" 和 ")
        width = 330
        height = 30
        x = (win.winfo_screenwidth()-width) // 2
        y = (win.winfo_screenheight()-height) // 2
        win.geometry("{}x{}+{}+{}".format(width, height, x, y))
        label1 = tkinter.Label(win, text="  和为:{}    ".format(s))
        button1 = tkinter.Button(win, text="  确定 ", command=lambda:EXIT(win, _win))
        button2 = tkinter.Button(win, text=" 复制计算结果 ", command=lambda:copy(s))
        label1.pack(side=tkinter.LEFT)
        button1.pack(side=tkinter.LEFT)
        button2.pack(side=tkinter.LEFT)
        win.mainloop()
    except:
        tkinter.messagebox.showerror("错误", "输入不正确!")

def add(_win):
    _win.withdraw()
    win = tkinter.Tk()
    win.title(" + ")
    width = 380
    height = 50
    x = (win.winfo_screenwidth()-width) // 2
    y = (win.winfo_screenheight()-height) // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    label2 = tkinter.Label(win, text="  ")
    entry1 = tkinter.Entry(win, width=12)
    label1 = tkinter.Label(win, text=" + ")
    entry2 = tkinter.Entry(win, width=12)
    button1 = tkinter.Button(win, text=" 获取和 ", command=lambda:GetSum(win, entry1.get(), entry2.get()))
    button2 = tkinter.Button(win, text=" 返回 ", command=lambda:EXIT(win, _win))
    label2.pack(side=tkinter.LEFT)
    entry1.pack(side=tkinter.LEFT)
    label1.pack(side=tkinter.LEFT)
    entry2.pack(side=tkinter.LEFT)
    button1.pack(side=tkinter.LEFT)
    button2.pack(side=tkinter.RIGHT)
    win.mainloop()
    

def com(_win):
    _win.withdraw()
    win = tkinter.Tk()
    win.title("计算器")
    width = 450
    height = 50
    x = (win.winfo_screenwidth()-width) // 2
    y = (win.winfo_screenheight()-height) // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    button1 = tkinter.Button(win, text=" + ", command=lambda:add(win))
    button2 = tkinter.Button(win, text=" － ", command=lambda:sub(win))
    button3 = tkinter.Button(win, text=" × ", command=lambda:mul(win))
    button4 = tkinter.Button(win, text=" ÷ ", command=lambda:div(win))
    button6 = tkinter.Button(win, text=" xⁿ ", command=lambda:ind(win))
    button5 = tkinter.Button(win, text=" 返回 ", command=lambda:EXIT(win, _win))
    button1.pack(side=tkinter.LEFT)
    button2.pack(side=tkinter.LEFT)
    button3.pack(side=tkinter.LEFT)
    button4.pack(side=tkinter.LEFT)
    button6.pack(side=tkinter.LEFT)
    button5.pack(side=tkinter.RIGHT)
    win.mainloop()


def start_file_in(app_dir):
    try:
        os.startfile(app_dir)
    except:
        tkinter.messagebox.showerror("错误", "输入不符合表达式或不合法, 请重试或检查输入内容")



def start_file(_win):
    _win.withdraw()
    win = tkinter.Tk()
    win.title("打开指定文件")
    width = 600
    height = 80
    x = (win.winfo_screenwidth()-width) // 2
    y = (win.winfo_screenheight()-height) // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    label1 = tkinter.Label(win, text="文件路径(例: X:\\XX\\XXX\\YY.exe)：")
    entry1 = tkinter.Entry(win, width=32)
    button2 = tkinter.Button(win, text="  打开文件  ", command=lambda:start_file_in(entry1.get()))
    button3 = tkinter.Button(win, text="   返回   ", command=lambda:EXIT(win, _win))
    button3.pack(side=tkinter.RIGHT)
    label1.pack(side=tkinter.LEFT)
    entry1.pack(side=tkinter.LEFT)
    button2.pack(side=tkinter.LEFT)
    win.mainloop()


def terminal():
    os.startfile('C:\Windows\System32\cmd.exe')


def sup1():
    os.startfile("X:\Files\sup\\ball.bat")


def sup2():
    os.startfile("X:\Files\sup\colors.bat")


def sup3():
    os.startfile("X:\Files\sup\\rain.bat")


def sup4():
    os.startfile("X:\Files\sup\\rain2.html")


def random_code_in(n, _win):
    text = '=-+_!@#$%^&*<>?|~ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 ==================='
    res = ''.join([''.join(text[random.randint(0, len(text)-1)] for _ in range(int(n)))])
    _win.withdraw()
    win = tkinter.Tk()
    win.title("随机码")
    width = 900
    height = 80
    x = (win.winfo_screenwidth()-width) // 2
    y = (win.winfo_screenheight()-height) // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    label1 = tkinter.Label(win, text=res)
    button2 = tkinter.Button(win, text="  复制结果  ", command=lambda:copy(res))
    button3 = tkinter.Button(win, text="   返回   ", command=lambda:EXIT(win, _win))
    button3.pack(side=tkinter.RIGHT)
    label1.pack(side=tkinter.LEFT)
    button2.pack(side=tkinter.LEFT)
    win.mainloop()

    


def random_code(_win):
    _win.withdraw()
    win = tkinter.Tk()
    win.title("生成随机码")
    width = 600
    height = 80
    x = (win.winfo_screenwidth()-width) // 2
    y = (win.winfo_screenheight()-height) // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    label1 = tkinter.Label(win, text="生成字符个数")
    entry1 = tkinter.Entry(win, width=32)
    button2 = tkinter.Button(win, text="  生成  ", command=lambda:random_code_in(entry1.get(), win))
    button3 = tkinter.Button(win, text="   返回   ", command=lambda:EXIT(win, _win))
    button3.pack(side=tkinter.RIGHT)
    label1.pack(side=tkinter.LEFT)
    entry1.pack(side=tkinter.LEFT)
    button2.pack(side=tkinter.LEFT)
    win.mainloop()



def suprise(_win):
    _win.withdraw()
    win = tkinter.Tk()
    win.title(" 小惊喜")
    width = 480
    height = 80
    x = (win.winfo_screenwidth()-width) // 2
    y = (win.winfo_screenheight()-height) // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    button1 = tkinter.Button(win, text="  字符球体  ", command=lambda:sup1())
    button2 = tkinter.Button(win, text="  闪闪闪  ", command=lambda:sup2())
    button3 = tkinter.Button(win, text="  字符雨  ", command=lambda:sup3())
    button4 = tkinter.Button(win, text="  web版下雨  ", command=lambda:sup4())
    button5 = tkinter.Button(win, text="   返回   ", command=lambda:EXIT(win, _win))
    button5.pack(side=tkinter.RIGHT)
    button1.pack(side=tkinter.LEFT)
    button2.pack(side=tkinter.LEFT)
    button3.pack(side=tkinter.LEFT)
    button4.pack(side=tkinter.LEFT)
    button5.pack(side=tkinter.RIGHT)
    win.mainloop()

    

def EXIT(_win, win):
    _win.withdraw()
    win.update()
    win.deiconify()


def serial_number(_win):
    n = '-'.join(["".join([chr(random.randint(65, 90)) if random.randint(0, 1) else str((random.randint(0, 9))) , chr(random.randint(65, 90)) if random.randint(0, 1) else str((random.randint(0, 9))), chr(random.randint(65, 90)) if random.randint(0, 1) else str((random.randint(0, 9))), chr(random.randint(65, 90)) if random.randint(0, 1) else str((random.randint(0, 9)))]) for i in range(4)])
    _win.withdraw()
    win = tkinter.Tk()
    win.title("序列号")
    width = 480
    height = 80
    x = (win.winfo_screenwidth()-width) // 2
    y = (win.winfo_screenheight()-height) // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    label1 = tkinter.Label(win, text=n)
    button4 = tkinter.Button(win, text="  复制  ", command=lambda:copy(n))
    button5 = tkinter.Button(win, text="   返回   ", command=lambda:EXIT(win, _win))
    label1.pack(side=tkinter.LEFT)
    button4.pack(side=tkinter.RIGHT)
    button5.pack(side=tkinter.RIGHT)
    win.mainloop()


def math_questions(_win):
    _win.withdraw()
    win = tkinter.Tk()
    win.title("常见数学问题")
    width = 410
    height = 80
    x = (win.winfo_screenwidth()-width) // 2
    y = (win.winfo_screenheight()-height) // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    button1 = tkinter.Button(win, text="  和差问题  ", command=lambda:math_sum_sub(win))
    button2 = tkinter.Button(win, text="  # TODO  ", command=lambda:   TODO  (win))
    button4 = tkinter.Button(win, text="    # TODO    ", command=lambda:  TODO  (win))
    button6 = tkinter.Button(win, text="  # TODO  ", command=lambda:  TODO  (win, _win))
    button3 = tkinter.Button(win, text="   返回   ", command=lambda:EXIT(win, _win))
    button3.pack(side=tkinter.RIGHT)
    button6.pack(side=tkinter.RIGHT)
    button1.pack(side=tkinter.LEFT)
    button2.pack(side=tkinter.LEFT)
    button4.pack(side=tkinter.LEFT)
    win.mainloop()



def in_mah_sum_sub(_win, um, ub):
    b = (int(um) + int(ub)) / 2
    s = (int(um) - int(ub)) / 2
    _win.withdraw()
    win = tkinter.Tk()
    win.title("和差问题_值")
    width = 410
    height = 80
    x = (win.winfo_screenwidth()-width) // 2
    y = (win.winfo_screenheight()-height) // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    label1 = tkinter.Label(win, text="大数 : {}".format(b))
    label2 = tkinter.Label(win, text=" || 小数 : {}".format(s))
    button2 = tkinter.Button(win, text="  复制  ", command=lambda:copy("大数: {}, 小数: {}".format(b, s)))
    button3 = tkinter.Button(win, text="   返回   ", command=lambda:EXIT(win, _win))
    button3.pack(side=tkinter.RIGHT)
    button2.pack(side=tkinter.RIGHT)
    label1.pack(side=tkinter.LEFT)
    label2.pack(side=tkinter.LEFT)
    win.mainloop()



def math_sum_sub(_win):
    _win.withdraw()
    win = tkinter.Tk()
    win.title("和差问题")
    width = 410
    height = 80
    x = (win.winfo_screenwidth()-width) // 2
    y = (win.winfo_screenheight()-height) // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    label1 = tkinter.Label(win, text="和 : ")
    entry1 = tkinter.Entry(win, width=18)
    label2 = tkinter.Label(win, text="  差 : ")
    entry2 = tkinter.Entry(win, width=18)
    button2 = tkinter.Button(win, text="  求两数值  ", command=lambda:in_mah_sum_sub(win, entry1.get(), entry2.get()))
    button3 = tkinter.Button(win, text="   返回   ", command=lambda:EXIT(win, _win))
    button3.pack(side=tkinter.RIGHT)
    button2.pack(side=tkinter.RIGHT)
    label1.pack(side=tkinter.LEFT)
    entry1.pack(side=tkinter.LEFT)
    label2.pack(side=tkinter.LEFT)
    entry2.pack(side=tkinter.LEFT)
    win.mainloop()
    

def More_page_3(_win, first_win):
    _win.withdraw()
    win = tkinter.Tk()
    win.title("更多功能: 第 3 页")
    width = 410
    height = 80
    x = (win.winfo_screenwidth()-width) // 2
    y = (win.winfo_screenheight()-height) // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    button1 = tkinter.Button(win, text="  小惊喜  ", command=lambda:suprise(win))
    button2 = tkinter.Button(win, text="  打开指定文件  ", command=lambda:start_file(win))
    button4 = tkinter.Button(win, text="    打开命令行    ", command=lambda:terminal())
    button6 = tkinter.Button(win, text="  上一页  ", command=lambda:EXIT(win, _win))
    button3 = tkinter.Button(win, text="   返回   ", command=lambda:EXIT(win, first_win))
    button3.pack(side=tkinter.RIGHT)
    button6.pack(side=tkinter.RIGHT)
    button1.pack(side=tkinter.LEFT)
    button2.pack(side=tkinter.LEFT)
    button4.pack(side=tkinter.LEFT)
    win.mainloop()
    


def More_page_2(_win, first_win):
    _win.withdraw()
    win = tkinter.Tk()
    win.title("更多功能: 第 2 页")
    width = 650
    height = 80
    x = (win.winfo_screenwidth()-width) // 2
    y = (win.winfo_screenheight()-height) // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    # TODO
    button1 = tkinter.Button(win, text="  常见数学问题  ", command=lambda:math_questions(win))
    # ☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝
    button2 = tkinter.Button(win, text="生成序列号（XXXX-XXXX-XXXX-XXXX)", command=lambda:serial_number(win))
    button4 = tkinter.Button(win, text="    生成随机码    ", command=lambda:random_code(win))
    button5 = tkinter.Button(win, text="  下一页  ", command=lambda:More_page_3(win, first_win))
    button6 = tkinter.Button(win, text="  上一页  ", command=lambda:EXIT(win, _win))
    button3 = tkinter.Button(win, text="   返回   ", command=lambda:EXIT(win, first_win))
    button3.pack(side=tkinter.RIGHT)
    button5.pack(side=tkinter.RIGHT)
    button6.pack(side=tkinter.RIGHT)
    button1.pack(side=tkinter.LEFT)
    button2.pack(side=tkinter.LEFT)
    button4.pack(side=tkinter.LEFT)
    win.mainloop()



def More_page_1(_win):
    _win.withdraw()
    win = tkinter.Tk()
    win.title("更多功能: 第 1 页")
    width = 450
    height = 80
    x = (win.winfo_screenwidth()-width) // 2
    y = (win.winfo_screenheight()-height) // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    button1 = tkinter.Button(win, text="  哈希MD5  ", command=lambda:HASH(win))
    button2 = tkinter.Button(win, text="  ASCII码  ", command=lambda:ASCII(win))
    button4 = tkinter.Button(win, text="    计算器    ", command=lambda:com(win))
    button5 = tkinter.Button(win, text="  下一页  ", command=lambda:More_page_2(win, _win))
    button3 = tkinter.Button(win, text="   返回   ", command=lambda:EXIT(win, _win))
    button3.pack(side=tkinter.RIGHT)
    button5.pack(side=tkinter.RIGHT)
    button1.pack(side=tkinter.LEFT)
    button2.pack(side=tkinter.LEFT)
    button4.pack(side=tkinter.LEFT)
    win.mainloop()


def ORD(n):
    try:
        tkinter.messagebox.showinfo("ASCII", ord(n))
    except:
        tkinter.messagebox.showerror("错误", "输入不正确!")

def CHR(n):
    try:
        n = int(n)
        tkinter.messagebox.showinfo("字符", chr(n))
    except:
        tkinter.messagebox.showerror("错误", "输入不正确!")

def ASCII(_win):
    _win.withdraw()
    win = tkinter.Tk()
    win.title("ASCII码---对照查询")
    width = 900
    height = 80
    x = (win.winfo_screenwidth()-width) // 2
    y = (win.winfo_screenheight()-height) // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    label1 = tkinter.Label(win, text="ASCII码:")
    entry1 = tkinter.Entry(win, width=32)
    entry2 = tkinter.Entry(win, width=32)
    label2 = tkinter.Label(win, text="字符:")
    button1 = tkinter.Button(win, text=" 获取ASCII码 ", command=lambda:ORD(entry1.get()))
    button3 = tkinter.Button(win, text=" 获取对应字符 ", command=lambda:CHR(entry2.get()))
    button2 = tkinter.Button(win, text="  退出  ", command=lambda:EXIT(win, _win))
    label2.pack(side=tkinter.LEFT)
    entry1.pack(side=tkinter.LEFT)
    button1.pack(side=tkinter.LEFT)
    label1.pack(side=tkinter.LEFT)
    entry2.pack(side=tkinter.LEFT)
    button3.pack(side=tkinter.LEFT)
    button2.pack(side=tkinter.RIGHT)
    win.mainloop()


def GetHash(n, _win):
    try:
        s = hashlib.md5(n.encode(encoding="utf-8")).hexdigest()
        _win.withdraw()
        win = tkinter.Tk()
        win.title(" 哈希值 ")
        width = 412
        height = 30
        x = (win.winfo_screenwidth()-width) // 2
        y = (win.winfo_screenheight()-height) // 2
        win.geometry("{}x{}+{}+{}".format(width, height, x, y))
        label1 = tkinter.Label(win, text="  md5值为:{}    ".format(s))
        button1 = tkinter.Button(win, text="  确定 ", command=lambda:EXIT(win, _win))
        button2 = tkinter.Button(win, text=" 复制结果 ", command=lambda:copy(s))
        label1.pack(side=tkinter.LEFT)
        button1.pack(side=tkinter.LEFT)
        button2.pack(side=tkinter.LEFT)
        win.mainloop()
    except:
        tkinter.messagebox.showerror("错误", "输入不正确!")

def HASH(_win):
    _win.withdraw()
    win = tkinter.Tk()
    win.title("Hash MD5 哈希---对照查询")
    width = 500
    height = 80
    x = (win.winfo_screenwidth()-width) // 2
    y = (win.winfo_screenheight()-height) // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    label1 = tkinter.Label(win, text="需要加密的的原文:")
    entry1 = tkinter.Entry(win, width=32)
    button1 = tkinter.Button(win, text=" 获取MD5值 ", command=lambda:GetHash(entry1.get(), win))
    button2 = tkinter.Button(win, text="  退出  ", command=lambda:quit(_win, win))
    label1.pack(side=tkinter.LEFT)
    entry1.pack(side=tkinter.LEFT)
    button1.pack(side=tkinter.LEFT)
    button2.pack(side=tkinter.RIGHT)
    win.mainloop()


def NextStep(n, _win, win, an):
    m = hashlib.md5(n.encode(encoding="utf-8")).hexdigest()
    if m == an:
        _win.withdraw()
        reg(win)
    else:
        tkinter.messagebox.showerror("错误", "填写错误!")

def que(_win):
    _win.withdraw()
    win = tkinter.Tk()
    win.title("安全问题")
    width = 430
    height = 80
    x = (win.winfo_screenwidth()-width) // 2
    y = (win.winfo_screenheight()-height) // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    que_dict = None
    File = "X:\\Files\\SafetyQuetions.txt"
    try:
        if os.path.exists(File):
            _f = open(File, "r", encoding='utf-8')
            _uesr = _f.read()
            _f.close()
            que_dict = eval(_uesr)
        else:
            pass
    except Exception as e:
        tkinter.messagebox.showerror("ERROR", "Something was error!({})".format(e))
        if _f:
            _f.close()
    # in_dict_pwd = hashlib.md5(password.encode(encoding="utf-8")).hexdigest()
    # _dict = {"username":username, "password":in_dict_pwd}
    # if _dict == user_dict:
    #     in_inside(win)
    # else:
    #     ipt_error()
    if que_dict == None:
        tkinter.messagebox.showerror("安全问题", "您还没有设置安全问题！")
        win.withdraw()
        _win.update()
        _win.deiconify()
    else:
        label1 = tkinter.Label(win, text="  {} ".format(que_dict["que"]))
        entry1 = tkinter.Entry(win, width=25)
        button1 = tkinter.Button(win, text="下一步", command=lambda: NextStep(entry1.get(), win, _win, que_dict["ans"]))
        button2 = tkinter.Button(win, text="退出", command=lambda:quit(_win, win))
        label1.pack(side=tkinter.LEFT)
        entry1.pack(side=tkinter.LEFT)
        button1.pack(side=tkinter.LEFT)
        button2.pack(side=tkinter.RIGHT)
        win.mainloop()
    

def TurnSleep():
    tkinter.messagebox.showinfo(None, "睡眠中...")
    time.sleep(0.5)
    os.system('Rundll32.exe Powrprof.dll,SetSuspendState Sleep')


def TurnOff():
    tkinter.messagebox.showinfo(None, "关机中...")
    time.sleep(0.5)
    os.system("shutdown -s -t 0")

def quit(_win, win):
    win.withdraw()
    _win.update()
    _win.deiconify()

def Sleep(_win):
    _win.withdraw()
    win = tkinter.Tk()
    win.title("确定睡眠?")
    width = 230
    height = 80
    x = (win.winfo_screenwidth()-width) // 2
    y = (win.winfo_screenheight()-height) // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    _button1 = tkinter.Button(win, text="确定(短按电源键可唤醒)", command=TurnSleep)
    _button2 = tkinter.Button(win, text="取消", command=lambda:quit(_win, win))
    _button1.pack(side=tkinter.LEFT)
    _button2.pack(side=tkinter.RIGHT)
    win.mainloop()

def Off(_win):
    _win.withdraw()
    win = tkinter.Tk()
    win.title("确定关机?")
    width = 230
    height = 80
    x = (win.winfo_screenwidth()-width) // 2
    y = (win.winfo_screenheight()-height) // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    _button1 = tkinter.Button(win, text="确定(注意!此操作不可逆!)", command=TurnOff)
    _button2 = tkinter.Button(win, text="取消", command=lambda:quit(_win, win))
    _button1.pack(side=tkinter.LEFT)
    _button2.pack(side=tkinter.RIGHT)
    win.mainloop()
 
def ipt_error():
    tkinter.messagebox.showinfo("error", "用户名或密码错误!")

def cancel(_w, _m):
    _w.withdraw()
    _m.update()
    _m.deiconify()

def close(_win, win):
    _win.withdraw()
    win.update()
    win.deiconify()

def _set(username, password):
    File = "X:\\Files\\info.txt"
    pwd_md5 = hashlib.md5(password.encode(encoding="utf-8")).hexdigest()
    _f = open(File, "w")
    user_dict = {"username":username, "password":pwd_md5}
    _f.write(str(user_dict))
    _f.close()
    tkinter.messagebox.showinfo("massage", "设置成功!")

def log_in(username, password):
    user_dict = None
    os.system("cls")
    File = "X:\\Files\\info.txt"
    try:
        if os.path.exists(File):
            _f = open(File, "r", encoding='utf-8')
            _uesr = _f.read()
            _f.close()
            user_dict = eval(_uesr)
        else:
            tkinter.messagebox.showwarning("messseage", "您还没有账户!")
    except Exception as e:
        tkinter.messagebox.showerror("ERROR","Something was error!({})".format(e))
        if _f:
            _f.close()

    in_dict_pwd = hashlib.md5(password.encode(encoding="utf-8")).hexdigest()
    _dict = {"username":username, "password":in_dict_pwd}
    if _dict == user_dict:
        return True
    else:
        return False
    # tkinter.messagebox.showinfo("massage", "welcome!dear {}".format(username))


def _log_in(a, b, _win):
    if log_in(a, b):
        in_inside(_win)
    elif log_in(a, b) == False:
        tkinter.messagebox.showerror("错误", "用户名或密码不正确!")
    

"""_____________________________________________________________________________________"""

def reg(win):
    w = tkinter.Tk()
    w.title("Set")
    width = 850
    height = 50
    x = (w.winfo_screenwidth()-width) // 2
    y = (w.winfo_screenheight()-height) // 2
    w.geometry("{}x{}+{}+{}".format(width, height, x, y))
    _label1 = tkinter.Label(w,text="  用户名: ")
    _entry1 = tkinter.Entry(w,width=30)
    
    _label2 = tkinter.Label(w,text="  密码: ")
    _entry2 = tkinter.Entry(w,width=27, show="●")
    
    _button1 = tkinter.Button(w,text="  注册  ", command=lambda:_set(_entry1.get(), _entry2.get()))
    
    _button2 = tkinter.Button(w,text="  返回  ", command=lambda:close(w, win))

    _label1.pack(side=tkinter.LEFT)
    _entry1.pack(side=tkinter.LEFT)
    _label2.pack(side=tkinter.LEFT)
    _entry2.pack(side=tkinter.LEFT)
    _button1.pack(side=tkinter.LEFT)
    _button2.pack(side=tkinter.RIGHT)
    # username = entry1.get()
    # password = entry2.get()
    # pwd_md5 = hashlib.md5(password.encode(encoding="utf-8")).hexdigest()
    # _f = open(File, "w")
    # user_dict = {"username":username, "password":pwd_md5}
    # _f.write(str(user_dict))
    # _f.close()
    # tkinter.messagebox.showinfo("massage", "Set success!")
    w.mainloop()



def main_win():
    File = "X:\\Files\\SafetyQuetions.txt"
    file = "X:\\Files\\info.txt"
    win = tkinter.Tk()
    win.title("Python工具箱")
    width = 800
    height = 50
    x = (win.winfo_screenwidth()-width) // 2
    y = (win.winfo_screenheight()-height) // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))

    label1 = tkinter.Label(text="  用户名: ")
    entry1 = tkinter.Entry(width=30)
    
    label2 = tkinter.Label(text="  密码: ")
    entry2 = tkinter.Entry(width=27, show="●")
    
    button1 = tkinter.Button(text="  登录  ", command=lambda:_log_in(entry1.get(), entry2.get(), win))
    _button3 = tkinter.Button(text=" 设置安全问题 ", command=lambda:BeforeSetQue(win))

    button2 = tkinter.Button(text="  注册  ", command=lambda:reg(win))
    _button2 = tkinter.Button(text="  重设密码  ", command=lambda:que(win))

    label1.pack(side=tkinter.LEFT)
    entry1.pack(side=tkinter.LEFT)
    label2.pack(side=tkinter.LEFT)
    entry2.pack(side=tkinter.LEFT)
    button1.pack(side=tkinter.LEFT)
    
    if not os.path.exists(File):
        _button3.pack(side=tkinter.RIGHT)

    if not os.path.exists(file):
        button2.pack(side=tkinter.RIGHT)
    else:
        _button2.pack(side=tkinter.RIGHT)

    win.mainloop()
    
def in_inside(_win):
    _win.withdraw()
    win = tkinter.Tk()
    win.title("welcome")
    width = 500
    height = 270
    x = (win.winfo_screenwidth()-width) // 2
    y = (win.winfo_screenheight()-height) // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    button3 = tkinter.Button(win, text=" 退出登录 ", command=lambda: cancel(win, _win))
    button4 = tkinter.Button(win, text="   关机   ", command=lambda: Off(win))
    button5 = tkinter.Button(win, text="   睡眠   ", command=lambda: Sleep(win))
    button6 = tkinter.Button(win, text="    更多    ", command=lambda: More_page_1(win))
    button7 = tkinter.Button(win, text=" 设置安全问题 ", command=lambda: SetQue(win))
    button8 = tkinter.Button(win, text=" --- 密码盒 --- ", command=lambda: pwd_box(win))
    button4.pack(side=tkinter.LEFT)
    button5.pack(side=tkinter.LEFT)
    button8.pack(side=tkinter.RIGHT)
    button7.pack()
    button6.pack()
    button3.pack()
    win.mainloop()

if __name__ == "__main__":
    main_win()
