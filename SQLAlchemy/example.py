# 使用sql进行数据库链接初始化
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:root@localhost:3306/sqlalchemy')
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    def __init__(self, name):
        self.name = name

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, index=True)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.name)


# 初始化环境
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
# 创建Sesion
Session = sessionmaker(bind=engine)
session = Session()
# 增删改查操作
user = User('stark')
session.add(user)
session.commit()

user = session.query(User).get(1)
print(user)

user.name = 'stark_tan'
session.add(user)
session.commit()
user = session.query(User).get(1)
print(user)

session.delete(user)
session.commit()
users = session.query(User).all()
print(users)
