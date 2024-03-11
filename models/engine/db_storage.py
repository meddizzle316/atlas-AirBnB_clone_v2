#!/usr/bin/python3
"""
Module to create an engine for database storage in SQL using SQLAlchemy
"""
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage():
    """Class to hold DB engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Init for dbstorage"""
        import os
        from sqlalchemy import create_engine
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{password}@{host}:3306/{database}',
            pool_pre_ping=True
            )
        if os.getenv('HBNB_ENV') == 'test':
            # Drop all tables if the environment is 'test'
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Gets all instances of cls or of all classes if cls is None"""
        import copy
        dict = {}
        classes = [User, State, City, Place, Amenity, Review]\
            if cls is None else [cls]
        for cls in classes:
            try:
                instances = self.__session.query(cls).all()
                for instance in instances:
                    deep_copy = copy.deepcopy(instance)
                    if '_sa_instance_state' in deep_copy.__dict__.keys():
                        del deep_copy.__dict__['_sa_instance_state']
                    dict[f"{cls.__name__}.{deep_copy.id}"] = deep_copy
            except Exception:
                pass
        return dict

    def new(self, obj):
        """Saves a specific object to the database"""
        print("new has run")
        try:
            self.__session.add(obj)
        except Exception:
            pass

    def save(self):
        """Saves the current session"""
        print("save has run")
        self.__session.commit()

    def delete(self, obj=None):
        """Remove obj from database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reloads the database into __session"""
        from sqlalchemy.orm import sessionmaker, scoped_session
        Base.metadata.create_all(self.__engine)
        dbsession = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(dbsession)
        self.__session = session()


    def close(self):
        """calls remove on private session attribute """
        from sqlalchemy.orm import scoped_session
        scoped_session.remove()
