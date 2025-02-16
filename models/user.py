#!/usr/bin/python3
""" holds class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
#import hashlib


class User(BaseModel, Base):
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        #chech whether 'password' is a key in the keyword args (kwargs)
        #pwd = kwargs.pop('password', None)
        #if pwd:
            #create MDS hash obj
            #secure.update(pwd.encode("utf-8"))
            # Get the hex digest of hash
            #secure_password = secure.hexdigest()
            # update the password key in kwargs with hash password
            #kwargs['password'] = secured_password 
        super().__init__(*args, **kwargs)
