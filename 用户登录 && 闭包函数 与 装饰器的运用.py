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

import os, time
import hashlib

def permission(func):
    a = 0
    admin = False 
    user_dict = None
    os.system("cls")
    File = "X:\\Files\\info.txt"
    _f = None
    _username = None
    password = None
    try:
        if os.path.exists(File):
            _f = open(File, "r", encoding='utf-8')
            _uesr = _f.read()
            _f.close()
            user_dict = eval(_uesr)
        else:
            username = input("Please set your username:")
            password = input("Please set your passsword:")
            pwd_md5 = hashlib.md5(password.encode(encoding="utf-8")).hexdigest()
            _f = open(File, "w")
            user_dict = {"username":username, "password":pwd_md5}
            _f.write(str(user_dict))
            _f.close()
            os.system("cls")
            print("Set succes!")
            time.sleep(0.9)
            os.system("cls")
    except Exception as e:
        print("Something was error!({})".format(e))
        if _f:
            _f.close()
        

    while True:
        if a == 0:
            _username = input("Please input your username:")
            _password = input("Please input your passsword:")
            in_dict_pwd = hashlib.md5(_password.encode(encoding="utf-8")).hexdigest()
            _dict = {"username":_username, "password":in_dict_pwd}
            if _dict == user_dict:
                # print("ok")
                admin = True
                break
            else:
                a += 1
        else:
            print("password or username was wrong!")
            time.sleep(0.9)
            os.system("cls")
            _username = input("Please input your username:")
            _password = input("Please input your passsword:")
            in_dict_pwd = hashlib.md5(_password.encode(encoding="utf-8")).hexdigest()
            _dict = {"username":_username, "password":in_dict_pwd}
            if _dict == user_dict:
                admin = True
                break     
            else:
                while True:
                    t = input("Do you forgot it?(yes:return '1' ; no:return '0')  :")
                    time.sleep(0.9)
                    os.system("cls")
                    if t=='1':
                        c = 0
                        while True:
                            an = input("Please Tell me: what's your branch school's teacher's first name?  :")
                            if an == "张":
                                print("answer correct!")
                                time.sleep(0.9)
                                os.system("cls")
                                username = input("Please set your username:")
                                password = input("Please set your passsword:")
                                pwd_md5 = hashlib.md5(password.encode(encoding="utf-8")).hexdigest()
                                _f = open(File, "w")
                                user_dict = {"username":username, "password":pwd_md5}
                                _f.write(str(user_dict))
                                _f.close()
                                os.system("cls")
                                print("Set succes!")
                                time.sleep(0.9)
                                os.system("cls")
                                time.sleep(1.5)
                                a = 0
                                break
                            else:
                                print("Wrong!")
                                time.sleep(0.9)
                                os.system("cls")
                                if c >= 1:
                                    _an = input("Do you want to exit?((yes:return '1' ; no:return '0')")
                                    if _an == '1':
                                        break
                                    elif _an == '0':
                                        continue
                                    else:
                                        print("Please input 1 or 0")
                            c += 1
                        break
                    elif t=='0':
                        a = 0
                        break
                    else:
                        print("Please input 1 or 0")
                        time.sleep(0.9)
                        os.system("cls")
                        a = 0
    print("welcome!dear {}".format(_username))
    def permission_func(*args, **kwargs):
        if admin:
            func(*args, **kwargs)
        else:
            print("You haven't any permission to access thins function!")
        return None
    return permission_func

def timer(func):
    def count_time(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print("Used {} seconds".format(end_time -start_time))
        return None
    return count_time

@timer
@permission
def test(x, y):
    print(x**y)

test(23,8)