#!/usr/bin/python3
"""
module for load from json file.
"""
import json


def load_from_json_file(filename):
    with open(filename, encoding='UTF-8') as f:
        return json.load(f)
