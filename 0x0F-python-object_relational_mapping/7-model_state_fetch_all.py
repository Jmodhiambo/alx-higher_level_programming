#!/usr/bin/python3
"""
This script that lists all State objects from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Unpacking commands
    s1, s2, s3 = sys.argv[1:4]

    eng_url = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(eng_url.format(s1, s2, s3), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")
