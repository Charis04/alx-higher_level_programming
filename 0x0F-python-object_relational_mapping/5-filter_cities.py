#!/usr/bin/python3
"""
A script that lists all cities of a state from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    qry = "select name from cities where state_id = (select id from states "\
        "where name = %s)"
    cur.execute(qry, (sys.argv[4],))
    rows = cur.fetchall()

    cities = [row[0] for row in rows]
    print(", ".join(cities))
