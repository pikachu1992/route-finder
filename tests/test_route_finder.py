from unittest import TestCase

from route_finder import RouteFinder, RouteMap, Node
from find_neighbours import FindNeighbours

class TestRouteFinder(TestCase):
    def test_ALeadsToB_returnsBparentA(self):
        node_a = Node(0, 0, 'A', 0)
        node_b = Node(0, 0, 'B', 0)
        class ALeadsToB(RouteMap):
            def get_node_neighbours(self, node):
                return ((1, node_b),)

        class TestRouteFinder(RouteFinder, ALeadsToB):
            pass

        test_finder = TestRouteFinder()
        route = test_finder.find_route(node_a, node_b)
        self.assertEqual(route[node_b], node_a)

class TestRouteFinderSLeadsToAALeadsToE(TestCase):
    class SLeadsToAALeadsToE(RouteMap):
        def __init__(self):
            self.node_s = Node(0, 0, 'S', 0)
            self.node_a = Node(0, 1, 'A', 0)
            self.node_e = Node(1, 1, 'E', 0)
            self.neighbours = {
                self.node_s: [(1, self.node_a)],
                self.node_a: [(1, self.node_e)],
                self.node_e: [(1, self.node_a)]
            }

        def get_node_neighbours(self, node):
            return self.neighbours[node]

    def test_startAtS_returnsSAE(self):
        class TestRouteFinder(RouteFinder, TestRouteFinderSLeadsToAALeadsToE.SLeadsToAALeadsToE):
            pass
        test_finder = TestRouteFinder()
        route = test_finder.find_route(Node(0, 0, 'S', 0), Node(1, 1, 'E', 0))
        self.assertEqual(route[Node(1, 1, 'E', 0)], Node(0, 1, 'A', 0))
        self.assertEqual(route[Node(0, 1, 'A', 0)], Node(0, 0, 'S', 0))
