#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import environ
import sqlalchemy

if environ['HBNB_TYPE_STORAGE'] == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                Column('place_id', String(60), ForeignKey('places.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True, nullable=False),        
                Column('amenity_id', String(60), ForeignKey('amenities.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True, nullable=False)    
            )


class Place(BaseModel, Base):
    """ A place to stay """


    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    
    try: 
        if environ['HBNB_TYPE_STORAGE'] == 'db':
            reviews = relationship("Review", backref="place",
                           cascade="all, delete, delete-orphan")
            amenities = relationship("Amenity", secondary='place_amenity', backref="place_amenities", viewonly=False)
    
    except Exception as ex:

        @property
        def reviews(self):
            """Returns the list of Review instances from current place"""
            from models import storage
            all_reviews = storage.all(BaseModel.Review)
            return [review for review in all_reviews.values()
                    if review.place_id == self.id]

        @property
        def amenities(self):
            """returns the list of amenity instances from current place"""
            from models import storage
            from models.amenity import Amenity
            print("the getter is running")
            return [amenity for amenity in storage.all(Amenity).values()
                    if amenity.id in self.amenity_id]

        @amenities.setter
        def amenities(self, value):
            """sets value of amenity property"""
            from models.amenity import Amenity
            print("the setter has run")
            self.amenity_id = []
            if isinstance(value, Amenity):
                if value.id not in self.amenity_id:
                    self.amenity_id.append(value.id) 

