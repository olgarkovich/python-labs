import unittest
from task_1 import merge_sort, merge, start


class MyTestCase(unittest.TestCase):
    def test_full(self):
        start()
        self.assertEqual(1, 1)

    def test_merge_sort(self):
        current_list = merge_sort([1, 5, 8, 2, 6])
        self.assertEqual(current_list, [1, 2, 5, 6, 8])

    def test_merge(self):
        current_list = merge([1, 5, 7, 8], [2, 3, 6])
        self.assertEqual(current_list, [1, 2, 3, 5, 6, 7, 8])


if __name__ == '__main__':
    unittest.main()
