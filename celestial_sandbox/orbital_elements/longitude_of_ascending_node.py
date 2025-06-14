"""
Utility functions related to Longitude of the Ascending Node

Longitude of the Ascending Node:
    Horizontally orients the ascending node of the ellipse
    (where the orbit passes from south to north through the reference plane, symbolized by ☊)
    with respect to the reference frame's vernal point (symbolized by ♈︎).
    This is measured in the reference plane, and is shown as the green angle Ω in the diagram.
"""
import math
import numpy as np


def longitude_of_ascending_node_from_momentum_vector(h: np.array) -> float:
    """
    Calculates the longitude of the ascending node from an orbital momentum vector.

    Args:
        h (np.array): The orbital momentum vector

    Returns:
        float: The longitude of the ascending node (in Radians)
    """
    longitude_of_ascending_node = math.atan2(h[0], -h[1])
    if longitude_of_ascending_node < 0:
        longitude_of_ascending_node += 2 * math.pi
    return longitude_of_ascending_node


def rotate_orbit_around_z(longitude_of_ascending_node: float, position: np.array) -> np.array:
    """
    Rotates the orbit around the z-axis.

    Args:
        longitude_of_ascending_node (float): The longitude of the ascending node (in Radians)
        position (np.array): The position of the satellite

    Returns:
        np.array: The rotated position of the satellite
    """
    rotation_matrix = np.array([
        [math.cos(longitude_of_ascending_node), -math.sin(longitude_of_ascending_node), 0],
        [math.sin(longitude_of_ascending_node), math.cos(longitude_of_ascending_node), 0],
        [0, 0, 1]
    ])
    return np.dot(rotation_matrix, position)


def longitude_of_ascending_node_from_momentum_and_x_axis(h: np.array) -> float:
    """
    Calculates the longitude of the ascending node given the orbital momentum vector and the x-axis.

    Args:
        h (np.array): The orbital momentum vector

    Returns:
        float: The longitude of the ascending node (in Radians)
    """
    x_axis = np.array([1, 0, 0])
    sin_longitude_of_ascending_node = np.dot(np.cross(x_axis, h), np.array([0, 0, 1])) / np.linalg.norm(h)
    cos_longitude_of_ascending_node = np.dot(x_axis, h) / np.linalg.norm(h)
    return math.atan2(sin_longitude_of_ascending_node, cos_longitude_of_ascending_node)
