#!/usr/bin/python3

"""
Query All states starting with N for database
"""

import MySQLdb
import sys


def main():
    db = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
        )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    rows = cur.fetchall()
    for row in rows:
        if row[1][0].isupper():
            print(row)


if __name__ == "__main__":
    main()
