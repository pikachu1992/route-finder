from unittest import TestCase

from fsnavigator_map import FsNavigatorMap

class TestFsNavigatorMap(FsNavigatorMap):
    def _read_file(self):
        return [
            'PESUL	40.881944	-8.115000	14	W2	    L	PRT	    41.273000	-8.687833	0	    Y	VIS	    40.723417	-7.885833	9500	Y'
        ]

class TestParseAirwayNode(TestCase):
    def setUp(self):
        self.map = TestFsNavigatorMap()

    def test_canParseNodeInfo(self):
        info = self.map.nodes['PESUL']
        self.assertEqual(info.x, 40.881944)
        self.assertEqual(info.y, -8.115000)
