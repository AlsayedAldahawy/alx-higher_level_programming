#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves all rows from the
    'states' table.
It requires command-line arguments for the MySQL user, password, and
    database name.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Establish a connection to the MySQL database
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2],
                           db=argv[3], charset="utf8")

    # Create a cursor to execute SQL queries
    cur = conn.cursor()

    # Execute a query to retrieve all states from the 'states' table
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()

    # Print each row retrieved from the database
    for row in query_rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    conn.close()
