#!/usr/bin/python3
"""
3-my_safe_filter_states script
"""
import MySQLdb
import sys


def get_N_states(uName, pWord, dbName, sName):
    """
        get_states
        - Lists 'sName' states from the database 'hbtn_0e_0_usa'
    """
    db = MySQLdb.connect(
            host='localhost', port=3306,
            user=uName, passwd=pWord,
            db=dbName
            )
    cur = db.cursor()
    exec_str = "SELECT * FROM states \
            WHERE name LIKE BINARY %s \
            ORDER BY id ASC"
    cur.execute(exec_str, (sName,))
    rows = cur.fetchall()
    for _ in rows:
        print(_)
    cur.close()
    db.close()


if __name__ == "__main__":
    try:
        uName, pWord, dbName, sName = sys.argv[1:5]
        get_N_states(uName, pWord, dbName, sName)
    except TypeError:
        ...
