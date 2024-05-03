#!/usr/bin/python3

"""
Query states for state mathcing 4th arguement
"""

import MySQLdb
import sys


def main():
    db = MySQLdb.connect(
        host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
        )
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)


if __name__ == "__main__":
    main()
