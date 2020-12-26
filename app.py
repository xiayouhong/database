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


# @app.route('/code')
# def code():
#     code, bstring = ImagCode().get_code()
#     response = make_response(bstring)
#     response.headers['Content-Type'] = 'image/jpeg'
#     session['imgVerifi'] = code.lower()
#     return response





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
