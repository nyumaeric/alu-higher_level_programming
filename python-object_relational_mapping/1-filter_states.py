#!/usr/bin/python3
"""Script that lists all states with a name starting with 'N'
from the database hbtn_0e_0_usa. Takes 3 arguments: mysql username,
mysql password and database name
"""

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states \
                Where name Like 'N%' \
                ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
