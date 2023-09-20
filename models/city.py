#!/usr/bin/python3
# Made by MEGA and LAILO
""" City Module for the HBNB project """
from models.base_model import BaseModel, Base
from models.stringtemplates import HBNB_TYPE_STORAGE, DB
from models.state import State
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, and contains state ID and name """

    __tablename__ = 'cities'
    if (getenv(HBNB_TYPE_STORAGE) == DB):
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship('Place', backref='cities',
                              cascade='all, delete, delete-orphan')
    else:
        state_id = ''
        name = ''
