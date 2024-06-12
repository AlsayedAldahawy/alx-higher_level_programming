#!/usr/bin/python3

"""
This script retrieves and prints city names along with their associated state
names from a MySQL database.

Usage:
    - Ensure you have the necessary dependencies installed
        (SQLAlchemy, MySQLdb).
    - Run the script with the following command:
        python3 script_name.py <username> <password> <database_name>

Arguments:
    <username> (str): MySQL username.
    <password> (str): MySQL password.
    <database_name> (str): Name of the database containing the tables.

Example:
    python3 script_name.py myuser mypassword mydatabase
"""

if __name__ == "__main__":
    from sys import argv
    from model_city import City
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    # Create a database connection
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the "states" table and order results by state ID
    cities = session.query(State.name, City).join(
        State).order_by(City.id).all()

    # Print city names along with their associated state names
    [print("{}: ({}) {}".format(city[0], city[1].id, city[1].name))
     for city in cities]
