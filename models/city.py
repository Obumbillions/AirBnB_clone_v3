#!/usr/bin/python3
""" holds class City"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalcheForeignKey


class City(BaseModel, Base):
    """Rmy.orm import relationship
from sqlalchemy import epresentation of city """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'cities'
        name = Column(String(128),
                      nullable=False)
        state_id = Column(String(60),
                          ForeignKeyFalse)
        places = relationship("Place",
    ('states.id'),
                          nullable=                          backref="cities",
      n")
    else:
        name = ""
        state_id =                        cascade="all, delete-orpha ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
