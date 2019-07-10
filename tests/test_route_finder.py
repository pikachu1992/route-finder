from unittest import TestCase
from math import sqrt
from collections import defaultdict

from route_finder import RouteFinder, RouteMap, Node

def generate_nodes():
    collumns = ['A', 'B', 'C', 'D', 'E']
    nodes = dict()
    for x in range(5):
        for y in range(5):
            collumn = collumns[x]
            name = f'{collumn}{y + 1}'
            nodes[name] = Node(x, y, name)
    return nodes

NODES = generate_nodes()

class TestMap(RouteMap):
    """A base test map composed of a 5 by 5 grid, where A1 is 0,0 and E5 is 4,4.
    """
    def __init__(self):
        self.neighbours = defaultdict(list)

    def _dist(self, node_a, node_b):
        """Simulate a smaller earth in terms of distance between lat, lng coordinates.
        """
        return sqrt(((node_a.x - node_b.x) ** 2) + ((node_a.y - node_b.y) ** 2)) * 6371

    def connect(self, node_a, node_b):
        dist = self._dist(node_a, node_b)
        self.neighbours[node_a].append((dist, node_b))
        self.neighbours[node_b].append((dist, node_a))

    def get_node_neighbours(self, node):
        try:
            return self.neighbours[node]
        except KeyError:
            return []

class TestFinder(RouteFinder, TestMap):
    pass

class TestNoConnections(TestCase):
    def setUp(self):
        self.finder = TestFinder(NODES['A1'], NODES['A2'])
    def test_withNoConnections_raiseError(self):
        with self.assertRaisesRegex(RuntimeError, 'Unable to find route.'):
            self.finder.find()

class TestSinglePath(TestCase):
    def setUp(self):
        finder = TestFinder(NODES['A1'], NODES['A2'])
        finder.connect(NODES['A1'], NODES['A2'])
        self.finder = finder

    def test_A1LeadsA2_returnsA1A2(self):
        self.finder.find()
        self.assertEqual(self.finder.nodes, [NODES['A1'], NODES['A2']])

class TestSinglePath3Nodes(TestCase):
    def setUp(self):
        finder = TestFinder(NODES['A1'], NODES['B2'])
        finder.connect(NODES['A1'], NODES['A2'])
        finder.connect(NODES['A2'], NODES['B2'])
        self.finder = finder
    def test_A1LeadsA2LeadsB2_returnsA1A2B2(self):
        self.finder.find()
        self.assertEqual(self.finder.nodes, [NODES['A1'], NODES['A2'], NODES['B2']])

class TestAPythagoreanTriangle(TestCase):
    def setUp(self):
        finder = TestFinder(NODES['A1'], NODES['E5'])
        finder.connect(NODES['A1'], NODES['C3'])
        finder.connect(NODES['C3'], NODES['D4'])
        finder.connect(NODES['D4'], NODES['E5'])
        finder.connect(NODES['A1'], NODES['C5'])
        finder.connect(NODES['C5'], NODES['E5'])
        self.finder = finder

    def test_followsHypotenuse(self):
        self.finder.find()
        self.assertEqual(
            self.finder.nodes,
            [NODES['A1'], NODES['C3'], NODES['D4'], NODES['E5']])

class TestShortHopsVsShortPath(TestCase):
    def setUp(self):
        finder = TestFinder(NODES['A1'], NODES['E5'])
        finder.connect(NODES['A1'], NODES['C3'])
        finder.connect(NODES['C3'], NODES['D4'])
        finder.connect(NODES['D4'], NODES['E5'])
        finder.connect(NODES['A1'], NODES['E5'])
        self.finder = finder

    def test_followsShortestPath(self):
        self.finder.find()
        self.assertEqual(self.finder.nodes, [NODES['A1'], NODES['E5']])
