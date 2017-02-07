import unittest


def fib_dynamic(n):

    if n == 0:
        return 0

    fib = {0: 0, 1: 1}

    for k in range(2, n+1):
        fib[k] = fib[k-1] + fib[k-2]

    return fib[n]


def fib_save_space(n):

    if n == 0:
        return 0

    back2 = 0
    back1 = 1

    for k in range(2, n):
        curr = back1 + back2
        back2 = back1
        back1 = curr

    return back2 + back1


class TestFibonacci(unittest.TestCase):

    def setUp(self):
        self.fib = fib_save_space

    def test_fib0(self):
        self.assertEqual(self.fib(0), 0)

    def test_fib1(self):
        self.assertEqual(self.fib(1), 1)

    def test_fib2(self):
        self.assertEqual(self.fib(2), 1)

    def test_fib10(self):
        self.assertEqual(self.fib(10), 55)

    def test_fib27(self):
        self.assertEqual(self.fib(27), 196418)
