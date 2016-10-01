import unittest


def sort_mode(a):
    op = 'unknown'
    idx1 = 0
    idx2 = 0

    prev = a[0]
    for i in range(1, len(a)):
        if a[i] < prev:
            if op == 'unknown':
                op = 'swap'
            elif op == 'swap':
                op = 'none'


    result = '{0} {1} {1}'. format(op, idx1, idx2)
    print result
    return result


class TestNumberNeeded(unittest.TestCase):

    def test_example1(self):
        a = [4, 2]
        result = sort_mode(a)
        self.assertEqual('swap 1 2', result)