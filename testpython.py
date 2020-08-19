# def fib (n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a**b
#     # return b
#     yield b
#
# for i in range(100):
#     print(fib(i))
#
# class student:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def watchMovies(self):
#         print("I can watch movies")
#
# zhangsan = student("zhangsan", "13", "male")
# print(zhangsan.name)
# zhangsan.watchMovies()
#
#
# class human(object):
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def run(self):
#         print("I can run!")
#
#
# class perents(human):
#     def __init__(self, name, age, sex, card_id):
#         super().__init__(name, age, sex)
#         self.card_id = card_id
#
#     def study(self):
#         print("I can study")
#
#     def __PlayFootball(self):
#         print("I can play football")
#
#
# class kids(perents):
#     def __init__(self, name, age, sex, card_id):
#         super().__init__(name, age, sex, card_id)
#
#     def sing(self):
#         print("I can sing")
#
#
# lisi = kids("lisi", 19, "male", "51013620050326796x")
# lisi.study()
# try:
#     lisi.__PlayFootball()
#
# except AttributeError as e:
#     print("can not visit this function")
#
# import time
# # def timer(func):
# #     def count_time():
# #         start_time = time.time()
# #         func()
# #         end_time = time.time()
# #         print("Used {} seconds".format(end_time -start_time))
# #         return None
# #     return count_time
# # @timer
# # def test():
# #     f = open("C:\\Users\\asus\\Desktop\\chenxuyux.txt", "r", encoding='utf-8')
# #     f.read()
# # test()
#
# import os, time
# a = 0
# admin = False
# username = input("Please set your username:")
# password = input("Please set your passsword:")
# os.system("cls")
# while True:
#     if a == 0:
#         _username = input("Please input your username:")
#         _password = input("Please input your passsword:")
#         if username == _username and password == _password:
#             break
#         else:
#             a += 1
#     else:
#         print("password or username was wrong!")
#         time.sleep(0.8)
#         os.system("cls")
#         _username = input("Please input your username:")
#         _password = input("Please input your passsword:")
#         if username == _username and password == _password:
#             break
#         else:
#             continue
#
# print("welcome!dear {}".format(username))
# admin = True
#
#
# def permission(func):
#     global admin
#     def permission_func(*args, **kwargs):
#         if admin:
#             func(*args, **kwargs)
#         else:
#             print("You haven't any permission to access thins function!")
#         return None
#     return permission_func
#
#
# @permission
# def test(x, y):
#     print(x**y)
#
# test(100, 9)
#
# # !/usr/bin/env python
# # -*- coding:utf-8 -*-
#
# import tkinter
#
#
# def func():
#     print("aaaaaaaaaaaaaaaaaaaaaaa")
#
#
# win = tkinter.Tk()
# win.title("yudanqu")
# win.geometry("400x400+200+50")
#
# button1 = tkinter.Button(win, text="按钮", command=func, width=10, height=10)
# button1.pack()
#
# button2 = tkinter.Button(win, text="按钮", command=lambda: print("bbbbbbbbbbbb"))
# button2.pack()
#
# button3 = tkinter.Button(win, text="退出", command=win.quit)
# button3.pack()
#
# win.mainloop()
#
# # !/usr/bin/env python
# # -*- coding:utf-8 -*-
#
# import tkinter
#
# win = tkinter.Tk()
# win.title("yudanqu")
# win.geometry("400x400+200+50")
#
# '''
# Entry：输入控件，用于显示简单的文本内容
# '''
#
# 密文显示
# entry1 = tkinter.Entry(win, show="*") # show="*" 可以表示输入密码
# entry1.pack()
#
# # 绑定变量
# e = tkinter.Variable()
#
# entry2 = tkinter.Entry(win, textvariable=e)
# entry2.pack()
#
# e就代表输入框这个对象
# 设置值
# e.set("wewewewewewe")
# 取值
# print(e.get())
# print(entry2.get())
#
# win.mainloop()
#
# class Employee(object):
#     def __init__(self, name):
#         self.name = name
#
#     def _salary(self):
#         print("I have salary.")
#
# class Manager(Employee):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def _salary(self):
#         print("My salary is $15000 .")
#
# class Programmer(Employee):
#     def __init__(self, name, hours):
#         super().__init__(name)
#         self.hours = hours
#
#     def _salary(self):
#         print("My salary is ${} .".format(150*self.hours))
#
# class Seller(Employee):
#     def __init__(self, name, money):
#         super().__init__(name)
#         self.money = money
#
#     def _salary(self):
#         print("My salary is ${}  .".format(int(0.05*self.money+1200)))
#
# M = Manager("ZhangSan")
# M._salary()
# P = Programmer("LiSi", 160)
# P._salary()
# S = Seller("WangWu", 100000)
# S._salary()
#
# import tkinter
# import tkinter.messagebox
#
# def log_in():
#     # win = tkinter.Tk()
#     # win.title("Hello!")
#     # width = 600
#     # height = 300
#     # x = (win.winfo_screenwidth()-width) // 2
#     # y = (win.winfo_screenheight()-height) // 2
#     # win.geometry("{}x{}+{}+{}".format(width, height, x, y))
#     tkinter.messagebox.showerror("messseage", "Hello")
#     tkinter.messagebox.showwarning("messseage", "Hello")
#     tkinter.messagebox.showinfo("messseage", "Hello")
#
# def main_win():
#     win = tkinter.Tk()
#     win.title("This is my first desktop execute!")
#     width = 400
#     height = 70
#     x = (win.winfo_screenwidth()-width) // 2
#     y = (win.winfo_screenheight()-height) // 2
#     win.geometry("{}x{}+{}+{}".format(width, height, x, y))
#     button1 = tkinter.Button(text="Log in now!", command=log_in)
#
#     label1 = tkinter.Label(text="username:")
#     entry1 = tkinter.Entry(width=13)
#
#     label2 = tkinter.Label(text="password")
#     entry2 = tkinter.Entry(width=13, show="●")
#
#     label1.pack(side=tkinter.LEFT)
#     entry1.pack(side=tkinter.LEFT)
#     label2.pack(side=tkinter.LEFT)
#     entry2.pack(side=tkinter.LEFT)
#     button1.pack(side=tkinter.LEFT)
#     win.mainloop()
#
# if __name__ == "__main__":
#     main_win()
#
# import hashlib
#
# x = 'zhang'
# a = hashlib.md5(x.encode(encoding="utf-8")).hexdigest()
#
# """________________________________________________________________________________"""
#
# print("%.{}f".format(2) % 2.645)
#
# # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# # =============================================================================
# # _____________________________________________________________________________
# # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# # -----------------------------------------------------------------------------
# # .............................................................................
# # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#
# def avg(C, M, E):
#     int_C, int_M, int_E = float(C), float(M), float(E)
#     return (int_C + int_M + int_E) / 3
#
# if __name__ == "__main__":
#     print(avg(97, 100, 78))
#
# # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# # =============================================================================
# # _____________________________________________________________________________
# # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# # -----------------------------------------------------------------------------
# # .............................................................................
# # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#
# def level(score):
#     if score >= 90 and score <= 100:
#         return "Excellent!"`
#     elif score < 90 and score >= 80:
#         return "Good"
#     elif score < 90 and score >= 70:
#         return "Medium"
#     elif score < 70 and score >= 60:
#         return "Pass"
#     elif score < 60 and score >= 0:
#         return "Fill"
#     elif score < 0 or score >100:
#         return "EEROR -- # Out of Range #"
#     else:
#         return "EEROR -- # Plese Input The Number #"
#
# if __name__ == "__main__":
#     while 1:
#         ipt = input("Please input your score:")
#         level(ipt)
#
# def APsum(last):
#     sum = 0
#     for i in range(last+1):
#         sum += i
#     print(sum)
# APsum(100)
# num, total = 0, 0
# while num <= 50:
#     total = total + num
#     num = num + 2
# print(total)
# # ========================================================
# def get_input(n):
#     return [int(i) for i in n.split(" ")]
#
#
# def main_func():
#     a, b = get_input(input())
#     book_id_list = []
#     need_code_list = []
#     len_need_code_list = []
#     for i in range(a):
#         book_id_list.append(input())
#     for j in range(b):
#         a, b = get_input(input())
#     need_code_list.append(a)
#     len_need_code_list.append(b)
#     for m in need_code_list:
#         m = str(m)
#         need_code_list.append(m)
#     for n in book_id_list:
#         n = str(n)
#         need_code_list.append(n)
#     res = []
#     for i in need_code_list:
#         for j in len_need_code_list:
#             for k in book_id_list:
#                 if i == k[-(j+1):]:
#                     res.append(k)
#                 elif i != k[-(j+1):]:
#                     res.append(-1)
#     for p in res:
#         print(p)
#
#
# if __name__ == "__main__":
#     main_func()
#
# lst = []
# for i in range(1, 101):
#     lst.append(i)
# print(sum(lst))
#
# a = 1
# for i in range(1,11):
#     a = a * i
# print(a)
#
# def fac(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fac(n-1)
#
# print(fac(10))
#
# def _sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n + _sum(n-1)
# print(_sum(100))
#
# def Fib(n):
#     if n == 1 or n == 2:
#         return (n, 1)
#     else:
#         a, b = Fib(n-1)
#         return (a + b, a)
# for i in range(1, 1000):
#     print("{}   fib: {}".format(i, Fib(i)[1]))
# import tkinter
#
#
# def hanoi(n, a, b, c):
#     if n == 1:
#         print("|{}| -> |{}|".format(a, c))
#     else:
#         hanoi(n-1, a, c, b)
#         print("|{}| -> |{}|".format(a, c))
#         hanoi(n-1, b, a, c)
#
#
# hanoi(3, 'A', 'B', 'C')
#
#
# def s(n: object) -> object:
#     if n < 10:
#         print("{}-".format(n), end="")
#     else:
#         s(n%(n//10))
#
#
# if __name__ == "__main__":
#     s(int(input(':::')))
#
#
# def monkey_eat_peach(n):
#     if n == 7:
#         return 1
#     else:
#         return (monkey_eat_peach(n+1) + 1) * 2
#
#
# print(monkey_eat_peach(0))
#
# def perm(lst, p, q):
#     if p == q:
#         print("".join(lst[0:q+1]))
#     else:
#         for i in range(p, q+1):
#             lst[p], lst[i] = lst[i], lst[p]
#             perm(lst, p+1, q)
#             lst[p], lst[i] = lst[i], lst[p]
#
#
# a = list("1A)'n+=")
# perm(a, 0, len(a)-1)
#
# import sys
#
#
# def gcd(x, y):
#     if x % y == 0 or y % x == 0:
#         print(str(x if x <= y else y))
#     else:
#         gcd(y, x % y)
#
#
# gcd(6, 4)
#
#
# def is_multiple(n, m):
#     if n % m == 0:
#         return True
#     else:
#         return False
#
#
# def is_even(k):
#     if int(k[-1]) in [0, 2, 4, 6, 8]:
#         return True
#     else:
#         return False
#
#
# print(is_even(input(":::")))
#
#
# def minmax(data):
#     return (sorted(data)[0], sorted(data)[-1])
#
#
#
# def func(n):
#     a = []
#     for i in range(1, n+1):
#         if i % 2 == 1:
#             a.append(i ** 2)
#         else:
#             pass
#     return sum(a)
#
#
# print(func(5))
#
#
# class Person(object):
#     def __init__(self, name, age, gender, height, weight, skin_color, nationality, _id):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.height = height
#         self.weight = weight
#         self.skin_color = skin_color
#         self.nationality = nationality
#         self.ID = _id
#
#     def play(self, what):
#         print("{} can play: {}".format(self.name, what))
#
#
# class ChinesePerson(Person):
#     def sing(self, what):
#         print("{} can sing 《{}》".format(self.name, what))
#
#
# if __name__ == "__main__":
#     jeff = ChinesePerson("Jeff Li", 18, 'male', 180, 70, "yellow", "Chinese", '41000220020101113X')
#     jeff.play("football")
#     jeff.sing("two big doudous")
#
#
# class Bird(object):
#     def __init__(self, color):
#         self.color = color
#
#     def say(self):
#         print("一只%s的小鸟在叽叽喳喳地叫" % self.color)
#
#
# class Parrot(Bird):
#     def say(self, what):
#         print('一只%s的鹦鹉在说:"%s"' % (self.color, what))
#
#
# b = Parrot("蓝色")
# b.say("你好")
#
# from turtle import *
#
# import random
# pencolor("orange")
# pensize(40)
# pc = ["red", "yellow", "orange", "green", "blue", "purple", "pink"]
# for _ in range(99999):
#     for j in range(9):
#         for i in range(7):
#             fd(7)
#             pencolor(pc[i])
#     rt(random.randint(0, 360))
#
#
# print(list(range(8, -9, -2)))
#
# a = []
# for i in range(0, 8+1):
#     a.append(2 ** i)
#
# print(a)
#
# a = [0]
# b = list(range(2, 19, 2))
# for j in range(9):
#     a.append(a[j] + b[j])
# print(a)
#
# print([i * (i+1) for i in range(10)])
#
# a = []
# for i in range(97, 123):
#     a.append(chr(i))
# print(a)
#
# def aeiou(n):
#     s = 0
#     a = ['a', 'e', 'i', 'o', 'u']
#     for i in range(len(n)):
#         if n[i].lower() in a:
#             s += 1
#     return s
#
#
# print(aeiou("aeiouAA"))
#
#
# def del_mark(n):
#     n = list(n)
#     m = []
#     for i in n:
#         if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122) or ord(i) == 32:
#             m.append(i)
#     print("".join(m))
#
#
# del_mark("hwad OPIKKJHVkjnrkjnfr")
#
#
# from abc import abstractmethod, ABCMeta
#
#
# class Human(metaclass=ABCMeta):
#     def __init__(self, *args, **kwargs):
#         self.name = args[0]
#
#     @abstractmethod
#     def say(self):
#         print("I can say")

