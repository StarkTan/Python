import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

# check version
# print(sqlalchemy.__version__)
# create connection; echo 表示是否输出日志
engine = create_engine('sqlite:///:memory:', echo=False)
# 创建ORM映射基类
Base = declarative_base()


# 创建ORM对象类
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User(id='%s',name='%s', fullname='%s', nickname='%s')>" % (
            self.id, self.name, self.fullname, self.nickname)


# 根据映射创建数据库表 默认不会创建已经存在的表
Base.metadata.create_all(engine)

# 创建一个实例
ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
# print(ed_user.id)

# 创建数据库链接池
Session = sessionmaker(bind=engine)
# Session = sessionmaker()
# Session.configure(bind=engine)

# 获取数据库链接
session = Session()
# 保存数据到数据库持久层，等待flush
session.add(ed_user)
session.commit()


# # 查询数据，先触发持久层flush，再从数据库查询
# our_user = session.query(User).filter_by(name='ed').first()
# # session 持有对象，不再重新创建
# print(ed_user is our_user)
#
# # 批量添加数据
# session.add_all([
#     User(name='wendy', fullname='Wendy Williams', nickname='windy'),
#     User(name='mary', fullname='Mary Contrary', nickname='mary'),
#     User(name='fred', fullname='Fred Flintstone', nickname='freddy')])
#
# ed_user.nickname = 'eddie'
# # 修改能被session 捕获
# print(session.dirty)
# # 查看到新增的数据
# print(session.new)
# # 提交事务，将数据写入数据库 一次update 3次insert
# session.commit()
#
# ed_user.name = 'Edwardo'
# fake_user = User(name='fakeuser', fullname='Invalid', nickname='12345')
#
# print(session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all())
# session.rollback()
# print(session.query(User).filter(User.name.in_(['ed', 'fakeuser'])).all())
#

def merge(user):
    method_session = Session()
    if user.id is None:
        session.add(user)
    else:
        our_user = session.query(User).filter_by(id=user.id).first()
        if not our_user:
            session.add(user)
        else:
            for attr in our_user.__dict__.keys():
                if attr == 'id':
                    continue
                if hasattr(user, attr) and getattr(user, attr):

                    setattr(our_user, attr, getattr(user, attr))
    method_session.commit()
    method_session.close()


print(session.query(User).filter_by(id=1).all())
update_user = User(id=1, name='fakeuser', nickname='12345', fullname=None)
merge(update_user)

print(session.query(type(update_user)).filter_by(id=1).all())
