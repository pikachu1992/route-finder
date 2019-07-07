from unittest import TestCase

from find_neighbours import FindNeighbours

class TestFsNavigatorMap(TestCase):
    line = "07BAN	35.207778	35.821111	14	R785	B	BAN	35.228286	35.957919	29000	Y	NIKAS	35.193333	35.716667	29000	Y"  
    test_line = FindNeighbours().parseline(line)    
    node = test_line[0]
    test_neighbours = FindNeighbours().parse_neighbours(test_line[1])

    def test_ParseLine(self):
        self.assertTrue(len(self.test_line) != 0)
        self.assertTrue(len(self.test_neighbours) != 0)
    
    def test_CalculateCost(self):
        for neighbour in self.test_neighbours:
            self.assertIsNot(FindNeighbours().calculate_cost(float(self.node[1]), float(self.node[2]), float(neighbour[1]), float(neighbour[2])), 0)
        
    


            
