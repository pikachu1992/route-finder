from route_finder import Node
from collections import defaultdict
import math


class FindNeighbours(): #devolver o node e os 2 vizinhos
    def parseline(self, line):
        node = line.split("\t")[:6]
        neighbours = line.split("\t")[6:] 
        
        return [node, neighbours]
    
    def parse_neighbours(self, neighbours):
        neighbours_list = []

        if neighbours[4] == "Y":
            neighbours_list.append(neighbours[:5])

        if neighbours[9] == "Y":
            neighbours_list.append(neighbours[5:])

        
        return neighbours_list

    def calculate_cost(self, *args):
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