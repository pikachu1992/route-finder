from unittest import TestCase
from math import sqrt

from heuristics import compute_heuristic

class TestHeuristicsFunc(TestCase):
    def test_withoutTuplesOfLength2_raisesValueError(self):
        with self.assertRaises(ValueError):
            a = None
            b = None
            compute_heuristic(a, b)

        with self.assertRaises(ValueError):
            a = (0, 0, 0)
            b = (0, 0, 0)
            compute_heuristic(a, b)

    def test_tupleWithOtherThanNumber_raisesTypeError(self):
        a = ('0', '0')
        b = ('0', '0')
        compute_heuristic(a, b)

    def test_withTupleOfLength2_works(self):
        a = (0, 0)
        b = (0, 0)
        compute_heuristic(a, b)

    def test_withSamePoint_returnsZero(self):
        a = (0, 0)
        b = (0, 0)
        h = compute_heuristic(a, b)
        self.assertEqual(sqrt(h), 0)

    def test_callingConvention(self):
        a = (0, 0)
        b = (0, 0)
        h = compute_heuristic(a, b)
        self.assertEqual(sqrt(h), 0)

        a = (0, 0)
        b = (0, 0)
        h = compute_heuristic(*(*a, *b))
        self.assertEqual(sqrt(h), 0)

    def test_aStraigthLine_returnsStraigthLineDistance(self):
        a = (1, 0)
        b = (0, 0)
        h = compute_heuristic(a, b)
        self.assertEqual(sqrt(h), 1)

        a = (5, 0)
        b = (0, 0)
        h = compute_heuristic(a, b)
        self.assertEqual(sqrt(h), 5)

        a = (-5, 0)
        b = (0, 0)
        h = compute_heuristic(a, b)
        self.assertEqual(sqrt(h), 5)

        a = (0, 5)
        b = (0, 0)
        h = compute_heuristic(a, b)
        self.assertEqual(sqrt(h), 5)
