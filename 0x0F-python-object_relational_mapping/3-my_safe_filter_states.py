#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.

This time the script is safe from
MySQL injections!
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
    arg = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=user, port=3306,
                         passwd=password, db=db_name)

    cursor = db.cursor()

    cursor.execute("""
            SELECT
                *
            FROM
                states
            WHERE
                name LIKE BINARY %(name)s
        """, {
        'name': arg
    })
    rows = cursor.fetchall()

    for i in rows:
        print(i)
    cursor.close()
    db.close()
