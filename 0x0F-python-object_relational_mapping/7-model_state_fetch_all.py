#!/usr/bin/python3
"""
This script that lists all State objects from the database hbtn_0e_6_usa,
sorted by states.id in ascending order.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Unpacking arguments (s1=username s2=password s3=database)
    s1, s2, s3 = sys.argv[1:4]

    # Create engine and connect to the database
    eng_url = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(eng_url.format(s1, s2, s3), pool_pre_ping=True)

    # Start a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and display all states sorted by id
    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
