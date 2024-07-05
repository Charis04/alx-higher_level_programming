#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    qry = "SELECT c.id, c.name, s.name FROM cities c INNER JOIN"\
        " states s ON c.state_id = s.id; ORDER BY cities.id ASC"
    cur.execute(qry)
    rows = cur.fetchall()

    for row in rows:
        print(row)
