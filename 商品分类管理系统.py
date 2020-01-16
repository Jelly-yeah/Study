# -*- coding: utf-8 -*-
import random

def read_txt(file_path):
    f = open(file_path,"r")
    data = f.read()
    f.close()
    return data

def write_txt(file_path, data):
    f = open(file_path,"w")
    f.write(data)
    f.close()
    return data

"""#############################################################"""

def rd_code():
    return str(random.randint(100000,1000000))

""">>>>>>>>>>>>>>>>>>>>>>>>>command<<<<<<<<<<<<<<<<<<<<<<<<<<<<"""
def cmd(cd):
    if cd=="add":
        add_goods()
    if cd=="count":
        count_goods()
        
"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
def get_goods():
    data = read_txt("goods.txt")
    if len(data) == 0:
        return []
    else:
        return eval(data)

def show_goods(goods):
    for g in goods:
        print("{},{},{},{}".format(g["no"], g["name"], g["typ"], g["num"]))
    
def goods_sum():
    return sum([g["num"]  for g in get_goods()])

"""*************************************************************"""
def add_goods():
    no = input("��Ʒ���:")
    name = input("��Ʒ��:")
    typ = input("��Ʒ����:")
    num = input("�������:")
    dic = {"no":no, "name":name, "typ":typ, "num":num}
    goods = get_goods()
    goods.append(dic)
    show_goods(goods)

def count_goods():
    print(goods_sum())
    show_goods(get_goods())
    


"""_____________________________________________________________"""
    
def login_form():
    code_data = rd_code()
    print("���ĵ�¼��֤��Ϊ:{}".format(code_data))
    name_data, pwd_data = read_txt("userpass.txt").split(",")
    name = input("�������û���:")
    pwd = input("����������:")
    code = input("��¼��֤��:")
    if (name_data==name) and (pwd_data==pwd) and (code_data==code):
        print("�����֤ͨ������ӭ��¼!")
        core_form
    else:
        print("�����֤ʧ��!")

"""--------------------------------------------------------------"""
def core_form():
    cmd(input("::"))
        

if __name__ == "__main__":
    login_form()
