#!/usr/bin/python3
"""
Module of generate JSON
"""
import json


def to_json_string(my_obj):
    """
    JSON representation of an object

    Returns:
        returns the JSON representation
    """
    return json.dumps(my_obj)
