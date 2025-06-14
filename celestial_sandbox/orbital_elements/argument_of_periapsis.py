"""
Utility functions related to Argument of Periapsis

Argument of Periapsis:
    Argument of periapsis (ω) defines the orientation of the ellipse in the orbital plane,
    as an angle measured from the ascending node to the periapsis
    (the closest point the satellite object comes to the primary object around which it orbits),
    the purple angle ω in the diagram.
"""
import math
import numpy as np


def argument_of_periapsis_from_eccentricity_vector(e: np.array):
    """
    Calculates the argument of periapsis from the eccentricity vector.

    Args:
        e (np.array): The eccentricity vector

    Returns:
        float: The argument of periapsis (in Radians)
    """
    argument_of_periapsis = math.atan2(e[1], e[0])
    if argument_of_periapsis < 0:
        argument_of_periapsis += 2 * math.pi
    return argument_of_periapsis


def rotate_position_in_orbital_plane(argument_of_periapsis: float, position: np.array) -> np.array:
    """
    Rotates the position of the satellite within the orbital plane.

    Args:
        argument_of_periapsis (float): The argument of periapsis (in Radians)
        position (np.array): The position of the satellite in the orbital plane

    Returns:
        np.array: The rotated position of the satellite
    """
    rotation_matrix = np.array([
        [math.cos(argument_of_periapsis), -math.sin(argument_of_periapsis)],
        [math.sin(argument_of_periapsis), math.cos(argument_of_periapsis)]
    ])
    return np.dot(rotation_matrix, position)


def argument_of_periapsis_from_longitude(longitude_of_periapsis: float, longitude_of_ascending_node: float) -> float:
    """
    Calculates the argument of periapsis given the longitude of periapsis and the longitude of the ascending node.

    Args:
        longitude_of_periapsis (float): The longitude of periapsis (in Radians)
        longitude_of_ascending_node (float): The longitude of the ascending node (in Radians)

    Returns:
        float: The argument of periapsis (in Radians)
    """
    return longitude_of_periapsis - longitude_of_ascending_node
