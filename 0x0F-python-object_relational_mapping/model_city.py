#!/usr/bin/python3
"""model that create a python file with the class defination
of Cities using SQLAlchemy"""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """ A state class tha maps to the state table in the database"""

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
