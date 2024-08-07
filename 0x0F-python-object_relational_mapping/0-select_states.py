#!/usr/bin/python3

"""
Query All states for database
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
        print(row)


if __name__ == "__main__":
    main()
