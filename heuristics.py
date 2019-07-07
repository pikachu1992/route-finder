import math

def compute_heuristic(*args):
    try:
        if len(args) == 2:
            args = (*args[0], *args[1])
        xa, ya, xb, yb = args
    except TypeError as crap:
        raise ValueError() from crap

    return ((float(xa) - float(xb)) ** 2) + ((float(ya) - float(yb)) ** 2)

class Heuristics:
    def astar_heuristic(self, *args):
        return compute_heuristic(*args)

    def haversine(self, *args):
        try:
            if len(args) == 2:
                args = (*args[0], *args[1])
            xa, ya, xb, yb = args
        except TypeError as crap:
            raise ValueError() from crap

        R = 6378137 # earth radius in meters
        # (source: https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html)

        phi1, phi2 = math.radians(xa), math.radians(xb)
        dphi       = math.radians(xb - xa)
        dlambda    = math.radians(yb - ya)

        a = math.sin(dphi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2)**2

        return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))
