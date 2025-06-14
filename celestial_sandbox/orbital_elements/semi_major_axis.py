"""
Utility functions related to semi-major axis

Semi-major Axis:
    The sum of the periapsis and apoapsis distances divided by two.
    For classic two-body orbits, the semimajor axis is the distance between the centers
    of the bodies, not the distance of the bodies from the center of mass.

Periapsis:
    The point closest to the orbiting body

Apoapsis:
    The point farthest from the orbiting body

Line of apsides:
    The line connecting the periapsis and apoapsis
"""
import math

import celestial_sandbox.constants
import celestial_sandbox.orbital_elements.eccentricity


def semi_major_axis_from_period_and_gravitational_parameter(period: float, gravitational_parameter: float) -> int:
    """
    Calculates the semi-major axis of an orbit from the gravitational period

    Args:
        period (float): The period of the orbit (in seconds).
        gravitational_parameter (float): The gravitational parameter of the attracting body (in km^3/s^2).
    Returns:
        int: The semi-major axis of the orbit (in Kilometers).
    """
    return int(
        ((period ** 2) * gravitational_parameter / (4 * math.pi ** 2)) ** (1 / 3)
    )


def semi_major_axis_from_mean_motion_and_gravitational_parameter(mean_motion: float, gravitational_parameter: float) -> int:
    """
    Calculates the semi-major axis from the mean motion and gravitational parameter of an orbit

    Args:
        mean_motion (float): The mean motion of the orbit (in radians per second).
        gravitational_parameter (float): The gravitational parameter of the attracting body (in km^3/s^2).

    Returns:
        int: The semi-major axis of the orbit (in kilometers).
    """
    return int(
        (gravitational_parameter / (mean_motion ** 2)) ** (1 / 3)
    )


def semi_major_axis_from_apoapsis_and_periapsis(apoapsis: float, periapsis: float) -> float:
    """
    Calculates the semi-major axis from the apoapsis and periapsis.
    Semi-major axis is just the average of the Apoapsis and Periapsis
    Args:
        apoapsis (float): The apoapsis distance from the center of attraction (in kilometers).
        periapsis (float): The periapsis distance from the center of attraction (in kilometers).

    Returns:
        float: The semi-major axis of the orbit (in kilometers).
    """
    return int((apoapsis + periapsis) / 2)


def semi_major_axis_from_eccentricity_and_mean_motion(eccentricity: float, mean_motion: float, gravitational_parameter: float) -> float:
    """
    Calculates the semi-major axis from the eccentricity, mean motion, and gravitational parameter
    Args:
        eccentricity (float): The eccentricity of the orbit.
        mean_motion (float): The mean motion of the orbit (in radians per second).
        gravitational_parameter (float): The gravitational parameter of the attracting body (in km^3/s^2).

    Returns:
        float: The semi-major axis of the orbit in kilometers.
    """
    celestial_sandbox.orbital_elements.eccentricity.validate_eccentricity(eccentricity)

    return (gravitational_parameter / (mean_motion ** 2 * (1 - eccentricity ** 2))) ** (1 / 3)


# ------------------------------------------------------------------------


def get_minor_axis(semi_major_axis: float, eccentricity: float) -> float:
    """
    Gets the minor axis from the semi-major axis and eccentricity
    Args:
        semi_major_axis (float): The semi-major axis (in Kilometers)
        eccentricity (float): The eccentricity of the orbit
    Returns:
        float: The minor axis (in Kilometers)
    """
    celestial_sandbox.orbital_elements.eccentricity.validate_eccentricity(eccentricity)

    return 2 * semi_major_axis * math.sqrt(1 - eccentricity ** 2)


def get_semi_major_axis_from_major_and_minor(minor_axis: float, major_axis: float) -> float:
    """
    Gets the semi-major axis from the major and minor axes
    Args:
        minor_axis (float): The minor axis (in Kilometers)
        major_axis (float): The major axis (in Kilometers)
    Returns:
        float: The semi-major axis (in Kilometers)
    """
    return int((major_axis + minor_axis) / 2.0)


# ------------------------------------------------------------------------


def apoapsis_from_semi_major_axis(semi_major_axis: float, eccentricity: float) -> float:
    """
    Gets the apoapsis from the semi-major axis and eccentricity
    Apoapsis is the farthest point in an orbit reached from the attracting body
    Args:
        semi_major_axis (float): The semi-major axis (in Kilometers)
        eccentricity (float): The eccentricity of the orbit
    Returns:
        float: The apoapsis (in Kilometers)
    """
    celestial_sandbox.orbital_elements.eccentricity.validate_eccentricity(eccentricity)

    return semi_major_axis * (1 + eccentricity)


