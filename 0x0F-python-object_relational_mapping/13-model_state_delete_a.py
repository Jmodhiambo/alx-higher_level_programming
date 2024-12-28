#!/usr/bin/python3
"""
This script deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
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

    # Start a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to change the name of the state which id is 2.
    for state in session.query(State).filter(State.name.ilike('%a%')):
        session.delete(state)

    session.commit()

    # Close the session
    session.close()
