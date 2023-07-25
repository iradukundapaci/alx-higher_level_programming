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

    db = MySQLdb.connect(host="localhost", user=user,
                         passwd=password, db=db_name)

    cursor = db.cursor()
    cursor.execute(
        """select cities.id, cities.name, states.name
        from cities join states on cities.state_id = states.id
        order by cities.id asc"""
    )
    rows = cursor.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
    cursor.close()
    db.close()
