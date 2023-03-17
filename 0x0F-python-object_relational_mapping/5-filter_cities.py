#!/usr/bin/python3
'''script that lists all states from the database hbtn_0e_0_usa
'''

import MySQLdb
import sys

if __name__ == "__main__":

    if (len(sys.argv) == 5):
        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()
        query = "SELECT cities.name FROM cities INNER JOIN states ON\
        cities.state_id = states.id WHERE\
        states.name = %s ORDER BY cities.id;"
        cur.execute(query, (sys.argv[4],))
        for row in cur.fetchall():
            print(row)
        cur.close()
        db.close()
