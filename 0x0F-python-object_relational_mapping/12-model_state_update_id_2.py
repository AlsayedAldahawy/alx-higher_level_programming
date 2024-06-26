#!/usr/bin/python3

"""
This script updates the name of a state with ID 2 to "New Mexico" in database.

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

    # Query the state with ID 2
    state = session.query(State).filter(State.id == 2).one_or_none()

    # Update the state name
    state.name = "New Mexico"

    # Commit the changes to the database
    session.commit()
