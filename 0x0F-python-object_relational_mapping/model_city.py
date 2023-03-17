#!/usr/bin/python3
'''contains the class definition of a City.
'''

from sqlalchemy.ext.declaration import declaration_base
from sqlalchemy import String, Integer, Column, ForeignKey
Base = declarative_base()


class City(Base):
    '''inherits from Base and links to the MySQL table cities
    fields:
    id - that represents a column of an auto-generated, unique integer,
    can’t be null and is a primary key
    name - that represents a column of a string of 128 characters and
    can’t be null
    state_id - that represents a column of an integer, can’t be null
    and is a foreign key to states.id
    '''
    __tablename__ = "cities"
    id = Colunm(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Colunm(String(128), nullable=False)
    state_id = Colunm(Integer, nullable=False ForeignKey('states.id'))
