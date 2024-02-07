#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class inherits from BaseModel that reps the user.

    Public class attributes:
    email: string - empty string, for the user
    password: string - empty string, for the user
    first_name: string - empty string, of the user
    last_name: string - empty string, of the user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

