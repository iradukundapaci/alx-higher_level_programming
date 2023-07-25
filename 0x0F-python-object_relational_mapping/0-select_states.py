#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """
    import MySQLdb
    import sys

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=user,
                         passwd=password, db=db_name)

    cursor = db.cursor()

    cursor.execute("select * from states order by id asc")
    rows = cursor.fetchall()

    for i in rows:
        print(i)
    cursor.close()
    db.close()
