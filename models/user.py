#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    # email = ''
    # password = ''
    # first_name = ''
    # last_name = ''

    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_column = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
