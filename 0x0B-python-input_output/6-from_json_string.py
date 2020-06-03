#!/usr/bin/python3
"""
Module json
"""
import json


def from_json_string(my_str):
    """
    object (Python data structure) represented by a JSON string

    Returns:
        returns an object
    """
    return json.loads(my_str)
