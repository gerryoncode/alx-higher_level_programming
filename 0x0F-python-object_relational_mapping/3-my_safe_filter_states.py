#!/usr/bin/python3
""""displays all values in the states, hbtn_0e_0_usa where name == argument"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    state = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s", (state,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
