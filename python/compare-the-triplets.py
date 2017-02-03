import unittest

if __name__ == '__main__':
    a0,a1,a2 = raw_input().strip().split(' ')
    a0,a1,a2 = [int(a0), int(a1), int(a2)]
    b0,b1,b2 = raw_input().strip().split(' ')
    b0,b1,b2 = [int(b0), int(b1), int(b2)]


def compare_the_triplets(t1, t2):
    r1 = 0
    r2 = 0

    print t1
    print t2

    for i in range(len(t1)):
        if t1[i] > t2[i]:
            r1 += 1
        elif t2[i] > t1[i]:
            r2 += 1

    return '{0} {1}'.format(r1, r2)


class TestCompareTheTriplets(unittest.TestCase):

    def test_example(self):
        t1 = [5, 6, 7]
        t2 = [3, 6, 10]

        result = compare_the_triplets(t1, t2)
        self.assertEqual('1 1', result)
