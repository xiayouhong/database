from flask import Blueprint, render_template, request, redirect, url_for

from module.classes import Classes
from module.institute import Institute
from module.major import Major
from module.sc import SC
from module.student import Student

institute = Blueprint('institute', __name__)

@institute.route('/institute-list/')
def institute_list():
    institute =Institute()
    result =institute.find_all()
    return render_template('institute.html', result=result)

@institute.route('/search/institute-<keyword>')
def search(keyword):
    keyword = keyword.strip()
    institute = Institute()
    ins = institute.find_by_insno(keyword)
    result = [ins]
    return render_template('institute.html', result=result)


@institute.route('/institute-list/<insno>')
def cou(insno):
    institute =Institute()
    result =institute.find_by_insno(insno)
    return render_template('update_institute.html', result=result)


@institute.route('/institute-major-list/<insno>')
def institute_class(insno):
    major = Major()
    result = major.find_by_insno(insno)
    return render_template('major.html', result=result)

@institute.route('/institute-stu-list/', methods=['GET', 'POST'])
def institute_ins():
    if request.method == 'GET':
        result = Institute().find_all()
        stu = []
        return render_template('/institute_stu.html/', result=result)
    else:
        student = Student()
        insname = request.values.get('insname')
        insno = Institute().find_insno_by_insname(insname)
        print(insno)
        stu = student.find_student_by_ins_all(insno)
        result = Institute().find_all()
        return render_template('/institute_stu.html/', result=result , stu=stu, insname=insname)



@institute.route('/add-institute/',methods=['GET', 'POST'])
def institute_add():
    if request.method == 'GET':
        return render_template('add_institute.html')
    else:
        insno = request.form.get('insno')
        insname = request.form.get('insname')
        instructor = request.form.get('instructor')
        insmennum = request.form.get('Insmennum')
        majornum= request.form.get('majornum')
        institute = Institute()
        if len(insno) > 0:
            institute.add_institute(insno, insname, instructor, insmennum, majornum)
            return redirect('/institute-list/')
        else:
            return "add-fail"

@institute.route('/edit-institute/', methods=['POST'])
def editinstitute():
    institute =Institute()
    insno = request.form.get('insno')
    insname = request.form.get('insname')
    instructor = request.form.get('instructor')
    insmennum = request.form.get('Insmennum')
    majornum = request.form.get('majornum')
    if len(insno) > 0:
        institute.update_institute(insno, insname, instructor, insmennum, majornum)
        return redirect('/institute-list/')
    else:
        return 'edit-fail'

@institute.route('/del-institute/<insno>')
def del_classes(insno):
    institute =Institute()
    result =institute.find_by_insno(insno)
    if result.Majornumber > 0 and result.insmennumber > 0:
        return 'del-fail'
    else:
        institute.Institute_del(insno)
        return redirect('/institute-list/')
