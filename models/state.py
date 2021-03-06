#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(
        'name',
        String(128),
        nullable=False
    )
    cities = relationship('City', cascade='all, delete', backref="state")

    @property
    def cities(self):
        """ Return all list of instances with state_id = actual State.id """
        city_instances = []
        obj = storage.all('City')
        for ke, va in obj.items():
            if self.id == va['state_id']:
                    city_instances.append(va)
        return city_instances
    