from sqlalchemy import Table, func
from common.database import dbconnect

from module.classes import Classes


dbsession, md, DBase = dbconnect()


class Major(DBase):
    __table__ = Table('Major', md, autoload=True)

    def find_all(self):
        result = dbsession.query(Major).filter_by(Is_delete='0').all()
        return result

    def find_by_majorno(self, Majorno):
        result = dbsession.query(Major).filter_by(Majorno=Majorno, Is_delete='0').first()
        return result

    def find_by_insno(self, Insno):
        result = dbsession.query(Major).filter_by(Insno=Insno, Is_delete='0').all()
        return result

    def find_majorno_by_majorname(self, majorname):
        result = dbsession.query(Major).filter_by(Majorname=majorname, Is_delete='0').first()
        return result.Majorno

    def find_class_all(self, Majorno):
        result = dbsession.query(Classes).filter_by(Majorno=Majorno, Is_delete='0').distinct().all()
        return result

    def add_major(self, Majorno, Majorname, Majormennumber, Insno, Classnumber):
        major = Major(Majorno=Majorno, Majornamename=Majorname, Majormennumber=Majormennumber,
                              Insno=Insno, Classnumber=Classnumber, Is_delete='0')
        dbsession.add(major)
        dbsession.commit()

    def update_major(self, Majorno, Majorname, Majormennumber, Insno, Classnumber,Is_delete):
        result = Major().find_by_majorno(Majorno)
        result.Majorname = Majorname
        result.Majormennumber = Majormennumber
        result.Insno = Insno
        result. Classnumber = Classnumber
        result.Is_delete = Is_delete
        dbsession.commit()

    def major_count(self):
        count = dbsession.query(Major).filter_by(Is_delete='0').count()
        return count

    def major_del(self, Majorno):
        result = Major().find_by_majorno(Majorno)
        result.Is_delete = '1'
        dbsession.commit()
