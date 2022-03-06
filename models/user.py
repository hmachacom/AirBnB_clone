#!/usr/bin/python3
""" Class User inherit from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ inherits Class User from BaseModel """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
