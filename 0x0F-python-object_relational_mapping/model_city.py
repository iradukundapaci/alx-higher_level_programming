#!/usr/bin/python3
""" Model for City table in database
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """City class

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The id of the class
        name (str): The name of the class
        state_id (int): The state the city belongs to

    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __init__(self, name, state_id) -> None:
        """ initializes state object
            args:
                name: name of state
        """
        self.name = name
        self.state_id = state_id

    def __repr__(self) -> String:
        """ String represantion of state object
            args:
                self: object
            return:
                String
        """
        return f"{self.id}: {self.name}"
