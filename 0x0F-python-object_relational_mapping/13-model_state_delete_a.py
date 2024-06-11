#!/usr/bin/python3

"""
This script queries and deletes states whose names contain the letter 'a'
from a MySQL database.

Usage:
    - Ensure you have the necessary dependencies installed
        (SQLAlchemy, MySQLdb).
    - Run the script with the following command:
        python3 script_name.py <username> <password> <database_name>

Arguments:
    <username> (str): MySQL username.
    <password> (str): MySQL password.
    <database_name> (str): Name of the database containing the "states" table.

Example:
    python3 script_name.py myuser mypassword mydatabase
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

    # Query states with names containing 'a'
    states = session.query(State).filter(State.name.like('%a%'))

    # Delete the selected states
    for state in states:
        # print(state, state.id, state.name) - testing the query before delete
        session.delete(state)

    # Commit the changes to the database
    session.commit()
