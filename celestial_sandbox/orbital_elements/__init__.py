import math


def orbital_period(semi_major_axis: int, gravitational_parameter: float) -> float:
    """
    Calculates the orbital period of a planet from its semi-major axis and gravitational parameter.

    Args:
        semi_major_axis (int): Semi-major axis of the orbit (in Kilometers)
        gravitational_parameter (float): Gravitational parameter of the planet (in km^3/s^2)
    Returns:
        float: Orbital period of the planet (in Seconds)
    """
    return 2 * math.pi * math.sqrt(semi_major_axis ** 3 / gravitational_parameter)


def orbital_speed(r: float, a: float, mu: float) -> float:
    """
    Calculates the orbital speed of a planet in an elliptical orbit at a given distance from the Sun.
    Using the vis-viva equation: https://www.omnicalculator.com/physics/orbital-velocity

    Args:
        r (float): Distance of the planet from the Sun (in kilometers)
        a (float): Semi-major axis of the orbit (in kilometers)
        mu (float): Gravitational parameter of the planet (in km^3/s^2)
    Returns:
        float: Orbital speed of the planet (in km/s)
    """
    return math.sqrt(mu * (2 / r - 1 / a))
