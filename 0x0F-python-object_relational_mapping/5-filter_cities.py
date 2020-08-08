#!/usr/bin/python3
# lists all states from the database hbtn_0e_0_usa

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
    cur.execute("SELECT cities.name FROM cities\
    JOIN states ON cities.state_id = states.id\
    WHERE states.name=%s ORDER BY cities.id ASC;", (state,))
    rows = cur.fetchall()
    i = 0
    for row in rows:
        if i != 0:
            print(", ", end="")
        print("".join([row[0]]), end="")
        i += 1
    print("")
    cur.close()
    db.close()
