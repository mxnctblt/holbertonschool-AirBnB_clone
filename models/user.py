#!/usr/bin/python3`
"""
This module contain the user class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Our user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
