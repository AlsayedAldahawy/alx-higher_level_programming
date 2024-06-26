#!/usr/bin/python3

"""
This script retrieves and prints state IDs and names from a database.
The query filters states whose names contain the letter 'a'.

Usage:
    - Ensure you have the necessary dependencies installed
        (SQLAlchemy, MySQLdb).
    - Run the script with the following command:
        ./9-model_state_filter_a.py <username> <password> <database_name>

Arguments:
    <username> (str): MySQL username.
    <password> (str): MySQL password.
    <database_name> (str): Name of the database containing the "states" table.

Example:
    ./9-model_state_filter_a.py myuser mypassword mydatabase
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

    # Query states and print IDs and names
    states = session.query(State).order_by(
        State.id).filter(State.name.like('%a%'))
    [print(state.id, state.name, sep=": ") for state in states]
