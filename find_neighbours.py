from route_finder import Node
from collections import defaultdict

class FindNeighbours():
    airways = []
    file = open('airac/wpnavrte.txt', 'r')
    lines = file.readlines()

    def __init__(self):
        self.airways = self.get_airways(self.lines)
    
    def get_airways(self, lines_from_file):
        airways = defaultdict(list)
        for line in lines_from_file:
            if line.startswith(';'):
                continue
            exploded_line = line.split()
            airways[exploded_line[0]].append(exploded_line)
        return airways

    def get_neighbours(self, node_name):
        neighbours = []
        for line in self.lines:
            if line.startswith(';'):
                continue
            elif len([x for x in line.split() if x == node_name]) != 0:
                for airway, nodes in self.airways.items():
                    for ref_node in nodes:
                        if node_name == ref_node[2]:
                            if int(ref_node[1]) != 1:
                                neighbours.append(Node(nodes[nodes.index(ref_node) - 1][3], nodes[nodes.index(ref_node) - 1][4], nodes[nodes.index(ref_node) - 1][2]))
                            elif int(nodes[nodes.index(ref_node) + 1][1]) == 1:
                                continue
                            neighbours.append(Node(nodes[nodes.index(ref_node) + 1][3], nodes[nodes.index(ref_node) + 1][4], nodes[nodes.index(ref_node) + 1][2]))

        return neighbours
