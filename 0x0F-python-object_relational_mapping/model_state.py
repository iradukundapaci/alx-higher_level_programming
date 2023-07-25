#!/usr/bin/python3
""" Model for State table in database
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ Blueprint for state table in database
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    def __init__(self, name) -> None:
        """ initializes state object
            args:
                name: name of state
        """
        self.name = name

    def __repr__(self) -> String:
        """ String represantion of state object
            args:
                self: object
            return:
                String
        """
        return f"{self.id}: {self.name}"
