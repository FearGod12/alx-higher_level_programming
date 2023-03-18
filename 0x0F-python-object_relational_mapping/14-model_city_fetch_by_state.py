#!/usr/bin/python3
'''lists first State objects from the database
'''

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sys
from model_state import Base, State
from model_city import City
args = sys.argv
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(args[1], args[2], args[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State.name, City.id, City.name)\
        .order_by(City.id).all()
    for each in result:
        print("{}: ({}) {}".format(each[0], each[1], each[2]))
