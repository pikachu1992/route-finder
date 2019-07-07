from unittest import TestCase

from route_finder import RouteFinder, RouteMap, Node

class TestRouteFinder(TestCase):
    def test_ALeadsToB_returnsBparentA(self):
        node_a = Node(0, 0, 'A')
        node_b = Node(0, 0, 'B')
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
            self.node_s = Node(0, 0, 'S')
            self.node_a = Node(0, 1, 'A')
            self.node_e = Node(1, 1, 'E')
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
        route = test_finder.find_route(Node(0, 0, 'S'), Node(1, 1, 'E'))
        self.assertEqual(route[Node(1, 1, 'E')], Node(0, 1, 'A'))
        self.assertEqual(route[Node(0, 1, 'A')], Node(0, 0, 'S'))
