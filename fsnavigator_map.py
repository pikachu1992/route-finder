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

from route_finder import RouteMap

def _read_airway_file(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    return [line.strip().split('\t') for line in lines if not line.strip().startswith(';')]

def _parse_airway_node(node):
    pass

def _parse_airway_neighbours(neighbours):
    pass

NEIGHBOURS = defaultdict(list)
# _AIRWAY_LINES = _read_airway_file('fsnavigator/Bin/AIRWAY.txt')
# for line in _AIRWAY_LINES:
#     node = line[:6]
#     neighbours = line[6:]
#     node = _parse_airway_node(node)
#     neighbours = _parse_airway_neighbours(neighbours)
#     NEIGHBOURS[node].append(*neighbours)

class FsNavigatorMap(RouteMap):
    def get_node_neighbours(self, node):
        return NEIGHBOURS[node]
