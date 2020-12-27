from flask import Blueprint, render_template, request, redirect, url_for

from module.classes import Classes
from module.sc import SC
from module.student import Student

classes = Blueprint('classes', __name__)

@classes.route('/classes-list/')
def classess():
    classes = Classes()
    result = classes.find_all()
    return render_template('classes.html', result=result)


@classes.route('/search/classes-<keyword>')
def search(keyword):
    keyword = keyword.strip()
    classes = Classes()
    cla = classes.find_by_classno(keyword)
    result = [cla]
    return render_template('classes.html', result=result)


@classes.route('/classes-list/<classno>')
def cou(classno):
    classes = Classes()
    result = classes.find_by_classno(classno)
    return render_template('update_class.html', result=result)


@classes.route('/classes-stu-list/<classno>')
def classes_stu(classno):
    student = Student()
    result = student.find_student_by_class_all(classno)
    return render_template('classes-stu.html', result=result)

@classes.route('/add-classes/',methods=['GET', 'POST'])
def classes_add():
    if request.method == 'GET':
        return render_template('add_classes.html')
    else:
        classno = request.form.get('classno')
        tname = request.values.get('tname')
        classmen = request.form.get('classmen')
        headteacher = request.form.get('headteacher')
        majorno = request.form.get('majorno')
        classes = Classes()
        if len(classno) > 0:
            classes.add_classes(classno, tname, classmen, headteacher, majorno)
            return "add-pass"
        else:
            return "add-fail"

@classes.route('/edit-class/', methods=['POST'])
def editstu():
    classes = Classes()
    classno = request.form.get('classno')
    tname = request.values.get('tname')
    classmen = request.form.get('classmen')
    headteacher = request.form.get('headteacher')
    majorno = request.form.get('majorno')
    if len(classno) > 0:
        classes.update_class(classno, tname, classmen, headteacher, majorno, '0')
        return redirect('/classes-list/')
    else:
        return 'edit-fail'

@classes.route('/del-class/<classno>')
def del_classes(classno):
    classes = Classes()
    result = classes.find_by_classno(classno)
    if result.Classmennumber > 0:
        return 'del-fail'
    else:
        classes.class_del(classno)
        return redirect('/classes-list/')


@classes.route('/add-sno-classno/', methods=['GET', 'POST'])
def add_sno_classno():
    if request.method == 'GET':
        return render_template('add_sno_class.html')
    else:
        classno = request.form.get('classno')
        sno = request.form.get('sno')
        if len(sno) > 0 and len(classno) > 0:
            Classes().class_add_count(classno)
            Student().update_stu_classno(sno, classno)
            return redirect(url_for('classes-stu-list', classno=classno))
        else:
            return 'add-fail'
