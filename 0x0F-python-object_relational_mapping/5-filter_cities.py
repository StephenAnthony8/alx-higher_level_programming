#!/usr/bin/python3
"""
5-filter_cities script
"""
import MySQLdb
import sys


def filter_cities(uName, pWord, dbName, aState):
    """
        filter_cities
        - filters cities via state arg in the db 'hbtn_0e_0_usa'
    """
    db = MySQLdb.connect(
            host='localhost', port=3306,
            user=uName, passwd=pWord,
            db=dbName
            )
    cur = db.cursor()
    exec_str = "SELECT cities.name \
            FROM cities \
            INNER JOIN states ON states.id = cities.state_id \
            WHERE states.name LIKE BINARY %s \
            ORDER BY cities.id ASC"
    cur.execute(exec_str, (aState,))
    rows = cur.fetchall()
    cNames = list(row[0] for row in rows)
    print(*cNames, sep=", ")

    cur.close()
    db.close()


if __name__ == "__main__":
    uName = sys.argv[1]
    pWord = sys.argv[2]
    dbName = sys.argv[3]
    aState = sys.argv[4]

    filter_cities(uName, pWord, dbName, aState)