def semi_major_axis_from_apoapsis(eccentricity: float, apoapsis: float) -> float:
    """
    Calculates the semi-major axis of an elliptical orbit given the eccentricity and either the periapsis or apoapsis distance.

    Args:
        eccentricity (float): The eccentricity of the orbit
        apoapsis (float): The apoapsis distance of the orbit (in Kilometers)

    Returns:
        float: The semi-major axis of the orbit
    """
    celestial_sandbox.orbital_elements.eccentricity.validate_eccentricity(eccentricity)
    return apoapsis / (1 + eccentricity)


# ------------------------------------------------------------------------


def periapsis_from_semi_major_axis(semi_major_axis: float, eccentricity: float) -> float:
    """
    Gets the periapsis from the semi-major axis and eccentricity
    Periapsis is the closest point in an orbit to the attracting body
    Args:
        semi_major_axis (float): The semi-major axis (in Kilometers)
        eccentricity (float): The eccentricity of the orbit
    Returns:
        float: The periapsis (in Kilometers)
    """
    celestial_sandbox.orbital_elements.eccentricity.validate_eccentricity(eccentricity)

    return semi_major_axis * (1 - eccentricity)


def semi_major_axis_from_periapsis(eccentricity: float, periapsis: float) -> float:
    """
    Calculates the semi-major axis of an elliptical orbit given the eccentricity and either the periapsis or apoapsis distance.

    Args:
        eccentricity (float): The eccentricity of the orbit
        periapsis (float): The periapsis distance of the orbit (in Kilometers)

    Returns:
        float: The semi-major axis of the orbit
    """
    celestial_sandbox.orbital_elements.eccentricity.validate_eccentricity(eccentricity)

    return periapsis / (1 - eccentricity)

# ------------------------------------------------------------------------


def minor_axis_from_semi_major_axis(semi_major_axis: float, eccentricity: float) -> float:
    """
    Gets the minor axis from the semi-major axis and eccentricity
    Minor axis is the diamiter of the ellipse at its narrowest
    Args:
        semi_major_axis (float): The semi-major axis (in Kilometers)
        eccentricity (float): The eccentricity of the orbit
    Returns:
        float: The minor axis (in Kilometers)
    """
    celestial_sandbox.orbital_elements.eccentricity.validate_eccentricity(eccentricity)

    return semi_major_axis * math.sqrt(1 - eccentricity**2)


# ------------------------------------------------------------------------


def major_axis_from_semi_major_axis(semi_major_axis: float) -> float:
    """
    Gets the major axis from the semi-major axis
    Major axis is the diamiter of the ellipse at its widest
    Args:
        semi_major_axis (float): The semi-major axis (in Kilometers)

    Returns:
        float: The major axis (in Kilometers)
    """
    return 2 * semi_major_axis


# ------------------------------------------------------------------------


def distance_to_center(semi_major_axis: float, eccentricity: float, true_anomaly: float) -> float:
    """
    Calculates the distance from the center of mass for an elliptical orbit
    Args:
        semi_major_axis (float): The semi-major axis of the orbit (in kilometers)
        eccentricity (float): The eccentricity of the orbit
        true_anomaly (float): The true anomaly of the orbit (in Radians)

    Returns:
        float: distance from the center of mass (in kilometers)
    """
    celestial_sandbox.orbital_elements.eccentricity.validate_eccentricity(eccentricity)

    # foormula for the distance from the center of mass
    return semi_major_axis * (1 - eccentricity ** 2) / (1 + eccentricity * math.cos(true_anomaly))


# ------------------------------------------------------------------------


def period_from_semi_major_axis(semi_major_axis: float, orbital_body_mass: float) -> float:
    """
    Calculates the period of an orbit from the semi-major axis
    An orbiting object's period squared is directly proportional to its semi-major axis cubed
    Args:
        semi_major_axis (float): The semi major axis (in Kilometers)
        orbital_body_mass (float): The mass of the orbital body (in Kilograms)
    Returns:
        float: The period of time it takes for the orbit to rotate the orbital body (in seconds)
    """
    a = semi_major_axis / 1000  # semi-major axis in meters
    T = math.sqrt((4 * math.pi**2) / (celestial_sandbox.constants.GRAVITATIONAL_CONSTANT * orbital_body_mass) * a**3)
    return T


def semi_major_axis_from_period(period: float, orbital_body_mass: float) -> float:
    """
    Calculates the semi-major axis of an orbit from the period
    An orbiting object's period squared is directly proportional to its semi-major axis cubed
    Args:
        period (float): The period of time it takes for the orbit to rotate the orbital body (in seconds)
        orbital_body_mass (float): The mass of the orbital body (in Kilograms)
    Returns:
        float: The semi major axis (in Kilometers)
    """
    semi_major_axis_meters = (
        (celestial_sandbox.constants.GRAVITATIONAL_CONSTANT * orbital_body_mass * period ** 2) / (4 * (math.pi ** 2))
    ) ** (1 / 3)
    return semi_major_axis_meters * 1000
