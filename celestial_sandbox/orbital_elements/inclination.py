"""
Utility functions related to Inclination

Inclination:
    Vertical tilt of the ellipse with respect to the reference plane, measured at the ascending node
    (where the orbit passes upward through the reference plane, the green angle i in the diagram).
    Tilt angle is measured perpendicular to line of intersection between orbital plane and reference plane.
    Any three points on an ellipse will define the ellipse orbital plane.
    The plane and the ellipse are both two-dimensional objects defined in three-dimensional space.
"""
import math
import numpy as np


def inclination_from_momentum_vector(h: np.array) -> float:
    """
    Calculates the inclination from the orbital momentum vector.

    Args:
        h (np.array): The orbital momentum vector
    Returns:
        float: The inclination (in Radians)
    """
    inclination = math.acos(h[2] / np.linalg.norm(h))
    return inclination


def rotate_position_around_x(inclination: float, position: np.array) -> np.array:
    """
    Rotates the position of the satellite around the x-axis.

    Args:
        inclination (float): The inclination (in Radians)
        position (np.array): The position of the satellite

    Returns:
        np.array: The rotated position of the satellite
    """
    rotation_matrix = np.array([
        [1, 0, 0],
        [0, math.cos(inclination), -math.sin(inclination)],
        [0, math.sin(inclination), math.cos(inclination)]
    ])
    return np.dot(rotation_matrix, position)


def inclination_from_momentum_and_z_axis(h: np.array) -> float:
    """
    Calculates the inclination given the orbital momentum vector and the z-axis.

    Args:
        h (np.array): The orbital momentum vector

    Returns:
        float: The inclination (in Radians)
    """
    z_axis = np.array([0, 0, 1])
    cos_inclination = np.dot(h, z_axis) / (np.linalg.norm(h) * np.linalg.norm(z_axis))
    return math.acos(cos_inclination)
