from flask import Blueprint, make_response, session, request, url_for, render_template, redirect

from module.user import User

user = Blueprint('user', __name__)

@user.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = User()
        Userno = request.form.get('Userno')
        Password = request.form.get('Password')
        result = user.find_by_userno(Userno)
        if result:
            if Userno == result.Userno and Password == result.Password:
                session['Userno'] = Userno
                session['Username'] = result.Username
                session['Power'] = result.Power
                return redirect('/home/')
            else:
                return u"用户名或密码错误，请确认后再登录。"
        else:
            return "没有此用户"

@user.route('/admin/')
def myinformation():
    userno = session.get('Userno')
    result = User().find_by_userno(userno)
    return render_template('admin.html', result=result)

@user.route('/add_admin/', methods=['GET', 'POST'])
def addadmin():
    if request.method == 'GET':
        return render_template('add_admin.html')
    else:
        userno = request.form.get('userno')
        username = request.form.get('username')
        password = request.form.get('password')
        power = request.form.get('power')
        user = User()
        user.add_user(userno, username, password, power)
        return redirect('/home/')

@user.route('/update_admin/', methods=['GET', 'POST'])
def update_admin():
    if request.method == 'GET':
        userno = session['Userno']
        result = User().find_by_userno(userno)
        return render_template('update_admin.html', result=result)
    else:
        userno = request.form.get('userno')
        username = request.form.get('username')
        password = request.form.get('password')
        rpassword =request.form.get('rpassword')
        power = request.form.get('power')
        user = User().find_by_userno(userno)
        if user.Password == password:
            user.update_user(userno, rpassword, username, power)
            return redirect('/home/')
        else:
            return '原密码错误，修改失败'

@user.route('/logout/')
def logout():
    session.clear()
    return redirect('/')
