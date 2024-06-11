#!/usr/bin/python3

"""
This script retrieves and prints the state ID for a given state name from a
    MySQL database.

Usage:
    - Ensure you have the necessary dependencies installed
        (SQLAlchemy, MySQLdb).
    - Run the script with the following command:
        ./scriptname.py <username> <password> <database_name> <state_name>

Arguments:
    <username> (str): MySQL username.
    <password> (str): MySQL password.
    <database_name> (str): Name of the database containing the "states" table.
    <state_name> (str): Name of the state to query.

Example:
    ./scriptname.py myuser mypassword mydatabase California
"""

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    # Create a database connection
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the state ID for the given state name
    state_id = session.query(State.id).filter(
        State.name.like(argv[4])).one_or_none()

    if state_id:
        print(state_id.id)
    else:
        print("Nothing")
