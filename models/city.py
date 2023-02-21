#!/usr/bin/python3
"""This module contain our city class that inherit from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Our City class"""
    state_id = ""
    name = ""
