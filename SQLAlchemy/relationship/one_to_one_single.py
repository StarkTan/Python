"""
单向一对一
"""
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship, backref

engine = create_engine('mysql+pymysql://root:root@localhost:3306/sqlalchemy?charset=utf8', echo=False)
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(32), nullable=False)
    #extend = relationship('UserExtend', uselist=True, cascade='all, delete')


class UserExtend(Base):
    __tablename__ = 'user_extend'
    id = Column(Integer, primary_key=True, autoincrement=True)
    school = Column(String(50))
    uid = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
    # 一对一的时候使用下面情况：
    user = relationship('User', backref=backref('extend', uselist=False))


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine, checkfirst=False)

Session = sessionmaker(bind=engine)
session = Session()

user = User(username='xiaowu')
extend_user1 = UserExtend(school='xxx school')
extend_user2 = UserExtend(school='xxxxxx school')
user.extend = extend_user1

session.add(user)
session.commit()

res = session.query(UserExtend).first()

session.delete(res)
session.commit()
print(session.query(User).count())
session.commit()
print(session.query(UserExtend).count())
