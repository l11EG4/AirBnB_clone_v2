#!/usr/bin/python3
# Made by MEGA
""" Create a unique FileStorage instance 4 ur application"""

from models.engine.file_storage import FileStorage
from os import getenv
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
