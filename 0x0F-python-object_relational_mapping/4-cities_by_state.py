#!/usr/bin/python3
"""
This script that lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Unpacking commands
    username, password, database = sys.argv[1:4]

    # Connects to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # Creating a cursor object
    cur = db.cursor()

    # Spliting the query to with PEP 8 standards (avoid pycodestyle error)
    query1 = "SELECT c.id, c.name, s.name FROM cities AS c "
    query2 = "JOIN states AS s ON c.state_id = s.id ORDER BY c.id"
    query = query1 + query2
    cur.execute(query)

    """ --The best way--
    query = ("SELECT c.id, c.name, s.name "
             "FROM cities AS c "
             "JOIN states AS s ON c.state_id = s.id "
             "ORDER BY c.id")
    """

    # Fetching and printing the resuts
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Closing the cursor and database connection
    cur.close()
    db.close()
