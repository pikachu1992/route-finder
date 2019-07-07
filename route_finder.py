import heapq
from heuristics import Heuristics
from find_neighbours import FindNeighbours

class Node:
    def __init__(self, x, y, name, min_altitude, parent=None):
        self.x = x
        self.y = y
        self.name = name
        self.min_altitude = min_altitude

    def __eq__(self, other):
        return self.name == other.name if isinstance(other, Node) else False

    def __hash__(self):
        return self.name.__hash__() * 13

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
        open_list = HeapQueue([(0, start_node)])
        closed_list = {}

        while len(open_list) > 0:
            node_cost, node = open_list.pop()
            for neighbour_cost, neighbour in super().get_node_neighbours(node):
                if neighbour in closed_list:
                    continue

                h = super().astar_heuristic(node.x, node.y, neighbour.x, neighbour.y)
                f = neighbour_cost + h

                closed_list[neighbour] = node

                if neighbour == end_node:
                    break

                open_list.push((f, neighbour))

        return closed_list
