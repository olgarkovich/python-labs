import unittest
from task_4 import fib, cached
from time import time


class MyTestCase(unittest.TestCase):
    def test_fib_1(self):
        numb = fib(6)
        self.assertEqual(numb, 8)

    def test_fib_2(self):
        self.assertEqual(fib(1), 1)

    def test_fib_3(self):
        numb = fib(8)
        self.assertEqual(fib(9), 34)

    def test_time(self):
        start = time()
        numb = fib(50)
        usual_time = time() - start
        start = time()
        cached(fib(50))
        cached_time = time() - start
        self.assertLess(cached_time, usual_time)

#1 1 2 3 5 8 13 21 34


if __name__ == '__main__':
    unittest.main()
