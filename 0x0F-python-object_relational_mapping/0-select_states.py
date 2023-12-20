#!/usr/bin/python3
""" Lists all states from the databse hbtn_0e_0_usa """
# host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
