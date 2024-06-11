#!/usr/bin/python3

"""
This script adds a new state named "Louisiana" to a MySQL database.

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

    # Create a new state object
    state = State(name="Louisiana")
    session.add(state)

    # Query the state ID for the newly added state
    state_id = session.query(State.id).filter(
        State.name == "Louisiana").one_or_none()
    print(state_id.id)

    # Commit the changes to the database
    session.commit()
