#!/usr/bin/python3
"""
This script lists all City objects from the database hbtn_0e_101_usa,
along with their corresponding State names.
"""
import sys
from relationship_state import Base, State
from relationship_city import City
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

    # Query all cities with their associated states
    cities = session.query(City).order_by(City.id).all()

    # Print results
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    # Close the session
    session.close()
