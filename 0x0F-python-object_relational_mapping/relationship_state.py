#!/usr/bin/python3
"""
This module defines the State class with a relationship to the City class.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import City
from relationship_base import Base


class State(Base):
    """Represents a state for a MySQL database."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City", back_populates="state", cascade="all, delete-orphan"
    )
