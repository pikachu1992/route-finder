from unittest import TestCase

from route_finder import RouteFinder, RouteMap, Node

class TestMap(RouteMap):
    node_s = Node(0, 0, 'S')
    node_a = Node(0, 1, 'A')
    node_e = Node(1, 1, 'E')
    node_b = Node(0, 2, 'B')
    node_c = Node(1, 2, 'C')

    def __init__(self):
        self.node_s = TestMap.node_s
        self.node_a = TestMap.node_a
        self.node_e = TestMap.node_e
        self.node_b = TestMap.node_b
        self.node_c = TestMap.node_c
        self.neighbours = {
            self.node_s: [(1, self.node_a)],
            self.node_a: [(1, self.node_e), (1, self.node_b)],
            self.node_e: [(1, self.node_c), (1, self.node_a)],
            self.node_b: [(1, self.node_a), (1, self.node_c)],
            self.node_c: [(1, self.node_e), (1, self.node_b)]
        }

    def get_node_neighbours(self, node):
        return self.neighbours[node]

class TwoNodeMap(TestMap):
    def get_node_neighbours(self, node):
        return [(1, self.node_b)]

class ThreeNodeMap(TestMap):
    def __init__(self):
        super().__init__()
        self.neighbours = {
            self.node_s: [(1, self.node_a)],
            self.node_a: [(1, self.node_e)],
            self.node_e: [(1, self.node_a)]
        }

class TestRouteFinderTwoNodeMap(TestCase):
    def test_startAtAEndAtB_returnsAB(self):
        class TestRouteFinder(RouteFinder, TwoNodeMap):
            pass
        route = TestRouteFinder(start=TestMap.node_a, end=TestMap.node_b)
        route.find()
        self.assertEqual(route.nodes, [TestMap.node_a, TestMap.node_b])
        # self.assertEqual(route.distance, 1)

class TestRouteFinderThreeNodeMap(TestCase):
    def test_startAtSEndAtE_returnsSAE(self):
        class TestRouteFinder(RouteFinder, ThreeNodeMap):
            pass
        route = TestRouteFinder(start=TestMap.node_s, end=TestMap.node_e)
        route.find()
        self.assertEqual(route.nodes, [TestMap.node_s, TestMap.node_a, TestMap.node_e])
        # self.assertEqual(route.distance, 3)

class TestRouteFinderTestMap(TestCase):
    def test_startAtSEndAtE_returnsSAE(self):
        class TestRouteFinder(RouteFinder, TestMap):
            pass
        route = TestRouteFinder(start=TestMap.node_s, end=TestMap.node_e)
        route.find()
        self.assertEqual(route.nodes, [TestMap.node_s, TestMap.node_a, TestMap.node_e])
        # self.assertEqual(route.distance, 3)
