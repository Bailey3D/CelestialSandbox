import celestial_sandbox.types.celestial_body


class Planet(celestial_sandbox.types.celestial_body.CelestialBody):
    def __init__(self, radius, atmospheric_pressure):
        """
        Args:
            atmospheric_pressure (float): The pressure of the atmosphere at sea level - measured in Pascals
        """
        super().__init__(radius, ...)

        # Atmospheric pressure on various planets:
        # Mars: 610 Pascals
        # Earth: 101,235 Pascals
        self.atmospheric_pressure = atmospheric_pressure
