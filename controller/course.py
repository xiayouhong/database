from flask import Blueprint, render_template, request, redirect, url_for

from module.course import Course
from module.sc import SC



course = Blueprint('course', __name__)

@course.route('/course-list/')
def courses():
    course = Course()
    result = course.find_all_list()
    return render_template('courses.html', result=result)

@course.route('/search/course-<keyword>')
def search(keyword):
    keyword = keyword.strip()
    course = Course()
    cou = course.find_by_cno(keyword)
    result = [cou]
    return render_template('courses.html', result=result)


@course.route('/course-list/<cno>')
def cou(cno):
    course = Course()
    result = course.find_by_cno(cno)
    return render_template('update_cou.html', result=result)


@course.route('/course-stu-list/<Cno>')
def course_stu(Cno):
    sc = SC()
    result = sc.find_all_student_by_cno(Cno)
    return render_template('courses-stu.html', result=result)

@course.route('/add-course/',methods=['GET', 'POST'])
def course_add():
    if request.method == 'GET':
        return render_template('add_course.html')
    else:
        cno = request.form.get('cno')
        ctype = request.values.get('ctype')
        cteach = request.form.get('cteacher')
        majorno = request.form.get('majorno')
        cname = request.form.get('cname')
        ctime = request.form.get('ctime')
        credit = request.form.get('credit')
        print(credit)
        course = Course()
        if len(cno) > 0:
            course.add_course(cno, cname, majorno, credit, ctime, ctype, cteach)
            return "add-pass"
        else:
            return "add-fail"

@course.route('/edit-cou/', methods=['POST'])
def editstu():
    course = Course()
    cno = request.form.get('cno')
    ctype = request.values.get('ctype')
    cteach = request.form.get('cteacher')
    majorno = request.form.get('majorno')
    cname = request.form.get('cname')
    ctime = request.form.get('ctime')
    credit = request.form.get('credit')
    if len(cno) > 0:
        course.update_course(cno, cname, majorno, credit, ctime, ctype, cteach, '0')
        return redirect('/course-list/')
    else:
        return 'edit-fail'

@course.route('/del-cou/<cno>')
def del_course(cno):
    course = Course()
    result = course.find_by_cno(cno)
    if result.Cnum > 0:
        return 'del-fail'
    else:
        course.course_del(cno)
        return redirect('/course-list/')


@course.route('/add-sno-cno/', methods=['GET', 'POST'])
def add_sno_cno():
    if request.method == 'GET':
        return render_template('add_sno_cno.html')
    else:
        cno = request.form.get('cno')
        sno = request.form.get('sno')
        # grade = request.form.get('grade')
        type = request.values.get('type')
        if len(sno) > 0 and len(cno) > 0:
            Course().course_add_count(cno)
            SC().add_sc(sno, cno, type, None)
            return redirect('/stu-sc-list/')
        else:
            return 'add-fail'

@course.route('/add-grade-sc/', methods=['GET', 'POST'])
def add_grade_sc():
    if request.method == 'GET':
        return render_template('add_grade_sc.html')
    else:
        cno = request.form.get('cno')
        sno = request.form.get('sno')
        grade = request.form.get('grade')
        type = request.values.get('type')

        if len(sno) > 0 and len(cno) > 0:
            result = SC().find_sc_by_sno_cno(sno, cno)
            if result:
                SC().sc_update(sno, cno, type, grade)
                return redirect('/stu-sc-list/')
            else:
                return '该课程无该学生'
        else:
            return 'add-fail'
