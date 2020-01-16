def update_pwd(new):
    _file = None
    try:
        file = 'password.txt'
        _file = open(file, 'w', encoding='utf-8')
        _file.write(new)
#    except FileExistsError or FileNotFoundError as e:
    except:
#       print(e)
        pass
    finally:
        if _file:
            _file.close()


def get_pwd():
    file = 'password.txt'
    _file = open(file, 'r', encoding='utf-8')
    ret = _file.read()
    _file.close()
    return ret


'''def log_in():
    user_name = 'lanqiaobei'
    pwd = get_pwd()
    if input("请输入账号:") == user_name:
        if input("请输入密码:") == pwd:
            new_pwd = input("请输入新密码:")
            if new_pwd != pwd:
                chek_new_pwd = input("请再输入新密码:")
                if new_pwd == chek_new_pwd:
                    print("密码修改成功!")
                    update_pwd(new_pwd)
                    return 0
                else:
                    print("两次输入的新密码不相同,密码修改失败!")
                    return 0
            else:
                print("新密码不能与原密码相同,密码修改失败!")
                return 0
        else:
            print("原密码输入错误,密码修改失败!")
            return 0
    else:
        print("没有此账户,密码修改失败!")
        return 0'''


def set_pwd():
    new_pwd = input("请输入新密码:")
    chek_new_pwd = input("请再输入新密码:")
    if new_pwd != pwd and new_pwd == chek_new_pwd:
        print("密码修改成功!")
        update_pwd(new_pwd)
    elif new_pwd == pwd:
        print("新密码不能与原密码相同,密码修改失败!")
    elif new_pwd != chek_new_pwd:
        print("两次输入的新密码不相同,密码修改失败!")


def login():
    global pwd
    user_name = 'lanqiaobei'
    pwd = get_pwd()
    input_username = input("请输入账号:")
    input_password = input("请输入密码:")
    if  input_username == user_name and input_password == pwd:
        set_pwd()
    elif input_password != pwd:
        print("原密码输入错误,密码修改失败!")
    elif input_username != user_name:
        print("没有此账户,密码修改失败!")


if __name__ == "__main__":
    login()
