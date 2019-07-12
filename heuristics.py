import math

def _parse_arg_points(*args):
    try:
        if len(args) == 2:
            args = (*args[0], *args[1])
        xa, ya, xb, yb = args
    except TypeError as crap:
        raise ValueError() from crap
    return xa, ya, xb, yb

def pytaghorian(*args):
    xa, ya, xb, yb = _parse_arg_points(*args)
    return ((float(ya) - float(yb)) ** 2) + ((float(xa) - float(xb)) ** 2)

def haversine(*args):
    xa, ya, xb, yb = _parse_arg_points(*args)

    R = 6378137 # earth radius in meters
    # (source: https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html)

    phi1, phi2 = math.radians(xa), math.radians(xb)
    dphi       = math.radians(xb - xa)
    dlambda    = math.radians(yb - ya)

    a = math.sin(dphi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2)**2

    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))
