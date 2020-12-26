import time

from sqlalchemy import Table
from common.database import dbconnect
from module.classes import Classes
from module.major import Major
from module.institute import Institute


dbsession, md, DBase = dbconnect()


class Student(DBase):
    __table__ = Table('Student', md, autoload=True)

    def find_all(self):
        result =dbsession.query(Student).filter_by(Is_delete='0').all()
        return result

    def find_by_sno(self, Sno):
        result = dbsession.query(Student).filter_by(Sno=Sno, Is_delete='0').first()
        return result

    def find_all_list(self):
        result = dbsession.query(Student,  Major.Majorname, Institute.Insname)\
            .join(Classes, Student.Classno == Classes.Classno)\
            .join(Major, Classes.Majorno == Major.Majorno)\
            .join(Institute, Major.Insno == Institute.Insno)\
            .filter(Student.Is_delete == '0').all()
        return result

    def find_by_sno_list(self, sno):
        result = dbsession.query(Student, Major.Majorname, Institute.Insname) \
            .join(Classes, Student.Classno == Classes.Classno) \
            .join(Major, Classes.Majorno == Major.Majorno) \
            .join(Institute, Major.Insno == Institute.Insno) \
            .filter(Student.Sno == sno, Student.Is_delete == '0').first()
        return result

    def add_stu(self, Sno, Sname, Ssex, Sbrith, Telephone, Home, Snote, Classno, Sdate):
        student = Student(Sno=Sno, Sname=Sname, Ssex=Ssex, Sbrith=Sbrith, Telephone=Telephone,
                          Home=Home, Snote=Snote, Classno=Classno, Sdate=Sdate, Is_delete='0')
        dbsession.add(student)
        dbsession.commit()

    def update_stu(self, Sno, Sname, Ssex, Sbrith, Telephone, Sdate, Home, Snote, Classno, Is_delete):
        result = Student().find_by_sno(Sno)
        result.Sname = Sname
        result.Ssex = Ssex
        result.Sbrith = Sbrith
        result.Telephone = Telephone
        result.Sdate = Sdate
        result.Home = Home
        result.Snote = Snote
        result.Classno = Classno
        result.Is_delete = Is_delete
        dbsession.commit()

    def update_stu_classno(self, Sno,  Classno):
        result = Student().find_by_sno(Sno)
        result.Classno = Classno
        dbsession.commit()

    def stu_count(self):
        count = dbsession.query(Student).filter_by(Is_delete='0').count()
        return count

    def find_student_by_class_all(self, Classno):
        result = dbsession.query(Student, Major.Majorname, Institute.Insname) \
            .join(Classes, Student.Classno == Classes.Classno) \
            .join(Major, Classes.Majorno == Major.Majorno) \
            .join(Institute, Major.Insno == Institute.Insno) \
            .filter(Classes.Classno == Classno, Student.Is_delete == '0').all()
        return result

    def find_student_by_major_all(self, Majorno):
        result = dbsession.query(Student, Major.Majorname, Institute.Insname) \
            .join(Classes, Student.Classno == Classes.Classno) \
            .join(Major, Classes.Majorno == Major.Majorno) \
            .join(Institute, Major.Insno == Institute.Insno) \
            .filter(Major.Majorno == Majorno, Student.Is_delete == '0').all()
        return result

    def find_student_by_ins_all(self, Insno):
        result = dbsession.query(Student, Major.Majorname, Institute.Insname) \
            .join(Classes, Student.Classno == Classes.Classno) \
            .join(Major, Classes.Majorno == Major.Majorno) \
            .join(Institute, Major.Insno == Institute.Insno) \
            .filter(Institute.Insno == Insno, Student.Is_delete == '0').all()
        return result

    def del_student_by_sno(self, Sno):
        result = dbsession.query(Student).filter_by(Sno=Sno, Is_delete='0').first()
        result.Is_delete = '1'
        classes = Classes().find_by_classno(result.Classno)
        classes.Classmennumber =classes.Classmennumber - 1
        major = Major().find_by_majorno(classes.Majorno)
        major.Majormennumber =major.Majormennumber - 1
        ins = Institute().find_by_insno(major.Insno)
        ins.Insmennumber =ins.Insmennumber - 1
        dbsession.commit()


