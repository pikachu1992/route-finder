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
