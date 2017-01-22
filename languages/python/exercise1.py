import unittest

#


def solution(X, A):

    x_total = sum(1 if x == X else 0 for x in A)
    print 'x_total:', x_total

    x_before = 0
    non_x_after = len(A) - x_total
    for i in xrange(len(A) + 1):
        print 'i:', i
        print 'x_before:', x_before
        print 'non_x_after:', non_x_after
        if x_before == non_x_after:
            return i
        if A[i] == X:
            x_before += 1
        else:
            non_x_after -= 1

    return -1


class TestOne(unittest.TestCase):

    def test_1(self):
        x = 5
        a = [5, 5, 1, 7, 2, 3, 5]
        sol = solution(x, a)
        self.assertEqual(4, sol)

    def test_2(self):
        x = 5
        a = [5, 5, 5, 5, 5, 5, 5]
        sol = solution(x, a)
        self.assertEqual(0, sol)

    def test_3(self):
        x = 5
        a = [0, 0, 0, 0, 0, 0, 0]
        sol = solution(x, a)
        self.assertEqual(len(a), sol)

    def test_4(self):
        x = 1
        a = [1, 0, 0, 0, 0, 0, 0]
        sol = solution(x, a)
        self.assertEqual(6, sol)

    def test_5(self):
        x = 1
        a = [0, 0, 0, 0, 0, 0, 1]
        sol = solution(x, a)
        self.assertEqual(6, sol)

    def test_6(self):
        x = 9
        a = [9, 0, 0, 0, 0, 0, 9]
        sol = solution(x, a)
        self.assertEqual(5, sol)

    def test_7(self):
        x = 9
        a = [9, 9, 0, 0, 0, 0, 9]
        sol = solution(x, a)
        self.assertEqual(4, sol)

    def test_8(self):
        x = 9
        a = [9, 0, 0, 0, 0, 9, 9]
        sol = solution(x, a)
        self.assertEqual(4, sol)

    def test_9(self):
        x = 9
        a = [9, 9, 0, 0, 9, 9, 9]
        sol = solution(x, a)
        self.assertEqual(2, sol)

    def test_10(self):
        x = 9
        a = [9, 9, 9, 0, 9, 9, 9]
        sol = solution(x, a)
        self.assertEqual(1, sol)

if __name__ == '__main__':
    pass
