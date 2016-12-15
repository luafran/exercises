# A left rotation operation on an array of size  shifts each of the array's elements  unit to the left.
# For example, if left rotations are performed on array , then the array would become .
#
# Given an array of  integers and a number, , perform  left rotations on the array. Then print the updated
# array as a single line of space-separated integers.
#
# Input Format
#
# The first line contains two space-separated integers denoting the respective values of  (the number of
# integers) and  (the number of left rotations you must perform).
# The second line contains  space-separated integers describing the respective elements of the array's
# initial state.
#
# Constraints
#
# Output Format
#
# Print a single line of  space-separated integers denoting the final state of the array after performing
# left rotations.
#
# Sample Input
# 5 4
# 1 2 3 4 5
#
# Sample Output
# 5 1 2 3 4
#
# Explanation
#
# When we perform  left rotations, the array undergoes the following sequence of changes:
#
# Thus, we print the array's final state as a single line of space-separated values, which is 5 1 2 3 4.
import unittest


def array_left_rotation(a, n, k):
    print 'a:', a
    print 'n:', n
    print 'k:', k
    # print 'a[k:]', a[k:]
    # print 'a[0:k]', a[0:k]
    temp = list(a[k:] + a[0:k])
    return temp


def array_left_rotation_brute(a, n, k):
    print 'a:', a
    print 'n:', n
    print 'k:', k
    temp = list(a)
    for i in range(n):
        j = i - k
        # print 'j0:', j
        if j < 0:
            j = n + j
        # print 'j1:', j
        temp[j] = a[i]
    return temp

if __name__ == '__main__':
    n, k = map(int, raw_input().strip().split(' '))
    a = map(int, raw_input().strip().split(' '))
    answer = array_left_rotation(a, n, k)
    print ' '.join(map(str, answer))


class TestArrayLeftRotation(unittest.TestCase):

    def test_0(self):
        input_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = array_left_rotation(input_array, len(input_array), 0)

        expected_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(expected_array, result)

    def test_1(self):
        input_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = array_left_rotation(input_array, len(input_array), 1)

        expected_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        self.assertEqual(expected_array, result)

    def test_4(self):
        input_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = array_left_rotation(input_array, len(input_array), 4)

        expected_array = [4, 5, 6, 7, 8, 9, 0, 1, 2, 3]
        self.assertEqual(expected_array, result)
