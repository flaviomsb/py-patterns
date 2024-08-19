from math import pi, pow


def calculate_circle_area(radius) -> float:
    """
    Calculate the area of a circle

    :param radius: Radius of a circle
    :return: Area of a circle
    """
    return pi * pow(radius, 2)


help(calculate_circle_area)
