import unittest
from fibonacci import Fibonacci

class FibonacciTest(unittest.TestCase):

    def test_iterator_should_work_correct(self):
        check = Fibonacci(5)
        x = [value for value in check]
        self.assertEqual(x, [0, 1, 1, 2, 3, 5])

    def test_iterator_should_not_work(self):
        check = Fibonacci(5)
        x = [value for value in check]
        self.assertNotEqual(x, [0, 1, 1, 2, 3])
