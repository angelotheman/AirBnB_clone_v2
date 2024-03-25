#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class to add a new state object"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        name = ""

        @projecty
        def cities(self):
            """
            Return the list of city objects from storage linked to the
            current State
            """
            city_list = []
            for city_obj in models.storage.all("City").values():
                if city_obj.state.id == self.id:
                    city_list.append(city_obj)
            return city_list

    def __init__(self, *args, **kwargs):
        super().__init__(args, **kwargs)
