#!/usr/bin/python3

"""
This module defines the SQLAlchemy model for the "states" table.

Usage:
    - Import this module to use the State class for database operations.
    - The State class represents a state entity with an ID and a name.

Example:
    from mymodule import State
    state = State(name="California")
    # Perform database operations using the state object.

Attributes:
    __tablename__ (str): The name of the database table.
    id (int): Primary key for the state entity.
    name (str): Name of the state (max length: 128 characters).
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents a state entity in the database.

    Attributes:
        id (int): Primary key for the state entity.
        name (str): Name of the state (max length: 128 characters).
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
