#!/usr/bin/python3
'''lists first State objects from the database
'''

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sys
from model_state import Base, State

args = sys.argv
if __name__ == '__main__':
    if (len(args) == 5):
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(args[1], args[2], args[3]),
                               pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        state_name = args[4]
        try:
            result = session.query(State.id)\
                .filter(State.name == state_name).order_by(State.id).one()
            print("{}".format(result[0]))
        except Exception:
            print("Not found")
