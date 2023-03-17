#!/usr/bin/python3
'''Defines a state class
'''

import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''
    Class State instance of Base
    Linked to mysql table state
    '''
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
