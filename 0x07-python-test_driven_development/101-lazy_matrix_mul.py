#!/usr/bin/python3
"""
This module multiplies 2 matrices 
"""
import numpy as n


def lazy_matrix_mul(m_a, m_b):
    """
    function that multiplies 2 matrices by using the module NumPy
    """
    return n.matmul(m_a, m_b)
