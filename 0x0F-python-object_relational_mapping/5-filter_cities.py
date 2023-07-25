#!/usr/bin/python3
"""
This script lists all cities from
the database `hbtn_0e_4_usa`.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Access to the database and get the cities
    from the database.
    """
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=user,
                         passwd=password, db=db_name)

    cursor = db.cursor()
    cursor.execute(
        f"""select name from cities where
        state_id=(select id from states where name='{state}')"""
    )
    rows = cursor.fetchall()

    if rows is not None:
        print(", ".join([row[0] for row in rows]))
    cursor.close()
    db.close()
