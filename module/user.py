from sqlalchemy import Table, func
from common.database import dbconnect

dbsession, md, DBase = dbconnect()


class User(DBase):
    __table__ = Table('User', md, autoload=True)

    def find_all(self):
        result = dbsession.query(User).all()
        return result

    def find_by_userno(self,userno):
        result = dbsession.query(User).filter_by(Userno=userno).first()
        return result

    def add_user(self, Userno, Password, Username, Power):
        user = User(Userno=Userno, Password=Password, Username=Username, Power=Power)
        dbsession.add(user)
        dbsession.commit()

    def update_user(self, Userno, Password, Username, Power):
        result = User().find_by_userno(Userno)
        result.Password = Password
        result.Username = Username
        result.Power = Power
        dbsession.commit()
