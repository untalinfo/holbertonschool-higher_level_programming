#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dataBase = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=dataBase)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s\
        ORDER BY id ASC;", (state,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
