#!/usr/bin/python3

"""
A python file that contains the class definition of a State and an instance
Base = declarative_base()
State class: inherits from Base Tips
    links to the MySQL table states
    class attribute id that represents a column of an auto-generated, unique
    integer, can’t be null and is a primary key
    class attribute name that represents a column of a string with maximum 128
    characters and can’t be null
"""
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class that represents states table in database
    """
    __tablename__ = 'states'
    id = Column(Integer, Sequence('states_id_seq'), primary_key=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return "<State(name='%s')>" % (self.name)
