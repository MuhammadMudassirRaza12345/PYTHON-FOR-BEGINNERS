"""
A module is a file, that contains related fucntions and classes 
"""
from math import sqrt as square


def area_of_triangle(length, width, unit='meters'):
    area = 1/2*(length*width)
    return area, unit


def check_right_triangle(a, b, c):
    # Pythagorous Theorem
    # H2 =  B2  +  P2
    #  c2 = b2 + a2
    if (square(c) == (square(a) + square(b))):
        return "Triangle is a right angle triangle"
    else:
        return"The triangle is not a right triangle"
