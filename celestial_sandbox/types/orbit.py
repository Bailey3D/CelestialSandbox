import math

import celestial_sandbox.orbit


class Orbit(object):
    def __init__(self, semi_major_axis, eccentricity, inclination, longitude_of_ascending_node, argument_of_periapsis, name=None, orbital_period=None):
        """
        Initializes the class with the given orbital elements.
        
        Args:
            semi_major_axis (float): The semi-major axis (in kilometers)
            eccentricity (float): The eccentricity
            inclination (float): The inclination (in radians)
            longitude_of_ascending_node (float): The longitude of the ascending node (in radians)
            argument_of_periapsis (float): The argument of periapsis (in radians)
        """
        self.semi_major_axis = semi_major_axis
        self.eccentricity = eccentricity
        self.inclination = inclination
        self.longitude_of_ascending_node = longitude_of_ascending_node
        self.argument_of_periapsis = argument_of_periapsis
        self.name = name

        self.orbital_period = orbital_period or 365

    def true_anomaly(self, t):
        """
        Calculates the true anomaly at a given time.
        Args:
            t (float): The time since periapsis (in days)
        Returns:
            float: The true anomaly (in radians)
        """
        '''n = 2 * math.pi / self.orbital_period
        M = n * t
        E = M
        while True:
            E_next = E - (E - self.eccentricity * math.sin(E) - M) / (1 - self.eccentricity * math.cos(E))
            if abs(E_next - E) < 1e-8:
                break
            E = E_next
        v = 2 * math.atan2(math.sqrt(1 + self.eccentricity) * math.sin(E / 2), math.sqrt(1 - self.eccentricity) * math.cos(E / 2))
        return v'''
        eccentric_anomaly = self.eccentric_anomaly(t)
        v = 2 * math.atan2(
            math.sqrt(1 + self.eccentricity) * math.sin(eccentric_anomaly / 2),
            math.sqrt(1 - self.eccentricity) * math.cos(eccentric_anomaly / 2)
        )
        return v

    def mean_anomaly(self, t):
        """
        Calculates the mean anomaly at a given time.
        Args:
            t (float): The time since periapsis (in days)
        Returns:
            float: The mean anomaly (in radians)
        """
        n = 2 * math.pi / self.orbital_period
        M = n * t
        return M

    def eccentric_anomaly(self, time, tol=1e-8):
        """
        Calculates the eccentric anomaly at a given time using an iterative solver method.
        Args:
            time (float): The current time (in seconds)
            tol (float): Tolerance
        Returns:
            float: Eccentric anomaly (in radians)
        """
        mean_anomaly = self.mean_anomaly(time)

        E = mean_anomaly
        num = 0
        while True:
            num += 1
            E_next = E - (E - self.eccentricity * math.sin(E) - mean_anomaly) / (1 - self.eccentricity * math.cos(E))
            if abs(E_next - E) < tol:
                break
            E = E_next
        return E

    def position_vector(self, time_value, semi_major_axis=None):
        """
        Gets the position of the orbit at a given time value
        Args:
            time_value (float): The time value to get the position at (in 24 hour days)
            semi_major_axis (float): Override value for the semi-major axis (in Kilometers)
        Returns:
            np.array: The xyz position at the given time
        """
        pos = celestial_sandbox.orbit.position_vector_from_orbital_elements(
            semi_major_axis or self.semi_major_axis,
            self.eccentricity,
            self.inclination,
            self.longitude_of_ascending_node,
            self.argument_of_periapsis,
            self.true_anomaly(time_value)
        )
        return pos
