#!/usr/bin/python3
'''lists first State objects from the database
'''

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sys
from model_state import Base, State

args = sys.argv
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(args[1], args[2], args[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_obj = session.query(State).filter(State.id == '2').one()
    state_obj.name = "New Mexico"
    session.commit()
