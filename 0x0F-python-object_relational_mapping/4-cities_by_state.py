#!/usr/bin/python3
'''script that lists all states from the database hbtn_0e_0_usa
'''

import MySQLdb
import sys

if __name__ == "__main__":

    if (len(sys.argv) == 4):
        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()
        query = "SELECT cities.id, cities.name, states.name FROM cities\
        JOIN states ON cities.state_id = states.id ORDER BY states.id;"
        cur.execute(query)
        for row in cur.fetchall():
            print(row)
        cur.close()
        db.close()
