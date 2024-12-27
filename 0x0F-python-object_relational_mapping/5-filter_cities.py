#!/usr/bin/python3
"""
This script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Unpacking commands
    username, password, database, state_name = sys.argv[1:5]

    # Connects to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # Creating a cursor object
    cur = db.cursor()

    # Spliting the query to with PEP 8 standards (avoid pycodestyle error)
    query = ("SELECT c.name "
             "FROM cities AS c "
             "JOIN states AS s ON c.state_id = s.id "
             "WHERE s.name = BINARY %s "
             "ORDER BY c.id")

    cur.execute(query, (state_name,))

    # Fetching and printing the resuts
    rows = cur.fetchall()
    print(", ".join(row[0] for row in rows))

    # Closing the cursor and database connection
    cur.close()
    db.close()
