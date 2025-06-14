"""
Common constant values
"""
# The gravitational constant (in `m^3/(kg*s^2)`)
# Used to calculate the force of gravity between two objects
GRAVITATIONAL_CONSTANT = 6.6743e-11

# One astronomical unit (in Kilometers)
# An astronomical unit is the average distance between the Earth and the Sun.
# (approximately 149.6 million Kilometers)
AU = 149_597_870  # one astronomical unit

# The speed of light (in km/s)
# fundimental constant in many physics equations
SPEED_OF_LIGHT = 299792.458

# The number of seconds in a 24 hour day
DAY_TO_SECONDS = 86400

# The number of seconds in 1 earth year (julian calendar)
YEAR_TO_SECONDS = 31557600

# Parsec to kilometers conversion factor
PARSEC_TO_KM = 3.086e+13

# Boltzmann constant (in J/K)
# Used to relate the average relative kinetic energy of particles in a gas with the temperature of the gas
BOLTZMANN_CONSTANT = 1.380649e-23

# Planck constant (in J*s)
# Used to relate the energy of a photon with its frequency
PLANCK_CONSTANT = 6.62607015e-34

# Stefan-Boltzmann constant in W/(m^2*K^4)
# Used to calculate the total radiated intensity of a black body
STEFAN_BOLTZMANN_CONSTANT = 5.670374419e-8


def parsec_to_km(parsec):
    """
    Converts a distance from parsecs to kilometers.

    Args:
        parsec (float): The distance in parsecs
    Returns:
        float: The equivalent distance in kilometers
    """
    return parsec * PARSEC_TO_KM


def km_to_parsec(km):
    """
    Converts a distance from kilometers to parsecs.

    Args:
        km (float): The distance in kilometers
    Returns:
        float: The equivalent distance in parsecs
    """
    return km / PARSEC_TO_KM
