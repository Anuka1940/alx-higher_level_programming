#!/usr/bin/python3
""" This script is safe from MYSQL injections by using parameterized queries
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
    query = "SELECT * FROM states WHERE name = %s\
            ORDER BY id"
    cursor.execute(query, (state_name,))

    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()
