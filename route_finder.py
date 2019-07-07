
class Node:
    def __init__(self, x, y, name, parent=None):
        self.x = x
        self.y = y
        self.name = name

    def __eq__(self, other):
        return self.name == other.name if isinstance(other, Node) else False

    def __hash__(self):
        return self.name.__hash__() * 13

class RouteMap:
    def get_node_neighbours(self, node):
        """Returns: (tuple) cost, node
        """
        raise NotImplemented()

class RouteFinder(RouteMap):
    def find_route(self, start_node, end_node):
        open_list = [(0, start_node, None),]
        closed_list = {}

        while len(open_list) > 0:
            cost, node, parent = open_list.pop()
            closed_list[node] = (cost, parent)

            if node == end_node:
                break

            for n_cost, neighbour in super().get_node_neighbours(node):
                if neighbour in closed_list:
                    continue

                open_list.append((n_cost + cost, neighbour, node))

        return closed_list
