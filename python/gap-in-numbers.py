import unittest

#


def solution_linear(A):

    offset = A[0]
    for i in range(len(A)):
        if A[i] != i + offset:
            return A[i]


def solution(A):

    print("A: {}".format(A))
    expected = (A[0] + A[len(A)-1]) // 2
    mid = A[len(A)//2]
    print("mid: {}, expected: {}".format(mid, expected))
    if len(A) == 1:
        return mid
    elif mid > expected:
        if len(A) == 2:
            return mid
        else:
            solution(A[:len(A)//2 + 1])
    elif mid == expected:
        solution(A[len(A)//2 + 1:])


class TestOne(unittest.TestCase):

    def test_1(self):
        a = [0, 1, 2, 4, 5, 6, 7]
        self.assertEqual(4, solution(a))

    def test_2(self):
        a = [3, 4, 5, 6, 7, 8, 10, 11]
        self.assertEqual(10, solution(a))

    def test_3(self):
        a = [1, 3, 4, 5, 6]
        self.assertEqual(10, solution(a))

    def test_4(self):
        a = [1, 2, 3, 5, 6]
        self.assertEqual(10, solution(a))


if __name__ == '__main__':
    pass
