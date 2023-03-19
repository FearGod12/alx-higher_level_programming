#!/usr/bin/python3
'''Creates the State "California" with the City "San Francisco"
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    # Connection arguments
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Open connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, password, db_name))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # Create California state
    new_state = State(name='California')
    # Create San Francisco city
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)
    # Add to session
    session.add(new_state)
    # Commit changes
    session.commit()
    # Close session
    session.close()
