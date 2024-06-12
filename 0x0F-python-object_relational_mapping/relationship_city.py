#!/usr/bin/python3

"""
This module defines the SQLAlchemy model for the "cities" table.

Usage:
    - Import this module to use the City class for database operations.
    - The City class represents a city entity with an ID, name, and
    associated state.

Attributes:
    __tablename__ (str): The name of the database table.
    id (int): Primary key for the city entity.
    name (str): Name of the city (max length: 128 characters).
    state_id (int): Foreign key referencing the associated state.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """
    Represents a city entity in the database.

    Attributes:
        id (int): Primary key for the city entity.
        name (str): Name of the city (max length: 128 characters).
        state_id (int): Foreign key referencing the associated state.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
