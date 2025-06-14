import enum

import celestial_sandbox.types.celestial_body
from . import type_mapping_table


class Star(celestial_sandbox.types.celestial_body.CelestialBody):
    def __init__(
            self,
            temperature=5772,
            luminosity=1,
            radius=696_340,
            rotation_period=(27.0 * 24.0),  # roughly 27 days for our sun (varies depending on longitude)
            surface_gravity=274.0,
            solar_masses=1
    ):
        """
        Note: All default values default to that of our Sun
        args:
            - temperature (int):
                The temperature of the star (in Kelvin)
            - radius (float):
                The radius of the body (in kilometers)
        kwargs:
            - luminosity (int):
                The luminosity of the star (in Solar Luminosities)
            - rotation_period (float):
                The time it takes the star to rotate 360 degrees (in hours)
            - surface_gravity (float):
                The surface gravity of the star (measured in m/s^2)
                This is the speed at which an object at the surface will accelerate downward each second.
            - solar_masses (float)
                The mass of the star in solar masses
                I.e, Sun = 1 solar mass
        """

        """
        Note: All default values default to that of our Sun
        :arg [<int:temperature>] The temperature of the star (in Kelvin)
        :kwarg [<int:luminosity>] The luminosity of the star (in Solar Luminosities)
        :kwarg [<float:radius>] The radius of the body (in kilometers)
        :kwarg [<float:rotation_period>] The time it takes the star to rotate 360 degrees (in hours)
        :kwarg [<float:surface_gravity>]
            The surface gravity of the star (measured in m/s^2)
            This is the speed at which an object at the surface will accelerate downward each second.
        :kwarg [<float:solar_masses>]
            The mass of the star in solar masses
            I.e, Sun = 1 solar mass
        """
        super().__init__(
            radius=radius,
            rotation_period=rotation_period,
            surface_gravity=surface_gravity,
            mass=(solar_masses * 1.98847e30)
        )

        # The temperature of the star (in Kelvin)
        # I.e,  Sun: 5772 Kelvin
        #       Sirius B: 25200 Kelvin
        self.temperature = temperature

        # The type of star
        # I.e,  `TTauri`
        self.type = type_mapping_table.YellowDwarf

        # The luminosity of the star (in Watts)
        self.luminosity = luminosity




        #
        self.MASS_CATEGORY = None
        self.STAGE = None

        # Other Notes:
        # Photosphere: The lowest layer oft he solar atmosphere (the solar surface - seen when we look at the sun in white light)
        # Chromosphere: Thin layer of plasma that lies between a star's visible surface (photosphere), and the corona (uper atmosphere)
        # Corona: The outer layer of a star's atmosphere. Consists of plasma.


class EMassCategory(enum.Enum):
    LOW_MASS = 0
    MEDIUM_MASS = 1
    HIGH_MASS = 2
    VERY_HIGH_MASS = 3


class EStarLifecycleStage(enum.Enum):
    FAILED_STAR = -1
    MOLECULAR_CLOUD = 0
    PROTOSTAR = 1
    PRE_MAIN_SEQUENCE = 2
    MAIN_SEQUENCE = 3
    POST_MAIN_SEQUENCE = 4
    SUBGIANT = 5
    SUPERGIANT = 6
    RED_GIANT_BRANCH = 7
    HORIZONTAL_BRANCH = 8
    ASYMPTOTIC_GIANT_BRANCH = 9
    FINAL_STAGE = 10
