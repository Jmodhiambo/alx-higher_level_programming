#!/usr/bin/python3
"""
This script creates the State “California” with the City “San Francisco”
in the database hbtn_0e_100_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    # Unpacking arguments
    username, password, database = sys.argv[1:4]

    # Create engine and connect to the database
    eng_url = f'mysql+mysqldb://{username}:{password}@localhost/{database}'
    engine = create_engine(eng_url, pool_pre_ping=True)

    # Create tables
    State.metadata.create_all(engine)

    # Start a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create State and City
    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)

    session.add(new_state)
    session.add(new_city)
    session.commit()

    # Close the session
    session.close()
