#!/usr/bin/python3
"""
This script deletes all State objects with a name containing
the letter 'a' from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    # Unpack command-line arguments
    username, password, database = sys.argv[1:4]

    # Create the database engine
    eng_url = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(eng_url.format(username, password, database), pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query states to delete
    states_to_delete = session.query(State).filter(State.name.ilike('%a%')).all()

    # Check if there are any states to delete
    if states_to_delete:
        for state in states_to_delete:
            session.delete(state)
        session.commit()  # Commit all deletions

    # Close the session
    session.close()
