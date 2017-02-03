# Given two strings, a and b, that may or may not be of the same length, determine the minimum number of
# character deletions required to make a and b anagrams.
# Any characters can be deleted from either of the strings.
#
# Input Format
# The first line contains a single string a
# The second line contains a single string b
#
# Constraints
# It is guaranteed that a and b consist of lowercase English alphabetic letters (i.e., a through z).
#
# Output Format
# Print a single integer denoting the number of characters you must delete to make the two strings anagrams
# of each other.
#
# Sample Input
# cde
# abc
#
# Sample Output
# 4
#
# Explanation
# We delete the following characters from our two strings to turn them into anagrams of each other:
# Remove d and e from cde to get c.
# Remove a and b from abc to get c.
#
# We must delete  characters to make both strings anagrams, so we print 4 on a new line.
import unittest
from collections import defaultdict


def number_needed(str_a, str_b):

    a = list(str_a)
    a_loop = list(str_a)
    b = list(str_b)

    for c in a_loop:
        if c in b:
            b.remove(c)
            a.remove(c)

    return len(a) + len(b)


def number_needed2(str_a, str_b):
    c_count = defaultdict(int)

    if len(str_a) >= len(str_b):
        a = str_a
        b = str_b
    else:
        b = str_a
        a = str_b

    for c in a:
        c_count[c] += 1

    from_a = True
    for c in b:
        current = c_count.get(c)
        if current is not None:
            if from_a:
                if current > 0:
                    increment = -1
                else:
                    from_a = False
                    increment = 1
            else:
                increment = 1
        else:
            increment = 1

        c_count[c] += increment

    needed = 0
    for k, count in c_count.items():
        needed += count

    return needed


if __name__ == '__main__':
    a = raw_input().strip()
    b = raw_input().strip()

    print number_needed(a, b)


class TestNumberNeeded(unittest.TestCase):

    def test_example(self):
        string_a = 'cde'
        string_b = 'abc'
        self.assertEqual(4, number_needed(string_a, string_b))

    def test_01(self):
        string_a = 'cde'
        string_b = 'cde'
        self.assertEqual(0, number_needed(string_a, string_b))

    def test_02(self):
        string_a = 'cde'
        string_b = 'dec'
        self.assertEqual(0, number_needed(string_a, string_b))

    def test_51(self):
        string_a = 'abc'
        string_b = 'xy'
        self.assertEqual(5, number_needed(string_a, string_b))

    def test_52(self):
        string_a = 'abcdefgh'
        string_b = 'hgfedcbapqrst'
        self.assertEqual(5, number_needed(string_a, string_b))

    def test_same_letter_1(self):
        string_a = 'a'
        string_b = 'aaaa'
        self.assertEqual(3, number_needed(string_a, string_b))

    def test_same_letter_2(self):
        string_a = 'bbbbbb'
        string_b = 'bb'
        self.assertEqual(4, number_needed(string_a, string_b))

    def test_11(self):
        string_a = 'bbbbbb'
        string_b = 'bbbbbba'
        self.assertEqual(1, number_needed(string_a, string_b))

    def test_12(self):
        string_a = 'bbbbbba'
        string_b = 'bbbbbb'
        self.assertEqual(1, number_needed(string_a, string_b))

    def test_13(self):
        string_a = ''
        string_b = 'bbbbbb'
        self.assertEqual(6, number_needed(string_a, string_b))

    def test_14(self):
        string_a = 'a' * 10000
        string_b = 'b' * 10000
        self.assertEqual(20000, number_needed(string_a, string_b))