import unittest
import sys


def chars_in_both_strings1(string1, string2):
    s1 = set(string1)
    s2 = set(string2)

    return list(s1 & s2)


def chars_in_both_strings_brute(string1, string2):

    result = []
    for c in string1:
        if c in string2:
            result.append(c)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "usage:",sys.argv[0],"string1 string2"
        raise SystemExit

    str1 = sys.argv[1]
    str2 = sys.argv[2]

    print chars_in_both_strings1(str1, str2)
    print chars_in_both_strings_brute(str1, str2)

else:
    print 'imported, __name__ =', __name__


class TestCharInBothStrings(unittest.TestCase):

    def setUp(self):
        self.f = chars_in_both_strings1

    def test_none(self):
        s1 = 'abcdefg'
        s2 = 'hijklmn'

        self.assertEqual(self.f(s1, s2), [])

    def test_some1(self):
        s1 = 'abcdefg'
        s2 = 'ghijklm'

        self.assertEqual(self.f(s1, s2), ['g'])

    def test_some2(self):
        s1 = 'abcdefg'
        s2 = 'fghijklma'

        self.assertItemsEqual(self.f(s1, s2), ['a', 'f', 'g'])

    def test_all(self):
        s1 = 'abcdefg'
        s2 = 'abcdefg'

        self.assertItemsEqual(self.f(s1, s2), [c for c in s1])
