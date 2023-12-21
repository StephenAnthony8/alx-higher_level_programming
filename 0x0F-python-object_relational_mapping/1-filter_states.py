#!/usr/bin/python3
"""
1-filter_states script
"""
import MySQLdb
import sys


def get_N_states(uName, pWord, dbName):
    """
        get_states
        - Lists all states from the database 'hbtn_0e_0_usa'
    """
    db = MySQLdb.connect(
            host='localhost', port=3306,
            user=uName, passwd=pWord,
            db=dbName
            )
    cur = db.cursor()
    cur.execute("SELECT * FROM states \
            WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for _ in rows:
        print(_)
    cur.close()
    db.close()


if __name__ == "__main__":
    try:
        uName, pWord, dbName = sys.argv[1:]
        get_N_states(uName, pWord, dbName)
    except TypeError:
        ...
