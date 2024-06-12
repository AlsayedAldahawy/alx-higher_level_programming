#!/usr/bin/python3

"""
This script establishes a one-to-many relationship between states and cities
in a MySQL database.

Usage:
    - Ensure you have the necessary dependencies installed
        (SQLAlchemy, MySQLdb).
    - Run the script with the following command:
        python3 script_name.py <username> <password> <database_name>

Arguments:
    <username> (str): MySQL username.
    <password> (str): MySQL password.
    <database_name> (str): Name of the database containing the "cities" and
        "states" tables.

Example:
    python3 script_name.py myuser mypassword mydatabase
"""

if __name__ == "__main__":
    from sys import argv
    from relationship_city import City
    from relationship_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    # Create a database connection
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a state and a city
    state = State(name="California")
    city = City(name="San Francisco")
    state.cities = [city]

    # Add to session and commit changes
    session.add(state)
    session.add(city)
    session.commit()
