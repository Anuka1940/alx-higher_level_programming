#!/usr/bin/python3
""" This script lists all states from the database hbtn_0e_0_usa using
the MySQLdb library in Python
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Access and query database"""

    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)
    cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name \
            FROM cities join states \
            ON cities.state_id=states.id \
            ORDER BY cities.id ASC"
    cursor.execute(query)

    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()
