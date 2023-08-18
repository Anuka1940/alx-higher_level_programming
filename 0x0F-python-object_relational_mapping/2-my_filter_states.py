#!/usr/bin/python3
""" This script lists all states starting with 'N' from the database
hbtn_0c_0_usa using MYSQLdd
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    Access and query database to get list of all states
    that contain the searched name"""

    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}'\
            ORDER BY id".format(state_name)
    cursor.execute(query)

    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()
