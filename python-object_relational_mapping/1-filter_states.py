#!/usr/bin/python3
"""Lists all states with a name starting with N (upper N) from the database"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to the database using arguments from the command line
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()

    # Execute the query with a filter
    # LIKE BINARY 'N%' ensures we only get names starting with specific uppercase 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
