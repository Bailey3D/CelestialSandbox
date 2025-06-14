class StarData(object):
    MIN_RADIUS = 0  # minimum radius (in solar radii)
    MAX_RADIUS = 1  # maximum radius (in solar radii)
    MIN_MASS = 0  # minimum mass (in solar masses)
    MAX_MASS = 1  # maximum mass (in solar masses)
    MIN_TEMP = 0  # minimum temperature (in kelvin)
    MAX_TEMP = 1  # maximum temperature (in kelvin)
    MIN_AGE = 0  # minimum age (in million-years)
    MAX_AGE = 1  # maximum age (in million years)


class TTauri(StarData):
    MIN_RADIUS = 0.4
    MAX_RADIUS = 2
    MIN_MASS = 0.08
    MAX_MASS = 2
    MIN_TEMP = 2800
    MAX_TEMP = 3900
    MIN_AGE = 1
    MAX_AGE = 10


class Herbig_Ae_Be(StarData):
    MIN_RADIUS = 1.5
    MAX_RADIUS = 6
    MIN_MASS = 2
    MAX_MASS = 20
    MIN_TEMP = 7000
    MAX_TEMP = 10000
    MIN_AGE = 1
    MAX_AGE = 10


class RedDwarf(StarData):
    MIN_RADIUS = 0.08
    MAX_RADIUS = 0.7
    MIN_MASS = 0.08
    MAX_MASS = 0.5
    MIN_TEMP = 2400
    MAX_TEMP = 3700
    MIN_AGE = 10
    MAX_AGE = 100


class RedSupergiant(StarData):
    MIN_RADIUS = 200
    MAX_RADIUS = 800
    MIN_MASS = 10
    MAX_MASS = 40
    MIN_TEMP = 3500
    MAX_TEMP = 4500
    MIN_AGE = 10
    MAX_AGE = 20


class OrangeDwarf(StarData):
    MIN_RADIUS = 0.7
    MAX_RADIUS = 1.4
    MIN_MASS = 0.7
    MAX_MASS = 1.5
    MIN_TEMP = 3700
    MAX_TEMP = 5000
    MIN_AGE = 1
    MAX_AGE = 10


class YellowDwarf(StarData):
    MIN_RADIUS = 0.7
    MAX_RADIUS = 1.4
    MIN_MASS = 0.7
    MAX_MASS = 1.5
    MIN_TEMP = 5000
    MAX_TEMP = 6000
    MIN_AGE = 1
    MAX_AGE = 10


class BlueDwarf(StarData):
    pass  # not observed


class OType(StarData):
    MIN_RADIUS = 15
    MAX_RADIUS = 90
    MIN_MASS = 15
    MAX_MASS = 90
    MIN_TEMP = 30000
    MAX_TEMP = 50000
    MIN_AGE = 1
    MAX_AGE = 10


class BType(StarData):
    MIN_RADIUS = 1.8
    MAX_RADIUS = 6.6
    MIN_MASS = 2
    MAX_MASS = 16
    MIN_TEMP = 10000
    MAX_TEMP = 30000
    MIN_AGE = 10
    MAX_AGE = 400


class AType(StarData):
    MIN_RADIUS = 1.4
    MAX_RADIUS = 1.8
    MIN_MASS = 1.4
    MAX_MASS = 2.1
    MIN_TEMP = 7500
    MAX_TEMP = 10000
    MIN_AGE = 400
    MAX_AGE = 2000


class FType(StarData):
    MIN_RADIUS = 1.15
    MAX_RADIUS = 1.4
    MIN_MASS = 1.04
    MAX_MASS = 1.4
    MIN_TEMP = 6000
    MAX_TEMP = 7500
    MIN_AGE = 2000
    MAX_AGE = 4000


class GType(StarData):
    MIN_RADIUS = 0.96
    MAX_RADIUS = 1.15
    MIN_MASS = 0.8
    MAX_MASS = 1.04
    MIN_TEMP = 5200
    MAX_TEMP = 6000
    MIN_AGE = 4000
    MAX_AGE = 10000


