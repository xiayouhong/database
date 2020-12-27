from flask import Blueprint, render_template, request, redirect, url_for

from module.classes import Classes
from module.major import Major
from module.sc import SC
from module.student import Student

major = Blueprint('major', __name__)

@major.route('/major-list/')
def major_list():
    major =Major()
    result =major.find_all()
    return render_template('major.html', result=result)


@major.route('/search/major-<keyword>')
def search(keyword):
    keyword = keyword.strip()
    major = Major()
    maj = major.find_by_majorno(keyword)
    result = [maj]
    return render_template('major.html', result=result)


@major.route('/major-list/<majorno>')
def cou(majorno):
    major =Major()
    result =major.find_by_majorno(majorno)
    return render_template('update_major.html', result=result)


@major.route('/major-class-list/<majorno>')
def major_class(majorno):
    classes = Classes()
    result = classes.find_by_majorno(majorno)
    return render_template('classes.html', result=result)

@major.route('/major-stu-list/', methods=['GET', 'POST'])
def institute_ins():
    if request.method == 'GET':
        result = Major().find_all()
        return render_template('/major_stu.html/', result=result)
    else:
        student = Student()
        stu = []
        majorname = request.values.get('majorname')
        majorno = Major().find_majorno_by_majorname(majorname)
        stu = student.find_student_by_major_all(majorno)
        result = Major().find_all()
        return render_template('/major_stu.html/', result=result , stu=stu, majorname=majorname)



@major.route('/add-major/',methods=['GET', 'POST'])
def major_add():
    if request.method == 'GET':
        return render_template('add_major.html')
    else:
        majorno = request.form.get('majorno')
        majorname = request.form.get('majorname')
        majormen = request.form.get('majormennumber')
        classnum = request.form.get('classnum')
        Insno = request.form.get('insno')
        major = Major()
        if len(majorno) > 0:
            major.add_major(majorno, majorname, majormen, Insno, classnum)
            return redirect('/major-list/')
        else:
            return "add-fail"

@major.route('/edit-major/', methods=['POST'])
def editmajor():
    major =Major()
    majorno = request.form.get('majorno')
    majorname = request.values.get('majorname')
    majormen = request.form.get('majormennumber')
    classnum = request.form.get('classnum')
    Insno = request.form.get('insno')
    if len(majorno) > 0:
        major.update_major(majorno, majorname, majorname, Insno, classnum, '0')
        return redirect('/major-list/')
    else:
        return 'edit-fail'

@major.route('/del-major/<majorno>')
def del_classes(majorno):
    major =Major()
    result =major.find_by_majorno(majorno)
    if result.Classnumber > 0 and result.Majormennumber > 0:
        return 'del-fail'
    else:
        major.major_del(majorno)
        return redirect('/major-list/')
