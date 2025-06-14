import math
import numpy as np


def get_rotation_matrix(i, Omega, omega):
    """
    Calculates the rotation matrix given the input orbital elements.

    Args:
        i (float): The inclination (in radians)
        Omega (float): The longitude of the ascending node (in radians)
        omega (float): The argument of periapsis (in radians)
    Returns:
        np.array: The rotation matrix
    """
    return get_rotation_matrix_z(-Omega) @ get_rotation_matrix_x(-i) @ get_rotation_matrix_z(-omega)


def get_rotation_matrix_x(theta):
    """
    Calculates the rotation matrix about the x-axis given an angle theta.

    Args:
        theta (float): The angle of rotation (in radians)

    Returns:
        np.array: The rotation matrix about the x-axis
    """
    return np.array([[1, 0, 0], [0, math.cos(theta), -math.sin(theta)], [0, math.sin(theta), math.cos(theta)]])


def get_rotation_matrix_y(theta):
    """
    Calculates the rotation matrix about the y-axis given an angle theta.

    Args:
        theta (float): The angle of rotation (in radians)

    Returns:
        np.array: The rotation matrix about the y-axis
    """
    return np.array([[math.cos(theta), 0, math.sin(theta)], [0, 1, 0], [-math.sin(theta), 0, math.cos(theta)]])


def get_rotation_matrix_z(theta):
    """
    Calculates the rotation matrix about the z- axis given the angle of theta
    Args:
        theta (float): The angle of rotation (in radians)
    Returns:
        np.array: The rotation matrix about the z-axis
    """
    return np.array([[math.cos(theta), -math.sin(theta), 0], [math.sin(theta), math.cos(theta), 0], [0, 0, 1]])


# -----------------------------------------------------------------------


def position_vector_from_orbital_elements(
        semi_major_axis, eccentricity, inclination, longitude_of_ascending_node, argument_of_periapsis, true_anomaly):
    """
    Calculates the position vector of a celestial body in world space given all of the input orbital elements.
    Args:
        semi_major_axis (float): The semi-major axis (in kilometers)
        eccentricity (float): The eccentricity
        inclination (float): The inclination (in radians)
        longitude_of_ascending_node (float): The longitude of the ascending node (in radians)
        argument_of_periapsis (float): The argument of periapsis (in radians)
        true_anomaly (float): The true anomaly (in radians)
    Returns:
        np.array: The position vector (in kilometers)
    """
    # Calculate the position relative to the orbital plane
    p = semi_major_axis * (1 - eccentricity ** 2)  # semi-latus rectum
    r = p / (1.0 + eccentricity * np.cos(true_anomaly))
    x = r * np.cos(true_anomaly)
    y = r * np.sin(true_anomaly)
    z = 0.0
    r = np.array([x, y, z])

    # rotate by argument of periapsis
    x = r[0] * np.cos(argument_of_periapsis) - r[1] * np.sin(argument_of_periapsis)
    y = r[0] * np.sin(argument_of_periapsis) + r[1] * np.cos(argument_of_periapsis)
    z = r[2]

    # rotate by inclination
    x1 = x
    y1 = y * np.cos(inclination) - z * np.sin(inclination)
    z1 = y * np.sin(inclination) + z * np.cos(inclination)

    # rotate by longitude of ascending node
    x2 = x1 * np.cos(longitude_of_ascending_node) - y1 * np.sin(longitude_of_ascending_node)
    y2 = x1 * np.sin(longitude_of_ascending_node) + y1 * np.cos(longitude_of_ascending_node)
    z2 = z1

    return np.array([x2, y2, z2])


'''def position_vector_from_orbital_elements(a, e, i, omega, w, nu):
    """
    Convert orbital elements to an x/y/z position vector using a rotation matrix.

    Parameters
    ----------
    a : float
        Semi-major axis
    e : float
        Eccentricity
    i : float
        Inclination (radians)
    omega : float
        Longitude of ascending node (radians)
    w : float
        Argument of periapsis (radians)
    nu : float
        True anomaly (radians)

    Returns
    -------
    r : ndarray
        Position vector [x, y, z]
    """
    # Calculate position in orbital plane
    p = a * (1 - e**2)
    r = p / (1 + e * np.cos(nu))
    x = r * np.cos(nu)
    y = r * np.sin(nu)
    z = 0

    # Rotate by argument of periapsis, inclination, and longitude of ascending node
    R = np.array([[-np.sin(omega) * np.cos(i) * np.sin(w) + np.cos(omega) * np.cos(w), -np.sin(omega) * np.cos(i) * np.cos(w) - np.cos(omega) * np.sin(w), np.sin(omega) * np.sin(i)],
                  [np.cos(omega) * np.cos(i) * np.sin(w) + np.sin(omega) * np.cos(w), np.cos(omega) * np.cos(i) * np.cos(w) - np.sin(omega) * np.sin(w), -np.cos(omega) * np.sin(i)],
                  [np.sin(i) * np.sin(w), np.sin(i) * np.cos(w), np.cos(i)]])
    xp, yp, zp = R @ [x, y, z]

    return np.array([xp, yp, zp])'''
