#!/usr/bin/python3
"""
3-my_safe_filter_states script
"""
import MySQLdb
import sys


def get_N_states(uName, pWord, dbName):
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
    exec_str = "SELECT cities.id, cities.name, states.name \
            FROM cities \
            INNER JOIN states ON cities.state_id = states.id \
            ORDER BY cities.id ASC"
    cur.execute(exec_str)
    rows = cur.fetchall()
    for _ in rows:
        print(_)
    cur.close()
    db.close()


if __name__ == "__main__":
    try:
        uName, pWord, dbName = sys.argv[1:4]
        get_N_states(uName, pWord, dbName)
    except TypeError:
        ...
