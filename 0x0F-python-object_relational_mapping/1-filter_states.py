#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves all rows from the 'states' table
where the state name starts with the letter 'N'.
It requires command-line arguments for the MySQL user, password, and database name.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Establish a connection to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    # Create a cursor to execute SQL queries
    cur = db.cursor()

    # Execute a query to retrieve states whose names start with 'N'
    cur.execute('SELECT * FROM states WHERE name LIKE "N%"')

    # Fetch all rows returned by the query
    rows = cur.fetchall()

    # Print each row retrieved from the database
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
