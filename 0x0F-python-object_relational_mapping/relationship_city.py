#!/usr/bin/python3
'''contains the class definition of a City.
'''

from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


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
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
