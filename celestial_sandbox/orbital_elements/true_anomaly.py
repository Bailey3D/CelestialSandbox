"""
Utility functions related to True Anomaly

True Anomaly:
    (ν, θ, or f) at epoch (t0) defines the position of the orbiting body along the ellipse at
    a specific time (the "epoch").
"""
import math


def true_anomaly_from_mean_anomaly(eccentricity: float, mean_anomaly: float) -> float:
    """
    Calculates the true anomaly from the mean anomaly and eccentricity.

    Args:
        eccentricity (float): The eccentricity of the orbit.
        mean_anomaly (float): The mean anomaly of the orbit (in radians).

    Returns:
        float: The true anomaly of the orbit (in radians).
    """
    # Uses an iterative method to solve Kepler's equation for eccentric anomaly
    # Start with initial guess equal to mean anomaly
    eccentric_anomaly = mean_anomaly
    for _ in range(10):  # usually converges in 5-6 iterations, 10 should be more than sufficient
        eccentric_anomaly = mean_anomaly + eccentricity * math.sin(eccentric_anomaly)

    # Convert eccentric anomaly to true anomaly
    true_anomaly = 2 * math.atan2(
        math.sqrt(1+eccentricity) * math.sin(eccentric_anomaly / 2),
        math.sqrt(1-eccentricity) * math.cos(eccentric_anomaly / 2)
    )

    return true_anomaly


def mean_anomaly_from_true_anomaly(eccentricity: float, true_anomaly: float) -> float:
    """
    Calculates the mean anomaly from the true anomaly and eccentricity.

    Args:
        eccentricity (float): The eccentricity of the orbit.
        true_anomaly (float): The true anomaly of the orbit (in radians).

    Returns:
        float: The mean anomaly of the orbit (in radians).
    """
    # Convert true anomaly to eccentric anomaly
    eccentric_anomaly = 2 * math.atan2(
        math.sqrt(1-eccentricity) * math.sin(true_anomaly / 2),
        math.sqrt(1+eccentricity) * math.cos(true_anomaly / 2)
    )

    # Calculate mean anomaly from eccentric anomaly
    mean_anomaly = eccentric_anomaly - eccentricity * math.sin(eccentric_anomaly)

    return mean_anomaly
