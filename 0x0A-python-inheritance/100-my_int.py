#!/usr/bin/python3
"""
Module My int
"""


class MyInt(int):
    """Class My int"""

    def __ne__(self, other):
        return super().__eq__(other)

    def __eq__(self, other):
        return super().__ne__(other)
