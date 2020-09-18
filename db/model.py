from sqlalchemy import create_engine, Column, Integer, String
from db import configdb

Base = configdb.Base

class User(Base):
    __tablename__ = 'user'  # if you use base it is obligatory

    id = Column(Integer, primary_key=True)  # obligatory
    name = Column(String)
    password = Column(String)

    def __repr__(self):  # optional
        return f'User {self.name}'

    @classmethod
    def find_by_name(cls, session, name):
        return session.query(cls).filter_by(name=name).all()

# def start():
#     engine = create_engine('sqlite:///test.db', echo=True)
#     engine.execute("PRAGMA journal_mode=WAL")
# 
#     Session = sessionmaker(bind=engine)
#     session = Session()
# 
#     Base.metadata.create_all(engine)
#     return engine, session
