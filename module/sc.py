from sqlalchemy import Table, func
from common.database import dbconnect
from module.course import Course
from module.student import Student

dbsession, md, DBase = dbconnect()


class SC(DBase):
    __table__ = Table('SC', md, autoload=True)

    def add_sc(self, Sno, Cno, Type, Grade):
        sc = SC(Sno=Sno, Cno=Cno, Type=Type, Grade=Grade,Is_delete='0')
        dbsession.add(sc)
        dbsession.commit()

    def find_sc_all(self):
        result = dbsession.query(SC, Student.Sname, Course.Cname)\
            .join(Student, Student.Sno == SC.Sno,)\
            .join(Course, SC.Cno == Course.Cno)\
            .filter(SC.Is_delete == '0').all()
        return result

    def find_sc_by_sno(self, Sno):
        result = dbsession.query(SC, Student.Sname, Course.Cname) \
            .join(Student, Student.Sno == SC.Sno, ) \
            .join(Course, SC.Cno == Course.Cno) \
            .filter(SC.Is_delete == '0', SC.Sno == Sno).all()
        return result

    def find_sc_by_sno_cno(self, Sno, Cno):
        result = dbsession.query(SC).filter_by(Sno=Sno, Cno=Cno).first()
        return result

    def find_all_student_by_cno(self, Cno):
        result = dbsession.query(Course.Cname, Student.Sname, SC) \
            .join(SC, SC.Cno == Course.Cno) \
            .join(Student, Student.Sno == SC.Sno) \
            .filter(Course.Is_delete == '0', Student.Is_delete == '0', SC.Is_delete == '0',
                    Course.Cno == Cno).all()
        return result

    def sc_count(self):
        count = dbsession.query(SC).filter_by(Is_delete='0').count()
        return count

    def sc_count_by_sno(self, Sno):
        count = dbsession.query(SC).filter_by(Is_delete='0', Sno=Sno).count()
        return count

    def sc_update(self, Sno, Cno, Type, Grade):
        result = SC().find_sc_by_sno_cno(Sno, Cno)
        result.Type = Type
        result.Grade = Grade
        dbsession.commit()

