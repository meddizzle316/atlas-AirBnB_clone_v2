#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models import place

# creation of a State
if place.amenities is None:
    print("None checked")
state = State(name="California")
state.save()
# creation of a City
city = City(state_id=state.id, name="San Francisco")
city.save()
# creation of a User
user = User(email="john@snow.com", password="johnpwd")
user.save()
# creation of 2 Places
place_1 = Place(user_id=user.id, city_id=city.id, name="House 1")
place_1.save()
place_2 = Place(user_id=user.id, city_id=city.id, name="House 2")
place_2.save()
# creation of 3 various Amenity
amenity_1 = Amenity(name="Wifi")
amenity_1.save()
amenity_2 = Amenity(name="Cable")
amenity_2.save()
amenity_3 = Amenity(name="Oven")
amenity_3.save()

# link place_1 with 2 amenities
print(f"\nPlace amenities list: {place_1.amenities}")
place_1.amenities.append(amenity_1)
place_1.amenities.append(amenity_2)
print(f"Place amenities list post append: {place_1.amenities[0]}\n")

# link place_2 with 3 amenities
print(f"\nPlace amenities list: {place_2.amenities}")
place_2.amenities.append(amenity_1)
print(f"Place amenities list post append: {place_2.amenities[0]}\n")
place_2.amenities.append(amenity_2)
place_2.amenities.append(amenity_3)
storage.save()
print("OK")
