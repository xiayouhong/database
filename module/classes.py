from sqlalchemy import Table, func
from common.database import dbconnect


dbsession, md, DBase = dbconnect()


class Classes(DBase):
    __table__ = Table('Class', md, autoload=True)

    def find_all(self):
        result = dbsession.query(Classes).filter_by(Is_delete='0').all()
        return result

    def find_by_classno(self, Classno):
        result = dbsession.query(Classes).filter_by(Classno=Classno, Is_delete='0').first()
        return result

    def find_by_majorno(self, Majorno):
        result = dbsession.query(Classes).filter_by(Majorno=Majorno, Is_delete='0').all()
        return result


    def add_class(self, Classno, Tname, Classmennumber, Headteacher, Majorno):
        aclass = Classes(Classno=Classno, Tname=Tname, Classmnenumber=Classmennumber,
                       Headteacher=Headteacher, Majorno=Majorno, Is_delete='0')
        dbsession.add(aclass)
        dbsession.commit()

    def update_class(self, Classno, Tname, Classmennumber, Headteacher, Majorno, Is_delete):
        result = Classes().find_by_classno(Classno)
        result.Tname = Tname
        result.Classmennumber = Classmennumber
        result.Headteacher = Headteacher
        result.Majorno = Majorno
        result.Is_delete = Is_delete
        dbsession.commit()

    def class_add_count(self, Classno):
        result = Classes().find_by_classno(Classno)
        result.Classmennumber = result.Classmennumber + 1
        dbsession.commit()

    def class_del(self, Classno):
        result = Classes().find_by_classno(Classno)
        result.Is_delete = '1'
        dbsession.commit()

