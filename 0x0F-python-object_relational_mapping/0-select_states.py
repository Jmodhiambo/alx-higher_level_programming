#!/usr/bin/python3

"""This script that lists all states from the database hbtn_0e_0_usa. """

import MySQLdb
import sys

if __name__ == "__main__":
    # Unpacking command-line arguments
    username, password, database = sys.argv[1:4]

    # Establishing a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # Creating a cursor object
    cur = db.cursor()

    # Executing the query
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetching and printing the results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Closing the cursor and database connection
    cur.close()
    db.close()
