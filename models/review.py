#!/usr/bin/python3
"""This module contain our review class that inherit from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Our review class"""
    place_id = ""
    user_id = ""
    text = ""
