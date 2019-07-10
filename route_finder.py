import heapq
import math
from heuristics import Heuristics

class Node:
    def __init__(self, x, y, name, parent=None):
        self.x = x
        self.y = y
        self.name = name

    def __eq__(self, other):
        return self.name == other.name if isinstance(other, Node) else False

    def __gt__(self, other):
        return self.name > other.name

    def __hash__(self):
        return self.name.__hash__() * 13

    def __repr__(self):
        return self.name

class RouteMap:

    def __init__(self):
        try:
            self.file_readlines = open('airac/AIRWAY.txt', 'r').readlines()
        except:
            self.file_readlines = []

    def parseline(self, line):
        node = line[:6]       
        neighbours = line[6:] 

        return [node, neighbours]

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

    def find_node_lines(self, node_name, file_lines):
        node_lines = []
        for line in file_lines:
            if line.startswith(';'):
                continue
            elif line.split("\t")[0] == node_name:
                node_lines.append(self.parseline(line.split('\t')))
        return node_lines

    def validate_neighbour(self, neighbour):
        if '' in neighbour:
            return None
        if 'N' in neighbour or 'N\n' in neighbour:
            return None
        return neighbour 

    def get_node_neighbours(self, node):
        """Returns: (tuple) cost, node
        """
        neighbour_nodes = []
        neighbour_0 = None
        neighbour_1 = None

        for line in self.find_node_lines(node, self.file_readlines):
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
print(RouteMap().get_node_neighbours("LIS"))
class HeapQueue:
    def __init__(self, items):
        self._heap = items
        heapq.heapify(self._heap)

    def push(self, item):
        heapq.heappush(self._heap, item)

    def pop(self):
        return heapq.heappop(self._heap)

    def pushpop(self, item):
        return heapq.heappushpop(self._heap, item)

    def __len__(self):
        return len(self._heap)

class RouteFinder(RouteMap, Heuristics):
    def __init__(self, start_node, end_node):
        super().__init__()
        self.start_node = start_node
        self.end_node = end_node
        self.closed_list = {}

    def find(self):
        open_list = HeapQueue([(0, 0, self.start_node, None)])
        self.closed_list = {}

        while len(open_list) > 0:
            node_f, node_g, node, parent = open_list.pop()
            self.closed_list[node] = (node_g, parent)

            if node == self.end_node:
                return

            for neighbour_g, neighbour in super().get_node_neighbours(node):
                if neighbour in self.closed_list:
                    continue

                h = super().astar_heuristic(neighbour.x, neighbour.y, self.end_node.x, self.end_node.y)
                g = neighbour_g + node_g
                f = g + h

                open_list.push((f, g, neighbour, node))
        raise RuntimeError('Unable to find route.')

    @property
    def nodes(self):
        return self._path_to(self.end_node)

    def _path_to(self, node):
        result = []
        while node:
            result.append(node)
            _, node = self.closed_list[node]
        result.reverse()
        return result
