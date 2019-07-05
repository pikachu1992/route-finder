
class Node:
    def __init__(self, x, y, name, parent=None):
        self.x = x
        self.y = y
        self.name = name
        self.parent = parent

    def __eq__(self, other):
        return self.name == other.name if isinstance(other, Node) else False

    def __hash__(self):
        return self.name.__hash__() * 13

class RouteMap:
    def get_node_neighbours(self, node):
        raise NotImplemented()

class RouteFinder(RouteMap):
    def find_route(self, start_node, end_node):
        open_list = [start_node,]
        closed_list = {}

        while len(open_list) > 0:
            node = open_list.pop()
            for neighbour in super().get_node_neighbours(node):
                if neighbour in closed_list:
                    continue

                closed_list[neighbour] = node

                if neighbour == end_node:
                    break

                open_list.append(neighbour)

        return closed_list
