#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa.
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    # Unpacking arguments
    username, password, database = sys.argv[1:4]

    # Create engine and connect to the database
    eng_url = (
        'mysql+mysqldb://{}:{}@localhost/{}'
    ).format(username, password, database)

    engine = create_engine(eng_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Start a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query
    results = session.query(State, City).\
        filter(State.id == City.state_id).order_by(City.id)
    for state, city in results:
        print(f"{state.name}: {city.id} {city.name}")

    # Close the session
    session.close()
