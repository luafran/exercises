# Programming Challenge Description:
# There are two wizards, one good and one evil. The evil wizard has captured the princess. The only way to defeat the evil wizard is to recite a set of magic numbers. The good wizard has given you two numbers, A and B. Find every magic number between A and B, inclusive. 

# A magic number is a number that has two characteristics:
# 1. No digits repeat.
# 2. Beginning with the leftmost digit, take the value of the digit and move that number of digits to the right. Repeat the process again using the value of the current digit to move right again. Wrap back to the leftmost digit as necessary. A magic number will visit every digit exactly once and end at the leftmost digit. 

# For example, consider the magic number 6231.
# 1. Start with '6'. Advance 6 steps to '3', wrapping around once.
# 2. From '3', advance to '2'.
# 3. From '2', advance to '1'.
# 4. From '1', advance to '6'.

# Input:
# The input consists of two integers on a line, separated by spaces. Each integer A and B is 1 <= A <= B <= 10000.

# Output:
# Print each magic number between A and B, inclusive, on a line. If there is no magic number between A and B, print -1.

# Test 1
# Test Input
# 100 1000
# Expected Output
# 147
# 174
# 258
# 285
# 417
# 471
# 528
# 582
# 714
# 741
# 825
# 852

import unittest


def is_valid(in_str):

    # print 'in_str:', in_str

    if len(set(in_str)) != len(in_str):
        return False

    # Don't add 0 since we always visit it.
    visited = []
    str_len = len(in_str)
    rem = str_len
    pos = 0

    while True:
        steps = int(in_str[pos])
        pos += steps
        if pos >= str_len:
            pos %= str_len
        rem -= 1
        # print 'pos:', pos
        # print 'rem:', rem
        if pos in visited:
            return False

        if rem == 0:
            return True

        visited.append(pos)
        # print


class TestIsValid(unittest.TestCase):

    def test_invalid1(self):
        val = '111'
        self.assertFalse(is_valid(val))

    def test_invalid2(self):
        val = '141'
        self.assertFalse(is_valid(val))

    def test_invalid3(self):
        val = '104'
        self.assertFalse(is_valid(val))

    def test_valid1(self):
        val = '147'
        self.assertTrue(is_valid(val))

    def test_valid2(self):
        val = '258'
        self.assertTrue(is_valid(val))

if __name__ == '__main__':
    min = 100
    max = 1000
    magic_numbers = []

    for i in range(min, max):
        if is_valid(str(i)):
            magic_numbers.append(i)

    print magic_numbers
