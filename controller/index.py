import math

from flask import Blueprint, render_template, request, redirect, url_for

from module.course import Course
from module.institute import Institute
from module.major import Major
from module.rp import RP
from module.sc import SC
from module.student import Student
from module.user import User

index = Blueprint('index', __name__)


@index.route('/home/')
def home():
    student = Student()
    s_count = student.stu_count()
    rp = RP()
    r_count = rp.R_count()
    institute = Institute()
    i_count = institute.Institute_count()
    major = Major()
    m_count = major.major_count()
    return render_template('index.html', s_count=s_count, r_count=r_count, i_count=i_count, m_count=m_count)


@index.route('/stu-list/')
def stupag():
    student = Student()
    result = student.find_all_list()
    return render_template('students.html', result=result)


@index.route('/stu-sno/<sno>')
def stu(sno):
    student = Student()
    result = student.find_by_sno(sno)
    return render_template('update_stu.html', result=result)


@index.route('/stu-sc-list/')
def stugradepag():
    sc = SC()
    result = sc.find_sc_all()
    return render_template('student_sc.html', result=result)

@index.route('/stu-rp-list/')
def sturppag():
    rp = RP()
    result =rp.find_all()
    return render_template('rps.html', result=result)


@index.route('/add-stu/', methods=['GET', 'POST'])
def addstu():
    if request.method == 'GET':
        return render_template('add_student.html')
    else:
        sname = request.form.get('name')
        ssex = request.values.get('sex')
        sno = request.form.get('sno')
        sbrith = request.form.get('sbrith')
        classno = request.form.get('classno')
        home = request.form.get('home')
        sdate = request.form.get('sdate')
        tel = request.form.get('telephone')
        snote = request.form.get("snote")
        sdate.replace('/', '-')
        sbrith.replace('/', '-')
        student = Student()
        if len(ssex) > 0 and len(sno) > 0:
            student.add_stu(sno, sname, ssex, sbrith, tel, home, snote, classno, sdate)
            return "add-pass"
        else:
            return "add-fail"


@index.route('/del-stu/<sno>')
def delstu(sno):
    student = Student()
    student.del_student_by_sno(sno)
    return redirect('/stu-list/')


@index.route('/edit-stu/', methods=['POST'])
def editstu():
    student = Student()
    sname = request.form.get('name')
    ssex = request.form.get('sex')
    sno = request.form.get('sno')
    sbrith = request.form.get('sbrith')
    classno = request.form.get('classno')
    home = request.form.get('home')
    sdate = request.form.get('sdate')
    tel = request.form.get('telephone')
    snote = request.form.get("snote")
    sdate.replace('/', '-')
    sbrith.replace('/', '-')
    if len(ssex) > 0 and len(sno) > 0:
        student.update_stu(sno, sname, ssex, sbrith, tel, sdate, home, snote, classno, '0')
        return redirect('/stu-list/')
    else:
        return 'edit-fail'








