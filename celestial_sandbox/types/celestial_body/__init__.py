"""
https://en.wikipedia.org/wiki/Rayleigh_scattering
Kelvin to RGB: https://tannerhelland.com/2012/09/18/convert-temperature-rgb-algorithm-code.html
Rayleigh Scattering: https://www.alanzucconi.com/2017/10/10/atmospheric-scattering-3/#:~:text=Most%20optical%20effects%20that%20planets%20exhibit%20can%20be,how%20light%20scatters%20on%20objects%20of%20different%20size.
    - Optical phenomenon that causes the sky to look a certain colour (Blue no Earth)
"""


class CelestialBody(object):
    def __init__(
            self,
            radius=6378,
            rotation_period=24,
            surface_gravity=9.8,
            mass=5972000000000000327155712
    ):
        """
        Note: All default values default to that of Earth

        Args:
            radius (float): The radius of the celestial body (in kilometers)
            rotation_period (float): The time it takes the body to rotate 360 degrees (in hours)
            surface_gravity (float): The surface gravity of the celestial body - measured in m/s^2
            mass (int): The mass of the celestial body (in KG)
        """
        # Radius notes:
        # Sun: 696340 km
        # Earth: 6378.1 km
        # The Moon: 1737.4 km
        # Juipter: 69911 km
        self.radius = radius

        # Rotation period notes:
        # Earth: 23.56 Hours
        # Venus: 5832.0 Hours
        # Mars: 24.6 Hours
        # The Sun: 587.28 Hours
        self.rotation_period = rotation_period

        # Surface gravity of various planets:
        # Mars: 3.71 m/s^2
        # Sun: 274 m/s^2
        # Earth: 9.807 m/s^2
        self.surface_gravity = surface_gravity

    @property
    def mass(self):
        return self.mass

    @property
    def solar_masses(self):
        return self.mass / 1.98847e30

    @property
    def earth_masses(self):
        return self.mass / 5.97e24
