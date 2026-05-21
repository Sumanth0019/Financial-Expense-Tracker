from sqlalchemy import Column,Integer,String,Float,ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):

    __tablename__="users"

    id=Column(Integer,primary_key=True)
    username=Column(String,unique=True)
    email=Column(String)
    password=Column(String)


class Expense(Base):

    __tablename__="expenses"

    id=Column(Integer,primary_key=True)

    username=Column(String)

    amount=Column(Float)

    category=Column(String)

    description=Column(String)