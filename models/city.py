#!/usr/bin/python3


from models.base_model import BaseModel


class City(BaseModel):
    """
    Rep a City inherited from base model

    Public class attributes:
    state_id: string - string: the State.id
    name: string - empty string
    """
    state_id = ""
    name = ""
