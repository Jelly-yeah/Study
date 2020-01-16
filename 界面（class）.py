#------------------------------------------------------------#
import tkinter  as tk
import hashlib as hash
import os as _
######################## 主界面 ###############################
class jiemian(object):
    def __init__(self, win, width, height, title):
        self.root = win
        self.root.title(title)
        self.frame = tk.Frame(win)
        
        """
        ↓ 生成主界面 ↓
        """
        x = (win.winfo_screenwidth()-width) // 2                    # ↓
        y = (win.winfo_screenheight()-height) // 2                  # ↓
        self.root.geometry("{}x{}+{}+{}".format(width, height, x, y))    # 确定窗口位置

        label1 = tk.Label(text="username:")
        entry1 = tk.Entry(width=30)
        
        label2 = tk.Label(text="password")
        entry2 = tk.Entry(width=27, show="●")
        
        user = User(entry1.get(), entry2.get())                     # 实例化用户这个类

        button1 = tk.Button(text="Log in now!", command=user.log_in)

        button2 = tk.Button(text="register", command=user.register)
        
        label1.pack(side=tk.LEFT)
        entry1.pack(side=tk.LEFT)
        label2.pack(side=tk.LEFT)
        entry2.pack(side=tk.LEFT)
        button1.pack(side=tk.LEFT)
        button2.pack(side=tk.RIGHT)

#-------------------------用户管理----------------------------#
class User(object):
    def __init__(self, username, password):
        self.usn = username
        self.pwd = password

    def log_in(self):
        """
        登录
        """
        ret = False
        user_dict = None
        File = "X:\\Files\\info.txt"
        try:
            if _.path.exists(File):
                _f = open(File, "r", encoding='utf-8')
                _uesr = _f.read()
                _f.close()
                user_dict = eval(_uesr)
            else:
                tk.messagebox.showwarning("消息", "您还没有注册!")
        except Exception as e:
            tk.messagebox.showerror("错误","文件发生错误,原因:({})".format(e))
            if _f:
                _f.close()

        in_dict_pwd = hash.md5(self.pwd.encode(encoding="utf-8")).hexdigest()
        _dict = {"username":self.usn, "password":in_dict_pwd}
        if _dict == user_dict:
            ret = True
        else:
            tk.messagebox.showinfo("error", "Username or password was error!")

        return ret

    def register(self):
        """
        注册
        """
        File = "X:\\Files\\info.txt"
        f = None                                                                    # ↓
        try:                                                                        # ↓
            f = open(File, "r", encoding='utf-8')                                   # ↓
            f.open()                                                                # ↓
            f.close()
            pwd_md5 = hash.md5(self.pwd.encode(encoding="utf-8")).hexdigest()
            _f = open(File, "w")
            user_dict = {"username":self.usn, "password":pwd_md5}
            _f.write(str(user_dict))
            _f.close()
            tk.messagebox.showinfo("消息", "注册成功!")                              # ↓
        except Exception as e:                                                      # ↓
            if f:                                                                   # ↓
                f.close()                                                           # ↓
            tk.messagebox.showerror("错误","文件发生错误,原因:({})".format(e))   # 测试文件打开是否正常
            

        
if __name__ == "__main__":
    window = jiemian(tk.Tk,200 ,300 ,"hello")
    window()