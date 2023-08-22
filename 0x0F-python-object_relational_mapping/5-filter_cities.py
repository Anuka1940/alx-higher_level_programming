#!/usr/bin/python3
""" This script lists all states from the database hbtn_0e_0_usa using
the MySQLdb library in Python
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Access and query database"""

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
    query = "SELECT cities.name, cities.id \
            FROM cities JOIN states \
            ON state_id=states.id \
            WHERE states.name =  %s \
            ORDER BY cities.id ASC"
    cursor.execute(query, (state_name,))

    results = cursor.fetchall()
    if results:
        print(", ".join([row[0] for row in results]))
    cursor.close()
    db.close()
