# def fib (n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a**b
#     # return b
#     yield b

# for i in range(100):
#     print(fib(i))

# class student:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

#     def watchMovies(self):
#         print("I can watch movies")
    
# zhangsan = student("zhangsan", "13", "male")
# print(zhangsan.name)
# zhangsan.watchMovies()


# class human(object):
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

#     def run(self):
#         print("I can run!")


# class perents(human):
#     def __init__(self, name, age, sex, card_id):
#         super().__init__(name, age, sex)
#         self.card_id = card_id
    
#     def study(self):
#         print("I can study")
    
#     def __PlayFootball(self):
#         print("I can play football")


# class kids(perents):
#     def __init__(self, name, age, sex, card_id):
#         super().__init__(name, age, sex, card_id)
    
#     def sing(self):
#         print("I can sing")

    
# lisi = kids("lisi", 19, "male", "51013620050326796x")
# lisi.study()
# try:
#     lisi.__PlayFootball()

# except AttributeError as e:
#     print("can not visit this function")



# import time
# def timer(func):
#     def count_time():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         print("Used {} seconds".format(end_time -start_time))
#         return None
#     return count_time
# @timer
# def test():
#     f = open("C:\\Users\\asus\\Desktop\\chenxuyux.txt", "r", encoding='utf-8')
#     f.read()
# test()

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

# print("welcome!dear {}".format(username))
# admin = True


# def permission(func):
#     global admin
#     def permission_func(*args, **kwargs):
#         if admin:
#             func(*args, **kwargs)
#         else:
#             print("You haven't any permission to access thins function!")
#         return None
#     return permission_func


# @permission
# def test(x, y):
#     print(x**y)

# test(100, 9)

#!/usr/bin/env python
# -*- coding:utf-8 -*-

# import tkinter


# def func():
#     print("aaaaaaaaaaaaaaaaaaaaaaa")


# win = tkinter.Tk()
# win.title("yudanqu")
# win.geometry("400x400+200+50")



# button1 = tkinter.Button(win, text="按钮", command=func, width=10, height=10)
# button1.pack()

# button2 = tkinter.Button(win, text="按钮", command=lambda: print("bbbbbbbbbbbb"))
# button2.pack()

# button3 = tkinter.Button(win, text="退出", command=win.quit)
# button3.pack()

# win.mainloop()

#!/usr/bin/env python
# -*- coding:utf-8 -*-

# import tkinter

# win = tkinter.Tk()
# win.title("yudanqu")
# win.geometry("400x400+200+50")

# '''
# Entry：输入控件，用于显示简单的文本内容
# '''

# # 密文显示
# entry1 = tkinter.Entry(win, show="*") # show="*" 可以表示输入密码
# entry1.pack()

# # 绑定变量
# e = tkinter.Variable()

# entry2 = tkinter.Entry(win, textvariable=e)
# entry2.pack()

# # e就代表输入框这个对象
# # 设置值
# e.set("wewewewewewe")
# # 取值
# print(e.get())
# print(entry2.get())

# win.mainloop()

# class Employee(object):
#     def __init__(self, name):
#         self.name = name

#     def _salary(self):
#         print("I have salary.")
        
# class Manager(Employee):
#     def __init__(self, name):
#         super().__init__(name)

#     def _salary(self):
#         print("My salary is $15000 .")

# class Programmer(Employee):
#     def __init__(self, name, hours):
#         super().__init__(name)
#         self.hours = hours

#     def _salary(self):
#         print("My salary is ${} .".format(150*self.hours))
        
# class Seller(Employee):
#     def __init__(self, name, money):
#         super().__init__(name)
#         self.money = money

#     def _salary(self):
#         print("My salary is ${}  .".format(int(0.05*self.money+1200)))

# M = Manager("ZhangSan")
# M._salary()
# P = Programmer("LiSi", 160)
# P._salary()
# S = Seller("WangWu", 100000)
# S._salary()

# import tkinter
# import tkinter.messagebox

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

# def main_win():
#     win = tkinter.Tk()
#     win.title("This is my first desktop execute!")
#     width = 400
#     height = 70
#     x = (win.winfo_screenwidth()-width) // 2
#     y = (win.winfo_screenheight()-height) // 2
#     win.geometry("{}x{}+{}+{}".format(width, height, x, y))
#     button1 = tkinter.Button(text="Log in now!", command=log_in)

#     label1 = tkinter.Label(text="username:")
#     entry1 = tkinter.Entry(width=13)
    
#     label2 = tkinter.Label(text="password")
#     entry2 = tkinter.Entry(width=13, show="●")
    
#     label1.pack(side=tkinter.LEFT)
#     entry1.pack(side=tkinter.LEFT)
#     label2.pack(side=tkinter.LEFT)
#     entry2.pack(side=tkinter.LEFT)
#     button1.pack(side=tkinter.LEFT)
#     win.mainloop()
    
# if __name__ == "__main__":
#     main_win()

# import hashlib

# x = 'zhang'
# a = hashlib.md5(x.encode(encoding="utf-8")).hexdigest()

# """________________________________________________________________________________"""

# print("%.{}f".format(2) % 2.645)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# =============================================================================
# _____________________________________________________________________________
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# -----------------------------------------------------------------------------
# .............................................................................
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# def avg(C, M, E):
#     int_C, int_M, int_E = float(C), float(M), float(E)
#     return (int_C + int_M + int_E) / 3

# if __name__ == "__main__"
#     print(avg(97, 100, 78))




# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# =============================================================================
# _____________________________________________________________________________
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# -----------------------------------------------------------------------------
# .............................................................................
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# def level(score):
#     if score >= 90 and score <= 100:
#         return "Excellent!"
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

# if __name__ == "__main__":
#     while 1:
#         ipt = input("Please input your score:")
#         level(ipt)



# def APsum(last):
#     sum = 0
#     for i in range(last+1):
#         sum += i
#     print(sum)
# APsum(100)

num, total = 0, 0
while num <= 50:
    total = total + num
    num = num + 2
print (total)