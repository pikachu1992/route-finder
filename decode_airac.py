from route_finder import Node
from collections import defaultdict

class DecodeAirac():
    lines = []
    airways = []

    def __init__(self, file):
        self.lines = file.readlines()
        self.airways = self.get_airways(self.lines)
        self.get_neighbours("TROIA", self.lines)
    
    def get_airways(self, lines_from_file):
        airways = defaultdict(list)
        for line in lines_from_file:
            if line.startswith(';'):
                continue
            exploded_line = line.split()
            airways[exploded_line[0]].append(exploded_line)
        return airways

    def get_neighbours(self, node, lines_from_file):
        neighbours = []
        for line in lines_from_file:
            if line.startswith(';'):
                continue
            elif len([x for x in line.split() if x == node]) != 0:
                for airway, nodes in self.airways.items():
                    for ref_node in nodes:
                        if node == ref_node[2]:
                            if int(ref_node[1]) != 1:
                                neighbours.append(Node(nodes[nodes.index(ref_node) - 1][3], nodes[nodes.index(ref_node) - 1][4], nodes[nodes.index(ref_node) - 1][2]))
                            elif int(nodes[nodes.index(ref_node) + 1][1]) == 1:
                                continue
                            neighbours.append(Node(nodes[nodes.index(ref_node) + 1][3], nodes[nodes.index(ref_node) + 1][4], nodes[nodes.index(ref_node) + 1][2]))
                                                       
        return neighbours

with open('airac/wpnavrte.txt') as file:
    data = DecodeAirac(file)