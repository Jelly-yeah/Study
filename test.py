# sum = 0
# for i in range(0 , int(input())+1):
#     if i % 2==1:
#        sum = sum + 1
# print(sum)
#

import tkinter
for i in range(50):
    #    tkinter.messagebox.showerror()
    #    tkinter.messagebox.showinfo()
    win = tkinter.Tk()
    win.title(" 木马病毒 ")
    width = 100
    height = 100
    x = (win.winfo_screenwidth()-width) // 2
    y = (win.winfo_screenheight()-height) // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    button1 = tkinter.Button(win, text=" 关闭 ", command=win.withdraw())
    button1.pack(side=tkinter.LEFT)
    win.mainloop()
