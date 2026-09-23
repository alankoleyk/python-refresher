
import unittest
import random
import numpy as np
from my_utils import find_mean, find_median, find_std_dev

#test mean function

class TestFindMean(unittest.TestCase):

    def test_known_values(self):
        self.assertEqual(find_mean([1, 2, 3, 4, 5]), 3)

    def test_random_matches_statistics_module(self):
        data = [random.randint(-1000, 1000) for i in range(1000)]
        self.assertAlmostEqual(find_mean(data), 0, delta = 50)

    def test_negative_numbers(self):
        self.assertEqual(find_mean([-10, -20, -30]), -20)

    def test_single_value(self):
        self.assertEqual(find_mean([42]), 42)


class TestFindMedian(unittest.TestCase):

    def test_odd_length(self):
        self.assertEqual(find_median([5, 1, 3]), 3)  # sorted: 1,3,5

    def test_even_length(self):
        self.assertEqual(find_median([1, 2, 3, 4]), 2.5)

    def test_random_matches_statistics_module(self):
        data = [random.randint(-500, 500) for i in range(1000)]
        self.assertAlmostEqual(find_median(data), 0, delta = 50)

    def test_negative_numbers(self):
        self.assertEqual(find_median([-5, -1, -10]), -5)


class TestFindStdDev(unittest.TestCase):

    def test_known_values(self):
        self.assertAlmostEqual(
            find_std_dev([2, 4, 4, 4, 5, 5, 7, 9]), 2.138, places=3
        )

    def test_random_matches_statistics_module(self):
        data = [random.randint(1, 100) for _ in range(1000)]
        self.assertAlmostEqual(find_std_dev(data), 29, delta = 3)

    def test_negative_numbers(self):
        data = [-10, -20, -30, -40]
        self.assertAlmostEqual(find_std_dev(data), 12, delta = 1)

