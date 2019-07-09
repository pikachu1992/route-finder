from unittest import TestCase
from airports import Airports

class TestAiports(TestCase):
    def test_airport_exists(self):
        self.assertEqual(Airports().find_airport("LPPT"), 'airac/SidStars/LPPT.txt')

    def test_airport_none(self):
        self.assertIsNone(Airports().find_airport("A0AA"))
    