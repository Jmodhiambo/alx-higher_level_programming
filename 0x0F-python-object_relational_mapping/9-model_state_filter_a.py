#!/usr/bin/python3
"""
This script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
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

    # Query to print states with letter a.
    for state in session.query(State).\
            filter(State.name.ilike('%a%')).order_by(State.id):
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
