from unittest import TestCase

from route_finder import RouteFinder, RouteMap, Node

class TestMap(RouteMap):
    node_s = Node(0, 0, 'S')
    node_a = Node(0, 1, 'A')
    node_e = Node(1, 1, 'E')
    node_b = Node(0, 2, 'B')
    node_c = Node(1, 2, 'C')

    def __init__(self):
        self.neighbours = {
            TestMap.node_s: [(10, TestMap.node_a)],
            TestMap.node_a: [(10, TestMap.node_e), (10, TestMap.node_s), (10, TestMap.node_b)],
            TestMap.node_e: [(10, TestMap.node_c), (10, TestMap.node_a)],
            TestMap.node_b: [(10, TestMap.node_a), (10, TestMap.node_c)],
            TestMap.node_c: [(10, TestMap.node_e), (10, TestMap.node_b)]
        }

    def get_node_neighbours(self, node):
        return self.neighbours[node]

class TwoNodeMap(TestMap):
    def get_node_neighbours(self, node):
        return [(10, self.node_b)]

class ThreeNodeMap(TestMap):
    def __init__(self):
        super().__init__()
        self.neighbours = {
            self.node_s: [(10, self.node_a)],
            self.node_a: [(10, self.node_e)],
            self.node_e: [(10, self.node_a)]
        }

class TestRouteFinderTwoNodeMap(TestCase):
    def test_startAtAEndAtB_returnsAB(self):
        class TestRouteFinder(RouteFinder, TwoNodeMap):
            pass
        route = TestRouteFinder(TestMap.node_a, TestMap.node_b)
        route.find()
        self.assertEqual(route.nodes, [TestMap.node_a, TestMap.node_b])
        # self.assertEqual(route.distance, 1)

class TestRouteFinderThreeNodeMap(TestCase):
    def test_startAtSEndAtE_returnsSAE(self):
        class TestRouteFinder(RouteFinder, ThreeNodeMap):
            pass
        route = TestRouteFinder(TestMap.node_s, TestMap.node_e)
        route.find()
        self.assertEqual(route.nodes, [TestMap.node_s, TestMap.node_a, TestMap.node_e])
        # self.assertEqual(route.distance, 3)

class TestRouteFinderTestMap(TestCase):
    def test_startAtSEndAtE_returnsSAE(self):
        class TestRouteFinder(RouteFinder, TestMap):
            pass
        route = TestRouteFinder(TestMap.node_s, TestMap.node_e)
        route.find()
        self.assertEqual(route.nodes, [TestMap.node_s, TestMap.node_a, TestMap.node_e])
        # self.assertEqual(route.distance, 3)

class TestRouteFinderDoesntWalkRoutesThatGetFarther(TestCase):
    def test_startAtAEndAtC_doesNotWalkS(self):
        class WalkSFailsMap(TestMap):
            def get_node_neighbours(self, node):
                if node == TestMap.node_s:
                    raise RuntimeError()
                else:
                    return super().get_node_neighbours(node)
        class TestRouteFinder(RouteFinder, WalkSFailsMap):
            pass
        route = TestRouteFinder(TestMap.node_a, TestMap.node_c)
        route.find()
        self.assertEqual(route.nodes,
            [TestMap.node_a, TestMap.node_b, TestMap.node_c])
