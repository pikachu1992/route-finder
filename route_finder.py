import heapq
from heuristics import Heuristics
from fsnavigator_map import RouteMap, Node

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
    def __init__(self, *args, start, end, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_node = start
        self.end_node = end
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

    @property
    def atc_route(self):
        route = []
        for node in self.nodes:
            if node.via:
                route.append(f'{node.via} {node.name}')
            else:
                route.append(f'{node.name}')
        return ' '.join(route)
