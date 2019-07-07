from unittest import TestCase

from find_neighbours import FindNeighbours

class TestFsNavigatorMap(TestCase):
    neighbours_test = FindNeighbours()
    line = "07BAN	35.207778	35.821111	14	R785	B	BAN	35.228286	35.957919	29000	Y	NIKAS	35.193333	35.716667	29000	Y"  
    test_line = neighbours_test.parseline(line.split())    
    node = test_line[0]
    neighbours = neighbours_test.parse_neighbours(test_line[1])

    def test_ParseLine(self):
        self.assertTrue(len(self.test_line) != 0)
        self.assertTrue(len(self.neighbours) != 0)
    
    def test_CalculateCost(self):
        for neighbour in self.neighbours:
            self.assertIsNot(self.neighbours_test.calculate_cost(float(self.node[1]), float(self.node[2]), float(neighbour[1]), float(neighbour[2])), 0)
        
    def test_find_node(self, node_name = "LIS"):
        self.assertTrue(len(self.neighbours_test.find_node_lines(node_name)) != 0)




            
