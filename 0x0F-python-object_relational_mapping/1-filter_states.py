#!/usr/bin/python3

"""
This script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Unpacking command-line arguments
    username, password, database = sys.argv[1:4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    cur = db.cursor()

    cur.execute("""
    SELECT * FROM states WHERE states.name LIKE BINARY 'N%' ORDER BY id ASC
    """)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