#coding:utf-8

# import sys
# from PyQt5.QtWidgets import *
#
#
# app = QApplication(sys.argv)
# w = QWidget()
# w.resize(400, 150)
# screen = QDesktopWidget().screenGeometry()
# size = w.geometry()
# w.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
# w.setWindowTitle("垃圾")
# w.show()
# sys.exit(app.exec_())


# def jump_level(grade_number):
#     if grade_number == 1:
#         return 1
#     if grade_number == 2:
#         return 2
#     if grade_number == 3:
#         return 4
#     else:
#         return jump_level(grade_number - 1) + jump_level(grade_number - 2) + jump_level(grade_number - 3)
#
#
# if __name__ == '__main__':
#     print(jump_level(int(input("总年级数"))))


# def colouring():
#     pearl = list(input())
#     plan_number = int(input())
#     need_colour = []
#     s = 0
#     for _ in range(plan_number):
#         a = input()
#         low_index, high_index = int(a[0])-1, int(a[2])
#         for i in pearl[low_index:high_index]:
#             if i == "B":
#                 s += 1
#         need_colour.append(s)
#         s = 0
#     return need_colour
#
#
# if __name__ == '__main__':
#     print(colouring())


# def make_Palindrome(n):
#     length = 1
#     i = 1
#     while 1:
#         if n // i < 10:
#             break
#         else:
#             i *= 10
#             length += 1
#             continue
#     for j in range(length+1):
#         n += (n % 10) * (10 ** (length - 1))
#         n //= 10
#     return n
#
#
# print(make_Palindrome(int(input())))


