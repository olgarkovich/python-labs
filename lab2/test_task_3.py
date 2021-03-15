import unittest
from task_3 import Vector


class MyTestCase(unittest.TestCase):
    def test_counter(self):
        x = Vector([1, 2, 3])
        self.assertEqual(x.counter(), 3)

    def test_get_by_index(self):
        x = Vector([6, 6, 5])
        self.assertEqual(x.get_by_index(2), 5)

    def test_check(self):
        x = Vector([1, 2, 3])
        y = Vector([1, 2])
        self.assertNotEqual(x.check(y), True)

    def test_sum(self):
        x = Vector([3, 3, 3])
        y = Vector([7, 9, 5])
        self.assertEqual(x.sum(y), [10, 12, 8])

    def test_sub(self):
        x = Vector([1, 0, 5])
        y = Vector([2, 4, 7])
        self.assertEqual(x.sub(y), [-1, -4, -2])

    def test_multiply(self):
        x = Vector([9, 9, 9])
        self.assertEqual(x.multiply(4), [36, 36, 36])

    def test_multiply_scalar(self):
        x = Vector([4, 4, 4])
        y = Vector([1, 2, 3])
        self.assertEqual(x.multi_scalar(y), 24)

    def test_comparer(self):
        x = Vector([1, 1])
        y = Vector([2, 2])
        self.assertEqual(x.compare(y), False)
