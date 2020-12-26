from sqlalchemy import Table, func
from common.database import dbconnect
from module.major import Major

dbsession, md, DBase = dbconnect()


class Institute(DBase):
    __table__ = Table('Institute', md, autoload=True)

    def find_all(self):
        result = dbsession.query(Institute).filter_by(Is_delete='0').all()
        return result

    def find_by_insno(self, Insno):
        result = dbsession.query(Institute).filter_by(Insno=Insno, Is_delete='0').first()
        return result

    def find_major_all(self, Insno):
        result = dbsession.query(Major).filter_by(Insno=Insno).distinct().all()
        return result

    def find_insno_by_insname(self, Insname):
        result = dbsession.query(Institute).filter_by(Insname=Insname, Is_delete='0').first()
        return result.Insno

    def add_institute(self, Insno, Insname, Instructor, Insmennumber, Majornumber):
        institute = Institute(Insno=Insno, Insname=Insname, Instructor=Instructor,
                              Insmennumber=Insmennumber, Majornumber=Majornumber)
        dbsession.add(institute)
        dbsession.commit()

    def update_institute(self, Insno, Insname, Instructor, Insmennumber, Majornumber):
        result = Institute().find_by_insno(Insno)
        result.Insname = Insname
        result.Instructor = Instructor
        result.Insmennumber = Insmennumber
        result.Majornumber = Majornumber
        dbsession.commit()

    def Institute_count(self):
        count = dbsession.query(Institute).filter_by(Is_delete='0').count()
        return count

    def Institute_del(self, Insno):
        result = Institute().find_by_insno(Insno)
        result.Is_delete = '1'
        dbsession.commit()

