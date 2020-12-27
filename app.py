from flask import Flask, render_template, request, session, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy

import pymysql

pymysql.install_as_MySQLdb()
app = Flask(__name__, template_folder='templates', static_url_path='/', static_folder='static')
app.config['SECRET_KEY'] = os.urandom(24)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234a@localhost:3306/StudentManager?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



@app.before_request#执行所有装饰器都要执行当前装饰器(简洁版实现同样功能)
def login_required():
    if request.path in ['/']: #如果登录的路由是和登录就返会none
        return None
    user=session.get('Userno')  #获取用户登录信息
    if not user:                 #没有登录就自动跳转到登录页面去
        return redirect('/')
    return None




if __name__ == '__main__':
    from controller.index import *
    app.register_blueprint(index)

    from controller.course import *
    app.register_blueprint(course)

    from controller.rp import *
    app.register_blueprint(rp)

    from controller.classes import *
    app.register_blueprint(classes)

    from controller.major import *
    app.register_blueprint(major)

    from controller.institute import *
    app.register_blueprint(institute)

    app.register_blueprint(classes)

    from controller.user import *
    app.register_blueprint(user)

    app.run(debug=True)