# def sort(a):
#     res = []
#     times = len(a)
#     for _ in range(times):
#         res.append(min(a))
#         a.remove(min(a))
#     return res
#
#
# if __name__ == "__main__":
#     a = [1, 23, 75, 6, 68, 76754653, 432, 45, 67, 5434]
#     print(sort(a))


# def insert_sort(n):
#     m = []
#     for i in range(len(n)):
#         if i == 0:
#             m.append(n[0])
#         else:
#             for j in range(len(m), 0, -1):
#                 if n[i] <= m[0]:
#                     m.insert(0, n[i])
#                 elif m[j-1] <= n[i]:
#                     m.insert(j, n[i])
#                     break
#     return m
#
#
# print(insert_sort([1, 23, 75, 6, 68, 76754653, 432, 45, 67, 5434)

# def check(n, d):
#     n, d = str(n), str(d)
#     if n in d:
#         return True
#     return False
#


# def lcm(a, b, c=1):
#     if a * c % b != 0:
#         return lcm(a, b, c+1)
#     else:
#         return a * c
#
#
# a, b = input("Lcm for (use space yo split two numbers) : ").split(" ")
# print(lcm(int(a), int(b)))


# def gcd(a, b):
#     if a % b == 0:
#         return b
#     else:
#         return gcd(b, a % b)
#
#
# print(gcd(27, 18))

# y = 1
# while 1:
#     x = 400 - y
#     if x + y / 3 == 200:
#         print(x, y, sep=", ")
#         break
#     else:
#         y += 1


class class_name(object):
    def __init__(self, k: int) -> list:
        self.k = k

    def func(self, k):
        x: int = 1
        y: int = 1
        res: list = []
        while 1:
            dct: dict = {}
            x = (k * x + k * y) / y
            if x == (k * x + k * y) / y and x >= y:
                dct["x"] = x
                dct["y"] = y
                res.append(dct)
            elif x < y:
                break
            else:
                y += 1
        return res


c = class_name(int(input()))