class KType(StarData):
    MIN_RADIUS = 0.7
    MAX_RADIUS = 0.96
    MIN_MASS = 0.45
    MAX_MASS = 0.8
    MIN_TEMP = 3700
    MAX_TEMP = 5200
    MIN_AGE = 10000
    MAX_AGE = 30000


class MType(StarData):
    MIN_RADIUS = 0.08
    MAX_RADIUS = 0.7
    MIN_MASS = 0.08
    MAX_MASS = 0.45
    MIN_TEMP = 2400
    MAX_TEMP = 3700
    MIN_AGE = 30000
    MAX_AGE = 1000000


class Subgiant(StarData):
    MIN_RADIUS = 1.5
    MAX_RADIUS = 5
    MIN_MASS = 0.8
    MAX_MASS = 8
    MIN_TEMP = 4800
    MAX_TEMP = 10000
    MIN_AGE = 1000
    MAX_AGE = 10000


class Subdwarf(StarData):
    pass


class RedGiant(StarData):
    MIN_RADIUS = 20
    MAX_RADIUS = 100
    MIN_MASS = 0.3
    MAX_MASS = 8
    MIN_TEMP = 3500
    MAX_TEMP = 5000
    MIN_AGE = 2000
    MAX_AGE = 10000


class RedClumpGiant(StarData):
    MIN_RADIUS = 10
    MAX_RADIUS = 60
    MIN_MASS = 0.4
    MAX_MASS = 2
    MIN_TEMP = 4000
    MAX_TEMP = 5200
    MIN_AGE = 2000
    MAX_AGE = 10000


'''class RRLyraeVariable(StarData):
    MIN_RADIUS = 1
    MAX_RADIUS = 5
    MIN_MASS = 0.8
    MAX_MASS = 8
    MIN_TEMP = 4800
    MAX_TEMP = 10000
    MIN_AGE = 1000
    MAX_AGE = 10000'''


'''class RedAGB(StarData):
    MIN_RADIUS = 10
    MAX_RADIUS = 100
    MIN_MASS = 0.6
    MAX_MASS = 10
    MIN_TEMP = 3000
    MAX_TEMP = 4000
    MIN_AGE = 1000
    MAX_AGE = 10000'''


'''class MiraVariable(StarData):
    MIN_RADIUS = 200
    MAX_RADIUS = 400
    MIN_MASS = 1
    MAX_MASS = 8
    MIN_TEMP = 2000
    MAX_TEMP = 3000
    MIN_AGE = 1000
    MAX_AGE = 10000'''


class CarbonStar(StarData):
    MIN_RADIUS = 100
    MAX_RADIUS = 200
    MIN_MASS = 4
    MAX_MASS = 9
    MIN_TEMP = 2600
    MAX_TEMP = 3500
    MIN_AGE = 1000
    MAX_AGE = 10000


class SType(StarData):
    MIN_RADIUS = 50
    MAX_RADIUS = 100
    MIN_MASS = 1
    MAX_MASS = 4
    MIN_TEMP = 3000
    MAX_TEMP = 4000
    MIN_AGE = 1000
    MAX_AGE = 10000


class WhiteDwarf(StarData):
    MIN_RADIUS = 0.01
    MAX_RADIUS = 0.01
    MIN_MASS = 0
    MAX_MASS = 0
    MIN_TEMP = 0
    MAX_TEMP = 0
    MIN_AGE = 0
    MAX_AGE = 0


class BlackHole(StarData):
    pass


class Pulsar(StarData):
    pass


class NeutronStar(StarData):
    pass


class Hyperhiant(StarData):
    pass


class BlueSupergiant(StarData):
    pass


class BrownDwarf(StarData):
    pass


class BlackDwarf(StarData):
    pass


class BlueStraggler(StarData):
    pass