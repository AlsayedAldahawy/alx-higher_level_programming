#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves rows from the
'states' table where the state name matches the specified input (provided
as a command-line argument). It requires command-line arguments for the MySQL
user, password, database name, and state name.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Establish a connection to the MySQL database
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )

    # Create a cursor to execute SQL queries
    cur = db.cursor()

    # Execute a query to retrieve rows with the specified state name
    querry = "SELECT * FROM states WHERE name LIKE BINARY %s;"
    param = (argv[4],)
    cur.execute(querry, param)

    # Fetch all rows returned by the query
    rows = cur.fetchall()

    # Print each row retrieved from the database
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
