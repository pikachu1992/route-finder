from unittest import TestCase

from fsnavigator_map import FsNavigatorMap

class TestFsNavigatorMap(FsNavigatorMap):
    def _read_file(self):
        return [
            'PESUL	40.881944	-8.115000	14	W2	    L	PRT	    41.273000	-8.687833	0	    Y	VIS	    40.723417	-7.885833	9500	Y',
            'ODLIX	38.678889	-9.317222	14	Y207	B	LIS	    38.887750	-9.162806	9500	N	EKMAR	38.557500	-9.521389	9500	Y'
        ]

class TestParseAirwayNode(TestCase):
    def setUp(self):
        self.map = TestFsNavigatorMap()

    def test_canParseNodeInfo(self):
        node = self.map.nodes['PESUL']
        self.assertEqual(node.x, 40.881944)
        self.assertEqual(node.y, -8.115000)
        self.assertEqual(node.via, 'W2')
        self.assertEqual(node.via_type, 'L')

        node = self.map.nodes['ODLIX']
        self.assertEqual(node.x, 38.678889)
        self.assertEqual(node.y, -9.317222)
        self.assertEqual(node.via, 'Y207')
        self.assertEqual(node.via_type, 'B')

    def test_canParseNeighboursForNode(self):
