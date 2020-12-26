import time

from sqlalchemy import Table, func
from common.database import dbconnect

dbsession, md, DBase = dbconnect()


class RP(DBase):
    __table__ = Table('RP', md, autoload=True)

    def find_all(self):
        result = dbsession.query(RP).filter_by(RP_delete='0').all()
        return result

    def find_by_rpid(self, id):
        result = dbsession.query(RP).filter_by(RPid=id, RP_delete='0').first()
        return result

    def find_by_sno(self, Sno):
        result = dbsession.query(RP).filter_by(Sno=Sno, RP_delete='0').all()
        return result

    def Delete_by_sno_R(self, Sno):
        result = dbsession.query(RP).filter_by(Sno=Sno, RP_delete='0').all()
        for i in range(len(result)):
            if result[i].RPtyep == 'R':
                result[i].RP_delete = '1'
        dbsession.commit()

    def Delete_by_sno_P(self, Sno):
        result = dbsession.query(RP).filter_by(Sno=Sno, RP_delete='0').all()
        for i in range(len(result)):
            if result[i].RPtyep == 'P':
                result[i].RP_delete = '1'
        dbsession.commit()

    def Delete_by_rpid(self, rpid):
        result = RP().find_by_rpid(rpid)
        result.RP_delete = '1'
        dbsession.commit()


    def Add_RP(self, Sno, RPname, RPtype, RPgrade, RPdate, Anote):
        rp = RP(Sno=Sno, RPname=RPname, RPtype=RPtype, RPgrade=RPgrade, RPdate=RPdate,
                Anote=Anote, RP_delete='0')
        dbsession.add(rp)
        dbsession.commit()
        return rp

    def update_rp(self, RPid, Sno, RPname, RPtype, RPgrade, RPdate, Anote):
        result = RP().find_by_rpid(RPid)
        result.Sno = Sno
        result.RPname = RPname
        result.RPtype = RPtype
        result.RPgrade = RPgrade
        result.RPdate = RPdate
        result.Anote = Anote
        dbsession.commit()

    def R_count(self):
        count = dbsession.query(RP).filter_by(RPtype='R', RP_delete='0').count()
        return count
