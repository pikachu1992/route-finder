from collections import defaultdict
import math


class FindNeighbours(): #devolver o node e os 2 vizinhos
    
    def parseline(self, line):
        node = line[:6]       
        neighbours = line[6:] 

        return [node, neighbours]
    
    def parse_neighbours(self, neighbours):

        neighbours_list = []
        
        if isinstance(neighbours[0], str):
            if neighbours[4] == "Y":
                neighbours_list.append(neighbours[:5])

            if neighbours[9] == "Y":
                neighbours_list.append(neighbours[5:])
        elif isinstance(neighbours[0], list):
            for neighbour in neighbours:
                if neighbour[4] == "Y":
                    neighbours_list.append(neighbour[:5])

                if neighbour[9] == "Y":
                    neighbours_list.append(neighbour[5:])

        
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
    
    def find_node_lines(self, node_name):
        node_lines = []
        with open('airac/AIRWAY.txt', 'r') as file:
            lines = file.readlines()
        for line in lines:
            if line.startswith(';'):
                continue
            elif line.split("\t")[0] == node_name:
                node_lines.append(self.parseline(line.split('\t')))
        return node_lines

    def validate_neighbour(self, neighbour):
        if '' in neighbour:
            return None
        return neighbour 

    def get_neighbours_nodes(self, node_lines):

        neighbour_nodes = []
        neighbour_0 = None
        neighbour_1 = None

        for line in node_lines:
            node = line[0]
            neighbours = line[1]

            self.validate_neighbour(neighbours[:5])
            neighbour_0 = self.validate_neighbour(neighbours[:5])
            neighbour_1 = self.validate_neighbour(neighbours[5:])

            if neighbour_0 is not None:
                neighbour_nodes.append((self.calculate_cost(float(node[1]), float(node[2]), float(neighbour_0[1]), float(neighbour_0[2])), neighbour_0))
            if neighbour_1 is not None:
                neighbour_nodes.append((self.calculate_cost(float(node[1]), float(node[2]), float(neighbour_1[1]), float(neighbour_1[2])), neighbour_1))
        return neighbour_nodes
