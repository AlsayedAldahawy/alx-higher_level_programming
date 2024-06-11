#!/usr/bin/python3
"""
Connects to a MySQL database and retrieves data from the 'cities' table,
joining it with the 'states' table. Prints the resulting rows.
Requires command-line arguments for MySQL user, password, and database name.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Establish a connection to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()

    # Execute a query to join 'cities' and 'states' tables
    query = "SELECT * FROM cities c LEFT JOIN states s ON c.state_id = s.id;"
    cur.execute(query)

    # Fetch all rows returned by the query
    rows = cur.fetchall()

    # Print each row retrieved from the database
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
