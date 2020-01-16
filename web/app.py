from flask import Flask, render_template, request, redirect, session
import core
import os, time

app = Flask(__name__)
app.config["SECRET_KEY"] = "1212121"
app.config['UPLOAD_FOLDER'] = "/static/images/photo/"


def permission(func):
    def permission_func(*args, **kwargs):
        if session.get("user"):
            return func(*args, **kwargs)
        else:
            return redirect("/")
    return permission_func


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/success')
@permission
def success():
    user = session.get("user")
    return render_template("success.html", data=user)
    
@app.route("/login1", methods=["POST"])
def _login():
    usn = request.form["usn"]
    pwd = request.form["pwd"]
    ret = core.login(usn, pwd)
    if ret["code"] == 200:
        session["user"] = ret["data"]
        return redirect("/success")
    else:
        return "登录失败"


@app.route("/upload", methods=["POST"])
def upload():

    base_path = os.path.dirname(app.instance_path)
    file_dir = base_path + "/static/images/photo/"

    
    print(base_path)
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    file = request.files["file"]

    ext = file.filename.split(".")[1]  # 获取文件后缀
    unix_time = int(time.time())
    new_filename = str(unix_time)+'.'+ext  # 修改了上传的文件名
    file.save(os.path.join(file_dir, new_filename))
    user_id = session.get("user")["user_id"]
    core.update(user_id, new_filename)
    user = session.get("user")
    user["head_photo"] = new_filename
    session["user"] = user
    return redirect("/success")




if __name__ == '__main__':
    app.run(port=5001, debug=True)
