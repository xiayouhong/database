from sqlalchemy import Table, func
from common.database import dbconnect
from module.major import Major


dbsession, md, DBase = dbconnect()


class   Course(DBase):
    __table__ = Table('Course', md, autoload=True)

    def find_all(self):
         result = dbsession.query(Course).filter_by(Is_delete='0').all()
         return result


    def find_all_list(self):
        result = dbsession.query(Course, Major.Majorname) \
            .join(Major, Course.Majorno == Major.Majorno) \
            .filter(Course.Is_delete == '0').all()
        return result



    def find_by_cno(self,Cno):
        result = dbsession.query(Course).filter_by(Cno=Cno, Is_delete='0').first()
        return result

    def add_course(self, Cno, Cname, Majorno, Credit, Ctime, Ctype, Cteacher):
        course = Course(Cno=Cno, Cname=Cname, Majorno=Majorno, Credit=Credit, Cnum=0,
                        Ctime=Ctime, Ctype=Ctype, Cteacher=Cteacher, Is_delete='0')
        dbsession.add(course)
        dbsession.commit()
        return course

    def update_course(self, Cno, Cname, Majorno, Credit, Ctime, Ctype, Cteacher, Is_delete):
        result = Course().find_by_cno(Cno)
        result.Cname = Cname
        result.Majorno = Majorno
        result. Credit = Credit
        result.Ctime = Ctime
        result.Ctype = Ctype
        result.Cteacher = Cteacher
        result.Is_delete = Is_delete
        dbsession.commit()

    def course_count(self):
        count = dbsession.query(Course).filter_by(Is_delete='0').all().count()
        return count

    def course_del(self, Cno):
        result = Course().find_by_cno(Cno)
        result.Is_delete = '1'
        dbsession.commit()

    def course_add_count(self, Cno):
        result = Course().find_by_cno(Cno)
        result.Cnum = result.Cnum + 1
        dbsession.commit()

