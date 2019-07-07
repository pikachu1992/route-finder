import heapq
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
    def get_node_neighbours(self, node):
        """Returns: (tuple) cost, node
        """
        raise NotImplemented()

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
    def find_route(self, start_node, end_node):
        open_list = HeapQueue([(0, 0, start_node, None)])
        closed_list = {}

        while len(open_list) > 0:
            node_f, node_g, node, parent = open_list.pop()
            closed_list[node] = (node_g, parent)

            if node == end_node:
                break
            for neighbour_g, neighbour in super().get_node_neighbours(node):
                if neighbour in closed_list:
                    continue

                h = super().astar_heuristic(node.x, node.y, neighbour.x, neighbour.y)
                g = neighbour_g + node_g
                f = g + h

                open_list.push((f, g, neighbour, node))

        return closed_list
