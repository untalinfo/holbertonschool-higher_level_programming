#!/usr/bin/python3
"""
module for load from json file.
"""
import json


def load_from_json_file(filename):
    with open(filename, 'r', encoding='UTF-8') as f:
        return json.loads(f.read())
