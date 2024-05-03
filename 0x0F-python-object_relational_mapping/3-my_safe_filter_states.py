#!/usr/bin/python3

"""
Query states for state mathcing 4th arguement and prevent sql injection
"""

import MySQLdb
import sys


def main():
    db = MySQLdb.connect(
        host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
        )
    cur = db.cursor()
    qry = "SELECT * FROM states WHERE BINARY name = %s ORDER BY states.id ASC"
    cur.execute(qry, (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
