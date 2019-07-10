""" This module implements the RouteMap interface to be injected to RouteFinder.

It provides airway information data from FS Navigator AIRAC files.

FS Navigator files:

    `AIRWAY.txt`

        It is a TAB delimited file. The compilation of the elements are the followings:
        1 - the name of the point
        2 - latitude of the point
        3 - longitude of the point
        4 - ignored
        5 - the name of the airway
        6 - the type of the airway
        7 - the previous point along the airway
        8 - latitude of the previous point
        9 - longitude of the previous point
        10 - minimum altitude from the previous point
        11 - airway can be used from this point to the previous
        12 - the next point along the airway
        13 - latitude of the next point
        14 - longitude of the next point
        15 - minimum altitude to the next point
        16 - airway can be used from this point to the previous
        12-16 is the same as 7-11 but for the next point
        (source: https://forums.vatsim.net/viewtopic.php?p=372310)

"""
from collections import defaultdict

class FsNavigatorMap():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        file_lines = self._read_file()
        self.nodes, self.neighbours = self._parse_lines(file_lines)

    def _read_file(self):
        lines = []
        with open('fsnavigator/Bin/AIRWAY.txt', 'r') as f:
            lines = f.readlines()
        return lines

    def _parse_lines(self, lines):
        lines = [line.strip().split('\t') for line in lines if not line.strip().startswith(';')]
        nodes = dict()
        neighbours = defaultdict(list)
        for line in lines:
            node = line[:6]
            node_neighbours = line[6:]
            node = self._parse_airway_node(node)
            node_neighbours = self._parse_airway_neighbours(node_neighbours)
            neighbours[node] = [*neighbours[node], *node_neighbours]
            nodes[node.name] = node
        return nodes, neighbours

    def _parse_airway_node(self, node):
        return Node(40.881944, -8.115, 'PESUL')

    def _parse_airway_neighbours(self, neighbours):
        return []

class RouteMap():
    def __init__(self, *args, map, **kwargs):
        super().__init__(*args, **kwargs)

        self._map = map
        self._neighbours = neighbours

    def get_node_neighbours(self, node):
        return self._map.neighbours[node]

    def get_node(self, name):
        return self._map.nodes[name]

class Node:
    def __init__(self, x, y, name):
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
