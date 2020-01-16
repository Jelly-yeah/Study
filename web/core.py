t = 'OK'
import sqlite3
import hashlib
import os
from flask import current_app
'''
'''
db_path = "pytools.db"  # sqlite数据库路径 # 在同一目录下的文件不需要指定详细路径
################################################

def add_user(_name, _mobile, _password, _head_photo):

    conn = None
    cursor = None

    try:
        # ==========连接数据库========== #
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # ===========sql命令=========== #
        pwd = hashlib.md5(_password.encode("utf-8")).hexdigest()  # 将明文密码转为哈希MD5值

        sql =  "insert into users(name, mobile, password, head_photo)values('%s', '%s', '%s', '%s')" % (_name, _mobile, pwd, _head_photo)
        cursor.execute(sql) # 执行sql命令

        # ============事务提交========== #
        conn.commit()

        # ============================ #
        cursor.close()
        conn.close()

        print(t)

    except Exception as e:
        print(e)
        if cursor:
            cursor.close()

        if conn:
            conn.close()
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

def update(user_id, photo_url):
    conn = None
    cursor = None

    try:
        

        # ==========连接数据库========== #
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # ===========sql命令=========== #
        sql =  "select head_photo from users where user_id={}".format(user_id)
        cur = cursor.execute(sql) # 执行sql命令
        query = cur.fetchone()

        base_path = os.path.dirname(current_app.instance_path)
        file_dir = base_path + "/static/images/photo/"
        oldfile = file_dir + query[0]
        if os.path.exists(oldfile):
            os.remove(oldfile)

        # ===========sql命令=========== #
        sql =  "update users set head_photo='{}'".format(photo_url)
        cursor.execute(sql) # 执行sql命令

        # ============事务提交========== #
        conn.commit()

        # ============================ #
        cursor.close()
        conn.close()

        print(t)

    except Exception as e:
        print(e)
        if cursor:
            cursor.close()

        if conn:
            conn.close() 


def login(_mobile, _password):
    
    conn = None
    cursor = None

    try:
        # ==========连接数据库========== #
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # ===========sql命令=========== #
        pwd = hashlib.md5(_password.encode("utf-8")).hexdigest()  # 将明文密码转为哈希MD5值

        sql =  "select * from users where (mobile='{0}' or name='{0}') and password='{1}'".format(_mobile, pwd)
        cursor.execute(sql) # 执行sql命令
        query = cursor.fetchall()

        if len(query) == 1:
            user_data = {}
            user = query[0]
            user_data["user_id"] = user[0]
            user_data["name"] = user[1]
            user_data["mobile"] = user[2]
            # 密码已经被MD5加密, 所以不用上传
            user_data["head_photo"] = user[4]
            return {"code": 200, "data": user_data, "message": "OK"}
        else:
            return {"code": 404, "data": None, "message": "ERROR"}

        # ============事务提交========== #
        conn.commit()

        # ============================ #
        cursor.close()
        conn.close()

        # print(t)

    except Exception as e:
        print(e)
        if cursor:
            cursor.close()

        if conn:
            conn.close()

        return {"code": 500, "data": None, "message": e}
    



if __name__ == "__main__":
    add_user('Jelly', '15982122086', '070727', '')
    # ret = login("Jelly", "070727")
    # if ret["code"] == 200:
    #     print("✔")
    #     print("姓名：{}".format(ret["data"]["name"]))
    # else:
    #     print("✘")