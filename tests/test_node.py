from unittest import TestCase

from fsnavigator_map import Node

class TestNode(TestCase):
    def test_latOrLngNotANumber_raisesValueError(self):
        with self.assertRaises(ValueError):
            Node('', '', 0)
            Node('', 0, '',)
