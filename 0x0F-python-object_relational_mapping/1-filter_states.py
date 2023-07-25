#!/usr/bin/python3
"""
This script lists all states with
a `name` starting with the letter `N`
from the database `hbtn_0e_0_usa`.
"""

if __name__ == "__main__":
    """
    Access to the database and get the states
    """
    import MySQLdb
    import sys

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=user,
                         passwd=password, db=db_name)

    cursor = db.cursor()

    cursor.execute(
        """select id, name from states where
        name like binary 'N%' order by id asc"""
    )
    rows = cursor.fetchall()

    for i in rows:
        print(i)
    cursor.close()
    db.close()
