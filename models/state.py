#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ
from operator import itemgetter


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    _cities = relationship("City", backref="state",
                           cascade="all, delete, delete-orphan")

    def __getitem__(self, item):
        return getattr(self, item)
    """trying something out for task 10 of the airbnb web flask project"""

    if environ['HBNB_TYPE_STORAGE'] == 'db':
        @property
        def cities(self):
            from models import storage
            sorted_list = []
            all_cities = storage.all(City)
            list = [city for city in all_cities.values()
                    if city.state_id == self.id]
            return sorted(list, key=itemgetter('name'))
    else:
        @property
        def cities(self):
            from models import storage
            all_cities = storage.all(City)
            list = [city for city in all_cities.values()
                    if city.state_id == self.id]
            return sorted(list, key=itemgetter('name'))
