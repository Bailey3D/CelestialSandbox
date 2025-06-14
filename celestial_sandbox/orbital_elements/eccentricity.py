"""
Utility functions related to Eccentricity

Eccentricity:
    The shape of the ellipse, describing how muc it is elongate compared to a circle.
"""
import math


def validate_eccentricity(eccentricity: float):
    """
    Checks that an eccentricity is between 0.0 and 1.0
    Raises an attribute error if it is not

    Args:
        eccentricity (float): The eccentricity to validate
    """
    if eccentricity >= 1.0 or eccentricity < 0.0:
        raise AttributeError(f"Eccentricity must be between 0.0 and 1.0, got {eccentricity}.")


def eccentric_anomaly(eccentricity: float, true_anomaly: float) -> float:
    """
    Gets the Eccentric Anomaly.
    The angle between the center of the orbit, and the point that the body would be if it moved in a circle (rather than an ellipse)

    Args:
        eccentricity (float): The eccentricity of the orbit
        true_anomaly (float): The true anomaly of the orbit
    Returns:
        float: The eccentric anomaly (in Radians)
    """
    return 2.0 * math.atan2(
        math.sqrt((1 - eccentricity) / (1 + eccentricity)) * math.sin(true_anomaly / 2),
        math.cos(true_anomaly / 2)
    )


def eccentric_anomaly_from_mean_anomaly(eccentricity: float, mean_anomaly: float) -> float:
    """
    Gets the Eccentric Anomaly.
    The angle between the center of the orbit, and the point that the body would be if it moved in a circle (rather than an ellipse)

    Args:
        eccentricity (float): The eccentricity of the orbit
        mean_anomaly (float): The mean anomaly of the orbit (in Radians)

    Returns:
        float: The eccentric anomaly (in Radians)
    """
    # use Newton's method to solve Kepler's equation iteratively
    # start with an initial guess equal to M
    E = mean_anomaly
    tol = 1e-6  # tolerance for convergence

    max_iter = 100
    n = 0
    while n < max_iter:
        # calculate the function value and its derivative
        f = E - eccentricity * math.sin(E) - mean_anomaly
        df = 1 - eccentricity * math.cos(E)

        E = E - f / df  # updare E using Newton's method

        if abs(f) < tol:
            # convergence achieved
            break

        n += 1

    return E


def true_anomaly(eccentricity: float, eccentric_anomaly: float) -> float:
    """
    Calculates the true anomaly of a planet in an elliptical orbit from its eccentricity and eccentric anomaly.

    Args:
        eccentricity (float): Eccentricity of the orbit
        eccentric_anomaly (float): Eccentric anomaly of the orbit (in radians)

    Returns:
        float: True anomaly of the orbit (in radians)
    """
    return 2 * math.atan(math.sqrt((1 + eccentricity) / (1 - eccentricity)) * math.tan(eccentric_anomaly / 2))


def mean_anomaly(eccentricity: float, eccentric_anomaly: float) -> float:
    """
    The angle that a body moving in a circle with constant speed would have covered
    in the same time as the actual body in its elliptical orbit
    In simple terms, this is the angle that a fake body would have if it moved in a perfect circle,
    with the same time as the real body, at a steady speed.

    Args:
        eccentricity (float): The eccentricity of the orbit
        eccentric_anomaly (float): The eccentric anomaly of the orbit

    Returns:
        float: The mean anomaly (in Radians)
    """
    # Uses Keplers equation that involves the eccentric anomaly and the shape of the orbit
    return eccentric_anomaly - eccentricity * math.sin(eccentric_anomaly)


def eccentricity_from_periapsis_apoapsis(periapsis: float, apoapsis: float) -> float:
    """
    Calculates the eccentricity of an elliptical orbit given the periapsis and apoapsis distances.

    Args:
        periapsis (float): The periapsis distance of the orbit (closest point to the central body)
        apoapsis (float): The apoapsis distance of the orbit (farthest point from the central body)

    Returns:
        float: The eccentricity of the orbit
    """
    return (apoapsis - periapsis) / (apoapsis + periapsis)
