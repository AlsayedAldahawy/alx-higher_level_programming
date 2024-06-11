#!/usr/bin/python3

"""
Script retrieves a list of cities in a specified state from a MySQL database.

Usage:
    ./5-filter_cities.py <username> <password> <database_name> <state_name>

Arguments:
    <username> (str): MySQL username.
    <password> (str): MySQL password.
    <database_name> (str): Name of the database.
    <state_name> (str): Name of the state.

Returns:
    None: Prints the list of city names to the console.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Establish a connection to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()

    # Define the SQL query to retrieve city names for a given state
    query = """SELECT c.name FROM cities c LEFT JOIN states s
               ON c.state_id = s.id WHERE s.name = %s ORDER BY c.id ASC;"""

    param = (argv[4],)  # Specify the state name as a parameter

    cur.execute(query, param)  # Execute the query

    # Fetch all rows returned by the query
    rows = cur.fetchall()

    # Extract city names from the rows
    cities = list(row[0] for row in rows)

    # Print the city names separated by commas
    print(*cities, sep=', ')
    # print(', '.join(city_name))

    # Close the cursor and database connection
    cur.close()
    db.close()
