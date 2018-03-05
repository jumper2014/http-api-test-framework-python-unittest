#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()   # create base class
engine = create_engine('mysql://root:123456@127.0.0.1:3306/api')    # init db connection
DBSession = sessionmaker(bind=engine)   # create DBSession class


class User(Base):
    __tablename__ = 'user'  # bind table name
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)
    age = Column(Integer, unique=False)

    def __init__(self, name, age):
        self.name = name
        self.age = age


def delete_user(name):
    session = DBSession()
    users = session.query(User)
    for user in users:
        if user.name == name:
            # find user
            session.delete(user)
            session.commit()
            session.close()
            break


if __name__ == "__main__":
    delete_user('Python')