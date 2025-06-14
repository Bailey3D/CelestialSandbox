import math
import celestial_sandbox.orbital_elements.orbital_speed
import celestial_sandbox.orbital_elements.semi_major_axis


def rotate_to_geocentric(a, e, i, omega, w, nu):
    """
    Rotates the position and velocity vectors from the orbital plane to the geocentric equatorial frame.

    Args:
        a (int): Semi-major axis of the orbit (in kilometers)
        e (float): Eccentricity of the orbit
        i (float): Inclination of the orbit (in radians)
        omega (float): Longitude of ascending node of the orbit (in radians)
        w (float): Argument of periapsis of the orbit (in radians)
        nu (float): True anomaly of the orbit (in radians)
    Returns:
        tuple: A tuple containing the position vector (x, y, z) and the velocity vector (vx, vy, vz)    
    """
    # compute the distance from the center of mass
    r = celestial_sandbox.orbital_elements.semi_major_axis.distance_to_center(a, e, nu)

    # compute the position vector components in the orbital plane
    # x_orb = r * cos(nu)
    # y_orb = r * sin(nu)
    x_orb = r * math.cos(nu)
    y_orb = r * math.sin(nu)

    # compute the velocity vector components in the orbital plane
    # vx_orb = -sqrt(mu / (a * (1 - e**2))) * (sin(nu) + e * sin(w))
    # vy_orb = sqrt(mu / (a * (1 - e**2))) * (cos(nu) + e * cos(w))
    mu = 3.986e14 # gravitational parameter of Earth in m^3/s^2
    mu = mu / 1e9  # from meters to kilometers
    vx_orb = -math.sqrt(mu / (a * (1 - e**2))) * (math.sin(nu) + e * math.sin(w))
    vy_orb = math.sqrt(mu / (a * (1 - e**2))) * (math.cos(nu) + e * math.cos(w))

    # rotate the position and velocity vectors to the geocentric-equatorial frame
    # using a matrix multiplication with a rotation matrix that depends on i, omega and w
    x = (math.cos(omega) * math.cos(w) - math.sin(omega) * math.sin(w) * math.cos(i)) * x_orb + (-math.cos(omega) * math.sin(w) - math.sin(omega) * math.cos(w) * math.cos(i)) * y_orb
    y = (math.sin(omega) * math.cos(w) + math.cos(omega) * math.sin(w) * math.cos(i)) * x_orb + (-math.sin(omega) * math.sin(w) + math.cos(omega) * math.cos(w) * math.cos(i)) * y_orb
    z = (math.sin(w) * math.sin(i)) * x_orb + (math.cos(w) * math.sin(i)) * y_orb

    vx = (math.cos(omega) * math.cos(w) - math.sin(omega) * math.sin(w) * math.cos(i)) * vx_orb + (-math.cos(omega) * math.sin(w) - math.sin(omega) * math.cos(w) * math.cos(i)) * vy_orb
    vy = (math.sin(omega) * math.cos(w) + math.cos(omega) * math.sin(w) * math.cos(i)) * vx_orb + (-math.sin(omega) * math.sin(w) + math.cos(omega) * math.cos(w) * math.cos(i)) * vy_orb
    vz = (math.sin(w) * math.sin(i)) * vx_orb + (math.cos(w) * math.sin(i)) * vy_orb

    # return the position and velocity vectors as tuples
    return ((x, y, z), (vx, vy, vz))


def orbital_to_euler(a, e, i, omega, w, nu):
    """
    Converts from orbital elements to Euler angles for an elliptical orbit.

    Args:
        a (float): Semi-major axis of the orbit (in kilometers)
        e (float): Eccentricity of the orbit
        i (float): Inclination of the orbit (in radians)
        omega (float): Longitude of ascending node of the orbit (in radians)
        w (float): Argument of periapsis of the orbit (in radians)
        nu (float): True anomaly of the orbit (in radians)
    Returns:
        tuple: A tuple containing the inclination, longitude of ascending node, and argument of periapsis (in radians)
    """
    a = float(a)

    # rotate the position and velocity vectors to the geocentric-equatorial frame
    r, v = rotate_to_geocentric(a, e, i, omega, w, nu)

    # unpack the vector components
    x, y, z = r
    vx, vy, vz = v

    # compute the Euler angles from the position and velocity vectors using inverse trigonometric functions
    # inclination = arccos(z / r)
    # longitude_of_ascending_node = arctan2(y, x)
    # argument_of_periapsis = arctan2(vz, vx) - longitude_of_ascending_node 
    inclination = math.acos(z / r)
    longitude_of_ascending_node = math.atan2(y, x)
    argument_of_periapsis = math.atan2(vz, vx) - longitude_of_ascending_node

    # returns the Euler angles as a tuple
    return (inclination, longitude_of_ascending_node, argument_of_periapsis)
